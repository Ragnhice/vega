import allure
import pytest

from models.api.startup_api_adapter import StartupApiAdapter


@allure.parent_suite("api")
@allure.suite("StartupApi")
@allure.sub_suite("queries")
class TestStartupApiQueries:

    @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-341")
    @pytest.mark.jira_issue("https://jira.steor.tech/browse/VEGA2-341")
    @allure.title("users")
    def test_get_users(self):
        users = StartupApiAdapter().get_query("users")
        assert isinstance(users[0]["id"], str), "Ошибка тип не равен str"
        assert users[0]["id"], "Нет ответа от запроса"

    @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-342")
    @pytest.mark.jira_issue("https://jira.steor.tech/browse/VEGA2-341")
    @allure.title("availableWeapons")
    def test_get_available_weapons(self):
        available_weapons = StartupApiAdapter().get_query("availableWeapons")
        assert available_weapons, "Нет ответа от запроса"

    @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-343")
    @pytest.mark.jira_issue("https://jira.steor.tech/browse/VEGA2-341")
    @allure.title("weapons")
    def test_get_weapons(self):
        weapons = StartupApiAdapter().get_query("weapons")
        assert isinstance(weapons[0]["id"], str), "Ошибка тип не равен str"

    @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-344")
    @pytest.mark.jira_issue("https://jira.steor.tech/browse/VEGA2-341")
    @allure.title("laneDatas")
    def test_get_lane_datas(self):
        lane_datas = StartupApiAdapter().get_query("laneDatas")
        assert isinstance(lane_datas[0]["laneNumber"], str), "Ошибка тип не равен str"

    @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-345")
    @pytest.mark.jira_issue("https://jira.steor.tech/browse/VEGA2-341")
    @allure.title("units")
    def test_get_units(self):
        units = StartupApiAdapter().get_query("units")
        assert isinstance(units[0]["id"], str), "Ошибка тип не равен str"

    @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-346")
    @pytest.mark.jira_issue("https://jira.steor.tech/browse/VEGA2-341")
    @allure.title("ammoTypes")
    def test_get_ammo_types(self):
        ammo_types = StartupApiAdapter().get_query("ammoTypes")
        assert isinstance(ammo_types[0]["id"], str), "Ошибка тип не равен str"

    @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-347")
    @pytest.mark.jira_issue("https://jira.steor.tech/browse/VEGA2-341")
    @allure.title("weaponTypes")
    def test_get_weapon_types(self):
        weapon_types = StartupApiAdapter().get_query("weaponTypes")
        assert isinstance(weapon_types[0]["id"], str), "Ошибка тип не равен str"

    @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-348")
    @pytest.mark.jira_issue("https://jira.steor.tech/browse/VEGA2-341")
    @allure.title("startupApiVersion")
    def test_get_startup_api_version(self):
        startup_api_version = StartupApiAdapter().get_query("startupApiVersion")
        assert isinstance(startup_api_version, str), "Ошибка тип не равен str"

    @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-349")
    @pytest.mark.jira_issue("https://jira.steor.tech/browse/VEGA2-341")
    @allure.title("allTasks")
    def test_get_all_tasks(self):
        all_tasks = StartupApiAdapter().get_query("allTasks")
        assert isinstance(all_tasks[0], str), "Ошибка тип не равен str"

    @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-350")
    @pytest.mark.jira_issue("https://jira.steor.tech/browse/VEGA2-341")
    @allure.title("hunterApiVersion")
    def test_get_hunter_api_version(self):
        hunter_api_version = StartupApiAdapter().get_query("hunterApiVersion")
        assert isinstance(hunter_api_version[0], str), "Ошибка тип не равен str"

    @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-351")
    @pytest.mark.jira_issue("https://jira.steor.tech/browse/VEGA2-341")
    @allure.title("availableUsers")
    def test_get_available_users(self):
        available_users = StartupApiAdapter().get_query("availableUsers")
        assert isinstance(available_users[0]["id"], str), "Ошибка тип не равен str"

    @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-352")
    @pytest.mark.jira_issue("https://jira.steor.tech/browse/VEGA2-341")
    @allure.title("shootingMode")
    def test_get_shooting_mode(self):
        shooting_mode = StartupApiAdapter().get_query("shootingMode")
        assert isinstance(shooting_mode["laneCount"], str), "Ошибка тип не равен str"

    @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-353")
    @pytest.mark.jira_issue("https://jira.steor.tech/browse/VEGA2-341")
    @allure.title("objectsByExerciseId")
    def test_get_objects_by_exercise_id(self):
        objects_by_exercise_id = StartupApiAdapter().get_query("objectsByExerciseId",
                                                               {"objectsByExerciseId": {"id": "1"}})
        assert isinstance(objects_by_exercise_id[0]["id"], str), "Ошибка тип не равен str"

    @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-354")
    @pytest.mark.jira_issue("https://jira.steor.tech/browse/VEGA2-341")
    @allure.title("exercises")
    def test_get_exercises(self):
        exercises = StartupApiAdapter().get_query("exercises")
        assert isinstance(exercises[0]["name"], str), "Ошибка. Имя пустое"

    @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-355")
    @pytest.mark.jira_issue("https://jira.steor.tech/browse/VEGA2-341")
    @allure.title("objects")
    def test_get_objects(self):
        objects = StartupApiAdapter().get_query("objects")
        assert isinstance(objects[0]["name"], str), "Ошибка. Имя пустое"
        assert objects, "Нет ответа от запроса"

    @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-356")
    @pytest.mark.jira_issue("https://jira.steor.tech/browse/VEGA2-341")
    @allure.title("scenes")
    def test_get_scenes(self):
        scenes = StartupApiAdapter().get_query("scenes")
        assert scenes[0]["name"] != "null", "Ошибка. Имя пустое"

    @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-357")
    @pytest.mark.jira_issue("https://jira.steor.tech/browse/VEGA2-341")
    @allure.title("exerciseApiVersion")
    def test_get_exercise_api_version(self):
        exercise_api_version = StartupApiAdapter().get_query("exerciseApiVersion")
        assert isinstance(exercise_api_version[0], str), "Ошибка тип не равен str"

    @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-358")
    @pytest.mark.jira_issue("https://jira.steor.tech/browse/VEGA2-341")
    @allure.title("screenSizes")
    def test_get_screen_sizes(self):
        screen_sizes = StartupApiAdapter().get_query("screenSizes")
        assert isinstance(screen_sizes[0]["id"], str), "Ошибка тип не равен str"


    @pytest.mark.skip(reason="no way of currently testing this")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-359")
    @pytest.mark.jira_issue("https://jira.steor.tech/browse/VEGA2-341")
    @allure.title("performedExercises")
    def test_get_performed_exercises(self):
        performed_exercises = StartupApiAdapter().get_query("performedExercises")
        assert isinstance(performed_exercises[0]["id"], str), "Ошибка тип не равен str"
