import aqas
from selenium.webdriver.common.by import By
from models.ui.forms.common_elements import CommonFormElements, CommonForm


class StatisticFormElements(aqas.BaseFormElements,CommonFormElements):
    """Класс, который содержит элементы, используемые при проверке страницы Статистика."""

    MENU_BTN = aqas.element_factory.button(
        By.XPATH, "//div[contains(@class, 'p-toolbar-group-left')]//span",
        "Меню")

    USER_1_IN_LIST_BTN = aqas.element_factory.button(
        By.XPATH, " ",
        " ")

    EX1_IN_LIST_BTN = aqas.element_factory.button(
        By.XPATH, " ",
        " ")

    SHOTS_BTN = aqas.element_factory.button(
        By.XPATH, " ",
        " ")

    OPEN_ROLES_LIST_BTN = aqas.element_factory.button(
        By.XPATH, " ",
        " ")

    MAKE_REPORT_BTN = aqas.element_factory.button(
        By.XPATH, " ",
        " ")


class UsersForm(aqas.BaseForm, CommonForm):
    """Класс, который содержит методы, используемые при проверке бокового меню."""
    elements = UsersFormElements()

    def __init__(self):
        super().__init__(By.XPATH, ".//div[@class='title'][contains(text(),' Пользователи')]")

    def save(self):
        self.elements.SAVE_BTN.click()
