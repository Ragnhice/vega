from selenium.webdriver.common.by import By

from aqas.element_factory import ElementFactory
from aqas.forms.base_form import BaseForm, BaseFormElements


class ShootingSettingsFormElements(BaseFormElements):
    """
    Класс, который содержит элементы, используемые при проверке страницы настроек тира
    """

    RADIOBUTTON_TIDE = ElementFactory.Button(
        By.XPATH, ".//label[contains(text(),'Узкий')]",
        "Узкий размер экрана")

    RADIOBUTTON_FULL = ElementFactory.Button(
        By.XPATH, ".//label[contains(text(),'Полный')]",
        "Полный размер экрана")

    RADIOBUTTON_WIDE = ElementFactory.Button(
        By.XPATH, ".//label[contains(text(),'Широкий')]",
        "Широкий размер экрана")

    RADIOBUTTON_DUEL = ElementFactory.Button(
        By.XPATH, ".//label[contains(text(),'Дуэль')]",
        "Режим Дуэль")

    LINE_COUNTS = ElementFactory.Button(
        By.XPATH, " //*[@id='linesCount']/span]",
        "Поле выбора количества полос")

    NOTIFICATIONS = ElementFactory.Labels(
        By.XPATH, "//div[contains(@class, 'p-toast-top-right')]",
        "Все уведомления")


class ShootingSettingsForm(BaseForm):
    """
              Класс, который содержит методы, используемые при проверке страницы настроек тира
    """
    elements = ShootingSettingsFormElements()

    def __init__(self):
        super().__init__(By.XPATH, "//div[ contains(text(),'Управление полосами')]", "Главная страница настроек тира")

    """
    Класс, который содержит методы, используемые при проверке страницы управления полосами
    """
