from aqas.element_factory import ElementFactory
from aqas.forms.base_form import BaseForm, BaseFormElements  # подгрузка из базового класса элементов
from selenium.webdriver.common.by import By


class AuthenticationFormElements(BaseFormElements):
    """
    Класс, который содержит элементы, используемые на странице аутентификации
    """

    LOGIN_INPUT = ElementFactory.text_box(
        By.XPATH, "//*[@id='login']",
        "Поле ввода логина")

    LOGIN_NAME_ADMIN = 'admin'
    PASSWORD_TAB_ADMIN = ElementFactory.button(
        locator_type=By.XPATH, locator_value="//div[contains(text(),'5')]",
        element_name="Кнопка пароля администратора")

    LOGIN_NAME_INSTRUCTOR = 'instuctor'
    PASSWORD_TAB_INSTRUCTOR = ElementFactory.button(
        locator_type=By.XPATH, locator_value="//div[contains(text(),'2')]",
        element_name="Кнопка пароля инструктора")

    LOGIN_NAME_SHOOTER = 'shooter'
    PASSWORD_TAB_SHOOTER = ElementFactory.button(
        locator_type=By.XPATH, locator_value="//div[contains(text(),'1')]",
        element_name="Кнопка пароля стрелка")


class AuthenticationForm(BaseForm):
    """
    Класс, который содержит методы, используемые на странице аутентификации
    """
    elements = AuthenticationFormElements()  # подгрузка в аргумент из данного  класса

    def __init__(self):
        super().__init__(By.CLASS_NAME, "login-page", "Страница аутентификации")
        # элемент проверки,что мы в этой форме

    def enter_login_admin(self):
        self.elements.LOGIN_INPUT.send_keys(self.elements.LOGIN_NAME_ADMIN)

    def enter_password_admin(self):
        for _ in range(4):
            self.elements.PASSWORD_TAB_ADMIN.click()

    def enter_login_instuctor(self):
        self.elements.LOGIN_INPUT.send_keys(self.elements.LOGIN_NAME_INSTRUCTOR)

    def enter_password_instuctor(self):
        for _ in range(4):
            self.elements.PASSWORD_TAB_INSTRUCTOR.click()

    def enter_login_shooter(self):
        self.elements.LOGIN_INPUT.send_keys(self.elements.LOGIN_NAME_SHOOTER)

    def enter_password_shooter(self):
        for _ in range(4):
            self.elements.PASSWORD_TAB_SHOOTER.click()
