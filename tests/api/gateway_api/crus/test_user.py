import allure
import pytest
from faker import Faker

from models.api.startup_api_adapter import GatewayApiAdapter
from utils.enums import UserTypeEnum


@allure.parent_suite("api")
@allure.suite("GatewayApi")
@allure.sub_suite("crus")
class TestsStartupApiUser:
    USER_ID = ""
    USER_NAME = ""

    # @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-360")
    # @allure.title("create_user_old")
    # def test_create_user(self):
    #     user = GatewayApiAdapter().create_user()
    #     assert isinstance(user["id"], int)

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-360")
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
                        # "birthDate": "{{$isoTimestamp}}",
                        # "appointment": "String",
                        # "personalId": "String",
                        # "title": "String",
                        "archived": True,
                        # "memo": "String",
                        "role": UserTypeEnum.SHOOTER,
                        # "sportsCategory": "{{$randomInt}}",
                        # "ageGroup": "{{$randomInt}}",
                        # "gender": "{{gender_createUser_1}}",
                        "login": "qa",
                        "password": "1111"
                        }
                }
            }
        user = GatewayApiAdapter().mutation("createUser", user)
        assert isinstance(user["id"], int)
        TestsStartupApiUser.USER_ID = user["id"]

    # @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-361")
    # @allure.title("update_user")
    # def test_update_user(self):
    #     user = GatewayApiAdapter().create_user()
    #     user_id_1 = user["id"]
    #     user_updated = GatewayApiAdapter().update_user(user_id_1)
    #     assert user_updated["id"] == user_id_1, "Пользователь не обновился"
    #     assert user_updated["shortName"] != user["shortName"], "Пользователь не обновился"
    #     assert user_updated["firstName"] != user["firstName"], "Пользователь не обновился"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-361")
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
                        # "birthDate": "{{$isoTimestamp}}",
                        # "appointment": "String",
                        # "personalId": "String",
                        # "title": "String",
                        "archived": True,
                        # "memo": "String",
                        "role": UserTypeEnum.SHOOTER,
                        # "sportsCategory": "{{$randomInt}}",
                        # "ageGroup": "{{$randomInt}}",
                        # "gender": "{{gender_createUser_1}}",
                        "login": "qa",
                        "password": "1111"
                        }
                }
            }
        user = GatewayApiAdapter().mutation("updateUser", user)
        assert TestsStartupApiUser.USER_NAME != user['firstName'], "Пользователь не обновился"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-362")
    @allure.title("remove_user")
    def test_remove_user(self):
        users = {"removeUsersById": {"userIds": [TestsStartupApiUser.USER_ID]}}
        result = GatewayApiAdapter().mutation("removeUsersById", users)
        assert TestsStartupApiUser.USER_ID in result["UserIds"], "Пользователь не удалён"
