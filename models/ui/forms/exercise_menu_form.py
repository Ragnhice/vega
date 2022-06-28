import aqas
from selenium.webdriver.common.by import By


class ExerciseMenuFormElements(aqas.BaseFormElements):
    """
       Класс, который содержит элементы, используемые при проверке страницы установки упражнения
    """

    SHOOTERS_MENU = aqas.element_factory.button(
        By.XPATH, ".//a[@href='/lines/1/shooters']//span",
        "открыть окно выбора стрелков")

    SHOOTER_CHOSEN_NAME = aqas.element_factory.button(
        By.XPATH, ".//div[@class='head_shooter__item-data']",
        "Имя выбранного стрелка")

    SEARCH_EXERCISE_FIELD = aqas.element_factory.button(
        By.XPATH, ".//input[@placeholder='Поиск упражнения']",
        "Поле поиска упражнения")

    EX_IN_LIST_NUM_1 = aqas.element_factory.button(
        By.XPATH, ".//li[aria-label()='1']//span[@class='p-ink']",
        "Имя первого упражнения в списке выбора")

    SAVE = aqas.element_factory.button(
        By.XPATH, ".//button[contains(text(),'Сохранить']",
        "Сохранить")

    OUT_WITHOUT_SAVE = aqas.element_factory.button(
        By.XPATH, ".//button[contains(text(),'Выйти без сохранения']",
        "Выйти без сохранения")

    NOTIFICATION = aqas.element_factory.button(
        By.XPATH, ".//div[@class='p-toast-detail']",
        "Уведомление")

    NOTIFICATIONS = aqas.element_factory.label(
        By.XPATH, "//div[contains(@class,'p-toast-top-right')]",
        "Все уведомления")

    BACK = aqas.element_factory.button(
        By.XPATH, ".//span[contains(text(),'arrow_back')]",
        "Стрелка Вернуться назад")

    LANE_IS_FREE = aqas.element_factory.label(
        By.XPATH, "//h2[contains(text(),'свободна')]",
        "Флаг свободной полосы")

    LANE_IS_BUSY = aqas.element_factory.label(
        By.XPATH, "//h2[contains(text(),'занята')]",
        "Флаг занятой полосы")

    BUSY_LANE_RADIO = aqas.element_factory.button(
        By.XPATH, "//div[contains(@class,'lane-head-items')]//span[contains(@class,'p-inputswitch-slider')]",
        "Занятость полосы")


class ExerciseMenuForm(aqas.BaseForm):
    """
          Класс, который содержит методы, используемые при проверке страницы установки упражнения
       """
    elements = ExerciseMenuFormElements()

    def __init__(self):
        super().__init__(By.CLASS_NAME, ".//div[contains(text(),'Выбор упражнения на полосу')]",
                         "Страница Выбор упражнения на полосу")

    def back_to_lane1(self):
        self.elements.BACK.click()

    def is_notification_invisible(self):
        return self.elements.NOTIFICATION.state.wait_for_invisible()

    def is_notifications_invisible(self):
        return self.elements.NOTIFICATIONS.state.wait_for_invisible()

    def change_busy_lane(self):
        self.elements.BUSY_LANE_RADIO.click()
