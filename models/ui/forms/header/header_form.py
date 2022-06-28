import aqas
from selenium.webdriver.common.by import By


class HeaderFormElements(aqas.BaseFormElements):
    """Класс, который содержит элементы, используемые при проверке кнопок шапки страницы."""

    MENU = aqas.element_factory.button(
        By.XPATH, "//div[contains(@class, 'p-toolbar-group-left')]//span",
        "Меню")


class HeaderForm(aqas.BaseForm):
    """Класс, который содержит методы, используемые при проверке кнопок шапки страницы."""

    elements = HeaderFormElements()

    def __init__(self):
        super().__init__(By.XPATH, "//div[contains(@role,'toolbar')]", "Шапка страницы")

    def go_to_menu(self):
        self.elements.MENU.click()
