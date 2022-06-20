import pytest
from aqas.utils.step import step

from models.ui.forms.shooters_chose_form import ShootersChoseForm


@pytest.mark.usefixtures("start_browser")
class TestShootersChose():
    """
    Класс, который содержит действия теста при проверке автозаполнения полей оружия и боеприса
    при быстром старте и на странице выбора стрелков
    """
    SEARCH_CONDITION = "Автотесты"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-246")
    def test_autostand_weapon_ammo_faststart(self, go_line1):
        line1_control_page = go_line1
        with step("Запуск упражнения"):
            line1_control_page.press_play()

        with step("Проверка автозаполнения поля выбора оружия"):
            assert line1_control_page.get_chosen_weapon() is not None, \
                "Поле выбора оружия пустое"
            assert line1_control_page.get_chosen_weapon() != 'p - emptylabel', \
                "Поле выбора оружия пустое"

        with step("Проверка автозаполнения поля выбора  боеприпаса"):
            assert line1_control_page.get_chosen_ammo() is not None, "Поле выбора боеприпаса пустое"
            assert line1_control_page.get_chosen_ammo() != 'p - emptylabel', \
                "Поле выбора боеприпаса пустое"

        with step("Закрыть таблицу выбора оружия"):
            line1_control_page.close_chose_weapon_tab()

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-305")
    def test_autostand_weapon_ammo_shooters_menu(self, go_line1):
        line1_control_page = go_line1
        with step("Переход на страницу выбора стрелков на полосу"):
            line1_control_page.go_shooters_menu()
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
            shooter_chose_page.back_to_line1()
