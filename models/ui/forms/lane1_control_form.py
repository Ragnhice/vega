from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from aqas.element_factory import ElementFactory
from aqas.forms.base_form import BaseForm, BaseFormElements


class Lane1ControlFormElements(BaseFormElements):
    """
    Класс, который содержит элементы, используемые при проверке управления первой полосой
    """

    BUSY_LANE_RADIO = ElementFactory.Labels(
        locator_type=By.XPATH,
        locator_value="//div[contains(@class, 'lane-head-items')]//span",
        name_prefix="Занятость полосы",
        )

    PLAY_BUTTON = ElementFactory.Button(
        By.XPATH, "//span[contains(text(),'play_arrow')]",
        "Старт упражнения")

    STOP_BUTTON = ElementFactory.Button(By.XPATH, ".//span[contains(text(),'stop')]",
                                        "Стоп упражнения")

    CHOSEN_WEAPON = ElementFactory.Button(By.XPATH, "//div[@id='weaponId']//span",
                                          "Поле выбранного оружия")

    CHOSEN_AMMO = ElementFactory.Button(By.XPATH, "//div[@id='ammoId']//span",
                                        "Поле выбранного боеприпаса")

    CLOSE_CHOSE_WEAPON_TAB = ElementFactory.Button(By.XPATH, "//span[contains(text(),'Закрыть')]",
                                                   "Закрыть выбор оружия")

    CONFIRM_CHOSEN_WEAPON = ElementFactory.Button(By.XPATH, "//span[contains(text(),'Подтвердить')]",
                                                  "Подтвердить выбор оружия")

    SHOOTERS_MENU = ElementFactory.Button(By.XPATH, "//a[@href='/lines/1/shooters']//span",
                                          "Переход к  странице выбора стрелков")

    PAUSE_BUTTON = ElementFactory.Button(
        By.XPATH, ".//span[contains(text(),'pause')]",
        "Приостановить упражнение")

    TIME = ElementFactory.Button(
        By.XPATH, ".//div[contains(text(),'Резульат')/div/div[5]/div[1]",
        "Значение времени от начала")

    CONDITIONS = ElementFactory.Button(
        By.XPATH,
        "//a[@href='/lines/1/conditions']",
        "открыть окно Выбор условий полосы 1")

    PRINT_QUICK = ElementFactory.Button(
        By.XPATH, "//a[@href='/lines/1/stats']",
        "Распечатать отчет")

    EX_MENU = ElementFactory.Button(
        By.XPATH, "//a[@href='/lines/1/exercises']//span",
        "Открыть окно Выбор упражнения на полосу 1")

    NOTIFICATION = ElementFactory.Labels(
        locator_type=By.CLASS_NAME,
        locator_value="p-toast-summary",
        name_prefix="Уведомление Полоса занята"
        )

    NOTIFICATIONS = ElementFactory.Labels(
        By.XPATH, "//div[contains(@class, 'p-toast-top-right')]",
        "Все уведомления")

    LANE_IS_FREE = ElementFactory.Labels(
        By.XPATH, "//h2[contains(text(),'свободна')]",
        "Флаг свободной полосы")

    LANE_IS_BUSY = ElementFactory.Labels(
        By.XPATH, "//h2[contains(text(),'занята')]",
        "Флаг занятой полосы")

    STOP_BUTTON_DISABLED = ElementFactory.Button(
        By.XPATH, "//button[contains(@class, 'p-disabled')]/span[contains(text(),'stop')]",
        "Кнопка остановки упражнения в НЕКЛИКАБЕЛЬНОМ СОСТОЯНИИ")

    PLAY_BUTTON_DISABLED = ElementFactory.Button(
        By.XPATH, "//button[contains(@class, 'p-disabled')]/span[contains(text(),'play_arrow')]",
        "Кнопка запуска упражнения в НЕКЛИКАБЕЛЬНОМ СОСТОЯНИИ")

    PAUSED_BUTTON_DISABLED = ElementFactory.Button(
        By.XPATH, "//button[contains(@class, 'p-disabled')]/span[contains(text(),'pause')]",
        "Кнопка паузы в НЕКЛИКАБЕЛЬНОМ СОСТОЯНИИ, упр. либо приостановлено либо оставновлено ")


class Lane1ControlForm(BaseForm):
    """
        Класс, который содержит методы, используемые при проверке страницы управления первой полосой
        """
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
        self.elements.PLAY_BUTTON.click()

    def get_chosen_weapon(self):
        return self.elements.CHOSEN_WEAPON.text

    def get_chosen_ammo(self):
        return self.elements.CHOSEN_AMMO.text

    def close_chose_weapon_tab(self):
        self.elements.CLOSE_CHOSE_WEAPON_TAB.click()

    def confirm_chosen_weapon(self):
        self.elements.CONFIRM_CHOSEN_WEAPON.click()

    def press_stop(self):
        self.elements.STOP_BUTTON.click()

    def wait_for_invisible_notification(self):
        return self.elements.NOTIFICATION.state.wait_for_invisible()

    def wait_for_invisible_notifications(self):
        return self.elements.NOTIFICATIONS.state.wait_for_invisible()

    def ex_is_playing(self):
        try:
            return self.elements.PLAY_BUTTON_DISABLED.state.wait_for_located()
        except TimeoutException:
            return False

    def ex_is_stopped(self):
        try:
            return self.elements.STOP_BUTTON_DISABLED.state.wait_for_located(timeout=3)
        except TimeoutException:
            return False

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
