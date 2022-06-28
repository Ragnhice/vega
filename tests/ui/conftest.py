# pylint: disable=W0621

import aqas
import pytest

from models.ui.forms.auth_form import AuthenticationForm
from models.ui.forms.lane1_control_form import Lane1ControlForm
from models.ui.forms.lanes_control_form import LanesControlForm
from utils.element_utils import *
from utils.enums import UserTypeEnum


@pytest.fixture(scope="function")
def start_browser():
    aqas.browser.start()
    aqas.browser.navigation.go_to(aqas.config.project_settings.url)
    yield
    aqas.browser.stop()


@pytest.fixture(scope="function")
def get_auth_admin():
    """Аутентификация администратором и переход на страницу управления полосами."""

    with aqas.pre_step("Переход на страницу аутентификации"):
        auth_page = AuthenticationForm()
        assert auth_page.is_wait_for_form_load(), "Страница не загрузилась"

    with aqas.pre_step("Переход на страницу управления полосами"):
        auth_page.login(UserTypeEnum.ADMINISTRATOR)
        lanes_control_page = LanesControlForm()
        assert lanes_control_page.is_wait_for_form_load(), "Страница не загрузилась"

    yield lanes_control_page


@pytest.fixture(scope="function")
def go_lane1(get_auth_admin):
    """Для проверок, когда нужно перейти на 1 полосу и занять ее."""

    lanes_control_page = get_auth_admin

    with aqas.pre_step("Подождать, пока не исчезнут Уведомления"):
        lanes_control_page.is_notifications_invisible()

    with aqas.pre_step("Переход на страницу управления 1 полосой"):
        lanes_control_page.go_to_lane1()
        lane1_control_page = Lane1ControlForm()
        assert lane1_control_page.is_wait_for_form_load(), "Страница не загрузилась"

    with aqas.pre_step("Занять полосу, если она освобождена"):
        if is_located(lane1_control_page.elements.LANE_IS_FREE):
            lane1_control_page.change_busy_lane()

    with aqas.pre_step("Остановить упражнение, если оно запущено"):
        if not is_located(lane1_control_page.elements.STOP_DISABLED):
            lane1_control_page.press_stop()  # остановить

    with aqas.pre_step("Подождать, пока не исчезнут Уведомления"):
        lane1_control_page.is_notification_invisible()

    yield lane1_control_page

    with aqas.post_step("Остановить упражнение, если оно запущено"):
        if not is_located(lane1_control_page.elements.STOP_DISABLED):
            lane1_control_page.press_stop()

    with aqas.post_step("Подождать, пока не исчезнут Уведомления"):
        lane1_control_page.is_notifications_invisible()

    with aqas.post_step("Освободить полосу, если она занята"):
        if is_located(lane1_control_page.elements.LANE_IS_BUSY):
            lane1_control_page.change_busy_lane()

        with aqas.post_step("Подождать, пока не исчезнут Уведомления"):
            lane1_control_page.is_notifications_invisible()


@pytest.fixture(scope="function")
def set_free_lane_and_stopped_ex(get_auth_admin):
    """Для проверок, когда нужно на экране Управление полосами освободить полосу и остановить упражнение."""

    lanes_control_page = get_auth_admin

    with aqas.pre_step("Подождать, пока не исчезнут Уведомления"):
        lanes_control_page.is_notifications_invisible()

    with aqas.pre_step("Освободить полосу, если она занята"):
        if is_located(lanes_control_page.elements.LANE1_IS_BUSY):
            lanes_control_page.change_busy_lane1_admin()

    with aqas.pre_step("Остановить упражнение, если оно запущено"):
        if not is_located(lanes_control_page.elements.STOP_LANE1_DISABLED):
            lanes_control_page.press_stop()

    with aqas.pre_step("Подождать, пока не исчезнут Уведомления"):
        lanes_control_page.is_notifications_invisible()

    yield lanes_control_page

    with aqas.post_step("Освободить полосу, если она занята"):
        if is_located(lanes_control_page.elements.LANE1_IS_BUSY):
            lanes_control_page.change_busy_lane1_admin()

    with aqas.post_step("Остановить упражнение, если оно запущено"):
        if not is_located(lanes_control_page.elements.STOP_LANE1_DISABLED):
            lanes_control_page.press_stop()

    with aqas.post_step("Подождать, пока не исчезнут Уведомления"):
        lanes_control_page.is_notifications_invisible()
        assert is_located(lanes_control_page.elements.STOP_LANE1_DISABLED), "Упражнение не останавливается"
        assert is_located(lanes_control_page.elements.LANE1_IS_FREE), "Страница не освободилась"


@pytest.fixture(scope="function")
def get_auth_shooter():
    """Аутентификация стрелком и переход на страницу управления полосами."""

    with aqas.pre_step("Переход на страницу аутентификации"):
        auth_page = AuthenticationForm()
        assert auth_page.is_wait_for_form_load(), "Страница не загрузилась"

    with aqas.pre_step("Переход на страницу управления полосами"):
        auth_page.login(UserTypeEnum.SHOOTER)
        lanes_control_page = LanesControlForm()
        assert lanes_control_page.is_wait_for_form_load(), "Страница не загрузилась"

    yield lanes_control_page


@pytest.fixture(scope="function")
def get_auth_instructor():
    """Аутентификация инструктором и переход на страницу управления полосами."""

    with aqas.pre_step("Переход на страницу аутентификации"):
        auth_page = AuthenticationForm()
        assert auth_page.is_wait_for_form_load(), "Страница не загрузилась"

    with aqas.pre_step("Переход на страницу управления полосами"):
        auth_page.login(UserTypeEnum.INSTRUCTOR)
        lanes_control_page = LanesControlForm()
        assert lanes_control_page.is_wait_for_form_load(), "Страница не загрузилась"

    yield lanes_control_page
