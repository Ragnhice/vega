from selenium.webdriver.common.by import By
from aqas.element_factory import ElementFactory
from aqas.forms.base_form import BaseForm, BaseFormElements
from selenium.common import TimeoutException

class LanesControlFormElements(BaseFormElements):
    """
    Класс, который содержит элементы, используемые при проверке страницы управления полосами
    """
    LANE1 = ElementFactory.Labels(
        locator_type=By.XPATH,
        locator_value="//tbody/tr[1]/td[1]",
        name_prefix="Переход к полосе №1",
        )

    PLAY_LANE1 = ElementFactory.Button(
        By.XPATH,
        ".//span[@class='p-ml-2'][normalize-space()='1']/span[contains('play_arrow')]",
        "Запустить упражнение на полосе №1")

    STOP_LANE1 = ElementFactory.Button(
        By.XPATH, ".//span[@class='p-ml-2'][normalize-space()='1']/span[contains('stop')] ",
        "Остановить упражнение на полосе №1")

    PAUSE_LANE1 = ElementFactory.Button(
        By.XPATH, ".//span[@class='p-ml-2'][normalize-space()='1']/span[contains('pause')] ",
        "Приостановить упражнение на полосе №1")

    EDIT_LANE1 = ElementFactory.Button(
        By.XPATH, "//span[@class='p-ml-2'][normalize-space()='1']",
        "Редактирвоать 1 полосу")

    NOTIFICATIONS = ElementFactory.Labels(
        By.XPATH, "//div[contains(@class, 'p-toast-top-right')]",
        "Все уведомления")

    NOTIFICATION = ElementFactory.Labels(
        locator_type=By.CLASS_NAME,
        locator_value="p-toast-summary",
        name_prefix="Уведомление"
        )

    EDIT_LANE2 = ElementFactory.Button(
        By.XPATH, "//span[@class='p-ml-2'][normalize-space()='2']",
        "Редактирвоать 2 полосу")

    BUSY_LANE1_RADIO = ElementFactory.Labels(
        locator_type=By.XPATH,
        locator_value="//tbody/tr[1]//span[contains(text(),'vpn_key_off')]",
        name_prefix="Занятость полосы",
        )

    LANE_IS_FREE = ElementFactory.Labels(
        By.XPATH,
        "//tbody/tr[1]//div[contains(text(),'не назначен')]",
        "Флаг свободной полосы")

    LANE_IS_BUSY = ElementFactory.Labels(
        By.XPATH,
        "//tbody/tr[1]//span[contains(text(),'check_circle')]",
        "Флаг занятой полосы")

    STOP_BUTTON_DISABLED = ElementFactory.Button(
        By.XPATH,
        "//tbody/tr[1]//button[contains(@class, 'p-disabled')]/span[contains(text(),'stop')]",
        "Кнопка остановки упражнения в НЕКЛИКАБЕЛЬНОМ СОСТОЯНИИ")

    PLAY_BUTTON_DISABLED = ElementFactory.Button(
        By.XPATH,
        "//tbody/tr[1]//button[contains(@class, 'p-disabled')]/span[contains(text(),'play_arrow')]",
        "Кнопка запуска упражнения в НЕКЛИКАБЕЛЬНОМ СОСТОЯНИИ")


    PLAY_BUTTON = ElementFactory.Button(
            By.XPATH, "//tbody/tr[1]//span[contains(text(),'play_arrow')]",
            "Старт упражнения")

    STOP_BUTTON = ElementFactory.Button(By.XPATH,
                                        "//tbody/tr[1]//span[contains(text(),'stop')]",
                                            "Стоп упражнения")

    CHOSEN_WEAPON = ElementFactory.Button(By.XPATH,
                                          "//div[@id='weaponId']//span",
                                          "Поле выбранного оружия")

    CHOSEN_AMMO = ElementFactory.Button(By.XPATH,
                                        "//div[@id='ammoId']//span",
                                        "Поле выбранного боеприпаса")

    CLOSE_CHOSE_WEAPON_TAB = ElementFactory.Button(By.XPATH,
                                                   "//span[contains(text(),'Закрыть')]",
                                                   "Закрыть выбор оружия")

    CONFIRM_CHOSEN_WEAPON = ElementFactory.Button(
        By.XPATH,
        "//span[contains(text(),'Подтвердить')]",
                                                  "Подтвердить выбор оружия")

class LanesControlForm(BaseForm):
    """
        Класс, который содержит методы, используемые при проверке страницы управления полосами
        """
    elements = LanesControlFormElements()

    def __init__(self):
        super().__init__(By.XPATH,
                         "//div[contains(text(),'Управление полосами')]",
                         "Страница управления полосами")

    def go_to_lane1(self):
        self.elements.LANE1.wait_and_click()

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

    def change_busy_lane1(self):
        self.elements.BUSY_LANE1_RADIO.click()

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