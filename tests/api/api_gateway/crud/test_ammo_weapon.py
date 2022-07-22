from random import choice
import allure
import aqas
import pytest
from faker import Faker

from models.api.api_gateway_adapter import ApiGatewayAdapter
from utils.constants import API


@allure.parent_suite("api")
@allure.suite("WeaponApi")
@allure.sub_suite("crud")
class TestsCrudAmmoWeapon:
    WEAPON_TYPE_ID = ""
    AMMO_TYPE_ID = ""
    LIFE_TIME_1 = ""

    @pytest.mark.dependency()
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-395")
    @allure.title("create_ammo_weapon")
    def test_create_ammo_weapon(self):
        create_ammo_weapon_input = {
            "createAmmoWeapon": {
                "ammoWeaponInput": {
                    "weaponTypeId": choice(list(API.WEAPON_TYPE_IDS.values())),
                    "ammoTypeId": choice(list(API.AMMO_TYPE_IDS.values())),
                    "lifeTimeSeconds": Faker().pyfloat(min_value=1, max_value=50),
                    "reactiveFactorTimeSeconds": Faker().pyfloat(min_value=1, max_value=50),
                    "reactiveFactor": Faker().pyfloat(min_value=1, max_value=50),
                    "bulletWeightKg": Faker().pyfloat(min_value=1, max_value=50),
                    "bulletWindCoef": Faker().pyfloat(min_value=1, max_value=50),
                    "reactiveWindCoef": Faker().pyfloat(min_value=1, max_value=50),
                    "bulletSpeedDispersion": Faker().pyfloat(min_value=1, max_value=50),
                    "bulletPitchDispersion": Faker().pyfloat(min_value=1, max_value=50),
                    "bulletFormMaxAngleDeg": Faker().pyfloat(min_value=1, max_value=50),
                    "bulletFormSpeedMps": Faker().pyfloat(min_value=1, max_value=50),
                    "bulletStartSpeedMps": Faker().pyfloat(min_value=1, max_value=50),
                    "bulletSecondWindFactor": Faker().pyfloat(min_value=1, max_value=50),
                    "bulletFormFactor ": Faker().pyfloat(min_value=1, max_value=50),
                    "bulletFactor": Faker().pyfloat(min_value=1, max_value=50),
                    "damageRadius": Faker().pyfloat(min_value=1, max_value=50),
                    "damageDepth": Faker().pyfloat(min_value=1, max_value=50),
                    "timeModifier": Faker().pyfloat(min_value=1, max_value=50),
                },
            },
        }
        with aqas.step("Отправка запроса с мутацией <createAmmoWeapon>"):
            create_ammo_weapon = ApiGatewayAdapter().mutation("createAmmoWeapon", create_ammo_weapon_input)
        with aqas.step("Сохранение полученных данных в переменных"):
            TestsCrudAmmoWeapon.WEAPON_TYPE_ID = create_ammo_weapon["weaponTypeId"]
            TestsCrudAmmoWeapon.AMMO_TYPE_ID = create_ammo_weapon["ammoTypeId"]
            TestsCrudAmmoWeapon.LIFE_TIME_1 = create_ammo_weapon["lifeTimeSeconds"]
        with aqas.step("Проверка типа"):
            assert isinstance(create_ammo_weapon["reactiveWindCoef"], float), "Ошибка тип не равен float"
        with aqas.step("Проверка типа"):
            assert isinstance(create_ammo_weapon["bulletFormMaxAngleDeg"], float), "Ошибка тип не равен float"
        with aqas.step("Проверка типа"):
            assert isinstance(create_ammo_weapon["bulletFormFactor"], float), "Ошибка тип не равен float"

    @pytest.mark.dependency(depends=["test_create_ammo_weapon"], scope="class")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-396")
    @allure.title("update_ammo_weapon")
    def test_update_ammo_weapon(self):
        update_ammo_weapon_input = {
            "updateAmmoWeapon": {
                "ammoWeaponInput": {
                    "weaponTypeId": TestsCrudAmmoWeapon.WEAPON_TYPE_ID,
                    "ammoTypeId": TestsCrudAmmoWeapon.AMMO_TYPE_ID,
                    "lifeTimeSeconds": Faker().pyfloat(min_value=1, max_value=50),
                    "reactiveFactorTimeSeconds": Faker().pyfloat(min_value=1, max_value=50),
                    "reactiveFactor": Faker().pyfloat(min_value=1, max_value=50),
                    "bulletWeightKg": Faker().pyfloat(min_value=1, max_value=50),
                    "bulletWindCoef": Faker().pyfloat(min_value=1, max_value=50),
                    "reactiveWindCoef": Faker().pyfloat(min_value=1, max_value=50),
                    "bulletSpeedDispersion": Faker().pyfloat(min_value=1, max_value=50),
                    "bulletPitchDispersion": Faker().pyfloat(min_value=1, max_value=50),
                    "bulletFormMaxAngleDeg": Faker().pyfloat(min_value=1, max_value=50),
                    "bulletFormSpeedMps": Faker().pyfloat(min_value=1, max_value=50),
                    "bulletStartSpeedMps": Faker().pyfloat(min_value=1, max_value=50),
                    "bulletSecondWindFactor": Faker().pyfloat(min_value=1, max_value=50),
                    "bulletFormFactor ": Faker().pyfloat(min_value=1, max_value=50),
                    "bulletFactor": Faker().pyfloat(min_value=1, max_value=50),
                    "damageRadius": Faker().pyfloat(min_value=1, max_value=50),
                    "damageDepth": Faker().pyfloat(min_value=1, max_value=50),
                    "timeModifier": Faker().pyfloat(min_value=1, max_value=50),
                },
            },
        }
        with aqas.step("Отправка запроса с мутацией <updateAmmoWeapon>"):
            update_ammo_weapon = ApiGatewayAdapter().mutation("updateAmmoWeapon", update_ammo_weapon_input)
        with aqas.step("Проверка обновления"):
            assert TestsCrudAmmoWeapon.LIFE_TIME_1 != update_ammo_weapon[
                "lifeTimeSeconds"], "Время жизни в секундах не обновилось"
        with aqas.step("Проверка типа"):
            assert isinstance(update_ammo_weapon["reactiveFactor"], float), "Ошибка тип не равен float"

    @pytest.mark.dependency(depends=["test_create_ammo_weapon"], scope="class")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-397")
    @allure.title("delete_ammo_weapon")
    def test_delete_ammo_weapon(self):
        result = ApiGatewayAdapter().remove_ammo_weapon(TestsCrudAmmoWeapon.WEAPON_TYPE_ID,
                                                        TestsCrudAmmoWeapon.AMMO_TYPE_ID)
        with aqas.step("Проверка наличия ответа"):
            assert result == 1, "Связь не удалена"
