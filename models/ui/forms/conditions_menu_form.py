import aqas
from selenium.webdriver.common.by import By
from models.ui.forms.common_elements import CommonFormElements, CommonForm


class ConditionsMenuFormElements(aqas.BaseFormElements,CommonFormElements):
    """Класс, который содержит элементы, используемые при проверке страницы с условиями."""

    BUSY_LANE_BTN = aqas.element_factory.button(
        By.XPATH, ".//span[@class='p-inputswitch-slider']",
        "Сменить занятость полосы")

    OPEN_EXERCISE_PAGE_BTN = aqas.element_factory.button(
        By.XPATH, ".//a[href='/lines/1/exercises']//span",
        "Перейти на страницу Выбор упражнения на полосу 1")

    LYING_POSITION_BTN = aqas.element_factory.button(
        By.XPATH, ".//div[aria-label='Сидя']",
        "Сидя")

    STANDING_POSITION_BTN = aqas.element_factory.button(
        By.XPATH, ".//div[aria-label='Стоя']",
        "Стоя")

    ITTING_POSITION_BTN = aqas.element_factory.button(
        By.XPATH, ".//div[aria-label='Лежа']",
        "Лежа")

    SPRING_SEASON_BTN = aqas.element_factory.button(
        By.ID, "btn-season-2",
        "Весна")

    SUMMER_SEASON_BTN = aqas.element_factory.button(
        By.ID, "btn-season-3",
        "Лето")

    AUTUMN_SEASON_BTN = aqas.element_factory.button(
        By.ID, "btn-season-4",
        "Осень")

    CHOOSE_TIME_OPEN_LIST_BTN = aqas.element_factory.button(
        By.XPATH, ".//div[@id='dayTime']",
        "Выбор точного времени")

    TIME_IN_LIST_12_BTN = aqas.element_factory.button(
        By.XPATH, ".//li[aria-label='12']",
        "Время в поле Точное время")

    VISIBILITY_SHOWN_BTN = aqas.element_factory.button(
        By.XPATH, ".//h3[contains(text(),'Видимость:')]",
        "Видимость показать")

    VISIBILITY_TO_CHANGE_BTN = aqas.element_factory.button(
        By.XPATH, ".//span[role='slider'][tabindex='0'][aria-valuemin='1']",
        "Видимость изменить")

    TEMPERATURE_SHOWN_BTN = aqas.element_factory.button(
        By.XPATH, ".//h3[contains(text(),'Температура:')]",
        "Температура")

    WIND_SPEED_SHOWN_BTN = aqas.element_factory.button(
        By.XPATH, ".//h3[contains(text(),'Скорость ветра:')]",
        "Скорость ветра")

    PRESSURE_SHOWN_BTN = aqas.element_factory.button(
        By.XPATH, ".//h3[contains(text(),'Давление:')]",
        "Давление")

    WIND_DIRECTION_SHOWN_BTN = aqas.element_factory.button(
        By.XPATH, ".//h3[contains(text(),'Направление ветра: ')]",
        "Направление ветра")

    HUMIDITY_SHOWN_BTN = aqas.element_factory.button(
        By.XPATH, ".//h3[contains(text(),'Влажность:')]  ",
        "Влажность")

    ALTITUDE_SHOWN_BTN = aqas.element_factory.button(
        By.XPATH, ". //h3[contains(text(),'Высота')] ",
        "Высота")

    PRECIPITATION_SHOWN_BTN = aqas.element_factory.button(
        By.XPATH, ".//h3[contains(text(),'Интенсивность осадков')]  ",
        "Интенсивность осадков:")

    CHOSEN_WEAPON_BTN = aqas.element_factory.button(
        By.XPATH, "//div[@id='weaponId']//span",
        "Поле выбранного оружия")

    CHOSEN_AMMO_BTN = aqas.element_factory.button(
        By.XPATH, "//div[@id='ammoId']//span",
        "Поле выбранного боеприпаса")

    CLOSE_CHOSE_WEAPON_BTN = aqas.element_factory.button(
        By.XPATH, "//span[contains(text(),'Закрыть')]",
        "Закрыть выбор оружия")

    CONFIRM_CHOSEN_WEAPON_BTN = aqas.element_factory.button(
        By.XPATH, "//span[contains(text(),'Подтвердить')]",
        "Подтвердить выбор оружия")


class ConditionsMenuForm(aqas.BaseForm, CommonForm):
    """Класс, который содержит методы, используемые при проверке страницы с условиями."""
    elements = ConditionsMenuFormElements()

    def __init__(self):
        super().__init__(By.XPATH, ".//div[contains(text(),'Выбор условий полосы 1')]",
                         "Страница Выбор условий полосы 1")

    def back_to_lane1(self):
        self.elements.BACK_BTN.click()

    def is_notification_invisible(self):
        return self.elements.NOTIFICATION_LBL.state.wait_for_invisible()

    def is_notifications_invisible(self):
        return self.elements.NOTIFICATIONS_LBL.state.wait_for_invisible()

    def change_busy_lane(self):
        self.elements.BUSY_LANE_BTN.click()

    def get_chosen_weapon(self):
        return self.elements.CHOSEN_WEAPON_BTN.text

    def get_chosen_ammo(self):
        return self.elements.CHOSEN_AMMO_BTN.text

    def close_chose_weapon_tab(self):
        self.elements.CLOSE_CHOSE_WEAPON_BTN.click()

    def confirm_chosen_weapon(self):
        self.elements.CONFIRM_CHOSEN_WEAPON_BTN.click()

    def press_play(self):
        self.elements.PLAY_BTN.click()
