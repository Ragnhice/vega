import aqas
from selenium.webdriver.common.by import By

from models.ui.common_elements import CommonElements


class StatisticFormElements(CommonElements):
    """Класс, который содержит элементы, используемые при проверке страницы Статистика."""

    MENU_BTN = aqas.element_factory.button(
        By.XPATH, "//div[contains(@class, 'p-toolbar-group-left')]//button",
        "Меню")

    USER_1_IN_LIST_BTN = aqas.element_factory.button(
        By.XPATH, ".//p[contains(text(),'МО РФ')]",
        "Выбрать первого пользователя в списке")

    EX_1_IN_LIST_BTN = aqas.element_factory.button(
        By.XPATH,
        "tbody[contains( @class = 'p-datatable-tbody')][2]//tr[contains( @class = 'p-selectable-row')][1]//td",
        "Выбрать первое упражнение в списке")

    MAKE_REPORT_BTN = aqas.element_factory.button(
        By.XPATH, "//div[contains(@class, 'p-col-6')][2]//button",
        "Сформировать отчет")


class StatisticForm(aqas.BaseForm):
    """Класс, который содержит методы, используемые при проверке бокового меню."""
    elements = StatisticFormElements()

    def __init__(self):
        super().__init__(By.XPATH, ".//div[@class='title'][contains(text(),' Статистика')]")

    def wait_for_notification_invisible(self):
        self.elements.NOTIFICATION_LBL.state.wait_for_invisible()

    def wait_for_notifications_invisible(self):
        self.elements.NOTIFICATIONS_LBL.state.wait_for_invisible()
