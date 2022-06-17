from random import choice
from typing import Union

from faker import Faker

from models.api.gql_adapter import GraphQLDataAdapter
from utils import Singleton


class StartupApiAdapterMutation(GraphQLDataAdapter, metaclass=Singleton):
    def __init__(self):
        super().__init__()
        self.base_url = "http://10.10.72.214"
        self.port = "5050"

    def create_user(self, expect_errors: Union[bool, type(None)] = False):
        """
        Создает пользователя
        """
        role = ["SHOOTER", "INSTRUCTOR", "ADMINISTRATOR"]
        mutation = f"""
        mutation {{ createUser(userInput: 
              {{firstName: "{Faker().first_name()}",
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
                role: {choice(role)},
                gender: MALE
                }})
              {{ id shortName firstName }}
               }}
        """
        response = self._call_service_method(mutation, expect_errors=expect_errors)
        return response.get('createUser')

    def update_user(self, user_id_to_update, expect_errors: Union[bool, type(None)] = False):
        """
        Обновляет пользователя
        """
        role = ["SHOOTER", "INSTRUCTOR", "ADMINISTRATOR"]
        gender = ["FEMALE", "MALE", ]
        mutation = f"""
        mutation {{ updateUser(userInput: 
              {{id :  {user_id_to_update},
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
                role: {choice(role)},
                gender: {choice(gender)},
                }})
              {{ id
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
      role }}
               }}
        """
        response = self._call_service_method(mutation, expect_errors=expect_errors)
        return response.get('updateUser')
