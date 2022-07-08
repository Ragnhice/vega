import allure
import aqas
import pytest

from models.api.api_gateway_adapter import ApiGatewayAdapter


@allure.parent_suite("api")
@allure.suite("ExerciseApi")
@allure.sub_suite("queries")
class TestExerciseApiQueries:

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-376")
    @allure.title("exerciseApiVersion")
    def test_get_exercise_api_version(self):
        with aqas.step("qwe"):
            exercise_api_version = ApiGatewayAdapter().query("exerciseApiVersion")
        with aqas.step("Проверка наличия ответа"):
            assert exercise_api_version[0], "Нет ответа от запроса"
        with aqas.step("Проверка типа"):
            assert isinstance(exercise_api_version[0], str), "Ошибка тип не равен str"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-373")
    @allure.title("get_exercises")
    def test_get_exercises(self):
        with aqas.step("qwe"):
            exercises = ApiGatewayAdapter().query("exercises")
        with aqas.step("Проверка наличия ответа"):
            assert exercises[0], "Нет ответа от запроса"
        with aqas.step("Проверка наличия поля"):
            assert isinstance(exercises[0]["name"], str), "Ошибка. Имя пустое"
        with aqas.step("Проверка типа"):
            assert isinstance(exercises[0]["scene"]["localizationName"], str), "Ошибка тип не равен str"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-374")
    @allure.title("objects")
    def test_get_objects(self):
        with aqas.step("qwe"):
            objects = ApiGatewayAdapter().query("objects")
        with aqas.step("Проверка наличия ответа"):
            assert objects, "Нет ответа от запроса"
        with aqas.step("Проверка наличия поля"):
            assert isinstance(objects[0]["name"], str), "Ошибка. Имя пустое"
        with aqas.step("Проверка типа"):
            assert isinstance(objects[0]["localizationName"], str), "Ошибка тип не равен str"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-375")
    @allure.title("scenes")
    def test_get_scenes(self):
        with aqas.step("qwe"):
            scenes = ApiGatewayAdapter().query("scenes")
        with aqas.step("Проверка наличия ответа"):
            assert scenes[0]["name"], "Нет ответа от запроса"
        with aqas.step("Проверка наличия поля"):
            assert scenes[0]["name"] != "null", "Ошибка. Имя пустое"
        with aqas.step("Проверка типа"):
            assert isinstance(scenes[0]["guid"], str), "Ошибка тип не равен str"
        with aqas.step("Проверка типа"):
            assert isinstance(scenes[0]["localizationName"], str), "Ошибка тип не равен str"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-382")
    @allure.title("restrictions")
    def test_get_environment_restrictions(self):
        with aqas.step("qwe"):
            result = ApiGatewayAdapter().environment_restrictions()
        with aqas.step("Проверка наличия ответа"):
            assert result[0]["key"], "Нет ответа от запроса"
        with aqas.step("Проверка типа"):
            assert isinstance(result[0]["key"], str), "Ошибка тип не равен str"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-372")
    @allure.title("objectsByExerciseId")
    def test_get_objects_by_exercise_id(self):
        with aqas.step("qwe"):
            objects_by_exercise_id = ApiGatewayAdapter().objects_by_exercise_id()
        with aqas.step("Проверка наличия ответа"):
            assert objects_by_exercise_id[0]["name"], "Нет ответа от запроса"
        with aqas.step("Проверка типа"):
            assert isinstance(objects_by_exercise_id[0]["name"], str), "Ошибка тип не равен str"
        with aqas.step("Проверка типа"):
            assert isinstance(objects_by_exercise_id[0]["localizationName"], str), "Ошибка тип не равен str"
