import aqas
from models.ui.forms.common_elements import CommonFormElements, CommonForm
from selenium.webdriver.common.by import By


class UsersFormElements(aqas.BaseFormElements,CommonFormElements):
    """Класс, который содержит элементы, используемые при проверке бокового меню."""

    MENU_BTN = aqas.element_factory.button(
        By.XPATH, "//div[contains(@class, 'p-toolbar-group-left')]//span",
        "Меню")

    ADD_BTN = aqas.element_factory.button(
        By.XPATH, " ",
        " ")

    DELETE_BTN = aqas.element_factory.button(
        By.XPATH, " ",
        " ")

    DELETE_DISABLED_LBL = aqas.element_factory.label(
        By.XPATH, " ",
        " ")

    SAVE_BTN = aqas.element_factory.button(
        By.XPATH, " ",
        " ")

    CHECKBOX_1_BTN = aqas.element_factory.button(
        By.XPATH, " ",
        " ")

    role = checkbox

    GROWTH_UP_BTN = aqas.element_factory.button(
        By.XPATH, " ",
        " ")

    PASSWORD_TBX = aqas.element_factory.text_box(
        By.XPATH, " ",
        " ")

    CHECKBOX_2_BTN = aqas.element_factory.button(
        By.XPATH, " ",
        " ")

    CHECKBOX_3_BTN = aqas.element_factory.button(
        By.XPATH, " ",
        " ")

    CHECKBOX_ALL_BTN = aqas.element_factory.button(
        By.XPATH, " ",
        " ")


class UsersForm(aqas.BaseForm, CommonForm):
    """Класс, который содержит методы, используемые при проверке бокового меню."""
    elements = UsersFormElements()

    def __init__(self):
        super().__init__(By.XPATH, ".//div[@class='title'][contains(text(),' Пользователи')]")

    def save(self):
        self.elements.SAVE_BTN.click()

    def delete(self):
        self.elements.DELETE_BTN.click()

    def add(self):
        self.elements.ADD_BTN.click()

    def choose_checkbox_1(self):
        self.elements.CLOSE_BTN.click()

    def choose_checkbox_2(self):
        self.elements.CLOSE.click()

    def choose_checkbox_3(self):
        self.elements.CLOSE.click()

    def save(self):
        self.elements.SAVE_BTN.click()

    def enter_password(self):
        self.elements.PA.click()

