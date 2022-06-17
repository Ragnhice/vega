import re
from collections import Counter
from typing import Union

from aqas.logger import Logger
from aqas.utils.gql_adapter import GraphQLDataAdapter


class StartupApiAdapterQuery(GraphQLDataAdapter):
    def __init__(self):
        super().__init__("StartupApi")
        self.recursion_list = []

    def get_version(self, expect_errors: Union[bool, type(None)] = False):
        """
        Получает текущую версию сервиса
        """
        response = self._call_service_method("""
        query {
          startupApiVersion
        }
        """, expect_errors=expect_errors)
        return response

    def get_users(self, expect_errors: Union[bool, type(None)] = False):
        """
        Получает список пользователей
        """
        query = self.query_builder() \
            .operation() \
            .query("users") \
            .fields(["id", "shortName", "firstName", "middleName", "lastName"]) \
            .generate()
        return self._call_service_method(query, expect_errors=expect_errors).get("users")

    def get_objects_by_exercise_id(self, expect_errors: Union[bool, type(None)] = False):
        """
        Обьекты использующиеся в упражнении с заданным номером
        """
        query = self.query_builder() \
            .operation() \
            .query("users") \
            .fields(["name", "localizationName", "guid", "prefab", "image"]) \
            .generate()
        return self._call_service_method(query, expect_errors=expect_errors).get("objectsByExerciseId")

    def get_exercises(self, expect_errors: Union[bool, type(None)] = False):
        """
        Получает список упражнений
        """
        response = self._call_service_method("""
       query{
        exercises{
        id
        name
        description
        tags
        type
        sceneId
    }
}
        """, expect_errors=expect_errors)
        return response

    def get_objects_1(self, expect_errors: Union[bool, type(None)] = False):
        """
        Доступные обьекты
        """
        query = self.query_builder() \
            .operation() \
            .query("objects") \
            .fields(["name", "localizationName", "guid", "prefab", "image"]) \
            .generate()
        return self._call_service_method(query, expect_errors=expect_errors).get("objects")

    def get_objects_2(self, expect_errors: Union[bool, type(None)] = False):
        """
            Доступные обьекты
        """
        available_commands = self.query_builder().query("availableCommands").fields(
            ["id", "name", "localizationName", "parameter", "isNeedPosition"]
            ).generate()
        query = self.query_builder().operation().query("objects").fields(
            ["name", "localizationName", "guid", "prefab", "image", available_commands]
            ).generate()
        return self._call_service_method(query, expect_errors=expect_errors).get("objects")

    def get_graphql(self, expect_errors: bool = False):
        """
        Получение данных из GraphQL

        :param expect_errors: Флаг ожидания ошибки выполнения запроса
        """
        query = """
            query IntrospectionQuery { __schema { types { kind name enumValues { name } fields { name description
            type { kind name ofType { kind name ofType { kind name ofType { kind name ofType { kind name ofType {
              kind name ofType { kind name ofType { kind name } } } } } } } } } } } }
                """
        return self._call_service_method(query, expect_errors=expect_errors)["__schema"]["types"]

    def get_of_type(self, field: dict):
        """
        Рекурсивная обработка поля ofType

        :param field: Обрабатываемое поле
        """
        if field.get("type"):
            field = field["type"]
        if field.get("ofType"):
            return self.get_of_type(field.get("ofType"))
        else:
            return field

    def get_all_queries(self, expect_errors: bool = False):
        """
        Получение списка query

        :param expect_errors: Флаг ожидания ошибки выполнения запроса
        """
        query = """
        query { __schema { queryType { fields { name type { name kind ofType { kind name ofType { kind name ofType {
               kind name  } } } fields { name type { name kind ofType { kind name ofType { kind name ofType {
                    kind name ofType { kind name } } } } } } } args { name type { name kind ofType { kind name } }} } } } }
                """
        return self._call_service_method(query, expect_errors=expect_errors)["__schema"]["queryType"]["fields"]

    def process_field(self,
                      field: dict,
                      objects: list,
                      expected_fields: list = [],
                      arguments: dict = {},
                      expect_errors: bool = False):
        """
        Метод обработки полей

        :param field: Обрабатываемое поле
        :param expected_fields: Список полей для обработки
        :param arguments: Параметры полей
        :param expect_errors: Флаг ожидания ошибки выполнения запроса
        """
        query_name = field["name"]
        if field.get("kind") is None:
            field = self.get_of_type(field)
        if field.get("kind") == "OBJECT":
            self.recursion_list.append(field["name"])
            counter = Counter(self.recursion_list)
            if counter[field["name"]] >= 3:
                return ""
            obj_fields = list(filter(lambda x: x["name"] == field["name"], objects))[0]["fields"]
            if obj_fields:
                query_fields = [self.process_field(obj, objects, expected_fields, arguments) for obj in obj_fields]
                return (self.query_builder()
                        .query(query_name, input=arguments.get(query_name, {}))
                        .fields(query_fields)
                        .generate())
            else:
                return self.query_builder().query(query_name, input=arguments.get(query_name, {})).generate()
        else:
            return query_name

    def get_query(self, query_name: str, arguments: dict = {}, expect_errors: bool = False):
        """
        Отправка запроса Query

        :param query_name: Название Query
        :param arguments: Параметры полей
        :param expect_errors: Флаг ожидания ошибки выполнения запроса
        """
        objects = self.get_graphql()
        try:
            find_query = list(filter(lambda x: x["name"] == query_name, self.get_all_queries()))[0]
        except IndexError:
            raise IndexError(f"{query_name} not found")
        if arguments:
            arguments[find_query["type"]["name"]] = arguments.pop(query_name)
            for keys, values in arguments.items():
                for key, value in values.items():
                    arguments[keys][key] = self.convert_parameter(value)
        fields = self.process_field(self.get_of_type(find_query), objects=objects, arguments=arguments)
        name = find_query["type"]["name"] or find_query["type"]["ofType"]["name"]
        query = re.sub(name, query_name, self.query_builder().fields([fields]).generate(), 1)
        self.recursion_list.clear()
        try:
            return self._call_service_method(query, expect_errors=expect_errors).get(query_name)
        except Exception as e:
            Logger().error(f"ERROR: {query_name} query - {e}")
