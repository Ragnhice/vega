from aqas.element_factory import ElementFactory
from aqas.forms.base_form import BaseForm, BaseFormElements
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By


class ConditionsMenuFormElements(BaseFormElements):
    """
      Класс, который содержит элементы, используемые при проверке страницы с условиями
      """
    SAVE_button = ElementFactory.button(
        By.XPATH, ".//button[contains(text(),'Сохранить ']",
        "Сохранить ")

    BUSY_LINE_SWITCH = ElementFactory.button(
        By.XPATH, ".//span[@class='p-inputswitch-slider']",
        "Сменить занятость полосы")

    OPEN_EXERCISE_PAGE = ElementFactory.button(
        By.XPATH, ".//div[@class='p-col-3']//a[href='/lines/1/exercises']",
        "Переход на страницу Выбор упражнения на полосу 1")

    LYING_POSITION = ElementFactory.button(
        By.XPATH, ".//div[aria-label='Сидя']",
        "Сидя")

    STANDING_POSITION = ElementFactory.button(
        By.XPATH, ".//div[aria-label='Стоя']",
        "Стоя")

    ITTING_POSITION = ElementFactory.button(
        By.XPATH, ".//div[aria-label='Лежа']",
        "Лежа")

    SEASON = ElementFactory.button(
        By.ID, "",
        "Выбор сезона")

    WINTER_SEASON = ElementFactory.button(
        By.ID, "",
        "Зима")

    SPRING_SEASON = ElementFactory.button(
        By.ID, "btn-season-2",
        "Весна")

    SUMMER_SEASON = ElementFactory.button(
        By.ID, "btn-season-3",
        "Лето")

    AUTUMN_SEASON = ElementFactory.button(
        By.ID, "btn-season-4",
        "Осень")

    SHOOTERS_MENU = ElementFactory.button(
        By.XPATH, ".//span[@class='material-icons md-22 md-light'][normalize-space()='launch']",
        "открыть окно выбора стрелков")

    CHOOSE_TIME_OPEN_LIST = ElementFactory.button(
        By.XPATH, ".//span[@class='p-dropdown-trigger-icon pi pi-chevron-down']",
        "Выбор точного времени")

    TIME_IN_LIST_12 = ElementFactory.button(
        By.XPATH, ".//li[aria-label='12'] ",
        "Время в поле Точное время")

    VISIBILITY_SHOWN = ElementFactory.button(
        By.XPATH, ".//h3[contains(text(),'Видимость: ')]",
        "Видимость показать")

    VISIBILITY_TO_CHANGE = ElementFactory.button(
        By.XPATH, ".//span[role='slider'][tabindex='0'][aria-valuemin='1']",
        "Видимость изменить")

    TEMPERATURE_SHOWN = ElementFactory.button(
        By.XPATH, ".//h3[contains(text(),'Температура: ')]",
        "Температура")

    WIND_SPEED_SHOWN = ElementFactory.button(
        By.XPATH, ".//h3[contains(text(),'Скорость ветра: ')]",
        "Скорость ветра")

    PRESSURE_SHOWN = ElementFactory.button(
        By.XPATH, ".//h3[contains(text(),'Давление:  ')]",
        "Давление")

    WIND_DIRECTION_SHOWN = ElementFactory.button(
        By.XPATH, ".//h3[contains(text(),'Направление ветра: ')]",
        "Направление ветра")

    HUMIDITY_SHOWN = ElementFactory.button(
        By.XPATH, ".//h3[contains(text(),'Влажность: ')]  ",
        "Влажность")

    ALTITUDE_SHOWN = ElementFactory.button(
        By.XPATH, ". //h3[contains(text(),'Высота')] ",
        "Высота")

    PRECIPITATION_SHOWN = ElementFactory.button(
        By.XPATH, ".//h3[contains(text(),'Интенсивность осадков')]  ",
        "Интенсивность осадков:")

    NOTIFICATION = ElementFactory.button(
        By.XPATH, ".//div[@class='p-toast-detail']",
        "Уведомление")

    NOTIFICATIONS = ElementFactory.label(
        By.XPATH, "//div[contains(@class, 'p-toast-top-right')]",
        "Все уведомления")

    BACK_button = ElementFactory.button(
        By.XPATH, ".//span[contains(text(),'arrow_back')]",
        "Стрелка Вернуться назад")

    LANE_IS_FREE = ElementFactory.label(
        By.XPATH, "//h2[contains(text(),'свободна')]",
        "Флаг свободной полосы")

    LANE_IS_BUSY = ElementFactory.label(
        By.XPATH, "//h2[contains(text(),'занята')]",
        "Флаг занятой полосы")

    BUSY_LANE_RADIO = ElementFactory.button(
        By.XPATH,
        "//div[contains(@class, 'lane-head-items')]//span[contains(@class, 'p-inputswitch-slider')]",
        "Занятость полосы"
        )

    CHOSEN_WEAPON = ElementFactory.button(By.XPATH, "//div[@id='weaponId']//span",
                                          "Поле выбранного оружия")

    CHOSEN_AMMO = ElementFactory.button(By.XPATH, "//div[@id='ammoId']//span",
                                        "Поле выбранного боеприпаса")

    CLOSE_CHOSE_WEAPON_TAB = ElementFactory.button(By.XPATH, "//span[contains(text(),'Закрыть')]",
                                                   "Закрыть выбор оружия")

    CONFIRM_CHOSEN_WEAPON = ElementFactory.button(By.XPATH, "//span[contains(text(),'Подтвердить')]",
                                                  "Подтвердить выбор оружия")

    PLAY_button = ElementFactory.button(
        By.XPATH, "//span[contains(text(),'play_arrow')]",
        "Старт упражнения")


class ConditionsMenuForm(BaseForm):
    """
            Класс, который содержит методы, используемые при проверке страницы с условиями
            """
    elements = ConditionsMenuFormElements()

    def __init__(self):
        super().__init__(By.XPATH, ".//div[contains(text(),'Выбор условий полосы 1')]",
                         "Страница Выбор условий полосы 1")

    def back_to_lane1(self):
        self.elements.BACK_button.click()

    def wait_for_invisible_notification(self):
        return self.elements.NOTIFICATION.state.wait_for_invisible()

    def wait_for_invisible_notifications(self):
        return self.elements.NOTIFICATIONS.state.wait_for_invisible()

    def lane_is_busy(self):
        try:
            return self.elements.LANE_IS_BUSY.state.wait_for_located(timeout=3)
        except TimeoutException:
            return False

    def lane_is_free(self):
        try:
            return self.elements.LANE_IS_FREE.state.wait_for_located(timeout=3)
        except TimeoutException:
            return False

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
        self.elements.PLAY_button.click()
