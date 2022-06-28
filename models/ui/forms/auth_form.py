import aqas
from selenium.webdriver.common.by import By
from models.ui.forms import *
from utils.enums import UserTypeEnum


class AuthenticationFormElements(aqas.BaseFormElements):
    """Класс, который содержит элементы, используемые на странице аутентификации."""

    LOGIN_INPUT = aqas.element_factory.text_box(
        By.XPATH, "//*[@id='login']",
        "Поле ввода логина")


class AuthenticationForm(aqas.BaseForm):
    """Класс, который содержит методы, используемые на странице аутентификации."""
    elements = AuthenticationFormElements()

    def __init__(self):
        super().__init__(By.CLASS_NAME, "login-page", "Страница аутентификации")
        self.password_locator = "//div[contains(text(),'{number}')]"

    def login(self, user_type: UserTypeEnum):
        login, password = self.__get_credentials_for_login(user_type)
        self.enter_login(login)
        self.enter_password(password)

    def enter_login(self, login_: str):
        self.elements.LOGIN_INPUT.send_keys(login_)

    def enter_password(self, password_: str):
        for number in password_:
            aqas.element_factory.button(By.XPATH, self.password_locator.format(number=number), f"<{number}>").click()

    def __get_credentials_for_login(self, user_type: UserTypeEnum):
        if user_type == UserTypeEnum.ADMINISTRATOR:
            login = aqas.config.get_property("ui.credentials.administrator.login")
            password = aqas.config.get_property("ui.credentials.administrator.password")
        elif user_type == UserTypeEnum.INSTRUCTOR:
            login = aqas.config.get_property("ui.credentials.instructor.login")
            password = aqas.config.get_property("ui.credentials.instructor.password")
        elif user_type == UserTypeEnum.SHOOTER:
            login = aqas.config.get_property("ui.credentials.shooter.login")
            password = aqas.config.get_property("ui.credentials.shooter.password")
        else:
            raise NotImplementedError(f"Нет возможности залогиниться с данным типом пользователя: {user_type.value}")

        if not login or not password:
            raise NotImplementedError(f"Задайте логин/пароль для пользователя с типом {user_type.value}")

        return login, password
