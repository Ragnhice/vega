import aqas
from selenium.webdriver.common.by import By

from models.ui.common_elements import CommonElements


class ShootingSettingsFormElements(CommonElements):
    """
    Класс, который содержит элементы, используемые при проверке страницы настроек тира
    """

    TIDE_BTN = aqas.element_factory.button(
        By.XPATH, ".//label[contains(text(),'Узкий')]",
        "Узкий размер экрана")

    FULL_BTN = aqas.element_factory.button(
        By.XPATH, ".//label[contains(text(),'Полный')]",
        "Полный размер экрана")

    WIDE_BTN = aqas.element_factory.button(
        By.XPATH, ".//label[contains(text(),'Широкий')]",
        "Широкий размер экрана")

    DUEL_BTN = aqas.element_factory.button(
        By.XPATH, ".//label[contains(text(),'Дуэль')]",
        "Режим Дуэль")

    LANE_COUNTS_BTN = aqas.element_factory.button(
        By.XPATH, "//*[@id='linesCount']/span]",
        "Поле выбора количества полос")

    APPLY_BTN = aqas.element_factory.button(
        By.XPATH, "//div[contains(@class, 'p-text-right')]//button",
        "Применить")

    CONFIRM_BTN = aqas.element_factory.button(
        By.XPATH, "//div[contains(@class, 'p-dialog-footer')]//button[2]",
        "Подтвердить")

    CONFIRM_BTN_2 = aqas.element_factory.button(
        By.XPATH, "//div[contains(@class, 'p-dialog-footer')]//button[2]",
        "Подтвердить")

    CONFIRM_BTN_3 = aqas.element_factory.button(
        By.XPATH, "//div[contains(@class, 'p-dialog-footer')]//button[2]",
        "Подтвердить")

    AMOUNT_LANE_BTN = aqas.element_factory.button(
        By.XPATH, "//span[contains(@class, 'p-dropdown-trigger-icon')]",
        "Открыть выбор количества полос")

    TWO_LANES_LBL = aqas.element_factory.button(
        By.XPATH, "//div[contains(@class, 'p-dropdown-items-wrapper')]//li[2]",
        "Выбрать 2 полосы")


class ShootingSettingsForm(aqas.BaseForm):
    """Класс, который содержит методы, используемые при проверке страницы настроек тира."""

    elements = ShootingSettingsFormElements()

    def __init__(self):
        super().__init__(By.XPATH, "//div[ contains(text(),'Настройки тира')]",
                         "Главная страница настроек тира")

    def wait_for_notification_invisible(self):
        self.elements.NOTIFICATION_LBL.state.wait_for_invisible()

    def wait_for_notifications_invisible(self):
        self.elements.NOTIFICATIONS_LBL.state.wait_for_invisible()
