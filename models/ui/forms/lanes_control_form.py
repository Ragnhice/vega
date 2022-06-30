import aqas
from selenium.webdriver.common.by import By

from models.ui.forms.common_elements import CommonFormElements


class LanesControlFormElements(CommonFormElements):
    """Класс, который содержит элементы, используемые при проверке страницы управления полосами."""

    LANE1_LBL = aqas.element_factory.label(
        By.XPATH, "//tbody/tr[1]/td[1]",
        "Переход к полосе №1")

    PAUSE_LANE1_BTN = aqas.element_factory.button(
        By.XPATH, ".//span[@class='p-ml-2'][normalize-space()='1']/span[contains('pause')] ",
        "Приостановить упражнение на полосе №1")

    EDIT_LANE1_BTN = aqas.element_factory.button(
        By.XPATH, "//span[@class='p-ml-2'][normalize-space()='1']",
        "Редактировать 1 полосу")

    EDIT_LANE2_BTN = aqas.element_factory.button(
        By.XPATH, "//span[@class='p-ml-2'][normalize-space()='2']",
        "Редактировать 2 полосу")

    BUSY_LANE1_ADMIN_BTN = aqas.element_factory.button(
        By.XPATH, "//tbody/tr[1]//span[contains(text(),'vpn_key_off')]",
        "Сменить статус занятость полосы в роли администратора")

    BUSY_LANE1_INSTRUCTOR_BTN = aqas.element_factory.button(
        By.XPATH, "//tbody/tr[1]//span[contains(text(),'vpn_key')]",
        "Сменить статус занятость полосы в роли инструктора")

    LANE1_IS_FREE_LBL = aqas.element_factory.label(
        By.XPATH, "//tbody/tr[1]//div[contains(text(),'не назначен')]",
        "Флаг свободной полосы")

    LANE1_IS_BUSY_LBL = aqas.element_factory.label(
        By.XPATH, "//tbody/tr[1]//span[contains(text(),'check_circle')]",
        "Флаг занятой полосы")

    STOP_LANE1_DISABLED_LBL = aqas.element_factory.label(
        By.XPATH, "//tbody/tr[1]//button[contains(@class, 'p-disabled')]/span[contains(text(),'stop')]",
        "Кнопка остановки упражнения в НЕКЛИКАБЕЛЬНОМ СОСТОЯНИИ")

    PLAY_LANE1_DISABLED_LBL = aqas.element_factory.label(
        By.XPATH, "//tbody/tr[1]//button[contains(@class, 'p-disabled')]/span[contains(text(),'play_arrow')]",
        "Кнопка запуска упражнения в НЕКЛИКАБЕЛЬНОМ СОСТОЯНИИ")

    PLAY_LANE1_BTN = aqas.element_factory.button(
        By.XPATH, "//tbody/tr[1]//span[contains(text(),'play_arrow')]",
        "Старт упражнения")

    STOP_LANE1_BTN = aqas.element_factory.button(
        By.XPATH, "//tbody/tr[1]//span[contains(text(),'stop')]",
        "Стоп упражнения")

    CHOSEN_WEAPON_DRDN = aqas.element_factory.dropdown(
        By.XPATH, "//div[@id='weaponId']//span",
        "Поле выбранного оружия")

    CHOSEN_AMMO_DRDN = aqas.element_factory.dropdown(
        By.XPATH, "//div[@id='ammoId']//span",
        "Поле выбранного боеприпаса")

    CLOSE_CHOSE_WEAPON_BTN = aqas.element_factory.button(
        By.XPATH, "//span[contains(text(),'Закрыть')]",
        "Закрыть выбор оружия")

    CONFIRM_CHOSEN_WEAPON_BTN = aqas.element_factory.button(
        By.XPATH, "//span[contains(text(),'Подтвердить')]",
        "Подтвердить выбор оружия")

    PAUSE_LANE1_DISABLED_LBL = aqas.element_factory.label(
        By.XPATH, "//tbody/tr[1]//button[contains(@class, 'p-disabled')]/span[contains(text(),'pause')]",
        "Кнопка паузы в НЕКЛИКАБЕЛЬНОМ СОСТОЯНИИ, упр. либо приостановлено либо остановлено")

    BUSY_LANE1_RADIO_DISABLED_LBL = aqas.element_factory.label(
        By.XPATH, "//tbody/tr[1]//button[contains(@class, 'p-disabled')]/span[contains(text(),'vpn_key')]",
        "Кнопка занятия полосы в НЕКЛИКАБЕЛЬНОМ СОСТОЯНИИ, упр. либо приостановлено либо остановлено")


class LanesControlForm(aqas.BaseForm):
    """Класс, который содержит методы, используемые при проверке страницы управления полосами."""

    elements = LanesControlFormElements()

    def __init__(self):
        super().__init__(By.XPATH, "//div[contains(text(),'Управление полосами')]",
                         "Страница управления полосами")

    def is_notification_invisible(self):
        return self.elements.NOTIFICATION_LBL.state.wait_for_invisible()

    def is_notifications_invisible(self):
        return self.elements.NOTIFICATIONS_LBL.state.wait_for_invisible()
