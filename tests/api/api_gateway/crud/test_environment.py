import allure
import aqas
import pytest
from faker import Faker

from models.api.api_gateway_adapter import ApiGatewayAdapter
from utils.constants import API
from utils.enums import PrecipitationEnum, SeasonEnum, ShooterPositionEnum


@allure.parent_suite("api")
@allure.suite("ExerciseApi")
@allure.sub_suite("crud")
class TestsCrudEnvironment:

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-403")
    @allure.title("change_exercise_environment")
    def test_change_exercise_environment(self):
        change_environment_input = {
            "changeExerciseEnvironment": {
                "environment": {
                    "season": SeasonEnum.SUMMER,
                    "shooterPosition": ShooterPositionEnum.STAY,
                    "hour": Faker().pyfloat(min_value=0, max_value=23),
                    "precipitation": PrecipitationEnum.MIDDLE,
                    "visibility": Faker().pyfloat(min_value=0, max_value=4000),
                    "temperature": Faker().pyfloat(min_value=-50, max_value=50),
                    "pressure": Faker().pyfloat(min_value=700, max_value=800),
                    "windDirection": Faker().pyfloat(min_value=0, max_value=360),
                    "windSpeed": Faker().pyfloat(min_value=0, max_value=30),
                    "humidity": Faker().pyfloat(min_value=1, max_value=50),
                    "altitude": Faker().pyfloat(min_value=1, max_value=50),
                },
                "laneNumber": 1,
            },
        }
        with aqas.step("Отправка запроса с мутацией <changeExerciseEnvironment>"):
            change_environment = ApiGatewayAdapter().mutation("changeExerciseEnvironment", change_environment_input)
        with aqas.step("Проверка типа"):
            assert isinstance(change_environment["laneNumber"], int), "Ошибка тип не равен int"
        with aqas.step("Проверка типа"):
            assert isinstance(change_environment["exerciseId"], int), "Ошибка тип не равен int"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-404")
    @allure.title("update_exercise_environment")
    def test_update_environment(self):
        update_environment_input = {
            "updateEnvironment": {
                "input": {
                    "exerciseId": API.EX_ID_SHOOTING_RANGE,
                    "season": SeasonEnum.WINTER,
                    "shooterPosition": ShooterPositionEnum.STAY,
                    "hour": Faker().pyfloat(min_value=0, max_value=23),
                    "precipitation": PrecipitationEnum.MIDDLE,
                    "visibility": Faker().pyfloat(min_value=0, max_value=4000),
                    "temperature": Faker().pyfloat(min_value=-50, max_value=50),
                    "pressure": Faker().pyfloat(min_value=700, max_value=800),
                    "windDirection": Faker().pyfloat(min_value=0, max_value=360),
                    "windSpeed": Faker().pyfloat(min_value=0, max_value=30),
                    "humidity": Faker().pyfloat(min_value=1, max_value=50),
                    "altitude": Faker().pyfloat(min_value=1, max_value=50),
                    "hitLimit": Faker().random_int(1, 50),
                    "targetLimit": Faker().random_int(1, 50),
                    "scoreLimit": Faker().random_int(1, 50),
                    "tracerEveryNShot": Faker().random_int(1, 50),
                },
            },
        }
        with aqas.step("Отправка запроса с мутацией <updateEnvironment>"):
            update_environment = ApiGatewayAdapter().mutation("updateEnvironment", update_environment_input)
        with aqas.step("Проверка типа"):
            assert isinstance(update_environment["hour"], int), "Ошибка тип не равен int"
        with aqas.step("Проверка типа"):
            assert isinstance(update_environment["exerciseId"], int), "Ошибка тип не равен int"
