from selenium.webdriver.common.by import By
from aqas.element_factory import ElementFactory
from aqas.forms.base_form import BaseForm, BaseFormElements


class HeaderFormElements(BaseFormElements):
    """
    Класс, который содержит элементы, используемые при проверке кнопок шапки страницы
    """
    MENU_BUTTON = ElementFactory.Button(
        By.CLASS_NAME, ". // span[contains(text(), 'menu']",
        "Меню")


class HeaderForm(BaseForm):
    """
    Класс, который содержит методы, используемые при проверке кнопок шапки страницы
    """
    elements = HeaderFormElements(BaseFormElements)

    def __init__(self):
        super().__init__(By.CLASS_NAME, "Header Form", "Шапка страницы")

    def go_to_menu(self):
        self.elements.MENU_BUTTON.click()
