import aqas
from selenium.webdriver.common.by import By


class SideBarFormElements(aqas.BaseFormElements):
    """Класс, который содержит элементы, используемые при проверке бокового меню."""

    MENU = aqas.element_factory.button(
        By.XPATH, "//div[contains(@class, 'p-toolbar-group-left')]//span",
        "Меню")

    SETTINGS = aqas.element_factory.button(
        By.XPATH, ".//span[contains(@class,'p-panelmenu-icon')]",
        "Настройки")

    LINES_CONTROLLING = aqas.element_factory.button(
        By.XPATH, ".//span[contains(text(),'Управление полосами')]",
        "Управление полосами")

    EX_EDITOR = aqas.element_factory.button(
        By.XPATH, ".//span[contains(text(),'Редактор упражнений')]",
        "Редактор упражнения")

    STAFF = aqas.element_factory.button(
        By.XPATH, ".//span[contains(text(),'Пользователи')]",
        "Пользователи")

    STATISTIC = aqas.element_factory.button(
        By.XPATH, ".//span[contains(text(),'Статистика')]",
        "Статистика")

    SHOOTING_MODE = aqas.element_factory.button(
        By.XPATH, ".//span[contains(text(),'Настройки')]",
        "Настройки тира")

    CAMERA_SETTINGS = aqas.element_factory.button(
        By.XPATH, ".//span[contains(text(),'Настройка камеры визуализатора')]",
        "Настройка камеры визуализатора")

    SERVICE = aqas.element_factory.button(
        By.XPATH, ".//span[contains(text(),'Сервисные функции')]",
        "Сервисные функции")

    ORGANISATIONS = aqas.element_factory.button(
        By.XPATH, ".//span[contains(text(),'Организации')]",
        "Организации")

    CLOSE = aqas.element_factory.button(
        By.XPATH, ".//span[contains(@class,'p-sidebar-close-icon')]",
        "Закрыть боковое меню")


class SideBarForm(aqas.BaseForm):
    """Класс, который содержит методы, используемые при проверке бокового меню."""
    elements = SideBarFormElements()

    def __init__(self):
        super().__init__(By.CLASS_NAME, "p-sidebar-header", "Страница бокового меню")

    def open_settings(self):
        self.elements.SETTINGS.click()

    def close_settings(self):
        self.elements.CLOSE.click()
