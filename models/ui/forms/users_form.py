import aqas
from selenium.webdriver.common.by import By

from models.ui.common_elements import CommonElements


class UsersFormElements(CommonElements):
    """Класс, который содержит элементы, используемые при проверке бокового меню."""

    MENU_USERS_BTN = aqas.element_factory.button(
        By.XPATH, "//div[contains(@class, 'p-toolbar-group-left')]//button",
        "Меню")

    ADD_BTN = aqas.element_factory.button(
        By.XPATH, "//div[contains(@class, 'p-grid p-mt-4')]//button",
        "Добавить")

    DELETE_BTN = aqas.element_factory.button(
        By.XPATH, "//button[contains(text(),'удалить')]",
        "Удалить выбранного пользователя")

    DELETE_DISABLED_LBL = aqas.element_factory.label(
        By.XPATH, "//button[contains(@class, 'p-disabled')]/span[contains(text(),'удалить')]",
        "Кнопка удаления в НЕКЛИКАБЕЛЬНОМ СОСТОЯНИИ")

    SAVE_BTN = aqas.element_factory.button(
        By.XPATH, "//button[contains(@class,'p-mr-4')][1]",
        "Кнопка сохранить")

    CHECKBOX_1_BTN = aqas.element_factory.button(
        By.XPATH, "//div[@role='checkbox'][2]",
        "Чекбокс 1-го пользователя")

    GROWTH_TBX = aqas.element_factory.button(
        By.XPATH, ".//input[@id='height']",
        "Поле ввода роста стрелка")

    PASSWORD_TBX = aqas.element_factory.text_box(
        By.XPATH, ".//input[@id='user-password']",
        "Поле ввода пароля")

    CHECKBOX_2_BTN = aqas.element_factory.button(
        By.XPATH, "// div[ @ role = 'checkbox'][3]",
        "Чекбокс 2-го пользователя")

    CHECKBOX_3_BTN = aqas.element_factory.button(
        By.XPATH, "// div[ @ role = 'checkbox'][4]",
        "Чекбокс 3-го пользователя")

    CHECKBOX_ALL_BTN = aqas.element_factory.button(
        By.XPATH, "// div[ @ role = 'checkbox'][1]",
        "Чекбокс всех  пользователей")

    CONFIRM_DELETE_USER_BTN = aqas.element_factory.button(
        By.XPATH, "//button[contains(text(),'УДАЛИТЬ')]",
        "Подтвердить удаление пользователя")

    CANCEL_DELETE_USER_BTN = aqas.element_factory.button(
        By.XPATH, "//button[contains(text(),'ОТМЕНИТЬ')] ",
        "Отменить удаление пользователя")

    NEW_USER_LBL = aqas.element_factory.button(
        By.XPATH, "//span[contains(text(),'Фамилия_тест')]",
        "Поле только что созданного пользователя")


class UsersForm(aqas.BaseForm):
    """Класс, который содержит методы, используемые при проверке бокового меню."""
    elements = UsersFormElements()

    def __init__(self):
        super().__init__(By.XPATH, ".//div[@class='title'][contains(text(),' Пользователи')]")

    def wait_for_notification_invisible(self):
        self.elements.NOTIFICATION_LBL.state.wait_for_invisible()

    def wait_for_notifications_invisible(self):
        self.elements.NOTIFICATIONS_LBL.state.wait_for_invisible()
