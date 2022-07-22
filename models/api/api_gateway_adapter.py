import json
from random import choice
from typing import Union

import aqas
from faker import Faker

from utils.constants import API
from utils.data_utils import generate_datetime


class ApiGatewayAdapter(aqas.GraphQLDataAdapter):
    def __init__(self):
        super().__init__("ApiGateway")
        self.recursion_list = []

    def objects_by_exercise_id(self, expect_errors: Union[bool, type(None)] = False):
        """Получает список обьектов использующихся в упражнении с заданным номером."""
        response = self._call_service_method(
            """
                query {
                    objectsByExerciseId (id: 1) {
                        name
                        localizationName
                        guid
                        prefab
                        image
                    }
                }
            """, expect_errors=expect_errors)
        return response.get("objectsByExerciseId")

    def environment_restrictions(self, expect_errors: Union[bool, type(None)] = False):
        """Получает список диапазонов погоды."""
        response = self._call_service_method(
            """
                query {
                    environmentRestrictions {
                        key
                        value
                    }
                }
            """, expect_errors=expect_errors)
        return response.get("environmentRestrictions")

    def get_users_fields(self, expect_errors: Union[bool, type(None)] = False):
        """Получает список пользователей."""
        query = (self.query_builder()
                 .operation()
                 .query("users")
                 .fields(["id", "shortName", "firstName", "middleName", "lastName"])
                 .generate())
        return self._call_service_method(query, expect_errors=expect_errors).get("users")

    def get_objects_by_exercise_id_fields(self, expect_errors: Union[bool, type(None)] = False):
        """Объекты использующиеся в упражнении с заданным номером."""
        query = (self.query_builder()
                 .operation()
                 .query("objectsByExerciseId")
                 .fields(["name", "localizationName", "guid", "prefab", "image"])
                 .generate())
        return self._call_service_method(query, expect_errors=expect_errors).get("objectsByExerciseId")

    def get_objects(self, expect_errors: Union[bool, type(None)] = False):
        """Доступные объекты."""
        query = (self.query_builder()
                 .operation()
                 .query("objects")
                 .fields(["name", "localizationName", "guid", "prefab", "image"])
                 .generate())
        return self._call_service_method(query, expect_errors=expect_errors).get("objects")

    def get_objects_commands(self, expect_errors: Union[bool, type(None)] = False):
        """Доступные объекты, в ответе доступные команды."""
        available_commands = (self.query_builder()
                              .query("availableCommands")
                              .fields(["id", "name", "localizationName", "parameter", "isNeedPosition"])
                              .generate())
        query = (self.query_builder()
                 .operation()
                 .query("objects")
                 .fields(["name", "localizationName", "guid", "prefab", "image", available_commands])
                 .generate())
        return self._call_service_method(query, expect_errors=expect_errors).get("objects")

    def remove_users_by_id(self, user_ids: list, expect_errors: Union[bool, type(None)] = False):
        """
        Удаляет пользователей по id.

        :param: user_ids - идентификаторы пользователей
        """
        query = (self.query_builder()
                 .operation("mutation")
                 .query("removeUsersById", input={"userIds": user_ids})
                 .generate())
        return self._call_service_method(query, expect_errors=expect_errors).get("removeUsersById")

    def create_weapon(self, expect_errors: Union[bool, type(None)] = False):
        """Создает оружие."""
        mutation = f"""
            mutation CreateWeapon {{
                createWeapon(
                    weaponInput: {{
                        id: {Faker().random_int(200, 300)},
                        hwid: {Faker().random_int(200, 300)},
                        shotsCount: {Faker().random_int(1, 3)},
                        typeId: {Faker().random_int(1, 5)},
                        mode:{choice(API.WEAPON_MODE)},
                        regDate: {generate_datetime()}
                        }})
                    {{
                        id
                        hwid
                        regDate
                        shotsCount
                        mode
                        magazines
                        ammoType{{
                            id
                            name
                            localizationName
                            description
                        }}
                    }}
            }}
        """
        response = self._call_service_method(mutation, expect_errors=expect_errors)
        return response.get("createWeapon")

    def remove_weapons_by_id(self,
                             weapon_ids: list,
                             expect_errors: Union[bool, type(None)] = False):
        """
        Удаляет оружия по id.

        :param: weapon_ids - идентификаторы оружий
        """
        query = (self.query_builder()
                 .operation("mutation")
                 .query("removeWeaponsById", input={"weaponIds": weapon_ids})
                 .generate())
        return self._call_service_method(query, expect_errors=expect_errors).get("removeWeaponsById")

    def add_oject(self,
                  create_object_input: Union[dict, str] = "null",
                  expect_errors: Union[bool, type(None)] = False):
        """Создает объект.

        :param: create_object_input - Словарь с данными нового объекта, предсталенными ниже
        :param expect_errors: Флаг ожидания ошибки выполнения запроса
        """
        available_commands = (self.query_builder()
                              .query("availableCommands")
                              .fields(["id", "name", "localizationName", "parameters"])
                              .generate())
        query = (self.query_builder()
                 .operation("mutation")
                 .query("addObject",
                        input={
                            "objectCreateInput": self.format_mutation(
                                json.dumps(create_object_input, ensure_ascii=False)),
                        },
                        )
                 .fields(["name", "localizationName", "guid", "prefab", "image", available_commands])
                 .generate())
        response = self._call_service_method(query, expect_errors=expect_errors)
        return response.get("addObject", response)

    def update_object_by_guid(self, update_object_input: Union[dict, str] = "null", expect_errors=False):
        """
        Обновление объекта

        :param update_object_input: Параметры объекта
        :param expect_errors: Флаг ожидания ошибки выполнения запроса
        """
        available_commands = (self.query_builder()
                              .query("availableCommands")
                              .fields(["id", "name", "localizationName", "parameters"])
                              .generate())
        query = (self.query_builder()
                 .operation("mutation")
                 .query("updateObjectByGuid",
                        input={
                            "objectInput": self.format_mutation(json.dumps(update_object_input, ensure_ascii=False)),
                        },
                        )
                 .fields(["name", "localizationName", "guid", "prefab", "image", available_commands])
                 .generate())
        response = self._call_service_method(query, expect_errors=expect_errors)
        return response.get("updateObjectByGuid", response)

    def remove_object_by_guid(self, object_guid: str, expect_errors: Union[bool, type(None)] = False):
        """
        Удаляет объект по guid.

        :param: object_guid - идентификатор объекта
        """
        query = (self.query_builder()
                 .operation("mutation")
                 .query("removeObjectByGuid", input={"guid": self.convert_parameter(object_guid)})
                 .generate())
        response = self._call_service_method(query, expect_errors=expect_errors)
        return response.get("removeObjectByGuid", response)

    def remove_scene_by_guid(self, guid_scene: str, expect_errors=False):
        """
        Удаление сцены

        :param guid_scene: guid сцены
        :param expect_errors: Флаг ожидания ошибки выполнения запроса
        """
        query = (self.query_builder()
                 .operation("mutation")
                 .query("removeSceneByGuid", input={"guid": self.convert_parameter(guid_scene)})
                 .generate())
        return self._call_service_method(query, expect_errors=expect_errors).get("removeSceneByGuid")

    def update_scene_by_guid(self, update_scene_input: Union[dict, str] = "null", expect_errors=False):
        """
        Обновление сцены

        :param update_scene_input: Параметры сцены
        :param expect_errors: Флаг ожидания ошибки выполнения запроса
        """
        query = (self.query_builder()
                 .operation("mutation")
                 .query("updateSceneByGuid",
                        input={
                            "sceneInput": self.format_mutation(json.dumps(update_scene_input, ensure_ascii=False)),
                        },
                        )
                 .fields([
                     "name",
                     "description",
                     "localizationName",
                     "guid",
                     "prefab",
                     "image",
                     "bounds",
                     "zeroPointShiftMeters",
                     "cameraDefaultPosition",
                     "cameraDefaultRotation",
                     "keepRealism",
                 ])
                 .generate())
        response = self._call_service_method(query, expect_errors=expect_errors)
        return response.get("updateSceneByGuid", response)

    def remove_exercise_by_id(self, id_exercise: str, expect_errors=False):
        """
        Удаление упражнения

        :param id_exercise: id упражнения
        :param expect_errors: Флаг ожидания ошибки выполнения запроса
        """
        query = (self.query_builder()
                 .operation("mutation")
                 .query("removeExerciseById", input={"id": id_exercise})
                 .fields(["response"])
                 .generate())
        response = self._call_service_method(query, expect_errors=expect_errors)
        return response.get("removeExerciseById", response)

    def update_exercise_by_id(self, update_exercise_input: Union[dict, str] = "null", expect_errors=False):
        """
        Обновление упражнения

        :param update_exercise_input: Параметры упражнения
        :param expect_errors: Флаг ожидания ошибки выполнения запроса
        """
        scene = (self.query_builder()
                 .query("scene")
                 .fields([
                     "name",
                     "description",
                     "localizationName",
                     "guid",
                     "prefab",
                     "image",
                 ])
                 .generate())
        query = (self.query_builder()
                 .operation("mutation")
                 .query("updateExerciseById",
                        input={
                            "Input": self.format_mutation(json.dumps(update_exercise_input,
                                                                     ensure_ascii=False)),
                        },
                        )
                 .fields([
                     "name",
                     "description",
                     "id",
                     "tags",
                     scene,
                 ])
                 .generate())
        response = self._call_service_method(query, expect_errors=expect_errors)
        return response.get("updateExerciseById", response)

    def remove_units_by_id(self,
                           unit_ids: list,
                           expect_errors: Union[bool, type(None)] = False):
        """
        Удаляет подразделения по id.

        :param: unit_ids - подразделения
        """
        query = (self.query_builder()
                 .operation("mutation")
                 .query("removeUnitsById", input={"unitIds": unit_ids})
                 .generate())
        return self._call_service_method(query, expect_errors=expect_errors).get("removeUnitsById")

    def remove_ammo_weapon(self,
                           weapon_type_id: int,
                           ammo_type_id: int,
                           expect_errors: Union[bool, type(None)] = False):
        """
        Удаляет связку боеприпасов и типа оружия

        :param: ammoTypeId - Тип боеприпасов
        :param: weaponTypeId - Тип боеприпасов
        """
        query = (self.query_builder()
                 .operation("mutation")
                 .query("removeAmmoWeapons", input={"weaponTypeId": weapon_type_id, "ammoTypeId": ammo_type_id})
                 .generate())
        return self._call_service_method(query, expect_errors=expect_errors).get("removeAmmoWeapons")
