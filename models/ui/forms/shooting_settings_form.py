import aqas

from selenium.webdriver.common.by import By


class ShootingSettingsFormElements(aqas.BaseFormElements):
    """
    Класс, который содержит элементы, используемые при проверке страницы настроек тира
    """

    TIDE = aqas.element_factory.button(
        By.XPATH, ".//label[contains(text(),'Узкий')]",
        "Узкий размер экрана")

    FULL = aqas.element_factory.button(
        By.XPATH, ".//label[contains(text(),'Полный')]",
        "Полный размер экрана")

    WIDE = aqas.element_factory.button(
        By.XPATH, ".//label[contains(text(),'Широкий')]",
        "Широкий размер экрана")

    DUEL = aqas.element_factory.button(
        By.XPATH, ".//label[contains(text(),'Дуэль')]",
        "Режим Дуэль")

    LANE_COUNTS = aqas.element_factory.button(
        By.XPATH, " //*[@id='linesCount']/span]",
        "Поле выбора количества полос")

    NOTIFICATIONS = aqas.element_factory.labels(
        By.XPATH, "//div[contains(@class, 'p-toast-top-right')]",
        "Все уведомления")


class ShootingSettingsForm(aqas.BaseForm):
    """Класс, который содержит методы, используемые при проверке страницы настроек тира."""

    elements = ShootingSettingsFormElements()

    def __init__(self):
        super().__init__(By.XPATH, "//div[ contains(text(),'Управление полосами')]",
                         "Главная страница настроек тира")
