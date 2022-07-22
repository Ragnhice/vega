from random import choice

import allure
import aqas
import pytest
from faker import Faker

from models.api.api_gateway_adapter import ApiGatewayAdapter
from utils.constants import API
from utils.enums import ExTypeEnum, PrecipitationEnum, SeasonEnum, ShooterPositionEnum


@allure.parent_suite("api")
@allure.suite("ExerciseApi")
@allure.sub_suite("crud")
class TestsCrudExercise:
    EXERCISE_ID = ""

    @pytest.mark.dependency()
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-402")
    @allure.title("create_exercise")
    def test_create_exercise(self):
        create_exercise_input = {
            "addExercise": {
                "exerciseCreateInput": {
                    "name": Faker().first_name(),
                    "description": Faker().first_name(),
                    "environment ": {
                        "timeLimit": choice(API.TIMELIMIT),
                        "season": SeasonEnum.SUMMER,
                        "shooterPosition": ShooterPositionEnum.KNEES,
                        "hour": Faker().pyfloat(min_value=0, max_value=23),
                        "precipitation": PrecipitationEnum.MIDDLE,
                        "visibility": Faker().pyfloat(min_value=1, max_value=4000),
                        "temperature": Faker().pyfloat(min_value=-50, max_value=50),
                        "pressure": Faker().pyfloat(min_value=700, max_value=800),
                        "windDirection": Faker().pyfloat(min_value=0, max_value=360),
                        "windSpeed": Faker().pyfloat(min_value=0, max_value=30),
                        "humidity": Faker().pyfloat(min_value=1, max_value=50),
                        "altitude": Faker().pyfloat(min_value=1, max_value=50),
                        "hitLimit": Faker().random_int(1, 10),
                        "targetLimit": Faker().random_int(1, 10),
                        "scoreLimit": Faker().random_int(1, 10),
                        "tracerEveryNShot": Faker().random_int(1, 10),
                    },
                    "exerciseObjects": [{
                        "objectId":  API.OBJECTS_GUUD_FLAT_TARGET,
                        "name": API.OBJECTS_NAME,
                        "isCommandsCycled": Faker().boolean(),
                        "index": Faker().random_int(1, 10),
                        "position": API.POSITION,
                        "rotation": API.POSITION,
                        "scale": API.POSITION,
                        "shotReactDistance": Faker().pyfloat(min_value=700, max_value=800),
                        "isTarget": Faker().boolean(),
                        "exerciseCommands": {
                            #"params": Faker().first_name(),
                            "index": 1,
                            "commandId": API.COMMAND_MOVE_ID,
                        },
                    }],
                    "exerciseWeaponPresets": [{
                        "weaponTypeId": API.WEAPON_ID_EX,
                        "ammoTypeId": API.AMMO_ID_EX,
                        "exerciseId": API.EX_ID_SHOOTING_RANGE,
                    }],
                    "sceneId": API.SCENE_ID_SHOOTING_RANGE,
                    "type": ExTypeEnum.EX3D,
                    "tags": Faker().first_name(),
                },
            },
        }
        with aqas.step("Отправка запроса с мутацией <addExercise>"):
            create_exercise = ApiGatewayAdapter().mutation("addExercise", create_exercise_input)
        with aqas.step("Сохранение полученных данных в переменных"):
            TestsCrudExercise.EXERCISE_ID = create_exercise["id"]
            TestsCrudExercise.EXERCISE_NAME = create_exercise["name"]
        with aqas.step("Проверка типа"):
            assert isinstance(create_exercise["name"], str), "Ошибка тип не равен str"
        with aqas.step("Проверка типа"):
            assert isinstance(create_exercise["sceneId"], str), "Ошибка тип не равен str"
        with aqas.step("Проверка типа"):
            assert isinstance(create_exercise["exerciseObjects"]["isCommandsCycled"], bool), "Ошибка тип не равен bool"

    @pytest.mark.dependency(depends=["test_create_exercise"], scope="class")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-405")
    @allure.title("update_exercise")
    def test_update_exercise(self):
        update_exercise_input = {
            "updateExerciseByid": {
                "exerciseInput": {
                    "id": API.EX_ID_SHOOTING_RANGE,
                    "name": Faker().first_name(),
                    "description": Faker().first_name(),
                    "sceneId": API.SCENE_ID_SHOOTING_RANGE,
                    "type": ExTypeEnum.DUEL,
                    "environment ": {
                        "timeLimit": choice(API.TIMELIMIT),
                        "season": SeasonEnum.SPRING,
                        "shooterPosition": ShooterPositionEnum.STAY,
                        "precipitation": PrecipitationEnum.MIDDLE,
                    },
                },
            },
        }
        with aqas.step("Отправка запроса с мутацией <updateExerciseById>"):
            update_exercise = ApiGatewayAdapter().mutation("updateExerciseById", update_exercise_input)
        with aqas.step("Проверка обновления"):
            assert TestsCrudExercise.EXERCISE_NAME != update_exercise["name"], "Сцена не обновилась"
        with aqas.step("Проверка типа"):
            assert isinstance(update_exercise["name"], str), "Ошибка тип не равен str"

    @pytest.mark.dependency(depends=["test_create_exercise"], scope="class")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-408")
    @allure.title("delete_exercise")
    def test_delete_exercise(self):
        result = ApiGatewayAdapter().mutation("removeExerciseById", {"id": TestsCrudExercise.EXERCISE_ID})
        with aqas.step("Проверка наличия ответа"):
            assert result == 1, "Упражнение не удалено"
