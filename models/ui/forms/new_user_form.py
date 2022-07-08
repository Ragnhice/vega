import aqas
from selenium.webdriver.common.by import By

from models.ui.common_elements import CommonElements


class NewUserFormElements(CommonElements):
    """Класс, который содержит элементы, используемые при проверке бокового меню."""

    MENU_BTN = aqas.element_factory.button(
        By.XPATH, "//div[contains(@class, 'p-toolbar-group-left')]//span",
        "Меню")

    LASTNAME_TBX = aqas.element_factory.text_box(
        By.XPATH, " .//input[@id='lastName']",
        "Фамилия")

    LOGIN_TBX = aqas.element_factory.button(
        By.XPATH, " .//input[@id='login']",
        "Логин")

    PASSWORD_TBX = aqas.element_factory.text_box(
        By.XPATH, ".//input[@id='password']",
        "Пароль")

    FIRSTNAME_TBX = aqas.element_factory.text_box(
        By.XPATH, ".//input[@id='firstName']",
        "Имя")

    MIDDLENAME_TBX = aqas.element_factory.text_box(
        By.XPATH, ".//input[@id='middleName']",
        "Отчество")

    GROWTH_TBX = aqas.element_factory.text_box(
        By.XPATH, ".//input[@id='height']",
        "Рост")

    ROLE_OPEN_LIST_BTN = aqas.element_factory.button(
        By.XPATH, "//span[contains(class(), 'p-dropdown-trigger-icon')]",
        "Открыть список ролей для выбора")

    ROLE_IN_LIST_BTN = aqas.element_factory.button(
        By.XPATH, ".//li[@aria-label='Администратор']",
        "Выбрать роль в списке")

    SAVE_BTN = aqas.element_factory.button(
        By.XPATH, "//div[contains(@class, 'p-text-right')]//button[1]",
        "Кнопка сохранить")

    EXIT_WITHOUT_SAVING_BTN = aqas.element_factory.button(
        By.XPATH, "//div[contains(@class, 'p-text-right')]//button[2]",
        "Выйти без сохранения")


class NewUserForm(aqas.BaseForm):
    """Класс, который содержит методы, используемые при проверке бокового меню."""
    elements = NewUserFormElements()

    def __init__(self):
        super().__init__(By.XPATH, ".//div[@class='title'][contains(text(),'Новый пользователь')]")

    def wait_for_notification_invisible(self):
        self.elements.NOTIFICATION_LBL.state.wait_for_invisible()

    def wait_for_notifications_invisible(self):
        self.elements.NOTIFICATIONS_LBL.state.wait_for_invisible()
