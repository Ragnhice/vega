import aqas
from selenium.webdriver.common.by import By


class StatisticFormElements(aqas.BaseFormElements):
    """Класс, который содержит элементы, используемые при проверке страницы Статистика."""

    MENU = aqas.element_factory.button(
        By.XPATH, "//div[contains(@class, 'p-toolbar-group-left')]//span",
        "Меню")

    USER_1_IN_LIST = aqas.element_factory.button(
        By.XPATH, " ",
        " ")

    EX1_IN_LIST = aqas.element_factory.button(
        By.XPATH, " ",
        " ")

    SHOTS = aqas.element_factory.button(
        By.XPATH, " ",
        " ")

    OPEN_ROLES_LIST = aqas.element_factory.button(
        By.XPATH, " ",
        " ")

    MAKE_REPORT = aqas.element_factory.button(
        By.XPATH, " ",
        " ")


class UsersForm(aqas.BaseForm):
    """Класс, который содержит методы, используемые при проверке бокового меню."""
    elements = UsersFormElements()

    def __init__(self):
        super().__init__(By.XPATH, ".//div[@class='title'][contains(text(),' Пользователи')]")

    def save(self):
        self.elements.SAVE.click()
