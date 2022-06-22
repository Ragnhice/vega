import pytest
from aqas.utils.step import step

from models.ui.forms.conditions_menu_form import ConditionsMenuForm
from models.ui.forms.exercise_menu_form import ExerciseMenuForm
from models.ui.forms.lanes_control_form import LanesControlForm
from models.ui.forms.shooters_chose_form import ShootersChoseForm
from models.ui.forms.header.header_form import HeaderForm
from models.ui.forms.side_bar_form import SideBarForm

@pytest.mark.usefixtures("start_browser")
class TestAuth():
    """
    Класс, который содержит действия теста при проверке ролей аутетификации
    """
    SEARCH_CONDITION = "Автотесты"

    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-331")
    def test_auth_admin(self, get_auth_admin):
        lanes_control_page = get_auth_admin
        with step("Занять полосу"):
            if lanes_control_page.lane_is_free():
                lanes_control_page.change_busy_lane1()

        with step("Подождать, пока не исчезнут Уведомления"):
            lanes_control_page.wait_for_invisible_notifications()

        with step("Переход к шапке страницы"):
            header_page = HeaderForm()
            assert header_page.is_wait_for_form_load(), "Страница не загрузилась"

        with step("Открыть боковое меню"):
            header_page.go_to_menu()
            sidebar_page = SideBarForm()
            assert sidebar_page.is_wait_for_form_load(), "Страница не загрузилась"

        with step("Поиск доступных сервисов для роли адмнистрантора"):
            sidebar_page.open_settings()

        with step("Проверка доступа к Установке режима работы тира"):
            assert sidebar_page.find_shooting_mode(), "Администратору недоступен редактор"

        with step("Проверить доступ к работе с базой упражнений"):
            assert sidebar_page.find_ex_editor(), "Администратору недоступен редактор"

        with step("Проверить доступ к работе с базой пользователей"):
            assert sidebar_page.find_staff(), "Администратору недоступен список пользователей"

        with step("Проверить доступ к Установке параметров работы оборудования"):
            assert sidebar_page.find_camera_settings(), "Администратору недоступны насройки камеры"
            assert sidebar_page.find_service(), "Администратору недоступны сервисные функции"

        with step("Закрыть боковое меню"):
            sidebar_page.close_settings()
            lanes_control_page = LanesControlForm()

        with step("Освободить полосу"):
            if lanes_control_page.lane_is_busy():
                lanes_control_page.change_busy_lane1()


    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-332")
    def test_auth_shooter(self, get_auth_shooter):
        lanes_control_page = get_auth_shooter
        with step("Занять полосу"):
            if lanes_control_page.lane_is_free():
                lanes_control_page.change_busy_lane1()

        with step("Подождать, пока не исчезнут Уведомления"):
            lanes_control_page.wait_for_invisible_notifications()

        with step("Переход к шапке страницы"):
            header_page = HeaderForm()
            assert header_page.is_wait_for_form_load(), "Страница не загрузилась"

        with step("Открыть боковое меню"):
            header_page.go_to_menu()
            sidebar_page = SideBarForm()
            assert sidebar_page.is_wait_for_form_load(), "Страница не загрузилась"

        with step("Поиск доступных сервисов для роли адмнистрантора"):
            sidebar_page.open_settings()

        with step("Проверка доступа к Установке режима работы тира"):
            assert sidebar_page.find_shooting_mode(), "Администратору недоступен редактор"

        with step("Проверить доступ к работе с базой упражнений"):
            assert sidebar_page.find_ex_editor(), "Администратору недоступен редактор"

        with step("Проверить доступ к работе с базой пользователей"):
            assert sidebar_page.find_staff(), "Администратору недоступен список пользователей"

        with step("Проверить доступ к Установке параметров работы оборудования"):
            assert sidebar_page.find_camera_settings(), "Администратору недоступны насройки камеры"
            assert sidebar_page.find_service(), "Администратору недоступны сервисные функции"

        with step("Закрыть боковое меню"):
            sidebar_page.close_settings()
            lanes_control_page = LanesControlForm()

        with step("Освободить полосу"):
            if lanes_control_page.lane_is_busy():
                lanes_control_page.change_busy_lane1()


    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-333")
    def test_auth_instuctor(self, get_auth_instuctor):
        lanes_control_page = get_auth_instuctor
        with step("Занять полосу"):
            if lanes_control_page.lane_is_free():
                lanes_control_page.change_busy_lane1()

        with step("Подождать, пока не исчезнут Уведомления"):
            lanes_control_page.wait_for_invisible_notifications()

        with step("Переход к шапке страницы"):
            header_page = HeaderForm()
            assert header_page.is_wait_for_form_load(), "Страница не загрузилась"

        with step("Открыть боковое меню"):
            header_page.go_to_menu()
            sidebar_page = SideBarForm()
            assert sidebar_page.is_wait_for_form_load(), "Страница не загрузилась"

        with step("Поиск доступных сервисов для роли адмнистрантора"):
            sidebar_page.open_settings()

        with step("Проверка доступа к Установке режима работы тира"):
            assert sidebar_page.find_shooting_mode(), "Администратору недоступен редактор"

        with step("Проверить доступ к работе с базой упражнений"):
            assert sidebar_page.find_ex_editor(), "Администратору недоступен редактор"

        with step("Проверить доступ к работе с базой пользователей"):
            assert sidebar_page.find_staff(), "Администратору недоступен список пользователей"

        with step("Проверить доступ к Установке параметров работы оборудования"):
            assert sidebar_page.find_camera_settings(), "Администратору недоступны насройки камеры"
            assert sidebar_page.find_service(), "Администратору недоступны сервисные функции"

        with step("Закрыть боковое меню"):
            sidebar_page.close_settings()
            lanes_control_page = LanesControlForm()

        with step("Освободить полосу"):
            if lanes_control_page.lane_is_busy():
                lanes_control_page.change_busy_lane1()

                changed
                locators, added
                ready
                test
                auth
                admin