import allure
import aqas
import pytest
from faker import Faker

from models.api.api_gateway_adapter import ApiGatewayAdapter


@allure.parent_suite("api")
@allure.suite("ExerciseApi")
@allure.sub_suite("crud")
class TestsCrudScene:
    SCENE_GUID = ""
    SCENE_NAME = ""

    @pytest.mark.dependency()
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-398")
    @allure.title("create_scene")
    def test_create_scene(self):
        create_scene_input = {
            "addScene": {
                "sceneCreateInput": {
                    "name": Faker().first_name(),
                    "description": Faker().first_name(),
                    "localizationName": Faker().first_name(),
                    "guid": Faker().first_name(),
                    "prefab": Faker().first_name(),
                    "image": Faker().first_name(),
                    "bounds": Faker().first_name(),
                    "zeroPointShiftMeters": Faker().first_name(),
                    "cameraDefaultPosition": Faker().first_name(),
                    "cameraDefaultRotation": Faker().first_name(),
                    "keepRealism": Faker().boolean(),
                },
            },
        }
        with aqas.step("Отправка запроса с мутацией <addScene>"):
            create_scene = ApiGatewayAdapter().mutation("addScene", create_scene_input)
        with aqas.step("Сохранение полученных данных в переменных"):
            TestsCrudScene.SCENE_GUID = create_scene["guid"]
            TestsCrudScene.SCENE_NAME = create_scene["name"]
        with aqas.step("Проверка типа"):
            assert isinstance(create_scene["name"], str), "Ошибка тип не равен str"
        with aqas.step("Проверка типа"):
            assert isinstance(create_scene["keepRealism"], bool), "Ошибка тип не равен bool"

    @pytest.mark.dependency(depends=["test_create_scene"], scope="class")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-399")
    @allure.title("update_scene")
    def test_update_scene(self):
        update_scene_input = {
            "name": f"'{Faker().first_name()}'",
            "description": f"'{Faker().first_name()}'",
            "localizationName": f"'{Faker().first_name()}'",
            "guid": f"'{TestsCrudScene.SCENE_GUID}'",
            "prefab": f"'{Faker().first_name()}'",
            "image": f"'{Faker().first_name()}'",
            "bounds": f"'{Faker().first_name()}'",
            "zeroPointShiftMeters": f"'{Faker().hex_color()}'",
            "cameraDefaultPosition": f"'{Faker().hex_color()}'",
            "cameraDefaultRotation": f"'{Faker().hex_color()}'",
            "keepRealism": f"{str(Faker().boolean()).lower()}",
        }
        with aqas.step("Отправка запроса с мутацией <updateSceneByGuid>"):
            update_scene = ApiGatewayAdapter().update_scene_by_guid(update_scene_input)
        with aqas.step("Проверка обновления"):
            assert TestsCrudScene.SCENE_NAME != update_scene["name"], "Сцена не обновилась"
        with aqas.step("Проверка типа"):
            assert isinstance(update_scene["name"], str), "Ошибка тип не равен str"

    @pytest.mark.dependency(depends=["test_create_scene"], scope="class")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-400")
    @allure.title("delete_scene")
    def test_delete_scene(self):
        result = ApiGatewayAdapter().remove_scene_by_guid(TestsCrudScene.SCENE_GUID)
        with aqas.step("Проверка наличия ответа"):
            assert result == 1, "Сцена не удалена"
