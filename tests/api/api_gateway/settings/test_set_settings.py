import allure
import aqas
import pytest
from faker import Faker

from models.api.api_gateway_adapter import ApiGatewayAdapter
from utils.enums import ScreenSizeEnum, WeaponModeEnum, StateEnum


@allure.parent_suite("api")
@allure.suite("HunterApi")
@allure.sub_suite("crud")
class TestsSettings:

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-410")
    @allure.title("set_shooting_mode")
    def test_set_shooting_mode(self):
        set_shooting_mode_input = {
            "setShootingMode": {
                "mode": {
                    "screenSize": ScreenSizeEnum.FULL,
                    "laneCount": Faker().random_int(1, 5),
                    "weaponMode": WeaponModeEnum.IMITATORS,
                    },
                },
            }
        with aqas.step("Отправка запроса с мутацией <setShootingMode>"):
            shooting_mode = ApiGatewayAdapter().mutation("setShootingMode", set_shooting_mode_input)
        with aqas.step("Проверка типа"):
            assert isinstance(shooting_mode["laneNumber"], int), "Ошибка тип не равен int"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-411")
    @allure.title("set_shooting_send_parameters")
    def test_set_shooting_send_parameters(self):
        set_shooting_send_parameters_input = {
            "set": Faker().random_int(1, 30),
            "elementsCount": Faker().random_int(1, 30)
            }
        with aqas.step("Отправка запроса с мутацией <setShootingSendParameters>"):
            shooting_send_parameters = ApiGatewayAdapter().mutation("setShootingSendParameters",
                                                                    set_shooting_send_parameters_input)
        with aqas.step("Проверка наличия ответа"):
            assert shooting_send_parameters == 1, "Не установлены настройки получения данных о выстрелах"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-412")
    @allure.title("set_state_to_lane")
    def test_set_state_to_lane(self):
        set_state_to_lane_input = {
            "state": StateEnum.STOP,
            "laneNumber": 1,
            }
        with aqas.step("Отправка запроса с мутацией <setStateToLane>"):
            state_to_lane = ApiGatewayAdapter().mutation("setStateToLane", set_state_to_lane_input)
        with aqas.step("Проверка типа"):
            assert isinstance(state_to_lane["laneNumber"], int), "Ошибка тип не равен int"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-413")
    @allure.title("set_instructor_to_lane")
    def test_set_instructor_to_lane(self):
        set_instructor_to_lane_input = {
            "instructorId": Faker().random_int(1, 5),
            "laneNumbers": [1]
            }
        with aqas.step("Отправка запроса с мутацией <setInstructorToLane>"):
            instructor_to_lane = ApiGatewayAdapter().mutation("setInstructorToLane", set_instructor_to_lane_input)
        with aqas.step("Проверка типа"):
            assert isinstance(instructor_to_lane["lane"], int), "Ошибка тип не равен int"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-414")
    @allure.title("set_zoom_target")
    def test_set_zoom_target(self):
        set_zoom_target_input = {
            "set": {

                "laneCount": Faker().random_int(1, 5),

                },
            }
        with aqas.step("Отправка запроса с мутацией <setZoomTarget>"):
            zoom_target = ApiGatewayAdapter().mutation("setZoomTarget", set_zoom_target_input)
        with aqas.step("Проверка типа"):
            assert isinstance(zoom_target["lane"], int), "Ошибка тип не равен int"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-415")
    @allure.title("set_display_shot_details")
    def test_set_display_shot_details(self):
        display_shot_details_input = {
            "set": {

                "laneCount": Faker().random_int(1, 5),

                },
            }
        with aqas.step("Отправка запроса с мутацией <setDisplayShotDetails>"):
            display_shot_details = ApiGatewayAdapter().mutation("setDisplayShotDetails", display_shot_details_input)
        with aqas.step("Проверка типа"):
            assert isinstance(display_shot_details["lane"], int), "Ошибка тип не равен int"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-416")
    @allure.title("select_shot")
    def test_select_shot(self):
        select_shot_input = {
            "set": {

                "laneCount": Faker().random_int(1, 5),

                },
            }
        with aqas.step("Отправка запроса с мутацией <selectShot>"):
            select_shot = ApiGatewayAdapter().mutation("selectShot", select_shot_input)
        with aqas.step("Проверка типа"):
            assert isinstance(select_shot["lane"], int), "Ошибка тип не равен int"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-417")
    @allure.title("run_task")
    def test_run_task(self):
        run_task_input = {
            "set": {
                "laneCount": Faker().random_int(1, 5),

                },
            }
        with aqas.step("Отправка запроса с мутацией <runTask>"):
            run_task = ApiGatewayAdapter().mutation("runTask", run_task_input)
        with aqas.step("Проверка типа"):
            assert isinstance(run_task["lane"], int), "Ошибка тип не равен int"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-418")
    @allure.title("stop_task")
    def test_stop_task(self):
        stop_task_input = {
            "set": {

                "laneCount": Faker().random_int(1, 5),

                },
            }
        with aqas.step("Отправка запроса с мутацией <stopTask>"):
            stop_task = ApiGatewayAdapter().mutation("stopTask", stop_task_input)
        with aqas.step("Проверка типа"):
            assert isinstance(stop_task["lane"], int), "Ошибка тип не равен int"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-442")
    @allure.title("set_instructor_to_lane")
    def test_(self):
        set_instructor_to_lane_input = {
            "set": {

                "laneCount": Faker().random_int(1, 5),

                },
            }
        with aqas.step("Отправка запроса с мутацией <setInstructorToLane>"):
            instructor_to_lane = ApiGatewayAdapter().mutation("setInstructorToLane", )
        with aqas.step("Проверка типа"):
            assert isinstance(instructor_to_lane["lane"], int), "Ошибка тип не равен int"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-443")
    @allure.title("install_content")
    def test_install_content(self):
        install_content_input = {
            "set": {

                "laneCount": Faker().random_int(1, 5),

                },
            }
        with aqas.step("Отправка запроса с мутацией <installContent>"):
            install_content = ApiGatewayAdapter().mutation("installContent", install_content_input)
        with aqas.step("Проверка типа"):
            assert isinstance(install_content["lane"], int), "Ошибка тип не равен int"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-444")
    @allure.title("install_full_exercise")
    def test_install_full_exercise(self):
        install_full_exercise_input = {
            "set": {

                "laneCount": Faker().random_int(1, 5),

                },
            }
        with aqas.step("Отправка запроса с мутацией <installFullExercise>"):
            install_full_exercise = ApiGatewayAdapter().mutation("installFullExercise", install_full_exercise_input)
        with aqas.step("Проверка типа"):
            assert isinstance(install_full_exercise["lane"], int), "Ошибка тип не равен int"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-445")
    @allure.title("")
    def test_export_exercise(self):
        export_exercise_input = {
            "set": {

                "laneCount": Faker().random_int(1, 5),

                },
            }
        with aqas.step("Отправка запроса с мутацией <exportExercise>"):
            export_exercise = ApiGatewayAdapter().mutation("exportExercise", export_exercise_input)
        with aqas.step("Проверка типа"):
            assert isinstance(export_exercise["lane"], int), "Ошибка тип не равен int"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-446")
    @allure.title("can_validate_user")
    def test_can_validate_user(self):
        can_validate_user_input = {
            "set": {
                "laneCount": Faker().random_int(1, 5),

                },
            }
        with aqas.step("Отправка запроса с мутацией <can_validate_user_input>"):
            can_validate_user = ApiGatewayAdapter().mutation("can_validate_user_input", can_validate_user_input)
        with aqas.step("Проверка типа"):
            assert isinstance(can_validate_user["lane"], int), "Ошибка тип не равен int"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-447")
    @allure.title("validate_user")
    def test_validate_user(self):
        validate_user_input = {
            "set": {

                "laneCount": Faker().random_int(1, 5),

                },
            }
        with aqas.step("Отправка запроса с мутацией <validate_user_input>"):
            validate_user = ApiGatewayAdapter().mutation("validate_user_input", validate_user_input)
        with aqas.step("Проверка типа"):
            assert isinstance(validate_user["lane"], int), "Ошибка тип не равен int"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-448")
    @allure.title("user_account_logout")
    def test_user_account_logout(self):
        user_account_logout_input = {
            "userId": 1
            }
        with aqas.step("Отправка запроса с мутацией Выхода из аккаунта пользователя <userAccountLogout>"):
            user_account_logout = ApiGatewayAdapter().mutation("userAccountLogout", user_account_logout_input)
        with aqas.step("Проверка типа"):
            assert isinstance(user_account_logout["id"], int), "Ошибка тип не равен int"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-449")
    @allure.title("user_statistics_report")
    def test_user_statistics_report(self):
        user_statistics_report_input = {
            "set": {

                "laneCount": Faker().random_int(1, 5),

                },
            }
        with aqas.step("Отправка запроса с мутацией <userStatisticsReport>"):
            user_statistics_report = ApiGatewayAdapter().mutation("userStatisticsReport", user_statistics_report_input)
        with aqas.step("Проверка типа"):
            assert isinstance(user_statistics_report["lane"], int), "Ошибка тип не равен int"
