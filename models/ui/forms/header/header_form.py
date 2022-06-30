import aqas
from selenium.webdriver.common.by import By

from models.ui.forms.common_elements import CommonFormElements


class HeaderFormElements(CommonFormElements):
    """Класс, который содержит элементы, используемые при проверке кнопок шапки страницы."""


class HeaderForm(aqas.BaseForm):
    """Класс, который содержит методы, используемые при проверке кнопок шапки страницы."""

    elements = HeaderFormElements()

    def __init__(self):
        super().__init__(By.XPATH, "//div[contains(@role,'toolbar')]", "Шапка страницы")
