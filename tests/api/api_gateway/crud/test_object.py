import allure
import aqas
import pytest
from faker import Faker

from models.api.api_gateway_adapter import ApiGatewayAdapter


@allure.parent_suite("api")
@allure.suite("HunterApi")
@allure.sub_suite("crud")
class TestsCrudObject:
    OBJECT_GUID = ""

    @pytest.mark.dependency()
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-392")
    @allure.title("create_object")
    def test_create_object(self):
        create_object_input = {
            "name": f"'{Faker().first_name()}'",
            "localizationName": f"'{Faker().locale()}'",
            "prefab": f"'{Faker().first_name()}'",
            "image": f"'{Faker().image_url()}'",
            "guid": f"'{Faker().uuid4()}'",
            "availableCommands": {
                "name": f"'{Faker().first_name()}'",
                "localizationName": f"'{Faker().city()}'",
                "parameters": f"'{Faker().domain_word()}'",
            },
        }
        with aqas.step("Отправка запроса с мутацией <addObject>"):
            create_object = ApiGatewayAdapter().add_oject(create_object_input)
        with aqas.step("Сохраняем полученые данные в переменные"):
            TestsCrudObject.OBJECT_GUID = create_object["guid"]
        with aqas.step("Проверка типа"):
            assert isinstance(create_object["name"], str)

    @pytest.mark.dependency(depends=["test_create_object"], scope="class")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-393")
    @allure.title("update_object")
    def test_update_object_by_guid(self):
        new_object_name = Faker().first_name()
        update_object_input = {
            "guid": f"'{TestsCrudObject.OBJECT_GUID}'",
            "name": f"'{new_object_name}'",
            "localizationName": f"'{Faker().locale()}'",
            "prefab": f"'{Faker().first_name()}'",
            "image": f"'{Faker().image_url()}'",
            "availableCommands": {
                "name": f"'{Faker().first_name()}'",
                "localizationName": f"'{Faker().city()}'",
                "parameters": f"'{Faker().domain_word()}'",
            },
        }
        with aqas.step("Отправка запроса с мутацией <updateObjectByGuid>"):
            update_object = ApiGatewayAdapter().update_object_by_guid(update_object_input)
        with aqas.step("Проверка обновления"):
            assert update_object["name"] == new_object_name
        with aqas.step("Проверка типа"):
            assert isinstance(update_object["guid"], str), "Ошибка тип не равен str"

    @pytest.mark.dependency(depends=["test_create_object"], scope="class")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-394")
    @allure.title("remove_object")
    def test_delete_object(self):
        result = ApiGatewayAdapter().remove_object_by_guid(TestsCrudObject.OBJECT_GUID)
        with aqas.step("Проверка наличия ответа"):
            assert result == 1, "Объект не удален"
