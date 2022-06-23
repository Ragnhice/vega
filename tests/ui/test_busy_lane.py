import pytest
from aqas.utils.step import step

from models.ui.forms.conditions_menu_form import ConditionsMenuForm
from models.ui.forms.exercise_menu_form import ExerciseMenuForm
from models.ui.forms.shooters_chose_form import ShootersChoseForm


@pytest.mark.usefixtures("start_browser")
class TestBusyLane():
    """
    Класс, который содержит действия теста при проверке смены занятости полосы
    """
    SEARCH_CONDITION = "Автотесты"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-319")
    def test_busy_on_lanescontrol(self, set_free_lane_and_stopped_ex):
        lanes_control_page = set_free_lane_and_stopped_ex
        with step("Занять полосу"):
            if lanes_control_page.lane_is_free():
                lanes_control_page.change_busy_lane1()

        with step("Подождать, пока не исчезнут Уведомления"):
            lanes_control_page.wait_for_invisible_notifications()

        with step("Освободить полосу"):
            if lanes_control_page.lane_is_busy():
                lanes_control_page.change_busy_lane1()

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-320")
    def test_busy_on_lane1(self, go_lane1):
        pass

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-322")
    def test_busy_on_shooters_menu(self, go_lane1):
        lane1_control_page = go_lane1
        with step("Переход на страницу выбора стрелков на полосу"):
            lane1_control_page.go_shooters_menu()
            shooter_chose_page = ShootersChoseForm()
            assert shooter_chose_page.is_wait_for_form_load(), "Страница не загрузилась"

        with step("Освободить полосу"):
            if shooter_chose_page.lane_is_busy():
                shooter_chose_page.change_busy_lane()

        with step("Подождать, пока не исчезнут Уведомления"):
            shooter_chose_page.wait_for_invisible_notifications()

        with step("Занять полосу"):
            if shooter_chose_page.lane_is_free():
                shooter_chose_page.change_busy_lane()

        with step("Вернуться на страницу Управление полосой 1"):
            shooter_chose_page.back_to_lane1()

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-323")
    def test_busy_on_exercise_menu(self, go_lane1):
        lane1_control_page = go_lane1
        with step("Переход на страницу выбора упражнения на полосу"):
            lane1_control_page.go_exercise_menu()
            exercise_menu_page = ExerciseMenuForm()

        with step("Освободить полосу"):
            if exercise_menu_page.lane_is_busy():
                exercise_menu_page.change_busy_lane()

        with step("Подождать, пока не исчезнут Уведомления"):
            exercise_menu_page.wait_for_invisible_notifications()

        with step("Занять полосу"):
            if exercise_menu_page.lane_is_free():
                exercise_menu_page.change_busy_lane()

        with step("Вернуться на страницу Управление полосой 1"):
            exercise_menu_page.back_to_lane1()

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-324")
    def test_busy_on_conditions_menu(self, go_lane1):
        lane1_control_page = go_lane1
        with step("Переход на страницу выбора условий на полосу"):
            lane1_control_page.go_conditions_menu()
            conditions_menu_page = ConditionsMenuForm()
            assert conditions_menu_page.is_wait_for_form_load(), "Страница не загрузилась"

        with step("Освободить полосу"):
            if conditions_menu_page.lane_is_busy():
                conditions_menu_page.change_busy_lane()

        with step("Подождать, пока не исчезнут Уведомления"):
            conditions_menu_page.wait_for_invisible_notifications()

        with step("Занять полосу"):
            if conditions_menu_page.lane_is_free():
                conditions_menu_page.change_busy_lane()

        with step("Вернуться на страницу Управление полосой 1"):
            conditions_menu_page.back_to_lane1()
