import aqas
from selenium.webdriver.common.by import By
from models.ui.forms.common_elements import CommonFormElements, CommonForm


class NewUserFormElements(aqas.BaseFormElements,CommonFormElements):
    """Класс, который содержит элементы, используемые при проверке бокового меню."""

    MENU = aqas.element_factory.button(
        By.XPATH, "//div[contains(@class, 'p-toolbar-group-left')]//span",
        "Меню")

    LOGIN = aqas.element_factory.button(
        By.XPATH, " ",
        " ")

    PASSWORD = aqas.element_factory.button(
        By.XPATH, " ",
        " ")

    NAME = aqas.element_factory.button(
        By.XPATH, " ",
        " ")

    SURNAME = aqas.element_factory.button(
        By.XPATH, " ",
        " ")

    PATRONYMIC = aqas.element_factory.button(
        By.XPATH, " ",
        " ")

    GROWTH = aqas.element_factory.button(
        By.XPATH, " ",
        " ")

    ROLE_OPEN_LIST = aqas.element_factory.button(
        By.XPATH, " ",
        " ")

    ROLE_TO_CHOSE = aqas.element_factory.button(
        By.XPATH, " ",
        " ")

    SAVE = aqas.element_factory.button(
        By.XPATH, " ",
        " ")

    EXIT_WITHOUT_SAVING = aqas.element_factory.button(
        By.XPATH, " ",
        " ")

    BACK = aqas.element_factory.button(
        By.XPATH, " ",
        " ")


class NewUserFormElements(aqas.BaseForm, CommonForm):
    """Класс, который содержит методы, используемые при проверке бокового меню."""
    elements = UsersFormElements()

    def __init__(self):
        super().__init__(By.XPATH, ".//div[@class='title'][contains(text(),' Пользователи')]")

    def save(self):
        self.elements.SAVE.click()
