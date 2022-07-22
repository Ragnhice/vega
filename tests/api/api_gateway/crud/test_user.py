import allure
import aqas
import pytest
from faker import Faker

from models.api.api_gateway_adapter import ApiGatewayAdapter
from utils.constants import API
from utils.enums import Gender, UserTypeEnum


@allure.parent_suite("api")
@allure.suite("HunterApi")
@allure.sub_suite("crud")
class TestsCrudUser:
    USER_ID = ""
    USER_NAME = ""
    ANONYM_USER_ID = ""

    @pytest.mark.dependency()
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-379")
    @allure.title("create_user")
    def test_create_user(self):
        TestsCrudUser.USER_NAME = Faker().first_name()
        user = {
            "createUser": {
                "userInput": {
                    "firstName": TestsCrudUser.USER_NAME,
                    "middleName": Faker().first_name(),
                    "lastName": Faker().last_name(),
                    "height": Faker().random_int(),
                    "birthCity": Faker().city(),
                    "birthDate": Faker().date(),
                    "appointment": Faker().domain_word(),
                    "personalId": Faker().isbn10(),
                    "title": Faker().isbn10(),
                    "archived": True,
                    "memo": Faker().isbn10(),
                    "role": UserTypeEnum.SHOOTER,
                    "gender": Gender.MALE,
                    "login": Faker().first_name(),
                    "password": API.TEST_PASSWORD_1,
                },
            },
        }
        user = ApiGatewayAdapter().mutation("createUser", user)
        assert isinstance(user["id"], int)
        TestsCrudUser.USER_ID = user["id"]

    @pytest.mark.dependency(depends=["test_create_user"], scope="class")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-380")
    @allure.title("update_user")
    def test_update_user(self):
        user = {
            "updateUser": {
                "userInput": {
                    "id": TestsCrudUser.USER_ID,
                    "firstName": Faker().first_name(),
                    "middleName": Faker().first_name(),
                    "lastName": Faker().last_name(),
                    "height": Faker().random_int(),
                    "birthCity": Faker().city(),
                    "birthDate": Faker().date(),
                    "appointment": Faker().domain_word(),
                    "personalId": Faker().isbn10(),
                    "title": Faker().isbn10(),
                    "archived": True,
                    "memo": Faker().isbn10(),
                    "role": UserTypeEnum.SHOOTER,
                    "gender": Gender.MALE,
                    "login": Faker().first_name(),
                    "password": API.TEST_PASSWORD_2,
                },
            },
        }
        user = ApiGatewayAdapter().mutation("updateUser", user)
        assert TestsCrudUser.USER_NAME != user["firstName"], "Пользователь не обновился"

    @pytest.mark.dependency()
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-419")
    @allure.title("create_anonymous_user")
    def test_create_anonymous_user(self):
        with aqas.step("Отправка запроса с мутацией"):
            user = ApiGatewayAdapter().mutation("addAnonymousUser")
        with aqas.step("Сохраняем полученые данные в переменные"):
            TestsCrudUser.ANONYM_USER_ID = user["id"]
        with aqas.step("Проверка типа"):
            assert isinstance(user["id"], int)
        with aqas.step("Проверка типа"):
            assert isinstance(user["height"], float)
        with aqas.step("Проверка типа"):
            assert isinstance(user["archived"], bool)
        with aqas.step("Проверка типа"):
            assert isinstance(user["shortName"], str)
        with aqas.step("Проверка типа"):
            assert isinstance(user["lastName"], str)
        with aqas.step("Проверка приcвоенного аргумента"):
            assert str(user["role"]) == API.ROLE[0], "Назначенная роль не стрелок"

    @pytest.mark.dependency(depends=["test_create_user"], scope="class")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-381")
    @allure.title("delete_user")
    def test_delete_user(self):
        result = ApiGatewayAdapter().remove_users_by_id([TestsCrudUser.USER_ID])
        with aqas.step("Проверка наличия ответа"):
            assert result == 1, "Пользователи не удалены"
