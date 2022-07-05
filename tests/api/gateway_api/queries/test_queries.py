import allure
import aqas
import pytest

from models.api.startup_api_adapter import GatewayApiAdapter


@allure.parent_suite("api")
@allure.suite("StartupApi")
@allure.sub_suite("queries")
class TestStartupApiQueries:

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-341")
    @allure.title("users")
    def test_get_users(self):
        users = GatewayApiAdapter().query("users")
        assert isinstance(users[0]["id"], int), "Ошибка тип не равен int"
        assert users[0]["id"], "Нет ответа от запроса"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-342")
    @allure.title("availableWeapons")
    def test_get_available_weapons(self):
        available_weapons = GatewayApiAdapter().query("availableWeapons")
        assert available_weapons, "Нет ответа от запроса"

    @allure.title("weapons")
    def test_get_weapons(self):
        weapons = GatewayApiAdapter().query("weapons")
        assert isinstance(weapons[0]["id"], int), "Ошибка тип не равен int"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-344")
    @allure.title("laneDatas")
    def test_get_lane_datas(self):
        lane_datas = GatewayApiAdapter().query("laneDatas")
        assert isinstance(lane_datas[0]["laneNumber"], str), "Ошибка тип не равен str"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-345")
    @allure.title("units")
    def test_get_units(self):
        units = GatewayApiAdapter().query("units")
        assert isinstance(units[0]["id"], str), "Ошибка тип не равен str"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-346")
    @allure.title("ammoTypes")
    def test_get_ammo_types(self):
        ammo_types = GatewayApiAdapter().query("ammoTypes")
        assert isinstance(ammo_types[0]["id"], str), "Ошибка тип не равен str"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-347")
    @allure.title("weaponTypes")
    def test_get_weapon_types(self):
        with aqas.step("qwe"):
            weapon_types = GatewayApiAdapter().query("weaponTypes")
        with aqas.step("Проверка типа id"):
            assert isinstance(weapon_types[0]["id"], str), "Ошибка тип не равен int"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-348")
    @allure.title("startupApiVersion")
    def test_get_startup_api_version(self):
        startup_api_version = GatewayApiAdapter().query("startupApiVersion")
        assert isinstance(startup_api_version, str), "Ошибка тип не равен str"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-349")
    #
    @allure.title("allTasks")
    def test_get_all_tasks(self):
        all_tasks = GatewayApiAdapter().query("allTasks")
        assert isinstance(all_tasks[0]['name'], str), "Ошибка тип не равен str"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-350")
    @allure.title("hunterApiVersion")
    def test_get_hunter_api_version(self):
        hunter_api_version = GatewayApiAdapter().query("hunterApiVersion")
        assert isinstance(hunter_api_version[0], str), "Ошибка тип не равен str"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-351")
    # 
    @allure.title("availableUsers")
    def test_get_available_users(self):
        available_users = GatewayApiAdapter().query("availableUsers")
        assert isinstance(available_users[0]["id"], str), "Ошибка тип не равен str"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-352")
    @allure.title("shootingMode")
    def test_get_shooting_mode(self):
        shooting_mode = GatewayApiAdapter().query("shootingMode")
        assert isinstance(shooting_mode["laneCount"], str), "Ошибка тип не равен str"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-353")
    @allure.title("objectsByExerciseId")
    def test_get_objects_by_exercise_id(self):
        objects_by_exercise_id = GatewayApiAdapter().query("objectsByExerciseId",
                                                           {"objectsByExerciseId": {"id": "1"}})
        assert isinstance(objects_by_exercise_id[0]["id"], str), "Ошибка тип не равен str"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-354")
    @allure.title("exercises")
    def test_get_exercises(self):
        exercises = GatewayApiAdapter().query("exercises")
        assert isinstance(exercises[0]["name"], str), "Ошибка. Имя пустое"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-355")
    @allure.title("objects")
    def test_get_objects(self):
        objects = GatewayApiAdapter().query("objects")
        assert isinstance(objects[0]["name"], str), "Ошибка. Имя пустое"
        assert objects, "Нет ответа от запроса"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-356")
    @allure.title("scenes")
    def test_get_scenes(self):
        scenes = GatewayApiAdapter().query("scenes")
        assert scenes[0]["name"] != "null", "Ошибка. Имя пустое"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-357")
    @allure.title("exerciseApiVersion")
    def test_get_exercise_api_version(self):
        exercise_api_version = GatewayApiAdapter().query("exerciseApiVersion")
        assert isinstance(exercise_api_version[0], str), "Ошибка тип не равен str"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-358")
    @allure.title("screenSizes")
    def test_get_screen_sizes(self):
        screen_sizes = GatewayApiAdapter().query("screenSizes")
        assert isinstance(screen_sizes[0]["id"], str), "Ошибка тип не равен str"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-359")
    @allure.title("performedExercises")
    def test_get_performed_exercises(self):
        performed_exercises = GatewayApiAdapter().query("performedExercises")
        assert isinstance(performed_exercises[0]["id"], str), "Ошибка тип не равен str"
