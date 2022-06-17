from selenium.webdriver.common.by import By
from aqas.element_factory import ElementFactory
from aqas.forms.base_form import BaseForm, BaseFormElements


class ConditionsMenuFormElements(BaseFormElements):
    """
      Класс, который содержит элементы, используемые при проверке страницы с условиями
      """
    SAVE_BUTTON = ElementFactory.Button(
        By.XPATH, ".//button[contains(text(),'Сохранить ']",
        "Сохранить ")

    NOTIFICATION = ElementFactory.Button(
        By.XPATH, ".//div[@class='p-toast-detail']",
        "Уведомление")

    BACK_BUTTON = ElementFactory.Button(
        By.XPATH, ".//span[normalize-space()='arrow_back']",
        "Стрелка выйти назад")

    BUSY_LINE_SWITCH = ElementFactory.Button(
        By.XPATH, ".//span[@class='p-inputswitch-slider']",
        "Сменить занятость полосы")

    OPEN_EXERCISE_PAGE = ElementFactory.Button(
        By.XPATH, ".//div[@class='p-col-3']//a[href='/lines/1/exercises']",
        "Переход на страницу Выбор упражнения на полосу 1")

    LYING_POSITION = ElementFactory.Button(
        By.XPATH, ".//div[aria-label='Сидя']",
        "Сидя")

    STANDING_POSITION = ElementFactory.Button(
        By.XPATH, ".//div[aria-label='Стоя']",
        "Стоя")

    ITTING_POSITION = ElementFactory.Button(
        By.XPATH, ".//div[aria-label='Лежа']",
        "Лежа")

    SEASON = ElementFactory.Button(
        By.ID, "",
        "Выбор сезона")

    WINTER_SEASON = ElementFactory.Button(
        By.ID, "",
        "Зима")

    SPRING_SEASON = ElementFactory.Button(
        By.ID, "btn-season-2",
        "Весна")

    SUMMER_SEASON = ElementFactory.Button(
        By.ID, "btn-season-3",
        "Лето")

    AUTUMN_SEASON = ElementFactory.Button(
        By.ID, "btn-season-4",
        "Осень")

    SHOOTERS_MENU = ElementFactory.Button(
        By.XPATH, ".//span[@class='material-icons md-22 md-light'][normalize-space()='launch']",
        "открыть окно выбора стрелков")

    CHOOSE_TIME_OPEN_LIST = ElementFactory.Button(
        By.XPATH, ".//span[@class='p-dropdown-trigger-icon pi pi-chevron-down']",
        "Выбор точного времени")

    TIME_IN_LIST_12 = ElementFactory.Button(
        By.XPATH, ".//li[aria-label='12'] ",
        "Время в поле Точное время")

    VISIBILITY_SHOWN = ElementFactory.Button(
        By.XPATH, ".//h3[contains(text(),'Видимость: ')]",
        "Видимость показать")

    VISIBILITY_TO_CHANGE = ElementFactory.Button(
        By.XPATH, ".//span[role='slider'][tabindex='0'][aria-valuemin='1']",
        "Видимость изменить")

    TEMPERATURE_SHOWN = ElementFactory.Button(
        By.XPATH, ".//h3[contains(text(),'Температура: ')]",
        "Температура")

    WIND_SPEED_SHOWN = ElementFactory.Button(
        By.XPATH, ".//h3[contains(text(),'Скорость ветра: ')]",
        "Скорость ветра")

    PRESSURE_SHOWN = ElementFactory.Button(
        By.XPATH, ".//h3[contains(text(),'Давление:  ')]",
        "Давление")

    WIND_DIRECTION_SHOWN = ElementFactory.Button(
        By.XPATH, ".//h3[contains(text(),'Направление ветра: ')]",
        "Направление ветра")

    HUMIDITY_SHOWN = ElementFactory.Button(
        By.XPATH, ".//h3[contains(text(),'Влажность: ')]  ",
        "Влажность")

    ALTITUDE_SHOWN = ElementFactory.Button(
        By.XPATH, ". //h3[contains(text(),'Высота')] ",
        "Высота")

    PRECIPITATION_SHOWN = ElementFactory.Button(
        By.XPATH, ".//h3[contains(text(),'Интенсивность осадков')]  ",
        "Интенсивность осадков:")


class ConditionsMenuForm(BaseForm):
    """
            Класс, который содержит методы, используемые при проверке страницы с условиями
            """
    elements = ConditionsMenuFormElements(BaseFormElements)

    def __init__(self):
        super().__init__(By.XPATH, ".//div[contains(text(),'Выбор условий полосы 1')]",
                         "Страница Выбор условий полосы 1")
