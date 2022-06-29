import aqas
from selenium.webdriver.common.by import By
from models.ui.forms.common_elements import CommonFormElements, CommonForm


class ExerciseMenuFormElements(aqas.BaseFormElements,CommonFormElements):
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


class ExerciseMenuForm(aqas.BaseForm, CommonForm):
    """
          Класс, который содержит методы, используемые при проверке страницы установки упражнения
       """
    elements = ExerciseMenuFormElements()

    def __init__(self):
        super().__init__(By.CLASS_NAME, ".//div[contains(text(),'Выбор упражнения на полосу')]",
                         "Страница Выбор упражнения на полосу")

    def back_to_lane1(self):
        self.elements.BACK_BTN.click()

    def is_notification_invisible(self):
        return self.elements.NOTIFICATION_LBL.state.wait_for_invisible()

    def is_notifications_invisible(self):
        return self.elements.NOTIFICATIONS_LBL.state.wait_for_invisible()

    def change_busy_lane(self):
        self.elements.BUSY_LANE_BTN.click()
