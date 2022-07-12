import aqas
from selenium.webdriver.common.by import By

from models.ui.common_elements import CommonElements


class ConfirmFormElements(CommonElements):
    """Класс, который содержит элементы, используемые в окне предупреждения действий."""

    CONFIRM_BTN = aqas.element_factory.button(
        By.XPATH, "//button[contains(@class,'p-confirm-dialog-accept')]",
        "Подтвердить")

    RETURN_BTN = aqas.element_factory.button(
        By.XPATH, "//button[contains(@class,'p-confirm-dialog-reject')]",
        "Вернуться")

    CLOSE_BTN = aqas.element_factory.button(
        By.XPATH, "//button[contains(@class,'p-dialog-header-close')]",
        "Закрыть")

    CONFIRM_DELETE_BTN = aqas.element_factory.button(
        By.XPATH, "//div[contains(@class,'p-dialog-footer')]//button[contains(@class,'custom_btn')]",
        "Подтвердить удаление")


class ConfirmForm(aqas.BaseForm):
    """Класс, который содержит методы, используемые в окне предупреждения действий."""

    elements = ConfirmFormElements()

    def __init__(self):
        super().__init__(By.XPATH, "//span[contains(@class,'p-dialog-title')]",
                         "Окно предупреждения действия")
