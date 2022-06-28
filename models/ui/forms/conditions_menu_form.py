import aqas
from selenium.webdriver.common.by import By


class ConditionsMenuFormElements(aqas.BaseFormElements):
    """Класс, который содержит элементы, используемые при проверке страницы с условиями."""
    SAVE = aqas.element_factory.button(
        By.XPATH, ".//button[contains(text(),'Сохранить ']",
        "Сохранить ")

    BUSY_LANE_RADIO = aqas.element_factory.button(
        By.XPATH, ".//span[@class='p-inputswitch-slider']",
        "Сменить занятость полосы")

    OPEN_EXERCISE_PAGE = aqas.element_factory.button(
        By.XPATH, ".//a[href='/lines/1/exercises']//span",
        "Переход на страницу Выбор упражнения на полосу 1")

    LYING_POSITION = aqas.element_factory.button(
        By.XPATH, ".//div[aria-label='Сидя']",
        "Сидя")

    STANDING_POSITION = aqas.element_factory.button(
        By.XPATH, ".//div[aria-label='Стоя']",
        "Стоя")

    ITTING_POSITION = aqas.element_factory.button(
        By.XPATH, ".//div[aria-label='Лежа']",
        "Лежа")

    SPRING_SEASON = aqas.element_factory.button(
        By.ID, "btn-season-2",
        "Весна")

    SUMMER_SEASON = aqas.element_factory.button(
        By.ID, "btn-season-3",
        "Лето")

    AUTUMN_SEASON = aqas.element_factory.button(
        By.ID, "btn-season-4",
        "Осень")

    SHOOTERS_MENU = aqas.element_factory.button(
        By.XPATH, ".//a[@href='/lines/1/shooters']//span",
        "открыть окно выбора стрелков")

    CHOOSE_TIME_OPEN_LIST = aqas.element_factory.button(
        By.XPATH, ".//div[@id='dayTime']",
        "Выбор точного времени")

    TIME_IN_LIST_12 = aqas.element_factory.button(
        By.XPATH, ".//li[aria-label='12']",
        "Время в поле Точное время")

    VISIBILITY_SHOWN = aqas.element_factory.button(
        By.XPATH, ".//h3[contains(text(),'Видимость:')]",
        "Видимость показать")

    VISIBILITY_TO_CHANGE = aqas.element_factory.button(
        By.XPATH, ".//span[role='slider'][tabindex='0'][aria-valuemin='1']",
        "Видимость изменить")

    TEMPERATURE_SHOWN = aqas.element_factory.button(
        By.XPATH, ".//h3[contains(text(),'Температура:')]",
        "Температура")

    WIND_SPEED_SHOWN = aqas.element_factory.button(
        By.XPATH, ".//h3[contains(text(),'Скорость ветра:')]",
        "Скорость ветра")

    PRESSURE_SHOWN = aqas.element_factory.button(
        By.XPATH, ".//h3[contains(text(),'Давление:')]",
        "Давление")

    WIND_DIRECTION_SHOWN = aqas.element_factory.button(
        By.XPATH, ".//h3[contains(text(),'Направление ветра: ')]",
        "Направление ветра")

    HUMIDITY_SHOWN = aqas.element_factory.button(
        By.XPATH, ".//h3[contains(text(),'Влажность:')]  ",
        "Влажность")

    ALTITUDE_SHOWN = aqas.element_factory.button(
        By.XPATH, ". //h3[contains(text(),'Высота')] ",
        "Высота")

    PRECIPITATION_SHOWN = aqas.element_factory.button(
        By.XPATH, ".//h3[contains(text(),'Интенсивность осадков')]  ",
        "Интенсивность осадков:")

    NOTIFICATION = aqas.element_factory.button(
        By.XPATH, ".//div[@class='p-toast-detail']",
        "Уведомление")

    NOTIFICATIONS = aqas.element_factory.label(
        By.XPATH, "//div[contains(@class, 'p-toast-top-right')]",
        "Все уведомления")

    BACK_BTN = aqas.element_factory.button(
        By.XPATH, ".//span[contains(text(),'arrow_back')]",
        "Стрелка Вернуться назад")

    LANE_IS_FREE = aqas.element_factory.label(
        By.XPATH, "//h2[contains(text(),'свободна')]",
        "Флаг свободной полосы")

    LANE_IS_BUSY = aqas.element_factory.label(
        By.XPATH, "//h2[contains(text(),'занята')]",
        "Флаг занятой полосы")

    CHOSEN_WEAPON = aqas.element_factory.button(
        By.XPATH, "//div[@id='weaponId']//span",
        "Поле выбранного оружия")

    CHOSEN_AMMO = aqas.element_factory.button(
        By.XPATH, "//div[@id='ammoId']//span",
        "Поле выбранного боеприпаса")

    CLOSE_CHOSE_WEAPON_TAB = aqas.element_factory.button(
        By.XPATH, "//span[contains(text(),'Закрыть')]",
        "Закрыть выбор оружия")

    CONFIRM_CHOSEN_WEAPON = aqas.element_factory.button(
        By.XPATH, "//span[contains(text(),'Подтвердить')]",
        "Подтвердить выбор оружия")

    PLAY = aqas.element_factory.button(
        By.XPATH, "//span[contains(text(),'play_arrow')]",
        "Старт упражнения")


class ConditionsMenuForm(aqas.BaseForm):
    """Класс, который содержит методы, используемые при проверке страницы с условиями."""
    elements = ConditionsMenuFormElements()

    def __init__(self):
        super().__init__(By.XPATH, ".//div[contains(text(),'Выбор условий полосы 1')]",
                         "Страница Выбор условий полосы 1")

    def back_to_lane1(self):
        self.elements.BACK_BTN.click()

    def is_notification_invisible(self):
        return self.elements.NOTIFICATION.state.wait_for_invisible()

    def is_notifications_invisible(self):
        return self.elements.NOTIFICATIONS.state.wait_for_invisible()

    def change_busy_lane(self):
        self.elements.BUSY_LANE_RADIO.click()

    def get_chosen_weapon(self):
        return self.elements.CHOSEN_WEAPON.text

    def get_chosen_ammo(self):
        return self.elements.CHOSEN_AMMO.text

    def close_chose_weapon_tab(self):
        self.elements.CLOSE_CHOSE_WEAPON_TAB.click()

    def confirm_chosen_weapon(self):
        self.elements.CONFIRM_CHOSEN_WEAPON.click()

    def press_play(self):
        self.elements.PLAY.click()
