from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from aqas.element_factory import ElementFactory
from aqas.forms.base_form import BaseForm, BaseFormElements


class ShootersChoseFormLocators(BaseFormElements):
    """
    Класс, который содержит элементы, используемые при проверке появления уведомления о неуспешном сохранении без оружия на
    странице выбора стрелков
    """

    CHOSEN_AMMO_2 = ElementFactory.Button(
        By.XPATH, "//*[@id='newAmmoId']/span",
        "Поле выбранного боеприпаса")

    CHOSEN_WEAPON_2 = ElementFactory.Button(
        By.XPATH, "//*[@id='newWeaponId']/span",
        "Поле выбранного оружия")

    ADD_WEAPON_BUTTON = ElementFactory.Button(By.XPATH, "//button[contains(text(),'добавить')]",
                                              "Добавить выбранное оружия")

    EDIT_EXERCISE = ElementFactory.Button(
        By.XPATH, "//a[@href='/lines/1/exercises']/div/span",
        "Открыть окно  Выбора упражнения на полосу")

    BACK_BUTTON = ElementFactory.Button(
        By.XPATH, "//a[@href='/lines/1']",
        "Стрелка - Врнуться назад")

    ADD_SHOOTER = ElementFactory.Button(
        By.XPATH, ".//div[@class='section-block__content']//button",
        "Добавить стрелка")

    SHOOTER_TO_CHOSE_LIST_1 = ElementFactory.Button(
        By.XPATH, ".//div[@id='shooterId']",
        "Открыть список для выбора 1-го стрелка")

    NOTIFICATIONS = ElementFactory.Labels(
        By.XPATH, "//div[contains(@class, 'p-toast-top-right')]",
        "Все уведомления")

    NOTIFICATION = ElementFactory.Labels(
        locator_type=By.CLASS_NAME,
        locator_value="p-toast-summary",
        name_prefix="Уведомление"
        )

    LANE_IS_FREE = ElementFactory.Labels(
        By.XPATH, "//h2[contains(text(),'свободна')]",
        "Флаг свободной полосы")

    LANE_IS_BUSY = ElementFactory.Labels(
        By.XPATH, "//h2[contains(text(),'занята')]",
        "Флаг занятой полосы")

    BUSY_LANE_RADIO = ElementFactory.Labels(
        locator_type=By.XPATH,
        locator_value="//div[contains(@class, 'lane-head-items')]//span",
        name_prefix="Занятость полосы",
        )

class ShootersChoseForm(BaseForm):
    """Класс методов для проверки появления уведомления о неуспешном сохранении без оружия на
    странице выбора стрелков"""
    elements = ShootersChoseFormLocators()

    def __init__(self):
        super().__init__(By.XPATH, "//div[contains(text(),'Выбор стрелков на полосу 1')]",
                         "Выбор стрелков на полосу 1")

    def get_chosen_weapon_2(self):
        return self.elements.CHOSEN_WEAPON_2.text

    def get_chosen_ammo_2(self):
        return self.elements.CHOSEN_AMMO_2.text

    def back_to_lane1(self):
        self.elements.BACK_BUTTON.click()

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