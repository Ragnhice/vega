import aqas
from selenium.webdriver.common.by import By


class CommonElements(aqas.BaseFormElements):
    """Класс, который содержит элементы, используемые на всех формах."""

    MENU_BTN = aqas.element_factory.button(
        By.XPATH, "//div[contains(@class,'p-toolbar-group-left')]//span",
        "Меню")

    NOTIFICATIONS_LBL = aqas.element_factory.label(
        By.XPATH, "//div[contains(@class,'p-toast-top-right')]",
        "Все уведомления")

    NOTIFICATION_LBL = aqas.element_factory.labels(
        By.CLASS_NAME, "p-toast-summary",
        "Уведомление")


class StateLaneElements(aqas.BaseFormElements):
    """Класс, который содержит элементы, используемые для изменения и проверки состояния полосы."""

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

    BUSY_LANE_BTN = aqas.element_factory.button(
        By.XPATH, "//div[contains(@class,'p-col-2')]//span",
        "Сменить занятость полосы")


class SettingsElements(aqas.BaseFormElements):
    """Класс, который содержит элементы, используемые для работы с экранами настроек полосы."""

    BACK_BTN = aqas.element_factory.button(
        By.XPATH, ".//span[contains(text(),'arrow_back')]",
        "Стрелка Вернуться назад")

    BACK_2_BTN = aqas.element_factory.button(
        By.XPATH, "//a[@href='/lines/1']",
        "Стрелка Вернуться назад")

    EX_MENU_BTN = aqas.element_factory.button(
        By.XPATH, "//a[@href='/lines/1/exercises']//span",
        "Открыть окно Выбор упражнения на полосу 1")

    CONDITIONS_MENU_BTN = aqas.element_factory.button(
        By.XPATH, "//a[@href='/lines/1/conditions']",
        "Открыть окно Выбор условий полосы 1")

    SHOOTERS_MENU_BTN = aqas.element_factory.button(
        By.XPATH, ".//a[@href='/lines/1/shooters']//span",
        "Открыть окно выбора стрелков")

    SAVE_BTN = aqas.element_factory.button(
        By.XPATH, ".//button[contains(text(),'Сохранить']",
        "Сохранить ")

    SHOOTERS_MENU_DRDN = aqas.element_factory.button(
        By.XPATH, ".//a[@href='/lines/1/shooters']//span",
        "Открыть окно выбора стрелков")
