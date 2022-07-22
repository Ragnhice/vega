# pylint: disable=W0621
import aqas
import pytest

from models.ui.forms.auth_form import AuthenticationForm
from models.ui.forms.lane1_control_form import Lane1ControlForm
from models.ui.forms.lanes_control_form import LanesControlForm
from utils.element_utils import is_located
from utils.enums import UserTypeEnum


@pytest.fixture(scope="function")
def start_browser(request):
    with aqas.pre_step("Запуск браузера"):
        aqas.browser.start(request.node.name)

    with aqas.pre_step("Переход на главную страницу"):
        aqas.browser.navigation.go_to(aqas.config.project_settings.url)

    yield

    with aqas.post_step("Закрытие браузера"):
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

    with aqas.pre_step("Подождать, пока не исчезнут Уведомления"):
        lanes_control_page.wait_for_notifications_invisible()

    yield lanes_control_page


@pytest.fixture(scope="function")
def go_lane1(get_auth_admin):
    """Для проверок, когда нужно перейти на 1 полосу и занять ее."""

    lanes_control_page = get_auth_admin

    with aqas.pre_step("Подождать, пока не исчезнут Уведомления"):
        lanes_control_page.wait_for_notifications_invisible()

    with aqas.pre_step("Переход на страницу управления 1 полосой"):
        lanes_control_page.elements.LANE1_LBL.wait_and_click()
        lane1_control_page = Lane1ControlForm()
        assert lane1_control_page.is_wait_for_form_load(), "Страница не загрузилась"

    with aqas.pre_step("Занять полосу, если она освобождена"):
        if is_located(lane1_control_page.elements.LANE_IS_FREE_LBL):
            lane1_control_page.elements.BUSY_LANE_BTN.click()

    with aqas.step("Проверить, что полоса стала занятой"):
        assert is_located(lane1_control_page.elements.LANE_IS_BUSY_LBL), "Полоса не стала занятой"

    with aqas.pre_step("Остановить упражнение, если оно запущено"):
        if not is_located(lane1_control_page.elements.STOP_DISABLED_LBL):
            lane1_control_page.elements.STOP_BTN.click()

    with aqas.pre_step("Подождать, пока не исчезнут Уведомления"):
        lane1_control_page.wait_for_notification_invisible()

    yield lane1_control_page

    with aqas.post_step("Подождать, пока не исчезнут Уведомления"):
        lane1_control_page.wait_for_notifications_invisible()

    with aqas.post_step("Остановить упражнение, если оно запущено"):
        if not is_located(lane1_control_page.elements.STOP_DISABLED_LBL):
            lane1_control_page.elements.STOP_BTN.click()

    with aqas.post_step("Подождать, пока не исчезнут Уведомления"):
        lane1_control_page.wait_for_notifications_invisible()

    with aqas.post_step("Освободить полосу, если она занята"):
        if is_located(lane1_control_page.elements.LANE_IS_BUSY_LBL):
            lane1_control_page.elements.BUSY_LANE_BTN.reset()
            lane1_control_page.elements.BUSY_LANE_BTN.click()

    with aqas.post_step("Проверить, что полоса стала свободной"):
        assert is_located(lane1_control_page.elements.LANE_IS_FREE_LBL), "Полоса не стала свободной"

    with aqas.post_step("Подождать, пока не исчезнут Уведомления"):
        lane1_control_page.wait_for_notifications_invisible()


@pytest.fixture(scope="function")
def set_free_lane_and_stopped_ex(get_auth_admin):
    """Для проверок, когда нужно на экране Управление полосами освободить полосу и остановить упражнение."""

    lanes_control_page = get_auth_admin

    with aqas.pre_step("Подождать, пока не исчезнут Уведомления"):
        lanes_control_page.wait_for_notifications_invisible()

    with aqas.pre_step("Освободить полосу, если она занята"):
        if is_located(lanes_control_page.elements.LANE1_IS_BUSY_LBL):
            lanes_control_page.elements.BUSY_LANE1_ADMIN_BTN.click()

    with aqas.pre_step("Остановить упражнение, если оно запущено"):
        if not is_located(lanes_control_page.elements.STOP_LANE1_DISABLED_LBL):
            lanes_control_page.elements.STOP_LANE1_BTN.click()

    with aqas.pre_step("Подождать, пока не исчезнут Уведомления"):
        lanes_control_page.wait_for_notifications_invisible()

    yield lanes_control_page

    with aqas.post_step("Освободить полосу, если она занята"):
        if is_located(lanes_control_page.elements.LANE1_IS_BUSY_LBL):
            lanes_control_page.elements.BUSY_LANE1_ADMIN_BTN.click()

    with aqas.post_step("Остановить упражнение, если оно запущено"):
        if not is_located(lanes_control_page.elements.STOP_LANE1_DISABLED_LBL):
            lanes_control_page.elements.STOP_LANE1_BTN.click()

    with aqas.post_step("Подождать, пока не исчезнут Уведомления"):
        lanes_control_page.wait_for_notifications_invisible()

    with aqas.post_step("Проверить, что полоса освободилась, упражнение остановлено"):
        assert is_located(lanes_control_page.elements.STOP_LANE1_DISABLED_LBL), "Упражнение не останавливается"
        assert is_located(lanes_control_page.elements.LANE1_IS_FREE_LBL), "Полоса не освободилась"


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

    with aqas.pre_step("Подождать, пока не исчезнут Уведомления"):
        lanes_control_page.wait_for_notifications_invisible()

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

    with aqas.pre_step("Подождать, пока не исчезнут Уведомления"):
        lanes_control_page.wait_for_notifications_invisible()

    yield lanes_control_page
