import aqas
from selenium.webdriver.common.by import By
from models.ui.forms.common_elements import CommonFormElements, CommonForm


class SideBarFormElements(aqas.BaseFormElements,CommonFormElements):
    """Класс, который содержит элементы, используемые при проверке бокового меню."""

    SETTINGS_BTN = aqas.element_factory.button(
        By.XPATH, ".//span[contains(@class,'p-panelmenu-icon')]",
        "Настройки")

    LANES_CONTROLLING_BTN = aqas.element_factory.button(
        By.XPATH, ".//span[contains(text(),'Управление полосами')]",
        "Управление полосами")

    EX_EDITOR_BTN = aqas.element_factory.button(
        By.XPATH, ".//span[contains(text(),'Редактор упражнений')]",
        "Редактор упражнения")

    USERS_BTN = aqas.element_factory.button(
        By.XPATH, ".//span[contains(text(),'Пользователи')]",
        "Пользователи")

    STATISTIC_BTN = aqas.element_factory.button(
        By.XPATH, ".//span[contains(text(),'Статистика')]",
        "Статистика")

    SHOOTING_MODE_BTN = aqas.element_factory.button(
        By.XPATH, ".//span[contains(text(),'Настройки')]",
        "Настройки тира")

    CAMERA_SETTINGS_BTN = aqas.element_factory.button(
        By.XPATH, ".//span[contains(text(),'Настройка камеры визуализатора')]",
        "Настройка камеры визуализатора")

    SERVICE_BTN = aqas.element_factory.button(
        By.XPATH, ".//span[contains(text(),'Сервисные функции')]",
        "Сервисные функции")

    ORGANISATIONS_BTN = aqas.element_factory.button(
        By.XPATH, ".//span[contains(text(),'Организации')]",
        "Организации")

    CLOSE_BTN = aqas.element_factory.button(
        By.XPATH, ".//span[contains(@class,'p-sidebar-close-icon')]",
        "Закрыть боковое меню")


class SideBarForm(aqas.BaseForm, CommonForm):
    """Класс, который содержит методы, используемые при проверке бокового меню."""
    elements = SideBarFormElements()

    def __init__(self):
        super().__init__(By.CLASS_NAME, "p-sidebar-header", "Страница бокового меню")

    def open_settings(self):
        self.elements.SETTINGS_BTN.click()

    def close_settings(self):
        self.elements.CLOSE_BTN.click()
