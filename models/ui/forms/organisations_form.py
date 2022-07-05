import aqas
from selenium.webdriver.common.by import By

from models.ui.common_elements import CommonElements


class OrganisationsFormElements(CommonElements):
    """Класс, который содержит элементы, используемые при проверке работы с организциями."""

    ADD_BTN = aqas.element_factory.button(
        By.XPATH, "div[contains(@class,'section - block__content')]//button",
        "Добавить")
   # section - block__content

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
        By.XPATH, "div[contains(@class,'p-dialog-footer')]//button[2]",
        "Отменить")

    CONFIRM_DELETE_BTN = aqas.element_factory.button(
        By.XPATH, "div[contains(@class,'p-dialog-footer')]//button[1]",
        "Подтвердить удаление")

    NEW_ORG_LBL = aqas.element_factory.label(
        By.XPATH, "//p[contains(text(),'Организация_тест')]",
        "Поле с только что созданной организацией")


class OrganisationsForm(aqas.BaseForm):
    """Класс, который содержит методы, используемые при проверке бокового меню."""
    elements = OrganisationsFormElements()

    def __init__(self):
        super().__init__(By.XPATH, ".//div[@class='title'][contains(text(),'Организации')]")

    def wait_for_notification_invisible(self):
        self.elements.NOTIFICATION_LBL.state.wait_for_invisible()

    def wait_for_notifications_invisible(self):
        self.elements.NOTIFICATIONS_LBL.state.wait_for_invisible()
