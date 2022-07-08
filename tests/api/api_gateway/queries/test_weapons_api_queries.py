import allure
import aqas
import pytest

from models.api.api_gateway_adapter import ApiGatewayAdapter


@allure.parent_suite("api")
@allure.suite("WeaponsApi")
@allure.sub_suite("queries")
class TestWeaponsApiQueries:

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-362")
    @allure.title("weapons")
    def test_get_weapons(self):
        with aqas.step("qwe"):
            weapons = ApiGatewayAdapter().query("weapons")
        with aqas.step("Проверка наличия ответа"):
            assert weapons[0]["id"], "Нет ответа от запроса"
        with aqas.step("Проверка типа"):
            assert isinstance(weapons[0]["id"], int), "Ошибка тип не равен int"
        with aqas.step("Проверка типа"):
            assert isinstance(weapons[0]["hwid"], int), "Ошибка тип не равен int"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-366")
    @allure.title("weaponTypes")
    def test_get_weapon_types(self):
        with aqas.step("qwe"):
            weapon_types = ApiGatewayAdapter().query("weaponTypes")
        with aqas.step("Проверка наличия ответа"):
            assert weapon_types[0]["id"], "Нет ответа от запроса"
        with aqas.step("Проверка типа id"):
            assert isinstance(weapon_types[0]["id"], int), "Ошибка тип не равен int"
        with aqas.step("Проверка типа"):
            assert isinstance(weapon_types[0]["name"], str), "Ошибка тип не равен str"
        with aqas.step("Проверка типа"):
            assert isinstance(weapon_types[0]["localizationName"], str), "Ошибка тип не равен str"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-365")
    @allure.title("ammoTypes")
    def test_get_ammo_types(self):
        with aqas.step("qwe"):
            ammo_types = ApiGatewayAdapter().query("ammoTypes")
        with aqas.step("Проверка наличия ответа"):
            assert ammo_types[0]["id"], "Нет ответа от запроса"
        with aqas.step("Проверка типа"):
            assert isinstance(ammo_types[0]["localizationName"], str), "Ошибка тип не равен str"
        with aqas.step("Проверка типа"):
            assert isinstance(ammo_types[0]["id"], int), "Ошибка тип не равен int"
