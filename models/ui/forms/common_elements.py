import aqas
from selenium.webdriver.common.by import By


class CommonFormElements(aqas.BaseFormElements):
    """Класс, который содержит элементы, используемые в 2+ разных формах."""

    BACK_BTN = aqas.element_factory.button(
        By.XPATH, ".//span[contains(text(),'arrow_back')]",
        "Стрелка Вернуться назад")

    BACK_2_BTN = aqas.element_factory.button(
        By.XPATH, "//a[@href='/lines/1']",
        "Стрелка Вернуться назад")

    BUSY_LANE_BTN = aqas.element_factory.button(
        By.XPATH, "//div[contains(@class, 'p-col-2')]//span",
        "Сменить занятость полосы")

    SHOOTERS_MENU_DRDN = aqas.element_factory.button(
        By.XPATH, ".//a[@href='/lines/1/shooters']//span",
        "открыть окно выбора стрелков")

    MENU_BTN = aqas.element_factory.button(
        By.XPATH, "//div[contains(@class, 'p-toolbar-group-left')]//span",
        "Меню")

    NOTIFICATIONS_LBL = aqas.element_factory.label(
        By.XPATH, "//div[contains(@class, 'p-toast-top-right')]",
        "Все уведомления")

    NOTIFICATION_LBL = aqas.element_factory.labels(
        By.CLASS_NAME, "p-toast-summary",
        "Уведомление")

    EX_MENU_BTN = aqas.element_factory.button(
        By.XPATH, "//a[@href='/lines/1/exercises']//span",
        "Открыть окно Выбор упражнения на полосу 1")

    CONDITIONS_MENU_BTN = aqas.element_factory.button(
        By.XPATH,
        "//a[@href='/lines/1/conditions']",
        "открыть окно Выбор условий полосы 1")

    SHOOTERS_MENU_BTN = aqas.element_factory.button(
        By.XPATH, ".//a[@href='/lines/1/shooters']//span",
        "открыть окно выбора стрелков")

    LANE_IS_FREE_LBL = aqas.element_factory.label(
        By.XPATH, "//h2[contains(text(),'свободна')]",
        "Флаг свободной полосы")

    LANE_IS_BUSY_LBL = aqas.element_factory.label(
        By.XPATH, "//h2[contains(text(),'занята')]",
        "Флаг занятой полосы")

    PLAY_BTN = aqas.element_factory.button(
        By.XPATH, "//span[contains(text(),'play_arrow')]",
        "Старт упражнения")

    STOP_BTN = aqas.element_factory.button(
        By.XPATH, ".//span[contains(text(),'stop')]",
        "Стоп упражнения")

    PAUSE_BTN = aqas.element_factory.button(
        By.XPATH, ".//span[contains(text(),'pause')]",
        "Приостановить упражнение")

    SAVE_BTN = aqas.element_factory.button(
        By.XPATH, ".//button[contains(text(),'Сохранить ']",
        "Сохранить ")


class CommonForm(aqas.BaseForm):
    """Класс, который содержит методы, используемые в 2+ разных формах."""
    elements = CommonFormElements()

    def __init__(self):
        super().__init__(By.XPATH, "//div[contains(@role,'toolbar')]", "Шапка страницы")

    def go_to_menu(self):
        self.elements.MENU_BTN.click()

    def is_notification_invisible(self):
        return self.elements.NOTIFICATION_LBL.state.wait_for_invisible()

    def is_notifications_invisible(self):
        return self.elements.NOTIFICATIONS_LBL.state.wait_for_invisible()

    def go_exercise_menu(self):
        self.elements.EX_MENU_BTN.click()

    def go_conditions_menu(self):
        self.elements.CONDITIONS_MENU_BTN.click()
