import aqas
from selenium.webdriver.common.by import By

from models.ui.forms.common_elements import CommonFormElements


class StatisticFormElements(CommonFormElements):
    """Класс, который содержит элементы, используемые при проверке страницы Статистика."""

    MENU_BTN = aqas.element_factory.button(
        By.XPATH, "//div[contains(@class, 'p-toolbar-group-left')]//span",
        "Меню")

    USER_1_IN_LIST_BTN = aqas.element_factory.button(
        By.XPATH, "tbody[contains( @class = 'p-datatable-tbody')][1]//tr[contains( @class = 'p-selectable-row')][1]",
        "Выбрать первое пользователя в списке")

    EX_1_IN_LIST_BTN = aqas.element_factory.button(
        By.XPATH, "tbody[contains( @class = 'p-datatable-tbody')][2]//tr[contains( @class = 'p-selectable-row')][1]",
        "Выбрать первое упражнение в списке")

    MAKE_REPORT_BTN = aqas.element_factory.button(
        By.XPATH, ".//button[contains(text(),'Сформировать отчет')]",
        "Сформировать отчет")

class StatisticForm(aqas.BaseForm):
    """Класс, который содержит методы, используемые при проверке бокового меню."""
    elements = StatisticFormElements()

    def __init__(self):
        super().__init__(By.XPATH, ".//div[@class='title'][contains(text(),' Статистика')]")

    def is_notification_invisible(self):
        return self.elements.NOTIFICATION_LBL.state.wait_for_invisible()

    def is_notifications_invisible(self):
        return self.elements.NOTIFICATIONS_LBL.state.wait_for_invisible()
