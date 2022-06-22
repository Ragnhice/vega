from aqas.element_factory import ElementFactory
from aqas.forms.base_form import BaseForm, BaseFormElements
from selenium.webdriver.common.by import By


class ShootingSettingsFormElements(BaseFormElements):
    """
    Класс, который содержит элементы, используемые при проверке страницы настроек тира
    """

    RADIOBUTTON_TIDE = ElementFactory.button(
        By.XPATH, ".//label[contains(text(),'Узкий')]",
        "Узкий размер экрана")

    RADIOBUTTON_FULL = ElementFactory.button(
        By.XPATH, ".//label[contains(text(),'Полный')]",
        "Полный размер экрана")

    RADIOBUTTON_WIDE = ElementFactory.button(
        By.XPATH, ".//label[contains(text(),'Широкий')]",
        "Широкий размер экрана")

    RADIOBUTTON_DUEL = ElementFactory.button(
        By.XPATH, ".//label[contains(text(),'Дуэль')]",
        "Режим Дуэль")

    LANE_COUNTS = ElementFactory.button(
        By.XPATH, " //*[@id='linesCount']/span]",
        "Поле выбора количества полос")

    NOTIFICATIONS = ElementFactory.label(
        By.XPATH, "//div[contains(@class, 'p-toast-top-right')]",
        "Все уведомления")


class ShootingSettingsForm(BaseForm):
    """
              Класс, который содержит методы, используемые при проверке страницы настроек тира
    """
    elements = ShootingSettingsFormElements()

    def __init__(self):
        super().__init__(By.XPATH, "//div[ contains(text(),'Управление полосами')]",
                         "Главная страница настроек тира")

    """
    Класс, который содержит методы, используемые при проверке страницы управления полосами
    """
