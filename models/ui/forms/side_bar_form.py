from aqas.element_factory import ElementFactory
from aqas.forms.base_form import BaseForm, BaseFormElements
from selenium.webdriver.common.by import By


class SideBarFormElements(BaseFormElements):
    """
    Класс, который содержит элементы, используемые при проверке бокового меню
    """

    MENU_BUTTON = ElementFactory.Button(By.XPATH,
        "//div[contains(@class, 'p-toolbar-group-left')]//span"),"Меню")


    SETTINGS = ElementFactory.Button(
    By.XPATH, ".//span[contains(text(),'Настройки')]",
    "Настройки")

    LINES_CONTROLLING = ElementFactory.Button(
    By.XPATH, ".//span[contains(text(),'Управление полосами')]",
    "Управление полосами")

    EX_EDITOR = ElementFactory.Button(
    By.XPATH, "//a[@href='/staff']",
    "Редактор упражнения")

    STAFF = ElementFactory.Button(
    By.XPATH, "//a[@href='/:ExerciseEditor']",
    "Пользователи")

    class SideBarForm(BaseForm):
        """
                Класс, который содержит методы, используемые при проверке бокового меню
        """
        elements = SideBarFormElements()

        def __init__(self):
            super().__init__(By.CLASS_NAME, "p-sidebar-header", "Страница бокового меню")
