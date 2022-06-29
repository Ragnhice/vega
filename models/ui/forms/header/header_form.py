import aqas
from selenium.webdriver.common.by import By
from models.ui.forms.common_elements import CommonFormElements, CommonForm


class HeaderFormElements(aqas.BaseFormElements,CommonFormElements):
    """Класс, который содержит элементы, используемые при проверке кнопок шапки страницы."""


class HeaderForm(aqas.BaseForm, CommonForm):
    """Класс, который содержит методы, используемые при проверке кнопок шапки страницы."""

    elements = HeaderFormElements()

    def __init__(self):
        super().__init__(By.XPATH, "//div[contains(@role,'toolbar')]", "Шапка страницы")

    def go_to_menu(self):
        self.elements.MENU.click()
