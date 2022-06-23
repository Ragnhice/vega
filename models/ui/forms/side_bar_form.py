from aqas.element_factory import ElementFactory
from aqas.forms.base_form import BaseForm, BaseFormElements
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By


class SideBarFormElements(BaseFormElements):
    """
    Класс, который содержит элементы, используемые при проверке бокового меню
    """

    MENU = ElementFactory.button(
        By.CLASS_NAME, ". // span[contains(text(), 'menu']",
        "Меню")

    SETTINGS = ElementFactory.button(
        By.XPATH, ".//span[contains(@class,'p-panelmenu-icon')]",
        "Настройки")

    LINES_CONTROLLING = ElementFactory.button(
        By.XPATH, ".//span[contains(text(),'Управление полосами')]",
        "Управление полосами")

    EX_EDITOR = ElementFactory.button(
        By.XPATH, ".//span[contains(text(),'Редактор упражнений')]",
        "Редактор упражнения")

    STAFF = ElementFactory.button(
        By.XPATH, ".//span[contains(text(),'Пользователи')]",
        "Пользователи")

    STATISTIC = ElementFactory.button(
        By.XPATH, ".//span[contains(text(),'Статистика')]",
        "Статистика")

    SHOOTING_MODE = ElementFactory.button(
        By.XPATH, ".//span[contains(text(),'Настройки')]",
        "")

    CAMERA_SETTINGS = ElementFactory.button(
        By.XPATH, ".//span[contains(text(),'Настройка камеры визуализатора')]",
        "Настройка камеры визуализатора")

    SERVICE_FUNCTION = ElementFactory.button(
        By.XPATH, ".//span[contains(text(),'Сервисные функции')]",
        "Сервисные функции")

    ORGANISATONS = ElementFactory.button(
        By.XPATH, ".//span[contains(text(),'Организации')]",
        "Организации")

    CLOSE = ElementFactory.button(
        By.XPATH, ".//span[contains(@class,'p-sidebar-close-icon')]",
        "Настройки")


class SideBarForm(BaseForm):
    """
            Класс, который содержит методы, используемые при проверке бокового меню
    """
    elements = SideBarFormElements()

    def __init__(self):
        super().__init__(By.CLASS_NAME, "p-sidebar-header", "Страница бокового меню")

    def open_settings(self):
        self.elements.SETTINGS.click()

    def close_settings(self):
        self.elements.CLOSE.click()

    def find_ex_editor(self):
        try:
            return self.elements.EX_EDITOR.state.wait_for_located(timeout=3)
        except TimeoutException:
            return False

    def find_shooting_mode(self):
        try:
            return self.elements.SHOOTING_MODE.state.wait_for_located(timeout=3)
        except TimeoutException:
            return False

    def find_camera_settings(self):
        try:
            return self.elements.CAMERA_SETTINGS.state.wait_for_located(timeout=3)
        except TimeoutException:
            return False

    def find_staff(self):
        try:
            return self.elements.STAFF.state.wait_for_located(timeout=3)
        except TimeoutException:
            return False

    def find_service(self):
        try:
            return self.elements.SERVICE_FUNCTION.state.wait_for_located(timeout=3)
        except TimeoutException:
            return False
