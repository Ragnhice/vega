import aqas
from selenium.webdriver.common.by import By

from models.ui.common_elements import CommonElements, SettingsElements, StateLaneElements


class Lane1ControlFormElements(CommonElements, SettingsElements, StateLaneElements):
    """Класс, который содержит элементы, используемые при проверке управления первой полосой."""

    STOP_DISABLED_LBL = aqas.element_factory.label(
        By.XPATH, "//button[contains(@class,'p-disabled')]/span[contains(text(),'stop')]",
        "Кнопка остановки упражнения в НЕКЛИКАБЕЛЬНОМ СОСТОЯНИИ")

    PLAY_DISABLED_LBL = aqas.element_factory.label(
        By.XPATH, "//button[contains(@class,'p-disabled')]/span[contains(text(),'play_arrow')]",
        "Кнопка запуска упражнения в НЕКЛИКАБЕЛЬНОМ СОСТОЯНИИ")

    PAUSE_DISABLED_LBL = aqas.element_factory.label(
        By.XPATH, "//button[contains(@class,'p-disabled')]/span[contains(text(),'pause')]",
        "Кнопка паузы в НЕКЛИКАБЕЛЬНОМ СОСТОЯНИИ, упр. либо приостановлено либо остановлено")

    TIME_LBL = aqas.element_factory.label(
        By.XPATH, ".//div[contains(@class,'p-justify-between')]/div[5]/div[contains(@class,'value')]",
        "Значение времени от начала")

    CLOSE_CHOSE_WEAPON_BTN = aqas.element_factory.button(
        By.XPATH, "//span[contains(text(),'Закрыть')]",
        "Закрыть выбор оружия")

    CONFIRM_CHOSEN_WEAPON_BTN = aqas.element_factory.button(
        By.XPATH, "//span[contains(text(),'Подтвердить')]",
        "Подтвердить выбор оружия")

    PRINT_QUICK_BTN = aqas.element_factory.button(
        By.XPATH, "//a[@href='/lines/1/stats']",
        "Распечатать отчет")

    CHOSEN_WEAPON_DRDN = aqas.element_factory.dropdown(
        By.XPATH, "//div[@id='weaponId']//span",
        "Поле выбранного оружия")

    CHOSEN_AMMO_DRDN = aqas.element_factory.dropdown(
        By.XPATH, "//div[@id='ammoId']//span",
        "Поле выбранного боеприпаса")


class Lane1ControlForm(aqas.BaseForm):
    """Класс, который содержит методы, используемые при проверке страницы управления первой полосой."""

    elements = Lane1ControlFormElements()

    def __init__(self):
        super().__init__(By.XPATH, "//div[contains(text(),'Управление полосой')]",
                         "Страница управления первой полосой")

    def wait_for_notification_invisible(self):
        self.elements.NOTIFICATION_LBL.state.wait_for_invisible()

    def wait_for_notifications_invisible(self):
        self.elements.NOTIFICATIONS_LBL.state.wait_for_invisible()
