import pytest
from aqas.utils.step import step

from models.ui.forms.conditions_menu_form import ConditionsMenuForm
from models.ui.forms.shooters_chose_form import ShootersChoseForm


@pytest.mark.usefixtures("start_browser")
class TestAutostandWeapon():
    """
    Класс, который содержит действия тестов при проверке автозаполнения полей оружия и боеприса
    при быстром старте;на странице выбора стрелков; на странице управления полосами;
     на странице выбора условий полосы;
    """
    SEARCH_CONDITION = "Автотесты"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-321")
    def test_autostand_faststart_lanescontrol(self, set_free_lane_and_stopped_ex):
        lanes_control_page = set_free_lane_and_stopped_ex
        with step("Занять полосу"):
            if lanes_control_page.lane_is_free():
                lanes_control_page.change_busy_lane1()

        with step("Запуск упражнения"):
            lanes_control_page.press_play()

        with step("Проверка автозаполнения поля выбора оружия"):
            assert lanes_control_page.get_chosen_weapon() is not None, \
                "Поле выбора оружия пустое"
            assert lanes_control_page.get_chosen_weapon() != 'p - emptylabel', \
                "Поле выбора оружия пустое"

        with step("Проверка автозаполнения поля выбора  боеприпаса"):
            assert lanes_control_page.get_chosen_ammo() is not None, \
                "Поле выбора боеприпаса пустое"
            assert lanes_control_page.get_chosen_ammo() != 'p - emptylabel', \
                "Поле выбора боеприпаса пустое"

        with step("Закрыть таблицу выбора оружия"):
            lanes_control_page.close_chose_weapon_tab()

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-246")
    def test_autostand_faststart_lane1(self, go_lane1):
        lane1_control_page = go_lane1
        with step("Запуск упражнения"):
            lane1_control_page.press_play()

        with step("Проверка автозаполнения поля выбора оружия"):
            assert lane1_control_page.get_chosen_weapon() is not None, \
                "Поле выбора оружия пустое"
            assert lane1_control_page.get_chosen_weapon() != 'p - emptylabel', \
                "Поле выбора оружия пустое"

        with step("Проверка автозаполнения поля выбора  боеприпаса"):
            assert lane1_control_page.get_chosen_ammo() is not None, \
                "Поле выбора боеприпаса пустое"
            assert lane1_control_page.get_chosen_ammo() != 'p - emptylabel', \
                "Поле выбора боеприпаса пустое"

        with step("Закрыть таблицу выбора оружия"):
            lane1_control_page.close_chose_weapon_tab()

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-305")
    def test_autostand_weapon_ammo_shooters_menu(self, go_lane1):
        lane1_control_page = go_lane1
        with step("Переход на страницу выбора стрелков на полосу"):
            lane1_control_page.go_shooters_menu()
            shooter_chose_page = ShootersChoseForm()
            assert shooter_chose_page.is_wait_for_form_load(), "Страница не загрузилась"

        with step("Проверка автозаполнения поля выбора оружия"):
            assert shooter_chose_page.get_chosen_weapon_2() is not None, \
                "Поле выбора оружия пустое"
            assert shooter_chose_page.get_chosen_weapon_2() != 'p - emptylabel', \
                "Поле выбора оружия пустое"

        with step("Проверка автозаполнения поля выбора  боеприпаса"):
            assert shooter_chose_page.get_chosen_ammo_2() is not None, \
                "Поле выбора боеприпаса пустое"
            assert shooter_chose_page.get_chosen_ammo_2() != 'p - emptylabel', \
                "Поле выбора боеприпаса пустое"

        with step("Вернуться на страницу Управление полосой 1"):
            shooter_chose_page.back_to_lane1()

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-329")
    def test_autostand_weapon_ammo_conditions_menu(self, go_lane1):
        lane1_control_page = go_lane1
        with step("Переход на страницу выбора условий на полосе"):
            lane1_control_page.go_conditions_menu()
            conditions_menu_page = ConditionsMenuForm()
            assert conditions_menu_page.is_wait_for_form_load(), "Страница не загрузилась"

        with step("Запуск упражнения"):
            conditions_menu_page.press_play()

        with step("Проверка автозаполнения поля выбора оружия"):
            assert conditions_menu_page.get_chosen_weapon() is not None, \
                "Поле выбора оружия пустое"
            assert conditions_menu_page.get_chosen_weapon() != 'p - emptylabel', \
                "Поле выбора оружия пустое"

        with step("Проверка автозаполнения поля выбора  боеприпаса"):
            assert conditions_menu_page.get_chosen_ammo() is not None, \
                "Поле выбора боеприпаса пустое"
            assert conditions_menu_page.get_chosen_ammo() != 'p - emptylabel', \
                "Поле выбора боеприпаса пустое"

        with step("Закрыть таблицу выбора оружия"):
            conditions_menu_page.close_chose_weapon_tab()

        with step("Вернуться на страницу Управление полосой 1"):
            conditions_menu_page.back_to_lane1()
