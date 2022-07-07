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
        hunter_api_version = ApiGatewayAdapter().query("hunterApiVersion")
        assert isinstance(hunter_api_version[0], str), "Ошибка тип не равен str"
        assert hunter_api_version[0], "Нет ответа от запроса"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-383")
    @allure.title("units")
    def test_get_units(self):
        units = ApiGatewayAdapter().query("units")
        assert isinstance(units[0]["name"], str), "Ошибка тип не равен str"
        assert isinstance(units[0]["id"], int), "Ошибка тип не равен int"
        assert units[0]["id"], "Нет ответа от запроса"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-360")
    @allure.title("users")
    def test_get_users(self):
        users = ApiGatewayAdapter().query("users")
        assert isinstance(users[0]["id"], int), "Ошибка тип не равен int"
        assert users[0]["id"], "Нет ответа от запроса"
        assert isinstance(users[0]["shortName"], str), "Ошибка тип не равен str"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-384")
    @allure.title("screenSizes")
    def test_get_screen_sizes(self):
        screen_sizes = ApiGatewayAdapter().query("screenSizes")
        assert isinstance(screen_sizes[0]["id"], int), "Ошибка тип не равен int"
        assert isinstance(screen_sizes[0]["value"], str), "Ошибка тип не равен str"
        assert isinstance(screen_sizes[0]["maxLaneCount"], int), "Ошибка тип не равен int"
        assert isinstance(screen_sizes[0]["description"], str), "Ошибка тип не равен str"
        assert screen_sizes[0]["id"], "Нет ответа от запроса"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-378")
    @allure.title("performedExercises")
    def test_get_performed_exercises(self):
        performed_exercises = ApiGatewayAdapter().query("performedExercises")
        assert isinstance(performed_exercises[0]["id"], int), "Ошибка тип не равен int"
        assert performed_exercises[0]["id"], "Нет ответа от запроса"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-385")
    @allure.title("shooting")
    def test_get_shooting(self):
        shoot = {
            "shooting": {
                "laneNumber": 1
                }
            }
        shoot = ApiGatewayAdapter().query("shooting", shoot)
        assert isinstance(shoot["pageInfo"]["hasNextPage"], bool), "Ошибка тип не равен bool"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-371")
    @allure.title("shootingMode")
    def test_get_shooting_mode(self):
        shooting_mode = ApiGatewayAdapter().query("shootingMode")
        assert isinstance(shooting_mode["laneCount"], int), "Ошибка тип не равен int"
        assert isinstance(shooting_mode["screenSize"], str), "Ошибка тип не равен str"
        assert isinstance(shooting_mode["weaponMode"], str), "Ошибка тип не равен str"
        assert shooting_mode["screenSize"], "Нет ответа от запроса"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-363")
    @allure.title("laneDatas")
    def test_get_lane_datas(self):
        lane_datas = ApiGatewayAdapter().query("laneDatas")
        assert isinstance(lane_datas[0]["laneNumber"], int), "Ошибка тип не равен int"
        assert lane_datas[0]["laneNumber"], "Нет ответа от запроса"
        assert isinstance(lane_datas[0]["isBusy"], bool), "Ошибка тип не равен bool"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-361")
    @allure.title("availableWeapons")
    def test_get_available_weapons(self):
        available_weapons = ApiGatewayAdapter().query("availableWeapons")
        assert available_weapons, "Нет ответа от запроса"
        assert isinstance(available_weapons[0]["id"], int), "Ошибка тип не равен int"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-370")
    @allure.title("availableUsers")
    def test_get_available_users(self):
        available_users = ApiGatewayAdapter().query("availableUsers")
        assert isinstance(available_users[0]["id"], int), "Ошибка тип не равен int"
        assert available_users[0]["id"], "Нет ответа от запроса"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-367")
    @allure.title("startupApiVersion")
    def test_get_startup_api_version(self):
        startup_api_version = ApiGatewayAdapter().query("startupApiVersion")
        assert isinstance(startup_api_version, str), "Ошибка тип не равен str"
        assert startup_api_version[0], "Нет ответа от запроса"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-368")
    @allure.title("allTasks")
    def test_get_all_tasks(self):
        all_tasks = ApiGatewayAdapter().query("allTasks")
        assert isinstance(all_tasks[0]['name'], str), "Ошибка тип не равен str"
        assert all_tasks[0]["name"], "Нет ответа от запроса"


@allure.parent_suite("api")
@allure.suite("ExerciseApi")
@allure.sub_suite("queries")
class TestExerciseApiQueries:

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-376")
    @allure.title("exerciseApiVersion")
    def test_get_exercise_api_version(self):
        exercise_api_version = ApiGatewayAdapter().query("exerciseApiVersion")
        assert isinstance(exercise_api_version[0], str), "Ошибка тип не равен str"
        assert exercise_api_version[0], "Нет ответа от запроса"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-372")
    @allure.title("objectsByExerciseId")
    def test_get_objects_by_exercise_id(self):
        objects_by_exercise_id = ApiGatewayAdapter().query("objectsByExerciseId",
                                                           {"objectsByExerciseId": {"id": "1"}})
        assert isinstance(objects_by_exercise_id[0]["name"], str), "Ошибка тип не равен str"
        assert objects_by_exercise_id[0]["name"], "Нет ответа от запроса"
        assert isinstance(objects_by_exercise_id[0]["localizationName"], str), "Ошибка тип не равен str"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-373")
    @allure.title("exercises")
    def test_get_exercises(self):
        exercises = ApiGatewayAdapter().query("exercises")
        assert isinstance(exercises[0]["name"], str), "Ошибка. Имя пустое"
        assert isinstance(exercises[0]["localizationName"], str), "Ошибка тип не равен str"
        assert exercises[0]["id"], "Нет ответа от запроса"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-374")
    @allure.title("objects")
    def test_get_objects(self):
        objects = ApiGatewayAdapter().query("objects")
        assert isinstance(objects[0]["name"], str), "Ошибка. Имя пустое"
        assert isinstance(objects[0]["localizationName"], str), "Ошибка тип не равен str"
        assert objects, "Нет ответа от запроса"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-375")
    @allure.title("scenes")
    def test_get_scenes(self):
        scenes = ApiGatewayAdapter().query("scenes")
        assert scenes[0]["name"] != "null", "Ошибка. Имя пустое"
        assert scenes[0]["id"], "Нет ответа от запроса"
        assert isinstance(scenes[0]["guid"], str), "Ошибка тип не равен str"
        assert isinstance(scenes[0]["localizationName"], str), "Ошибка тип не равен str"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-382")
    @allure.title("restrictions")
    def test_get_environment_restrictions(self):
        restrictions = ApiGatewayAdapter().query("environmentRestrictions")
        assert isinstance(restrictions[0]["key"], str), "Ошибка тип не равен str"
        assert isinstance(restrictions[0]["value"], int), "Ошибка тип не равен int"
        assert restrictions[0]["id"], "Нет ответа от запроса"


@allure.parent_suite("api")
@allure.suite("WeaponsApi")
@allure.sub_suite("queries")
class TestWeaponsApiQueries:

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-362")
    @allure.title("weapons")
    def test_get_weapons(self):
        weapons = ApiGatewayAdapter().query("weapons")
        assert isinstance(weapons[0]["id"], int), "Ошибка тип не равен int"
        assert weapons[0]["id"], "Нет ответа от запроса"
        assert isinstance(weapons[0]["localizationName"], str), "Ошибка тип не равен str"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-366")
    @allure.title("weaponTypes")
    def test_get_weapon_types(self):
        with aqas.step("qwe"):
            weapon_types = ApiGatewayAdapter().query("weaponTypes")
        with aqas.step("Проверка типа id"):
            assert isinstance(weapon_types[0]["id"], str), "Ошибка тип не равен int"
            assert weapon_types[0]["id"], "Нет ответа от запроса"
            assert isinstance(weapon_types[0]["name"], str), "Ошибка тип не равен str"
            assert isinstance(weapon_types[0]["localizationName"], str), "Ошибка тип не равен str"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-365")
    @allure.title("ammoTypes")
    def test_get_ammo_types(self):
        ammo_types = ApiGatewayAdapter().query("ammoTypes")
        assert isinstance(ammo_types[0]["localizationName"], str), "Ошибка тип не равен str"
        assert ammo_types[0]["id"], "Нет ответа от запроса"
        assert isinstance(ammo_types[0]["id"], int), "Ошибка тип не равен int"
