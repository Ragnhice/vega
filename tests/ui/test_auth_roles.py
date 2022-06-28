import allure
import pytest
import aqas


from models.ui.forms.header.header_form import HeaderForm
from models.ui.forms.lanes_control_form import LanesControlForm
from models.ui.forms.side_bar_form import SideBarForm
from utils.element_utils import *


@allure.parent_suite("ui")
@allure.suite("Authorization Roles")
@pytest.mark.usefixtures("start_browser")
class TestAuthRoles:
    """
    Класс, который содержит действия теста при проверке авторизации ролей:
    - администратора;
    - стрелка;
    - инструктора.
    """

    @allure.title("auth_admin")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-331")
    def test_auth_admin(self, get_auth_admin):
        lanes_control_page = get_auth_admin

        with aqas.step("Подождать, пока не исчезнут Уведомления"):
            lanes_control_page.is_notifications_invisible()

        with aqas.step("Занять полосу"):
            if is_located(lanes_control_page.elements.LANE1_IS_FREE):
                lanes_control_page.change_busy_lane1_admin()

        with aqas.step("Подождать, пока не исчезнут Уведомления"):
            lanes_control_page.is_notifications_invisible()

        with aqas.step("Переход к шапке страницы"):
            header_page = HeaderForm()
            assert header_page.is_wait_for_form_load(), "Страница не загрузилась"

        with aqas.step("Открыть боковое меню"):
            header_page.go_to_menu()
            sidebar_page = SideBarForm()
            assert sidebar_page.is_wait_for_form_load(), "Страница не загрузилась"

        with aqas.step("Поиск доступных сервисов для роли администратора"):
            sidebar_page.open_settings()

        with aqas.step("Проверка доступа к Установке режима работы тира"):
            assert is_located(sidebar_page.elements.SHOOTING_MODE), "Администратору недоступны настройки тира"

        with aqas.step("Проверить доступ к работе с базой упражнений"):
            assert is_located(sidebar_page.elements.EX_EDITOR), "Администратору недоступен редактор"

        with aqas.step("Проверить доступ к работе с базой пользователей"):
            assert is_located(sidebar_page.elements.STAFF), "Администратору недоступен список пользователей"

        with aqas.step("Проверить доступ к Установке параметров работы оборудования"):
            assert is_located(sidebar_page.elements.CAMERA_SETTINGS), "Администратору недоступны настройки камеры"
            assert is_located(sidebar_page.elements.SERVICE), "Администратору недоступны сервисные функции"

        with aqas.step("Закрыть боковое меню"):
            sidebar_page.close_settings()
            lanes_control_page = LanesControlForm()

        with aqas.step("Освободить полосу"):
            if is_located(lanes_control_page.elements.LANE1_IS_BUSY):
                lanes_control_page.change_busy_lane1_admin()

    @allure.title("auth_shooter")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-332")
    def test_auth_shooter(self, get_auth_shooter):
        lanes_control_page = get_auth_shooter

        with aqas.step("Подождать, пока не исчезнут Уведомления"):
            lanes_control_page.is_notifications_invisible()

        with aqas.step("Проверить отсутствие доступа к изменению занятости полосы"):
            assert is_located(
                lanes_control_page.elements.BUSY_LANE1_RADIO_DISABLED), "Стрелку доступен запуск упражнения"

        with aqas.step("Проверить отсутствие доступа к изменению режима упражнения"):
            assert is_located(lanes_control_page.elements.PLAY_LANE1_DISABLED), "Стрелку доступен запуск упражнения"
            assert is_located(lanes_control_page.elements.STOP_LANE1_DISABLED), "Стрелку доступна остановка упражнения"
            assert is_located(
                lanes_control_page.elements.PAUSE_LANE1_DISABLED), "Стрелку доступен приостановка упражнения"

        with aqas.step("Переход к шапке страницы"):
            header_page = HeaderForm()
            assert header_page.is_wait_for_form_load(), "Страница не загрузилась"

        with aqas.step("Открыть боковое меню"):
            header_page.go_to_menu()
            sidebar_page = SideBarForm()
            assert sidebar_page.is_wait_for_form_load(), "Страница не загрузилась"

        with aqas.step("Проверить доступ к настройкам"):
            assert not is_located(sidebar_page.elements.SETTINGS), "Стрелку доступны настройки"

        with aqas.step("Проверить доступ к работе со статистикой"):
            assert is_located(sidebar_page.elements.STATISTIC), "Стрелку не доступна статистика"

        with aqas.step("Проверка доступа к Установке режима работы тира"):
            assert not is_located(sidebar_page.elements.SHOOTING_MODE), "Стрелку доступны настройки тира"

        with aqas.step("Проверить доступ к работе с базой упражнений"):
            assert not is_located(sidebar_page.elements.EX_EDITOR), "Стрелку доступен редактор"

        with aqas.step("Проверить доступ к работе с базой пользователей"):
            assert not is_located(sidebar_page.elements.STAFF), "Стрелку доступен список пользователей"

        with aqas.step("Проверить доступ к Установке параметров работы оборудования"):
            assert not is_located(sidebar_page.elements.CAMERA_SETTINGS), "Стрелку доступны насройки камеры"
            assert not is_located(sidebar_page.elements.SERVICE), "Стрелку доступны сервисные функции"

        with aqas.step("Закрыть боковое меню"):
            sidebar_page.close_settings()
            lanes_control_page = LanesControlForm()

    @allure.title("auth_instructor")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-333")
    def test_auth_instructor(self, get_auth_instructor):
        lanes_control_page = get_auth_instructor

        with aqas.step("Подождать, пока не исчезнут Уведомления"):
            lanes_control_page.is_notifications_invisible()

        with aqas.step("Занять полосу"):
            if is_located(lanes_control_page.elements.LANE1_IS_FREE):
                lanes_control_page.change_busy_lane1_instructor()

        with aqas.step("Подождать, пока не исчезнут Уведомления"):
            lanes_control_page.is_notifications_invisible()

        with aqas.step("Проверить наличие доступа к изменению режима упражнения"):
            assert not is_located(lanes_control_page.elements.PLAY_LANE1_DISABLED), "Инструктору не доступен запуск упражнения"

        with aqas.step("Переход к шапке страницы"):
            header_page = HeaderForm()
            assert header_page.is_wait_for_form_load(), "Страница не загрузилась"

        with aqas.step("Открыть боковое меню"):
            header_page.go_to_menu()
            sidebar_page = SideBarForm()
            assert sidebar_page.is_wait_for_form_load(), "Страница не загрузилась"

        with aqas.step("Проверить доступ к работе с базой пользователей"):
            assert is_located(sidebar_page.elements.STAFF), "Инструктору недоступен список пользователей"

        with aqas.step("Проверить доступ к работе со статистикой"):
            assert is_located(sidebar_page.elements.STATISTIC), "Инструктору не доступна статистика"

        with aqas.step("Проверить доступ к работе с организациями"):
            assert is_located(sidebar_page.elements.ORGANISATONS), "Инструктору не доступны организации"

        with aqas.step("Проверить доступ к Установке параметров работы оборудования"):
            assert not is_located(sidebar_page.elements.CAMERA_SETTINGS), "Инструктору доступны настройки камеры"
            assert not is_located(sidebar_page.elements.SERVICE), "Инструктору доступны сервисные функции"

        with aqas.step("Проверка доступа к Установке режима работы тира"):
            assert not is_located(sidebar_page.elements.SHOOTING_MODE), "Инструктору доступны настройки тира"

        with aqas.step("Проверить доступ к работе с базой упражнений"):
            assert not is_located(sidebar_page.elements.EX_EDITOR), "Инструктору доступен редактор"

        with aqas.step("Проверить доступ к настройкам"):
            assert not is_located(sidebar_page.elements.SETTINGS), "Инструктору доступны настройки"

        with aqas.step("Закрыть боковое меню"):
            sidebar_page.close_settings()
            lanes_control_page = LanesControlForm()

        with aqas.step("Освободить полосу"):
            if is_located(lanes_control_page.elements.LANE1_IS_BUSY):
                lanes_control_page.change_busy_lane1_instructor()

        with aqas.step("Подождать, пока не исчезнут Уведомления"):
            lanes_control_page.is_notifications_invisible()
