import aqas
from selenium.webdriver.common.by import By


class UsersFormElements(aqas.BaseFormElements):
    """Класс, который содержит элементы, используемые при проверке бокового меню."""

    MENU = aqas.element_factory.button(
        By.XPATH, "//div[contains(@class, 'p-toolbar-group-left')]//span",
        "Меню")

    ADD = aqas.element_factory.button(
        By.XPATH, " ",
        " ")

    DELETE = aqas.element_factory.button(
        By.XPATH, " ",
        " ")

    DELETE_DISABLED = aqas.element_factory.button(
        By.XPATH, " ",
        " ")

    SAVE = aqas.element_factory.button(
        By.XPATH, " ",
        " ")

    CHECKBOX_1 = aqas.element_factory.button(
        By.XPATH, " ",
        " ")


role = checkbox

GROWTH_UP = aqas.element_factory.button(
    By.XPATH, " ",
    " ")

PASSWORD = aqas.element_factory.button(
    By.XPATH, " ",
    " ")

CHECKBOX_2 = aqas.element_factory.button(
    By.XPATH, " ",
    " ")

CHECKBOX_3 = aqas.element_factory.button(
    By.XPATH, " ",
    " ")

CHECKBOX_ALL = aqas.element_factory.button(
    By.XPATH, " ",
    " ")


class UsersForm(aqas.BaseForm):
    """Класс, который содержит методы, используемые при проверке бокового меню."""
    elements = UsersFormElements()

    def __init__(self):
        super().__init__(By.XPATH, ".//div[@class='title'][contains(text(),' Пользователи')]")

    def save(self):
        self.elements.SAVE.click()

    def delete(self):
        self.elements.DELETE.click()

    def add(self):
        self.elements.ADD.click()

    def choose_checkbox_1(self):
        self.elements.CLOSE.click()

    def choose_checkbox_2(self):
        self.elements.CLOSE.click()

    def choose_checkbox_3(self):
        self.elements.CLOSE.click()

    def choose_checkbox_all(self):
        self.elements.CLOSE.click()

    enter_password
