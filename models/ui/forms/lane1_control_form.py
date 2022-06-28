import aqas
from selenium.webdriver.common.by import By


class Lane1ControlFormElements(aqas.BaseFormElements):
    """Класс, который содержит элементы, используемые при проверке управления первой полосой."""

    BUSY_LANE_RADIO = aqas.element_factory.label(
        By.XPATH, "//div[contains(@class, 'lane-head-items')]//span",
        "Занятость полосы")

    PLAY = aqas.element_factory.button(
        By.XPATH, "//span[contains(text(),'play_arrow')]",
        "Старт упражнения")

    STOP = aqas.element_factory.button(
        By.XPATH, ".//span[contains(text(),'stop')]",
        "Стоп упражнения")

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

    SHOOTERS_MENU = aqas.element_factory.button(
        By.XPATH, ".//a[@href='/lines/1/shooters']//span",
        "Переход к  странице выбора стрелков")

    PAUSE = aqas.element_factory.button(
        By.XPATH, ".//span[contains(text(),'pause')]",
        "Приостановить упражнение")

    TIME = aqas.element_factory.button(
        By.XPATH, ".//div[contains(text(),'Резульат')/div/div[5]/div[1]",
        "Значение времени от начала")

    CONDITIONS_MENU = aqas.element_factory.button(
        By.XPATH,
        "//a[@href='/lines/1/conditions']",
        "открыть окно Выбор условий полосы 1")

    PRINT_QUICK = aqas.element_factory.button(
        By.XPATH, "//a[@href='/lines/1/stats']",
        "Распечатать отчет")

    EX_MENU = aqas.element_factory.button(
        By.XPATH, "//a[@href='/lines/1/exercises']//span",
        "Открыть окно Выбор упражнения на полосу 1")

    NOTIFICATION = aqas.element_factory.label(
        By.CLASS_NAME, "p-toast-summary",
        "Уведомление")

    NOTIFICATIONS = aqas.element_factory.label(
        By.XPATH, "//div[contains(@class, 'p-toast-top-right')]",
        "Все уведомления")

    LANE_IS_FREE = aqas.element_factory.label(
        By.XPATH, "//h2[contains(text(),'свободна')]",
        "Флаг свободной полосы")

    LANE_IS_BUSY = aqas.element_factory.label(
        By.XPATH, "//h2[contains(text(),'занята')]",
        "Флаг занятой полосы")

    STOP_DISABLED = aqas.element_factory.button(
        By.XPATH, "//button[contains(@class, 'p-disabled')]/span[contains(text(),'stop')]",
        "Кнопка остановки упражнения в НЕКЛИКАБЕЛЬНОМ СОСТОЯНИИ")

    PLAY_DISABLED = aqas.element_factory.button(
        By.XPATH, "//button[contains(@class, 'p-disabled')]/span[contains(text(),'play_arrow')]",
        "Кнопка запуска упражнения в НЕКЛИКАБЕЛЬНОМ СОСТОЯНИИ")

    PAUSE_DISABLED = aqas.element_factory.button(
        By.XPATH, "//button[contains(@class, 'p-disabled')]/span[contains(text(),'pause')]",
        "Кнопка паузы в НЕКЛИКАБЕЛЬНОМ СОСТОЯНИИ, упр. либо приостановлено либо оставновлено")


class Lane1ControlForm(aqas.BaseForm):
    """Класс, который содержит методы, используемые при проверке страницы управления первой полосой."""
    elements = Lane1ControlFormElements()

    def __init__(self):
        super().__init__(By.XPATH, "//div[contains(text(),'Управление полосой')]",
                         "Страница управления первой полосой")

    def change_busy_lane(self):
        self.elements.BUSY_LANE_RADIO.click()

    def go_shooters_menu(self):
        self.elements.SHOOTERS_MENU.state.wait_for_visible()
        self.elements.SHOOTERS_MENU.click()

    def press_play(self):
        self.elements.PLAY.click()

    def get_chosen_weapon(self):
        return self.elements.CHOSEN_WEAPON.text

    def get_chosen_ammo(self):
        return self.elements.CHOSEN_AMMO.text

    def close_chose_weapon_tab(self):
        self.elements.CLOSE_CHOSE_WEAPON_TAB.click()

    def confirm_chosen_weapon(self):
        self.elements.CONFIRM_CHOSEN_WEAPON.click()

    def press_stop(self):
        self.elements.STOP.click()

    def is_notification_invisible(self):
        return self.elements.NOTIFICATION.state.wait_for_invisible()

    def is_notifications_invisible(self):
        return self.elements.NOTIFICATIONS.state.wait_for_invisible()

    def go_exercise_menu(self):
        self.elements.EX_MENU.click()

    def go_conditions_menu(self):
        self.elements.CONDITIONS_MENU.click()
