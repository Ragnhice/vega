from random import choice
from typing import Union

import aqas
from faker import Faker

from utils.constants import API


class ApiGatewayAdapter(aqas.GraphQLDataAdapter):

        """Добавляет оружие."""
        mutation = f"""
            mutation createWeapon {{
                createWeapon(
                    weaponInput: {{
                        firstName: "{Faker().first_name()}",
                        middleName: "{Faker().first_name()}",
                        lastName: "{Faker().last_name()}",
                        height: {Faker().random_int(1, 100)},
                        birthCity: "{Faker().city()}",
                        birthDate: "05.11.1991",
                        appointment: "String",
                        personalId: "String",
                        title: "String",
                        memo: "String",
                        archived: true,
                        gender: {choice(API.GENDER)},
                        role: {choice(API.ROLE)},
                        login: "{login}",
                        password: "{password}"
                    }})
                {{
                    id
                    shortName
                    firstName
                }}
            }}
        """
        response = self._call_service_method(mutation, expect_errors=expect_errors)
        return response.get("createUser")

    def update_user(self, user_id_to_update, expect_errors: Union[bool, type(None)] = False):
        """Обновляет пользователя."""
        mutation = f"""
            mutation {{
                updateUser(
                    userInput: {{
                        id: {user_id_to_update},
                        firstName: "{Faker().first_name()}",
                        middleName: "{Faker().first_name()}",
                        lastName: "{Faker().last_name()}",
                        height: {Faker().random_int(1, 100)},
                        birthCity: "{Faker().city()}",
                        birthDate: "05.11.1991",
                        appointment: "String",
                        personalId: "String",
                        title: "String",
                        archived: true,
                        memo: "String",
                        gender: {choice(API.GENDER)},
                        role: {choice(API.ROLE)},
                    }})
                {{
                    id
                    shortName
                    firstName
                    middleName
                    lastName
                    height
                    birthCity
                    birthDate
                    appointment
                    dutyDate
                    personalId
                    title
                    archived
                    memo
                    role
                }}
            }}
        """
        response = self._call_service_method(mutation, expect_errors=expect_errors)
        return response.get("updateUser")

    def remove_users_by_id(self, user_ids: list, expect_errors: Union[bool, type(None)] = False):
        """Удаляет пользователей по id.
        :param: user_ids - идентификаторы пользователей
        """
        query = (self.query_builder()
                 .operation("mutation")
                 .query("removeUsersById", input={"userIds": user_ids})
                 .generate())
        return self._call_service_method(query, expect_errors=expect_errors).get("removeUsersById")













    def __init__(self):
        super().__init__("ApiGateway")
        self.recursion_list = []

    # region Mutation's
    def create_user(self,
                    login: str = "admin",
                    password: str = "0000",
                    expect_errors: Union[bool, type(None)] = False,
                    ):
        """Создает пользователя."""
        mutation = f"""
            mutation createUser {{
                createUser(
                    userInput: {{
                        firstName: "{Faker().first_name()}",
                        middleName: "{Faker().first_name()}",
                        lastName: "{Faker().last_name()}",
                        height: {Faker().random_int(1, 100)},
                        birthCity: "{Faker().city()}",
                        birthDate: "05.11.1991",
                        appointment: "String",
                        personalId: "String",
                        title: "String",
                        memo: "String",
                        archived: true,
                        gender: {choice(API.GENDER)},
                        role: {choice(API.ROLE)},
                        login: "{login}",
                        password: "{password}"
                    }})
                {{
                    id
                    shortName
                    firstName
                }}
            }}
        """
        response = self._call_service_method(mutation, expect_errors=expect_errors)
        return response.get("createUser")

    def update_user(self, user_id_to_update, expect_errors: Union[bool, type(None)] = False):
        """Обновляет пользователя."""
        mutation = f"""
            mutation {{
                updateUser(
                    userInput: {{
                        id: {user_id_to_update},
                        firstName: "{Faker().first_name()}",
                        middleName: "{Faker().first_name()}",
                        lastName: "{Faker().last_name()}",
                        height: {Faker().random_int(1, 100)},
                        birthCity: "{Faker().city()}",
                        birthDate: "05.11.1991",
                        appointment: "String", 
                        personalId: "String",
                        title: "String",
                        archived: true,
                        memo: "String",
                        gender: {choice(API.GENDER)},
                        role: {choice(API.ROLE)},
                    }})
                {{
                    id
                    shortName
                    firstName
                    middleName
                    lastName
                    height
                    birthCity
                    birthDate
                    appointment
                    dutyDate
                    personalId
                    title
                    archived
                    memo
                    role
                }}
            }}
        """
        response = self._call_service_method(mutation, expect_errors=expect_errors)
        return response.get("updateUser")

    # endregion

    # region Queries
    def get_version(self, expect_errors: Union[bool, type(None)] = False):
        """Получает текущую версию сервиса."""
        response = self._call_service_method(
            """
                query {
                    startupApiVersion
                }
             """, expect_errors=expect_errors)
        return response

    def get_users(self, expect_errors: Union[bool, type(None)] = False):
        """Получает список пользователей."""
        query = (self.query_builder()
                 .operation()
                 .query("users")
                 .fields(["id", "shortName", "firstName", "middleName", "lastName"])
                 .generate())
        return self._call_service_method(query, expect_errors=expect_errors).get("users")

    def get_objects_by_exercise_id(self, expect_errors: Union[bool, type(None)] = False):
        """Объекты использующиеся в упражнении с заданным номером."""
        query = (self.query_builder()
                 .operation()
                 .query("users")
                 .fields(["name", "localizationName", "guid", "prefab", "image"])
                 .generate())
        return self._call_service_method(query, expect_errors=expect_errors).get("objectsByExerciseId")

    def get_exercises(self, expect_errors: Union[bool, type(None)] = False):
        """Получает список упражнений."""
        response = self._call_service_method(
            """
                query {
                    exercises {
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
        """Доступные объекты."""
        query = (self.query_builder()
                 .operation()
                 .query("objects")
                 .fields(["name", "localizationName", "guid", "prefab", "image"])
                 .generate())
        return self._call_service_method(query, expect_errors=expect_errors).get("objects")

    def get_objects_2(self, expect_errors: Union[bool, type(None)] = False):
        """Доступные объекты."""
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

    # endregion

    # region Mutation's
    def create_weapon(self, expect_errors: Union[bool, type(None)] = False):
        """Создает пользователя."""

        mutation = f"""
            mutation CreateWeapon_1
($weaponInput: CreateWeaponInput)
{{
    createWeapon(weaponInput: {{"weaponInput":
{{
"id": 123,
"hwid": 123 ,
"regDate": "{{$isoTimestamp}}",  
"shotsCount": {{shotsCount_CreateWeapon_1}},
"typeId": {{typeId_CreateWeapon_1}},
"mode": "{{mode_CreateWeapon_1}}"
     
}}
}}){{
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


    def remove_users_by_id(self, user_ids: list, expect_errors: Union[bool, type(None)] = False):
        """Удаляет пользователей по id.
        :param: user_ids - идентификаторы пользователей
        """
        query = (self.query_builder()
                 .operation("mutation")
                 .query("removeUsersById", input={"userIds": user_ids})
                 .generate())
        return self._call_service_method(query, expect_errors=expect_errors).get("removeUsersById")


    def get_object_3(self, expect_errors: Union[bool, type(None)] = False):
        response = self._call_service_method(
            """
                query {
                    objects {
                        name
                        localizationName
                        guid
                        prefab
                        image
                        availableCommands {
                            id
                            name
                            localizationName
                            parameters
                        }                       
                    }
                }
            """, expect_errors=expect_errors)
        return response.get("objects")