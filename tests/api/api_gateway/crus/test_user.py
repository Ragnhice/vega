import allure
import pytest
from faker import Faker

from models.api.api_gateway_adapter import ApiGatewayAdapter
from utils.enums import UserTypeEnum, Gender


@allure.parent_suite("api")
@allure.suite("ApiGateway")
@allure.sub_suite("crus")
class TestsStartupApiUser:
    USER_ID = ""
    USER_NAME = ""
    WEAPON_ID = ""

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-379")
    @allure.title("create_user_new")
    def test_create_user(self):
        TestsStartupApiUser.USER_NAME = Faker().first_name()
        user = {
            "createUser": {
                "userInput":
                    {
                        "firstName": TestsStartupApiUser.USER_NAME,
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
                        "login": "qa",
                        "password": "1111"
                        }
                }
            }
        user = ApiGatewayAdapter().mutation("createUser", user)
        assert isinstance(user["id"], int)
        TestsStartupApiUser.USER_ID = user["id"]

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-381")
    @allure.title("update_user")
    def test_update_user(self):
        user = {
            "updateUser": {
                "userInput":
                    {
                        "id": TestsStartupApiUser.USER_ID,
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
                        "login": "testlogin",
                        "password": "1111"
                        }
                }
            }
        user = ApiGatewayAdapter().mutation("updateUser", user)
        assert TestsStartupApiUser.USER_NAME != user['firstName'], "Пользователь не обновился"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-362")
    @allure.title("remove_user")
    def test_remove_user(self):
        result = ApiGatewayAdapter().remove_users_by_id([TestsStartupApiUser.USER_ID])
        assert result == 1, "Пользователи не удалены"
