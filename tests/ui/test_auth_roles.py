import allure
import aqas
import pytest

from models.ui.forms.lanes_control_form import LanesControlForm
from models.ui.forms.new_user_form import NewUserForm
from models.ui.forms.organisations_form import OrganisationsForm
from models.ui.forms.shooting_settings_form import ShootingSettingsForm
from models.ui.forms.side_bar_form import SideBarForm
from models.ui.forms.statistic_form import StatisticForm
from models.ui.forms.users_form import UsersForm
from utils.element_utils import is_located


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
            lanes_control_page.wait_for_notifications_invisible()

        with aqas.step("Занять полосу"):
            if is_located(lanes_control_page.elements.LANE1_IS_FREE_LBL):
                lanes_control_page.elements.BUSY_LANE1_ADMIN_BTN.click()

        with aqas.step("Подождать, пока не исчезнут Уведомления"):
            lanes_control_page.wait_for_notifications_invisible()

        with aqas.step("Открыть боковое меню"):
            lanes_control_page.elements.MENU_BTN.click()
            sidebar_page = SideBarForm()
            assert sidebar_page.is_wait_for_form_load(), "Страница не загрузилась"

        with aqas.step("Поиск доступных сервисов для роли администратора"):
            sidebar_page.elements.SETTINGS_BTN.click()

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
            sidebar_page.elements.CLOSE_BTN.click()
            lanes_control_page = LanesControlForm()

        with aqas.step("Освободить полосу"):
            if is_located(lanes_control_page.elements.LANE1_IS_BUSY_LBL):
                lanes_control_page.elements.BUSY_LANE1_ADMIN_BTN.click()

    @allure.title("auth_shooter_view_buttons")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-332")
    def test_auth_shooter(self, get_auth_shooter):
        lanes_control_page = get_auth_shooter

        with aqas.step("Подождать, пока не исчезнут Уведомления"):
            lanes_control_page.wait_for_notifications_invisible()

        with aqas.step("Проверить отсутствие доступа к изменению занятости полосы"):
            assert is_located(
                lanes_control_page.elements.BUSY_LANE1_RADIO_DISABLED_LBL), "Стрелку доступен запуск упражнения"

        with aqas.step("Проверить отсутствие доступа к изменению режима упражнения"):
            assert is_located(lanes_control_page.elements.PLAY_LANE1_DISABLED_LBL), "Стрелку доступен запуск упражнения"
            assert is_located(
                lanes_control_page.elements.STOP_LANE1_DISABLED_LBL), "Стрелку доступна остановка упражнения"
            assert is_located(
                lanes_control_page.elements.PAUSE_LANE1_DISABLED_LBL), "Стрелку доступен приостановка упражнения"

        with aqas.step("Открыть боковое меню"):
            lanes_control_page.elements.MENU_BTN.click()
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
            sidebar_page.elements.CLOSE_BTN.click()

    @allure.title("auth_instructor_view_buttons")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-333")
    def test_auth_instructor(self, get_auth_instructor):
        lanes_control_page = get_auth_instructor

        with aqas.step("Подождать, пока не исчезнут Уведомления"):
            lanes_control_page.wait_for_notifications_invisible()

        with aqas.step("Занять полосу"):
            if is_located(lanes_control_page.elements.LANE1_IS_FREE_LBL):
                lanes_control_page.elements.BUSY_LANE1_INSTRUCTOR_BTN.click()

        with aqas.step("Подождать, пока не исчезнут Уведомления"):
            lanes_control_page.wait_for_notifications_invisible()

        with aqas.step("Проверить наличие доступа к изменению режима упражнения"):
            assert not is_located(
                lanes_control_page.elements.PLAY_LANE1_DISABLED_LBL), "Инструктору не доступен запуск упражнения"

        with aqas.step("Открыть боковое меню"):
            lanes_control_page.elements.MENU_BTN.click()
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
            sidebar_page.elements.CLOSE_BTN.click()

        with aqas.step("Освободить полосу"):
            if is_located(lanes_control_page.elements.LANE1_IS_BUSY_LBL):
                lanes_control_page.elements.BUSY_LANE1_INSTRUCTOR_BTN.click()

        with aqas.step("Подождать, пока не исчезнут Уведомления"):
            lanes_control_page.wait_for_notifications_invisible()

    @allure.title("auth_instructor_functional")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-359")
    def test_auth_instructor_functional(self, get_auth_instructor):
        lanes_control_page = get_auth_instructor

        with aqas.step("Подождать, пока не исчезнут Уведомления"):
            lanes_control_page.wait_for_notifications_invisible()

        with aqas.step("Открыть боковое меню"):
            lanes_control_page.elements.MENU_BTN.click()
            sidebar_page = SideBarForm()
            assert sidebar_page.is_wait_for_form_load(), "Страница не загрузилась"

        with aqas.step("Открыть базу пользователей"):
            sidebar_page.elements.USERS_BTN.click()
            users_page = UsersForm()
            assert users_page.is_wait_for_form_load(), "Страница не загрузилась"

        with aqas.step("Проверить, что нет кнопки удаления в некликабельном состоянии"):
            assert not is_located(users_page.elements.DELETE_DISABLED_LBL), "Инструтору видна кнопка удаления"

        with aqas.step("Перейти на страницу добавления пользователя"):
            users_page.elements.ADD_BTN.click()
            new_user_page = NewUserForm()
            assert new_user_page.is_wait_for_form_load(), "Страница не загрузилась"

        with aqas.step("Ввести данные нового пользователя"):
            new_user_page.elements.LASTNAME_TBX.send_keys("Фамилиятест")
            new_user_page.elements.LOGIN_TBX.send_keys("Логинтест")
            new_user_page.elements.PASSWORD_TBX.send_keys("1111")
            new_user_page.elements.FIRSTNAME_TBX.send_keys("Имятест")
            new_user_page.elements.MIDDLENAME_TBX.send_keys("Отчествотест")
            new_user_page.elements.SAVE_BTN.click()

        with aqas.step("Подождать, пока не исчезнут Уведомления"):
            users_page.wait_for_notifications_invisible()

        with aqas.step("Изменить только что созданного стрелка"):
            users_page.elements.NEW_USER_LBL.click()
            users_page.elements.PASSWORD_TBX.send_keys("1111")
            users_page.elements.SAVE_BTN.click()

        with aqas.step("Подождать, пока не исчезнут Уведомления"):
            users_page.wait_for_notifications_invisible()

        with aqas.step("Открыть боковое меню"):
            users_page.elements.MENU_USERS_BTN.click()
            assert sidebar_page.is_wait_for_form_load(), "Страница не загрузилась"

        with aqas.step("Открыть окно управлени полосами"):
            sidebar_page.elements.LANES_CONTROLLING_BTN.click()
            assert lanes_control_page.is_wait_for_form_load(), "Страница не загрузилась"

    @allure.title("auth_admin_func_users")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-357")
    def test_auth_admin_users(self, get_auth_admin):
        lanes_control_page = get_auth_admin

        with aqas.step("Подождать, пока не исчезнут Уведомления"):
            lanes_control_page.wait_for_notifications_invisible()

        with aqas.step("Занять полосу"):
            if is_located(lanes_control_page.elements.LANE1_IS_FREE_LBL):
                lanes_control_page.elements.BUSY_LANE1_ADMIN_BTN.click()

        with aqas.step("Подождать, пока не исчезнут Уведомления"):
            lanes_control_page.wait_for_notifications_invisible()

        with aqas.step("Открыть боковое меню"):
            lanes_control_page.elements.MENU_BTN.click()
            sidebar_page = SideBarForm()
            assert sidebar_page.is_wait_for_form_load(), "Страница не загрузилась"

        with aqas.step("Открыть базу пользователей"):
            sidebar_page.elements.USERS_BTN.click()
            users_page = UsersForm()
            assert users_page.is_wait_for_form_load(), "Страница не загрузилась"

        with aqas.step("Перейти на страницу добавления пользователя"):
            users_page.elements.ADD_BTN.click()
            new_user_page = NewUserForm()
            assert new_user_page.is_wait_for_form_load(), "Страница не загрузилась"

        with aqas.step("Ввести данные нового пользователя"):
            new_user_page.elements.LASTNAME_TBX.send_keys("Фамилия_тест")
            new_user_page.elements.LOGIN_TBX.send_keys("Логин_тест")
            new_user_page.elements.PASSWORD_TBX.send_keys("Пароль_тест")
            new_user_page.elements.FIRSTNAME_TBX.send_keys("Имя_тест")
            new_user_page.elements.MIDDLENAME_TBX.send_keys("Отчество_тест")
            new_user_page.elements.SAVE_BTN.click()

        with aqas.step("Подождать, пока не исчезнут Уведомления"):
            users_page.wait_for_notifications_invisible()

        with aqas.step("Проверить, что есть кнопка удаления в некликабельном состоянии"):
            assert is_located(users_page.elements.DELETE_DISABLED_LBL), "Администратор не видит кнопки удаления"

        with aqas.step("Изменить только что созданного стрелка"):
            users_page.elements.NEW_USER_LBL.click()
            users_page.elements.PASSWORD_TBX.send_keys("Пароль_тест")
            users_page.elements.SAVE_BTN.click()

        with aqas.step("Подождать, пока не исчезнут Уведомления"):
            users_page.wait_for_notifications_invisible()

        with aqas.step("Открыть боковое меню"):
            users_page.elements.MENU_USERS_BTN.wait_and_click()
            assert sidebar_page.is_wait_for_form_load(), "Страница не загрузилась"

        with aqas.step("Открыть окно управлени полосами"):
            sidebar_page.elements.LANES_CONTROLLING_BTN.click()
            assert lanes_control_page.is_wait_for_form_load(), "Страница не загрузилась"

    @allure.title("auth_admin_shooting")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-386")
    def test_auth_admin_shooting(self, get_auth_admin):
        lanes_control_page = get_auth_admin

        with aqas.step("Подождать, пока не исчезнут Уведомления"):
            lanes_control_page.wait_for_notifications_invisible()

        with aqas.step("Занять полосу"):
            if is_located(lanes_control_page.elements.LANE1_IS_FREE_LBL):
                lanes_control_page.elements.BUSY_LANE1_ADMIN_BTN.click()

        with aqas.step("Подождать, пока не исчезнут Уведомления"):
            lanes_control_page.wait_for_notifications_invisible()

        with aqas.step("Открыть боковое меню"):
            lanes_control_page.elements.MENU_BTN.click()
            sidebar_page = SideBarForm()
            assert sidebar_page.is_wait_for_form_load(), "Страница не загрузилась"

        with aqas.step("Открыть окно установки режима работы тира"):
            sidebar_page.elements.SETTINGS_BTN.click()
            sidebar_page.elements.SHOOTING_MODE_BTN.click()
            shooting_settings_page = ShootingSettingsForm()
            assert shooting_settings_page.is_wait_for_form_load(), "Страница не загрузилась"

        with aqas.step("Сменить режим работы тира на узкий экран"):
            shooting_settings_page.elements.TIDE_BTN.click()
            shooting_settings_page.elements.APPLY_BTN.click()
            shooting_settings_page.elements.CONFIRM_BTN.reset()
            shooting_settings_page.elements.CONFIRM_BTN.click()

        with aqas.step("Сменить режим работы тира на полный экран"):
            shooting_settings_page.elements.FULL_BTN.click()
            shooting_settings_page.elements.APPLY_BTN.click()
            shooting_settings_page.elements.CONFIRM_BTN.reset()
            shooting_settings_page.elements.CONFIRM_BTN.click()

        with aqas.step("Подождать, пока не исчезнут Уведомления"):
            shooting_settings_page.wait_for_notifications_invisible()

        with aqas.step("Сменить режим работы тира на широкий экран"):
            shooting_settings_page.elements.WIDE_BTN.click()
            shooting_settings_page.elements.AMOUNT_LANE_BTN.click()
            shooting_settings_page.elements.TWO_LANES_LBL.click()
            shooting_settings_page.elements.APPLY_BTN.wait_and_click()
            shooting_settings_page.elements.CONFIRM_BTN.reset()
            shooting_settings_page.elements.CONFIRM_BTN.click()

        with aqas.step("Подождать, пока не исчезнут Уведомления"):
            shooting_settings_page.wait_for_notifications_invisible()

        with aqas.step("Открыть боковое меню"):
            shooting_settings_page.elements.MENU_BTN.click()
            assert sidebar_page.is_wait_for_form_load(), "Страница не загрузилась"

        with aqas.step("Открыть окно управлени полосами"):
            sidebar_page.elements.LANES_CONTROLLING_BTN.click()
            assert lanes_control_page.is_wait_for_form_load(), "Страница не загрузилась"

    @allure.title("auth_admin_statistic")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-338")
    def test_auth_admin_statistic(self, get_auth_admin):
        lanes_control_page = get_auth_admin

        with aqas.step("Подождать, пока не исчезнут Уведомления"):
            lanes_control_page.wait_for_notifications_invisible()

        with aqas.step("Занять полосу"):
            if is_located(lanes_control_page.elements.LANE1_IS_FREE_LBL):
                lanes_control_page.elements.BUSY_LANE1_ADMIN_BTN.click()

        with aqas.step("Подождать, пока не исчезнут Уведомления"):
            lanes_control_page.wait_for_notifications_invisible()

        with aqas.step("Открыть боковое меню"):
            lanes_control_page.elements.MENU_BTN.click()
            sidebar_page = SideBarForm()
            assert sidebar_page.is_wait_for_form_load(), "Страница не загрузилась"

        with aqas.step("Открыть окно со статистикой"):
            sidebar_page.elements.STATISTIC_BTN.click()
            statistic_page = StatisticForm()
            assert statistic_page.is_wait_for_form_load(), "Страница не загрузилась"

        with aqas.step("Найти кнопку сформировать отчет"):
            statistic_page.elements.USER_1_IN_LIST_BTN.click()
            assert is_located(statistic_page.elements.MAKE_REPORT_BTN), "Администратору не доступно создание отчета"

        with aqas.step("Открыть боковое меню"):
            statistic_page.elements.MENU_BTN.click()
            assert sidebar_page.is_wait_for_form_load(), "Страница не загрузилась"

        with aqas.step("Открыть окно управлени полосами"):
            sidebar_page.elements.LANES_CONTROLLING_BTN.click()
            assert lanes_control_page.is_wait_for_form_load(), "Страница не загрузилась"

    @allure.title("auth_admin_organisations")
    @pytest.mark.test_case("https://jira.steor.tech/browse/VEGA2-387")
    def test_auth_admin_func_organisations(self, get_auth_admin):
        lanes_control_page = get_auth_admin

        with aqas.step("Подождать, пока не исчезнут Уведомления"):
            lanes_control_page.wait_for_notifications_invisible()

        with aqas.step("Занять полосу"):
            if is_located(lanes_control_page.elements.LANE1_IS_FREE_LBL):
                lanes_control_page.elements.BUSY_LANE1_ADMIN_BTN.click()

        with aqas.step("Подождать, пока не исчезнут Уведомления"):
            lanes_control_page.wait_for_notifications_invisible()

        with aqas.step("Открыть боковое меню"):
            lanes_control_page.elements.MENU_BTN.click()
            sidebar_page = SideBarForm()
            assert sidebar_page.is_wait_for_form_load(), "Страница не загрузилась"

        with aqas.step("Открыть окно с Организациями"):
            sidebar_page.elements.ORGANISATIONS_BTN.click()
            organisations_page = OrganisationsForm()
            assert organisations_page.is_wait_for_form_load(), "Страница не загрузилась"

        with aqas.step("Создать организацию"):
            organisations_page.elements.ADD_BTN.click()
            organisations_page.elements.INPUT_NAME_TBX.send_keys("Организация_тест")
            organisations_page.elements.SAVE_BTN.click()

        with aqas.step("Удалить организацию"):
            organisations_page.elements.NEW_ORG_LBL.click()
            organisations_page.elements.DELETE_BTN.click()
            organisations_page.elements.CONFIRM_DELETE_BTN.click()

        with aqas.step("Подождать, пока не исчезнут Уведомления"):
            organisations_page.wait_for_notifications_invisible()

        with aqas.step("Открыть боковое меню"):
            organisations_page.elements.MENU_BTN.click()
            assert sidebar_page.is_wait_for_form_load(), "Страница не загрузилась"

        with aqas.step("Открыть окно управлени полосами"):
            sidebar_page.elements.LANES_CONTROLLING_BTN.click()
            assert lanes_control_page.is_wait_for_form_load(), "Страница не загрузилась"
