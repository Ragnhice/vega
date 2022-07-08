import allure
import aqas
import pytest

from models.api.api_gateway_adapter import ApiGatewayAdapter


@allure.parent_suite("api")
@allure.suite("HunterApi")
@allure.sub_suite("queries")
class TestHunterApiQueries:

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-369")
    @allure.title("hunterApiVersion")
    def test_get_hunter_api_version(self):
        with aqas.step("qwe"):
            hunter_api_version = ApiGatewayAdapter().query("hunterApiVersion")
        with aqas.step("Проверка наличия ответа"):
            assert hunter_api_version[0], "Нет ответа от запроса"
        with aqas.step("Проверка типа"):
            assert isinstance(hunter_api_version[0], str), "Ошибка тип не равен str"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-383")
    @allure.title("units")
    def test_get_units(self):
        with aqas.step("qwe"):
            units = ApiGatewayAdapter().query("units")
        with aqas.step("Проверка наличия ответа"):
            assert units[0]["id"], "Нет ответа от запроса"
        with aqas.step("Проверка типа"):
            assert isinstance(units[0]["name"], str), "Ошибка тип не равен str"
        with aqas.step("Проверка типа"):
            assert isinstance(units[0]["id"], int), "Ошибка тип не равен int"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-360")
    @allure.title("users")
    def test_get_users(self):
        with aqas.step("qwe"):
            users = ApiGatewayAdapter().query("users")
        with aqas.step("Проверка наличия ответа"):
            assert users[0]["id"], "Нет ответа от запроса"
        with aqas.step("Проверка типа"):
            assert isinstance(users[0]["id"], int), "Ошибка тип не равен int"
        with aqas.step("Проверка типа"):
            assert isinstance(users[0]["shortName"], str), "Ошибка тип не равен str"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-384")
    @allure.title("screenSizes")
    def test_get_screen_sizes(self):
        with aqas.step("qwe"):
            screen_sizes = ApiGatewayAdapter().query("screenSizes")
        with aqas.step("Проверка наличия ответа"):
            assert screen_sizes[0]["id"], "Нет ответа от запроса"
        with aqas.step("Проверка типа"):
            assert isinstance(screen_sizes[0]["id"], int), "Ошибка тип не равен int"
        with aqas.step("Проверка типа"):
            assert isinstance(screen_sizes[0]["value"], str), "Ошибка тип не равен str"
        with aqas.step("Проверка типа"):
            assert isinstance(screen_sizes[0]["maxLaneCount"], int), "Ошибка тип не равен int"
        with aqas.step("Проверка типа"):
            assert isinstance(screen_sizes[0]["description"], str), "Ошибка тип не равен str"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-378")
    @allure.title("performedExercises")
    def test_get_performed_exercises(self):
        with aqas.step("qwe"):
            performed_exercises = ApiGatewayAdapter().query("performedExercises")
        with aqas.step("Проверка наличия ответа"):
            assert performed_exercises[0]["id"], "Нет ответа от запроса"
        with aqas.step("Проверка типа"):
            assert isinstance(performed_exercises[0]["id"], int), "Ошибка тип не равен int"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-385")
    @allure.title("shooting")
    def test_get_shooting(self):
        with aqas.step("qwe"):
            shoot = {"shooting": {"laneNumber": 1}}
            shoot = ApiGatewayAdapter().query("shooting", shoot)
        with aqas.step("Проверка типа"):
            assert isinstance(shoot["pageInfo"]["hasNextPage"], bool), "Ошибка тип не равен bool"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-371")
    @allure.title("shootingMode")
    def test_get_shooting_mode(self):
        with aqas.step("qwe"):
            shooting_mode = ApiGatewayAdapter().query("shootingMode")
        with aqas.step("Проверка наличия ответа"):
            assert shooting_mode["screenSize"], "Нет ответа от запроса"
        with aqas.step("Проверка типа"):
            assert isinstance(shooting_mode["laneCount"], int), "Ошибка тип не равен int"
        with aqas.step("Проверка типа"):
            assert isinstance(shooting_mode["screenSize"], str), "Ошибка тип не равен str"
        with aqas.step("Проверка типа"):
            assert isinstance(shooting_mode["weaponMode"], str), "Ошибка тип не равен str"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-363")
    @allure.title("laneDatas")
    def test_get_lane_datas(self):
        with aqas.step("qwe"):
            lane_datas = ApiGatewayAdapter().query("laneDatas")
        with aqas.step("Проверка наличия ответа"):
            assert lane_datas[0]["laneNumber"], "Нет ответа от запроса"
        with aqas.step("Проверка типа"):
            assert isinstance(lane_datas[0]["laneNumber"], int), "Ошибка тип не равен int"

        with aqas.step("Проверка типа"):
            assert isinstance(lane_datas[0]["isBusy"], bool), "Ошибка тип не равен bool"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-361")
    @allure.title("availableWeapons")
    def test_get_available_weapons(self):
        with aqas.step("qwe"):
            available_weapons = ApiGatewayAdapter().query("availableWeapons")
        with aqas.step("Проверка наличия ответа"):
            assert available_weapons, "Нет ответа от запроса"
        with aqas.step("Проверка типа"):
            assert isinstance(available_weapons[0]["id"], int), "Ошибка тип не равен int"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-370")
    @allure.title("availableUsers")
    def test_get_available_users(self):
        with aqas.step("qwe"):
            available_users = ApiGatewayAdapter().query("availableUsers")
        with aqas.step("Проверка наличия ответа"):
            assert available_users[0]["id"], "Нет ответа от запроса"
        with aqas.step("Проверка типа"):
            assert isinstance(available_users[0]["id"], int), "Ошибка тип не равен int"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-367")
    @allure.title("startupApiVersion")
    def test_get_startup_api_version(self):
        with aqas.step("qwe"):
            startup_api_version = ApiGatewayAdapter().query("startupApiVersion")
        with aqas.step("Проверка наличия ответа"):
            assert startup_api_version[0], "Нет ответа от запроса"
        with aqas.step("Проверка типа"):
            assert isinstance(startup_api_version, str), "Ошибка тип не равен str"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-368")
    @allure.title("allTasks")
    def test_get_all_tasks(self):
        with aqas.step("qwe"):
            all_tasks = ApiGatewayAdapter().query("allTasks")
        with aqas.step("Проверка наличия ответа"):
            assert all_tasks[0]["name"], "Нет ответа от запроса"
        with aqas.step("Проверка типа"):
            assert isinstance(all_tasks[0]["name"], str), "Ошибка тип не равен str"
