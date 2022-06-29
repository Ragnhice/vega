import allure
import pytest
import aqas


from models.ui.forms.header.header_form import HeaderForm
from models.ui.forms.lanes_control_form import LanesControlForm
from models.ui.forms.side_bar_form import SideBarForm
from models.ui.forms.common_elements import CommonFormElements, CommonForm
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

    @allure.title("auth_admin_view_buttons")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-331")
    def test_auth_admin(self, get_auth_admin):
        lanes_control_page = get_auth_admin

        with aqas.step("Подождать, пока не исчезнут Уведомления"):
            lanes_control_page.is_notifications_invisible()

        with aqas.step("Занять полосу"):
            if is_located(lanes_control_page.elements.LANE1_IS_FREE_LBL):
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
            assert is_located(sidebar_page.elements.SHOOTING_MODE_BTN), "Администратору недоступны настройки тира"

        with aqas.step("Проверить доступ к работе с базой упражнений"):
            assert is_located(sidebar_page.elements.EX_EDITOR_BTN), "Администратору недоступен редактор"

        with aqas.step("Проверить доступ к работе с базой пользователей"):
            assert is_located(sidebar_page.elements.USERS_BTN), "Администратору недоступен список пользователей"

        with aqas.step("Проверить доступ к Установке параметров работы оборудования"):
            assert is_located(sidebar_page.elements.CAMERA_SETTINGS_BTN), "Администратору недоступны настройки камеры"
            assert is_located(sidebar_page.elements.SERVICE_BTN), "Администратору недоступны сервисные функции"

        with aqas.step("Закрыть боковое меню"):
            sidebar_page.close_settings()
            lanes_control_page = LanesControlForm()

        with aqas.step("Освободить полосу"):
            if is_located(lanes_control_page.elements.LANE1_IS_BUSY_LBL):
                lanes_control_page.change_busy_lane1_admin()

    @allure.title("auth_shooter_view_buttons")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-332")
    def test_auth_shooter(self, get_auth_shooter):
        lanes_control_page = get_auth_shooter

        with aqas.step("Подождать, пока не исчезнут Уведомления"):
            lanes_control_page.is_notifications_invisible()

        with aqas.step("Проверить отсутствие доступа к изменению занятости полосы"):
            assert is_located(
                lanes_control_page.elements.BUSY_LANE1_RADIO_DISABLED_LBL), "Стрелку доступен запуск упражнения"

        with aqas.step("Проверить отсутствие доступа к изменению режима упражнения"):
            assert is_located(lanes_control_page.elements.PLAY_LANE1_DISABLED_LBL), "Стрелку доступен запуск упражнения"
            assert is_located(lanes_control_page.elements.STOP_LANE1_DISABLED_LBL), "Стрелку доступна остановка упражнения"
            assert is_located(
                lanes_control_page.elements.PAUSE_LANE1_DISABLED_LBL), "Стрелку доступен приостановка упражнения"

        with aqas.step("Переход к шапке страницы"):
            header_page = HeaderForm()
            assert header_page.is_wait_for_form_load(), "Страница не загрузилась"

        with aqas.step("Открыть боковое меню"):
            header_page.go_to_menu()
            sidebar_page = SideBarForm()
            assert sidebar_page.is_wait_for_form_load(), "Страница не загрузилась"

        with aqas.step("Проверить доступ к настройкам"):
            assert not is_located(sidebar_page.elements.SETTINGS_BTN), "Стрелку доступны настройки"

        with aqas.step("Проверить доступ к работе со статистикой"):
            assert is_located(sidebar_page.elements.STATISTIC_BTN), "Стрелку не доступна статистика"

        with aqas.step("Проверка доступа к Установке режима работы тира"):
            assert not is_located(sidebar_page.elements.SHOOTING_MODE_BTN), "Стрелку доступны настройки тира"

        with aqas.step("Проверить доступ к работе с базой упражнений"):
            assert not is_located(sidebar_page.elements.EX_EDITOR_BTN), "Стрелку доступен редактор"

        with aqas.step("Проверить доступ к работе с базой пользователей"):
            assert not is_located(sidebar_page.elements.USERS_BTN), "Стрелку доступен список пользователей"

        with aqas.step("Проверить доступ к Установке параметров работы оборудования"):
            assert not is_located(sidebar_page.elements.CAMERA_SETTINGS_BTN), "Стрелку доступны насройки камеры"
            assert not is_located(sidebar_page.elements.SERVICE_BTN), "Стрелку доступны сервисные функции"

        with aqas.step("Закрыть боковое меню"):
            sidebar_page.close_settings()
            lanes_control_page = LanesControlForm()

    @allure.title("auth_instructor_view_buttons")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-333")
    def test_auth_instructor(self, get_auth_instructor):
        lanes_control_page = get_auth_instructor

        with aqas.step("Подождать, пока не исчезнут Уведомления"):
            lanes_control_page.is_notifications_invisible()

        with aqas.step("Занять полосу"):
            if is_located(lanes_control_page.elements.LANE1_IS_FREE_LBL):
                lanes_control_page.change_busy_lane1_instructor()

        with aqas.step("Подождать, пока не исчезнут Уведомления"):
            lanes_control_page.is_notifications_invisible()

        with aqas.step("Проверить наличие доступа к изменению режима упражнения"):
            assert not is_located(lanes_control_page.elements.PLAY_LANE1_DISABLED_LBL), "Инструктору не доступен запуск упражнения"

        with aqas.step("Переход к шапке страницы"):
            header_page = HeaderForm()
            assert header_page.is_wait_for_form_load(), "Страница не загрузилась"

        with aqas.step("Открыть боковое меню"):
            header_page.go_to_menu()
            sidebar_page = SideBarForm()
            assert sidebar_page.is_wait_for_form_load(), "Страница не загрузилась"

        with aqas.step("Проверить доступ к работе с базой пользователей"):
            assert is_located(sidebar_page.elements.USERS_BTN), "Инструктору недоступен список пользователей"

        with aqas.step("Проверить доступ к работе со статистикой"):
            assert is_located(sidebar_page.elements.STATISTIC_BTN), "Инструктору не доступна статистика"

        with aqas.step("Проверить доступ к работе с организациями"):
            assert is_located(sidebar_page.elements.ORGANISATIONS_BTN), "Инструктору не доступны организации"

        with aqas.step("Проверить доступ к Установке параметров работы оборудования"):
            assert not is_located(sidebar_page.elements.CAMERA_SETTINGS_BTN), "Инструктору доступны настройки камеры"
            assert not is_located(sidebar_page.elements.SERVICE_BTN), "Инструктору доступны сервисные функции"

        with aqas.step("Проверка доступа к Установке режима работы тира"):
            assert not is_located(sidebar_page.elements.SHOOTING_MODE_BTN), "Инструктору доступны настройки тира"

        with aqas.step("Проверить доступ к работе с базой упражнений"):
            assert not is_located(sidebar_page.elements.EX_EDITOR_BTN), "Инструктору доступен редактор"

        with aqas.step("Проверить доступ к настройкам"):
            assert not is_located(sidebar_page.elements.SETTINGS_BTN), "Инструктору доступны настройки"

        with aqas.step("Закрыть боковое меню"):
            sidebar_page.close_settings()
            lanes_control_page = LanesControlForm()

        with aqas.step("Освободить полосу"):
            if is_located(lanes_control_page.elements.LANE1_IS_BUSY_LBL):
                lanes_control_page.change_busy_lane1_instructor()

        with aqas.step("Подождать, пока не исчезнут Уведомления"):
            lanes_control_page.is_notifications_invisible()


    @allure.title("auth_instructor_functional")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-333")
    def test_auth_instructor(self, get_auth_instructor):
        lanes_control_page = get_auth_instructor

        with aqas.step("Подождать, пока не исчезнут Уведомления"):
            lanes_control_page.is_notifications_invisible()

        with aqas.step("Занять полосу"):
            if is_located(lanes_control_page.elements.LANE1_IS_FREE_LBL):
                lanes_control_page.change_busy_lane1_instructor()

        with aqas.step("Подождать, пока не исчезнут Уведомления"):
            lanes_control_page.is_notifications_invisible()

        with aqas.step("Проверить наличие доступа к изменению режима упражнения"):
            assert not is_located(lanes_control_page.elements.PLAY_LANE1_DISABLED_LBL), "Инструктору не доступен запуск упражнения"

        with aqas.step("Переход к шапке страницы"):
            header_page = HeaderForm()
            assert header_page.is_wait_for_form_load(), "Страница не загрузилась"

        with aqas.step("Открыть боковое меню"):
            header_page.go_to_menu()
            sidebar_page = SideBarForm()
            assert sidebar_page.is_wait_for_form_load(), "Страница не загрузилась"

        with aqas.step("Проверить доступ к работе с базой пользователей"):
            assert is_located(sidebar_page.elements.USERS_BTN), "Инструктору недоступен список пользователей"

    Можно
    создать пользователя


    отредактировать
    пользователя

    Печать
    отчетов
    на
    полосе

    Можно
    сформировать
    отчет в статистике



    @allure.title("auth_admin_functional")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-331")
    def test_auth_admin(self, get_auth_admin):
        lanes_control_page = get_auth_admin

        with aqas.step("Подождать, пока не исчезнут Уведомления"):
            lanes_control_page.is_notifications_invisible()

        with aqas.step("Занять полосу"):
            if is_located(lanes_control_page.elements.LANE1_IS_FREE_LBL):
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

        with aqas.step("Проверить доступ к работе с базой пользователей"):
            assert is_located(sidebar_page.elements.USERS_BTN), "Администратору недоступен список пользователей"

            Работать
            на
            чужой
            полосе

            Установке
            режима
            работы
            тира

            есть недоступная кнопка удаления пользователя

            Можно
            создать и удалить поьзователя
