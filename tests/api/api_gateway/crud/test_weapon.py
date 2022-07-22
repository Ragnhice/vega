import allure
import aqas
import pytest
from faker import Faker

from models.api.api_gateway_adapter import ApiGatewayAdapter


@allure.parent_suite("api")
@allure.suite("WeaponApi")
@allure.sub_suite("crud")
class TestsCrudWeapon:
    WEAPON_ID = ""

    @pytest.mark.dependency()
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-389")
    @allure.title("CreateWeapon")
    def test_create_weapon(self):
        with aqas.step("Отправка мутации создания оружия"):
            create_weapon = ApiGatewayAdapter().create_weapon()
        with aqas.step("Проверка наличия ответа"):
            assert create_weapon["id"], "Нет ответа от запроса"
        with aqas.step("Сохраняем полученые данные в переменные"):
            TestsCrudWeapon.WEAPON_ID = create_weapon["id"]
            TestsCrudWeapon.WEAPON_REG_DATE = create_weapon["regDate"]
        with aqas.step("Проверка типа"):
            assert isinstance(create_weapon["hwid"], int), "Ошибка тип не равен int"
        with aqas.step("Проверка типа"):
            assert isinstance(create_weapon["mode"], str), "Ошибка тип не равен str"

    @pytest.mark.dependency(depends=["test_create_weapon"], scope="class")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-390")
    @allure.title("updateWeapon")
    def test_update_weapon(self):
        weapon = {
            "updateWeapon": {
                "weaponInput": {
                    "id": TestsCrudWeapon.WEAPON_ID,
                    "hwid": Faker().random_int(200, 300),
                    "shotsCount": Faker().random_int(1, 3),
                    "typeId": Faker().random_int(1, 5),
                },
            },
        }
        with aqas.step("Отправка мутации обновлении оружия"):
            weapon = ApiGatewayAdapter().mutation("updateWeapon", weapon)
        with aqas.step("Проверка типа"):
            assert isinstance(weapon["mode"], str), "Ошибка тип не равен str"

    @pytest.mark.dependency(depends=["test_create_weapon"], scope="class")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-391")
    @allure.title("delete_weapon")
    def test_delete_weapon(self):
        result = ApiGatewayAdapter().remove_weapons_by_id([TestsCrudWeapon.WEAPON_ID])
        with aqas.step("Проверка наличия ответа"):
            assert result == 1, "Оружие не удалено"
