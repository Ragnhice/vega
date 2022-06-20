import pytest
from aqas.utils.step import step

from models.ui.forms.shooters_chose_form import ShootersChoseForm
from models.ui.forms.lanes_control_form import LanesControlForm
from models.ui.forms.conditions_menu_form import ConditionsMenuForm
from models.ui.forms.lane1_control_form import Lane1ControlForm
from models.ui.forms.exercise_menu_form import ExerciseMenuForm

@pytest.mark.usefixtures("start_browser")
class TestBusyLane():
    """
    Класс, который содержит действия теста при проверке смены занятости полосы
    """
    SEARCH_CONDITION = "Автотесты"


    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-319")
    def test_busy_on_lanescontrol(self,set_free_lane_and_stopped_ex):
        lanes_control_page = set_free_lane_and_stopped_ex
        with step("Занять полосу"):
            if lanes_control_page.lane_is_free():
                lanes_control_page.change_busy_lane()

        with step("Подождать, пока не исчезнут Уведомления"):
            lanes_control_page.wait_for_invisible_notifications()

        with step("Освободить полосу"):
            if lanes_control_page.lane_is_busy():
                lanes_control_page.change_busy_lane()