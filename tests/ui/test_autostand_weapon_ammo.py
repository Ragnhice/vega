import allure
import aqas
import pytest

from models.ui.forms.conditions_menu_form import ConditionsMenuForm
from models.ui.forms.shooters_chose_form import ShootersChoseForm
from utils.constants import UI
from utils.element_utils import *


@allure.parent_suite("ui")
@allure.suite("Autostand Weapon Ammo")
@pytest.mark.usefixtures("start_browser")
class TestAutostandWeapon:
    """
    Класс, который содержит действия тестов:
    - при проверке автозаполнения полей оружия и боеприпаса при быстром старте;
    - на странице выбора стрелков;
    - на странице управления полосами;
    - на странице выбора условий полосы.
    """

    @allure.title("autostand_faststart_lanes_control")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-321")
    def test_autostand_faststart_lanes_control(self, set_free_lane_and_stopped_ex):
        lanes_control_page = set_free_lane_and_stopped_ex

        with aqas.step("Занять полосу, если она освобождена"):
            if is_located(lanes_control_page.elements.LANE1_IS_FREE_LBL):
                lanes_control_page.elements.BUSY_LANE1_ADMIN_BTN.click()

        with aqas.step("Запуск упражнения"):
            lanes_control_page.elements.PLAY_BTN.click()

        with aqas.step("Проверка автозаполнения поля выбора оружия"):
            assert lanes_control_page.elements.CHOSEN_WEAPON_DRDN.text is not None, "Поле выбора оружия пустое"
            assert lanes_control_page.elements.CHOSEN_WEAPON_DRDN.text != UI.EMPTY, "Поле выбора оружия пустое"

        with aqas.step("Проверка автозаполнения поля выбора  боеприпаса"):
            assert lanes_control_page.elements.CHOSEN_AMMO_DRDN.text is not None, "Поле выбора боеприпаса пустое"
            assert lanes_control_page.elements.CHOSEN_AMMO_DRDN.text != UI.EMPTY, "Поле выбора боеприпаса пустое"

        with aqas.step("Закрыть таблицу выбора оружия"):
            lanes_control_page.elements.CLOSE_CHOSE_WEAPON_BTN.click()

    @allure.title("autostand_faststart_lane1")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-246")
    def test_autostand_faststart_lane1(self, go_lane1):
        lane1_control_page = go_lane1

        with aqas.step("Запуск упражнения"):
            lane1_control_page.elements.PLAY_BTN.click()

        with aqas.step("Проверка автозаполнения поля выбора оружия"):
            assert lane1_control_page.elements.CHOSEN_WEAPON_DRDN.text is not None, "Поле выбора оружия пустое"
            assert lane1_control_page.elements.CHOSEN_WEAPON_DRDN.text != UI.EMPTY, "Поле выбора оружия пустое"

        with aqas.step("Проверка автозаполнения поля выбора  боеприпаса"):
            assert lane1_control_page.elements.CHOSEN_AMMO_DRDN.text is not None, "Поле выбора боеприпаса пустое"
            assert lane1_control_page.elements.CHOSEN_AMMO_DRDN.text != UI.EMPTY, "Поле выбора боеприпаса пустое"

        with aqas.step("Закрыть таблицу выбора оружия"):
            lane1_control_page.elements.CLOSE_CHOSE_WEAPON_BTN.click()

    @allure.title("autostand_weapon_ammo_shooters_menu")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-305")
    def test_autostand_weapon_ammo_shooters_menu(self, go_lane1):
        lane1_control_page = go_lane1

        with aqas.step("Подождать, пока не исчезнут Уведомления"):
            lane1_control_page.is_notifications_invisible()

        with aqas.step("Переход на страницу выбора стрелков на полосу"):
            lane1_control_page.elements.SHOOTERS_MENU_BTN.click()
            shooter_chose_page = ShootersChoseForm()
            assert shooter_chose_page.is_wait_for_form_load(), "Страница не загрузилась"

        with aqas.step("Проверка автозаполнения поля выбора оружия"):
            assert shooter_chose_page.elements.CHOSEN_WEAPON_2_DRDW.text is not None, "Поле выбора оружия пустое"
            assert shooter_chose_page.elements.CHOSEN_WEAPON_2_DRDW.text != UI.EMPTY, "Поле выбора оружия пустое"

        with aqas.step("Проверка автозаполнения поля выбора  боеприпаса"):
            assert shooter_chose_page.elements.CHOSEN_AMMO_2_DRDW.text is not None, "Поле выбора боеприпаса пустое"
            assert shooter_chose_page.elements.CHOSEN_AMMO_2_DRDW.text != UI.EMPTY, "Поле выбора боеприпаса пустое"

        with aqas.step("Вернуться на страницу Управление полосой 1"):
            shooter_chose_page.elements.BACK_BTN.click()

    @allure.title("autostand_weapon_ammo_conditions_menu")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-329")
    def test_autostand_weapon_ammo_conditions_menu(self, go_lane1):
        lane1_control_page = go_lane1

        with aqas.step("Переход на страницу выбора условий на полосе"):
            lane1_control_page.elements.CONDITIONS_MENU_BTN.click()
            conditions_menu_page = ConditionsMenuForm()
            assert conditions_menu_page.is_wait_for_form_load(), "Страница не загрузилась"

        with aqas.step("Запуск упражнения"):
            conditions_menu_page.elements.PLAY_BTN.click()

        with aqas.step("Проверка автозаполнения поля выбора оружия"):
            assert conditions_menu_page.elements.CHOSEN_WEAPON_DRDN.text is not None, "Поле выбора оружия пустое"
            assert conditions_menu_page.elements.CHOSEN_WEAPON_DRDN.text != UI.EMPTY, "Поле выбора оружия пустое"

        with aqas.step("Проверка автозаполнения поля выбора  боеприпаса"):
            assert conditions_menu_page.elements.CHOSEN_AMMO_DRDN.text is not None, "Поле выбора боеприпаса пустое"
            assert conditions_menu_page.elements.CHOSEN_AMMO_DRDN.text != UI.EMPTY, "Поле выбора боеприпаса пустое"

        with aqas.step("Закрыть таблицу выбора оружия"):
            conditions_menu_page.elements.CLOSE_CHOSE_WEAPON_BTN.click()

        with aqas.step("Вернуться на страницу Управление полосой 1"):
            conditions_menu_page.elements.BACK_BTN.click()
