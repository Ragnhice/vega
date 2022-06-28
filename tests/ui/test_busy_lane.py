import allure
import pytest
import aqas

from models.ui.forms.conditions_menu_form import ConditionsMenuForm
from models.ui.forms.exercise_menu_form import ExerciseMenuForm
from models.ui.forms.shooters_chose_form import ShootersChoseForm
from utils.element_utils import *


@allure.parent_suite("ui")
@allure.suite("Busy Lane")
@pytest.mark.usefixtures("start_browser")
class TestBusyLane:
    """Класс, который содержит действия теста при проверке смены занятости полосы."""

    @allure.title("busy_on_lanes_control")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-319")
    def test_busy_on_lanes_control(self, set_free_lane_and_stopped_ex):
        lanes_control_page = set_free_lane_and_stopped_ex

        with aqas.step("Занять полосу"):
            if is_located(lanes_control_page.elements.LANE1_IS_FREE):
                lanes_control_page.change_busy_lane1_admin()

        with aqas.step("Подождать, пока не исчезнут Уведомления"):
            lanes_control_page.is_notifications_invisible()

        with aqas.step("Освободить полосу"):
            if is_located(lanes_control_page.elements.LANE1_IS_BUSY):
                lanes_control_page.change_busy_lane1_admin()

    @allure.title("busy_on_lane1")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-320")
    def test_busy_on_lane1(self, go_lane1):
        pass

    @allure.title("busy_on_shooters_menu")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-322")
    def test_busy_on_shooters_menu(self, go_lane1):
        lane1_control_page = go_lane1

        with aqas.step("Подождать, пока не исчезнут Уведомления"):
            lane1_control_page.is_notifications_invisible()

        with aqas.step("Переход на страницу выбора стрелков на полосу"):
            lane1_control_page.go_shooters_menu()
            shooter_chose_page = ShootersChoseForm()
            assert shooter_chose_page.is_wait_for_form_load(), "Страница не загрузилась"

        with aqas.step("Освободить полосу"):
            if is_located(shooter_chose_page.elements.LANE_IS_BUSY):
                shooter_chose_page.change_busy_lane()

        with aqas.step("Подождать, пока не исчезнут Уведомления"):
            shooter_chose_page.is_notifications_invisible()

        with aqas.step("Занять полосу"):
            if is_located(shooter_chose_page.elements.LANE_IS_FREE):
                shooter_chose_page.change_busy_lane()

        with aqas.step("Вернуться на страницу Управление полосой 1"):
            shooter_chose_page.back_to_lane1()

    @allure.title("busy_on_exercise_menu")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-323")
    def test_busy_on_exercise_menu(self, go_lane1):
        lane1_control_page = go_lane1

        with aqas.step("Переход на страницу выбора упражнения на полосу"):
            lane1_control_page.go_exercise_menu()
            exercise_menu_page = ExerciseMenuForm()

        with aqas.step("Освободить полосу"):
            if is_located(exercise_menu_page.elements.LANE_IS_BUSY):
                exercise_menu_page.change_busy_lane()

        with aqas.step("Подождать, пока не исчезнут Уведомления"):
            exercise_menu_page.is_notifications_invisible()

        with aqas.step("Занять полосу"):
            if is_located(exercise_menu_page.elements.LANE_IS_FREE):
                exercise_menu_page.change_busy_lane()

        with aqas.step("Вернуться на страницу Управление полосой 1"):
            exercise_menu_page.back_to_lane1()

    @allure.title("busy_on_conditions_menu")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-324")
    def test_busy_on_conditions_menu(self, go_lane1):
        lane1_control_page = go_lane1

        with aqas.step("Переход на страницу выбора условий на полосу"):
            lane1_control_page.go_conditions_menu()
            conditions_menu_page = ConditionsMenuForm()
            assert conditions_menu_page.is_wait_for_form_load(), "Страница не загрузилась"

        with aqas.step("Освободить полосу"):
            if is_located(conditions_menu_page.elements.LANE_IS_BUSY):
                conditions_menu_page.change_busy_lane()

        with aqas.step("Подождать, пока не исчезнут Уведомления"):
            conditions_menu_page.is_notifications_invisible()

        with aqas.step("Занять полосу"):
            if is_located(conditions_menu_page.elements.LANE_IS_FREE):
                conditions_menu_page.change_busy_lane()

        with aqas.step("Вернуться на страницу Управление полосой 1"):
            conditions_menu_page.back_to_lane1()
