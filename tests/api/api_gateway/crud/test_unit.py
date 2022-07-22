import allure
import aqas
import pytest
from faker import Faker

from models.api.api_gateway_adapter import ApiGatewayAdapter
from utils.constants import API


@allure.parent_suite("api")
@allure.suite("HunterApi")
@allure.sub_suite("crud")
class TestsCrudUnit:
    UNIT_ID = ""
    UNIT_NAME = ""

    @pytest.mark.dependency()
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-406")
    @allure.title("create_unit")
    def test_create_unit(self):
        create_unit_input = {
            "createUnit": {
                "unitInput": {
                    "name": Faker().first_name(),
                    "parentId": API.PARENT_UNIT_ID,
                },
            },
        }
        with aqas.step("Отправка запроса с мутацией <createUnit>"):
            create_unit = ApiGatewayAdapter().mutation("createUnit", create_unit_input)
        with aqas.step("Сохранение полученных данных в переменных"):
            TestsCrudUnit.UNIT_ID = create_unit["id"]
            TestsCrudUnit.UNIT_NAME = create_unit["name"]
        with aqas.step("Проверка типа"):
            assert isinstance(create_unit["parentId"], int), "Ошибка тип не равен int"

    @pytest.mark.dependency(depends=["test_create_unit"], scope="class")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-407")
    @allure.title("update_unit")
    def test_update_unit(self):
        update_unit_input = {
            "updateUnit": {
                "unitInput": {
                    "id": TestsCrudUnit.UNIT_ID,
                    "name": Faker().first_name(),
                    "parentId": API.PARENT_UNIT_ID,

                },
            },
        }
        with aqas.step("Отправка запроса с мутацией <updateUnit>"):
            update_unit = ApiGatewayAdapter().mutation("updateUnit", update_unit_input)
        with aqas.step("Проверка обновления"):
            assert TestsCrudUnit.UNIT_NAME != update_unit["name"], "Имя обновилось"
        with aqas.step("Проверка типа"):
            assert isinstance(update_unit["parentId"], int), "Ошибка тип не равен int"

    @pytest.mark.dependency(depends=["test_create_unit"], scope="class")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-409")
    @allure.title("delete_unit")
    def test_delete_unit(self):
        result = ApiGatewayAdapter().remove_units_by_id([TestsCrudUnit.UNIT_ID])
        with aqas.step("Проверка наличия ответа"):
            assert result == 1, "Подразделение не удалено"
