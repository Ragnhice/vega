import pytest
from aqas.browser import Browser
from aqas.utils.config import ConfigManager
from aqas.utils.step import pre_step,post_step
from models.ui.forms.auth_form import AuthenticationForm
from models.ui.forms.lanes_control_form import LanesControlForm
from models.ui.forms.lane1_control_form import Lane1ControlForm
from models.ui.forms.conditions_menu_form import ConditionsMenuForm

@pytest.fixture(scope="function")
def start_browser():
    Browser.start()
    Browser.navigate(ConfigManager().project_settings.url)
    yield
    Browser.stop()

@pytest.fixture(scope="function")
def get_auth_admin():
    """Аутентификация администратором и переход на страницу управления полосами"""

    with pre_step("Переход на страницу аутентификации"):
        auth_page = AuthenticationForm()
        assert auth_page.is_wait_for_form_load(), "Страница не загрузилась"
    with pre_step("Переход на страницу управления полосами"):
        auth_page.enter_login_admin()
        auth_page.enter_password_admin()
        lanes_control_page = LanesControlForm()
        assert lanes_control_page.is_wait_for_form_load(), "Страница не загрузилась"
    return lanes_control_page


@pytest.fixture(scope="function")
def go_line1(get_auth_admin):
    """Для проверок, когда нужно перейти на 1 полосу и  занять ее"""

    lines_control_page = get_auth_admin
    with pre_step("Подождать, пока не исчезнут Уведомления"):
        lines_control_page.wait_for_invisible_notifications()
    with pre_step("Переход на страницу управления 1 полосой"):
        lines_control_page.go_to_line1()
        line1_control_page = Lane1ControlForm()
        assert line1_control_page.is_wait_for_form_load(), "Страница не загрузилась"

    with pre_step("Занять полосу, если она освобождена"):
        if line1_control_page.lane_is_free():
            line1_control_page.change_busy_line()



    with pre_step("Остановить упражнение, если оно запущено"):
        if not lane1_control_page.ex_is_stopped(): # если упр. не остановлено
            lane1_control_page.press_stop() # остановить

    with pre_step("Подождать, пока не исчезнут Уведомления"):
        lane1_control_page.wait_for_invisible_notifications()

    yield  lane1_control_page

    with post_step("Остановить упражнение, если оно запущено"):
        if not lane1_control_page.ex_is_stopped(): # если упр. не остановлено
            lane1_control_page.press_stop() # остановить

    with post_step("Освободить полосу, если она занята"):
        if lane1_control_page.lane_is_busy():  #Если полоса занята
            lane1_control_page.change_busy_lane() #поменять занятость, освободить
        assert lane1_control_page.lane_is_free(), "Страница не освободилась"




@pytest.fixture(scope="function")
def set_free_lane_and_stopped_ex(get_auth_admin):
    """Для проверок, когда нужно на экране Управление полосами освободить полосу и остановить упражнение"""

    lanes_control_page = get_auth_admin
    with pre_step("Подождать, пока не исчезнут Уведомления"):
        lanes_control_page.wait_for_invisible_notifications()

    with pre_step("Освободить полосу, если она занята"):
        if lanes_control_page.lane_is_busy():
            lanes_control_page.change_busy_lane()

    with pre_step("Остановить упражнение, если оно запущено"):
        if not lanes_control_page.ex_is_stopped(): # если упр. не остановлено
            lanes_control_page.press_stop() # остановить

    with pre_step("Подождать, пока не исчезнут Уведомления"):
        lanes_control_page.wait_for_invisible_notifications()

    yield  lanes_control_page

    with post_step("Остановить упражнение, если оно запущено"):
        if not lanes_control_page.ex_is_stopped(): # если упр. не остановлено
            lanes_control_page.press_stop() # остановить

    with post_step("Освободить полосу, если она занята"):
        if lanes_control_page.lane_is_busy():  #Если полоса занята
            lanes_control_page.change_busy_lane() #поменять занятость, освободить
        assert lanes_control_page.lane_is_free(), "Страница не освободилась"






#"url": "http://10.10.72.214",