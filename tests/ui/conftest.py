import pytest
from aqas.browser import Browser
from aqas.utils.config import ConfigManager
from aqas.utils.step import pre_step,post_step
from models.ui.forms.auth_form import AuthenticationForm
from models.ui.forms.lines_control_form import LinesControlForm
from models.ui.forms.line1_control_form import Line1ControlForm

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
        lines_control_page = LinesControlForm()
        assert lines_control_page.is_wait_for_form_load(), "Страница не загрузилась"
    return lines_control_page


@pytest.fixture(scope="function")
def go_line1(get_auth_admin):
    """Для проверок, когда нужно перейти на 1 полосу и  занять ее"""

    lines_control_page = get_auth_admin
    with pre_step("Подождать, пока не исчезнут Уведомления"):
        lines_control_page.wait_for_invisible_notifications()
    with pre_step("Переход на страницу управления 1 полосой"):
        lines_control_page.go_to_line1()
        line1_control_page = Line1ControlForm()
        assert line1_control_page.is_wait_for_form_load(), "Страница не загрузилась"

    with pre_step("Занять полосу, если она освобождена"):
        if line1_control_page.lane_is_free():
            line1_control_page.change_busy_line()



    with pre_step("Остановить упражнение, если оно запущено"):
        if not line1_control_page.ex_is_stopped(): # если упр. не остановлено
            line1_control_page.press_stop() # остановить

    with pre_step("Подождать, пока не исчезнут Уведомления"):
        line1_control_page.wait_for_invisible_notifications()

    yield  line1_control_page

    with post_step("Остановить упражнение, если оно запущено"):
        if not line1_control_page.ex_is_stopped(): # если упр. не остановлено
            line1_control_page.press_stop() # остановить

    with post_step("Освободить полосу, если она занята"):
        if line1_control_page.lane_is_busy():  #Если полоса занята
            line1_control_page.change_busy_line() #поменять занятость, освободить
        assert line1_control_page.lane_is_free(), "Страница не освободилась"

#"url": "http://10.10.72.214",