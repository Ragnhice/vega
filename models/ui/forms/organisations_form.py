import aqas
from models.ui.forms.common_elements import CommonFormElements, CommonForm
from selenium.webdriver.common.by import By


class OrganisationsFormElements(aqas.BaseFormElements,CommonFormElements):
    """Класс, который содержит элементы, используемые при проверке работы с организциями."""

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


class UsersForm(aqas.BaseForm, CommonForm):
    """Класс, который содержит методы, используемые при проверке бокового меню."""
    elements = UsersFormElements()

    def __init__(self):
        super().__init__(By.XPATH, ".//div[@class='title'][contains(text(),' Пользователи')]")