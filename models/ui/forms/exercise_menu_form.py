from selenium.webdriver.common.by import By
from aqas.element_factory import ElementFactory
from aqas.forms.base_form import BaseForm, BaseFormElements


class ExerciseMenuFormElements(BaseFormElements):
    """
       Класс, который содержит элементы, используемые при проверке страницы установки упражнения
    """
    BUSY_LINE_SWITCH = ElementFactory.Button(
        By.XPATH, ".//div [@class='p-inputswitch p-component p-mt-2 p-mr-2'] //span[@class='p-inputswitch-slider']",
        "Сменить занятость полосы")

    SHOOTERS_CHOOSE = ElementFactory.Button(
        By.XPATH, ".//div[@class='p-col-6']//span[@class='material-icons md-22 md-light'][normalize-space()='launch']",
        "Перейти в раздел выбора стрелков")

    SHOOTER_CHOSEN_NAME = ElementFactory.Button(
        By.XPATH, ".//div[@class='head_shooter__item-data']",
        "Имя выбранного стрелка")

    SEARCH_EXERCISE_FIELD = ElementFactory.Button(
        By.XPATH, ".//input[@placeholder='Поиск упражнения']",
        "Поле поиска упражнения")

    EX_IN_LIST_NUM_1 = ElementFactory.Button(
        By.XPATH, ".//li[aria-label()='1']//span[@class='p-ink p-ink-active']",
        "Имя ервого упражнения в списке выбора")

    SAVE_BUTTON = ElementFactory.Button(
        By.XPATH, ".//button[contains(text(),'Сохранить']",
        "Сохранить")

    OUT_WITHOUT_SAVE_BUTTON = ElementFactory.Button(
        By.XPATH, ".//button[contains(text(),'Выйти без сохранения']",
        "Выйти без сохранения")

    NOTIFICATION = ElementFactory.Button(
        By.XPATH, ".//div[@class='p-toast-detail']",
        "Уведомление")

    NOTIFICATIONS = ElementFactory.Labels(
        By.XPATH, "//div[contains(@class, 'p-toast-top-right')]",
        "Все уведомления")

    BACK_BUTTON = ElementFactory.Button(
        By.XPATH, ".//span[contains('arrow_back')]",
        "Стрелка Вернуться назад")


class ExerciseMenuForm(BaseForm):
    """
          Класс, который содержит методы, используемые при проверке страницы установки упражнения
       """
    elements = ExerciseMenuFormElements()

    def __init__(self):
        super().__init__(By.CLASS_NAME, ".//div[contains(text(),' Выбор упражнения на полосу')]",
                         "Страница Выбор упражнения на полосу")
