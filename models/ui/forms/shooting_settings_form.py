import aqas
from selenium.webdriver.common.by import By

from models.ui.forms.common_elements import CommonFormElements


class ShootingSettingsFormElements(CommonFormElements):
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


class ShootingSettingsForm(aqas.BaseForm):
    """Класс, который содержит методы, используемые при проверке страницы настроек тира."""

    elements = ShootingSettingsFormElements()

    def __init__(self):
        super().__init__(By.XPATH, "//div[ contains(text(),'Управление полосами')]",
                         "Главная страница настроек тира")

    def is_notification_invisible(self):
        return self.elements.NOTIFICATION_LBL.state.wait_for_invisible()

    def is_notifications_invisible(self):
        return self.elements.NOTIFICATIONS_LBL.state.wait_for_invisible()
