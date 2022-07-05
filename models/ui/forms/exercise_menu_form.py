import aqas
from selenium.webdriver.common.by import By

from models.ui.common_elements import CommonElements, SettingsElements, StateLaneElements


class ExerciseMenuFormElements(CommonElements, SettingsElements, StateLaneElements):
    """
       Класс, который содержит элементы, используемые при проверке страницы установки упражнения
    """

    SHOOTER_CHOSEN_NAME_LBL = aqas.element_factory.label(
        By.XPATH, ".//div[@class='head_shooter__item-data']",
        "Имя выбранного стрелка")

    SEARCH_EXERCISE_TBX = aqas.element_factory.text_box(
        By.XPATH, ".//input[@placeholder='Поиск упражнения']",
        "Поле поиска упражнения")

    EX_IN_LIST_NUM_1_LBL = aqas.element_factory.label(
        By.XPATH, ".//li[aria-label()='1']//span[@class='p-ink']",
        "Имя первого упражнения в списке выбора")

    OUT_WITHOUT_SAVE_BTN = aqas.element_factory.button(
        By.XPATH, ".//button[contains(text(),'Выйти без сохранения']",
        "Выйти без сохранения")

    BUSY_LANE_BTN_EX_MENU = aqas.element_factory.button(
        By.XPATH, "//div[contains(@class, 'p-col-2')]//span",
        "Сменить занятость полосы")


class ExerciseMenuForm(aqas.BaseForm):
    """
          Класс, который содержит методы, используемые при проверке страницы установки упражнения
       """
    elements = ExerciseMenuFormElements()

    def __init__(self):
        super().__init__(By.CLASS_NAME, ".//div[contains(text(),'Выбор упражнения на полосу')]",
                         "Страница Выбор упражнения на полосу")

    def wait_for_notification_invisible(self):
        self.elements.NOTIFICATION_LBL.state.wait_for_invisible()

    def wait_for_notifications_invisible(self):
        self.elements.NOTIFICATIONS_LBL.state.wait_for_invisible()
