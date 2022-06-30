import aqas
from selenium.webdriver.common.by import By

from models.ui.forms.common_elements import CommonFormElements


class OrganisationsFormElements(CommonFormElements):
    """Класс, который содержит элементы, используемые при проверке работы с организциями."""

    ADD_BTN = aqas.element_factory.button(
        By.XPATH, "//button[contains(text(),'ДОБАВИТЬ')]",
        "Добавить")

    EDIT_BTN = aqas.element_factory.button(
        By.XPATH, "//button[contains(text(),'РЕДАКТИРОВАТЬ')]",
        "Редактировать")

    DELETE_BTN = aqas.element_factory.button(
        By.XPATH, "//button[contains(text(),'УДАЛИТЬ')]",
        "Удалить")

    INPUT_NAME_TBX = aqas.element_factory.text_box(
        By.XPATH, "//input[contains(@class, 'p-inputtext')]",
        "Поле ввода названия новой организации")

    SAVE_BTN = aqas.element_factory.button(
        By.XPATH, "//button[contains(text(),'СОХРАНИТЬ')]",
        "Кнопка сохранить")

    CANCEL_BTN = aqas.element_factory.button(
        By.XPATH, "//button[contains(text(),'ОТМЕНИТЬ')] ",
        "Отменить создание организации")


class OrganisationsForm(aqas.BaseForm):
    """Класс, который содержит методы, используемые при проверке бокового меню."""
    elements = OrganisationsFormElements()

    def __init__(self):
        super().__init__(By.XPATH, ".//div[@class='title'][contains(text(),'Организации')]")

    def is_notification_invisible(self):
        return self.elements.NOTIFICATION_LBL.state.wait_for_invisible()

    def is_notifications_invisible(self):
        return self.elements.NOTIFICATIONS_LBL.state.wait_for_invisible()
