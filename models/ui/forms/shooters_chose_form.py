import aqas

from selenium.webdriver.common.by import By


class ShootersChoseFormLocators(aqas.BaseFormElements):
    """
    Класс, который содержит элементы, используемые при проверке появления уведомления о неуспешном сохранении
    без оружия на странице выбора стрелков.
    """

    CHOSEN_AMMO_2 = aqas.element_factory.button(
        By.XPATH, "//*[@id='newAmmoId']/span",
        "Поле выбранного боеприпаса")

    CHOSEN_WEAPON_2 = aqas.element_factory.button(
        By.XPATH, "//*[@id='newWeaponId']/span",
        "Поле выбранного оружия")

    ADD_WEAPON = aqas.element_factory.button(
        By.XPATH,
        "//button[contains(text(),'добавить')]",
        "Добавить выбранное оружия")

    EDIT_EXERCISE = aqas.element_factory.button(
        By.XPATH, "//a[@href='/lines/1/exercises']/div/span",
        "Открыть окно  Выбора упражнения на полосу")

    BACK = aqas.element_factory.button(
        By.XPATH, "//a[@href='/lines/1']",
        "Стрелка - Врнуться назад")

    ADD_SHOOTER = aqas.element_factory.button(
        By.XPATH, ".//div[@class='section-block__content']//button",
        "Добавить стрелка")

    SHOOTER_TO_CHOSE_LIST_1 = aqas.element_factory.button(
        By.XPATH, ".//div[@id='shooterId']",
        "Открыть список для выбора 1-го стрелка")

    NOTIFICATIONS = aqas.element_factory.label(
        By.XPATH, "//div[contains(@class, 'p-toast-top-right')]",
        "Все уведомления")

    NOTIFICATION = aqas.element_factory.label(
        By.CLASS_NAME, "p-toast-summary",
        "Уведомление")

    LANE_IS_FREE = aqas.element_factory.label(
        By.XPATH, "//h2[contains(text(),'свободна')]",
        "Флаг свободной полосы")

    LANE_IS_BUSY = aqas.element_factory.label(
        By.XPATH, "//h2[contains(text(),'занята')]",
        "Флаг занятой полосы")

    BUSY_LANE_RADIO = aqas.element_factory.label(
        By.XPATH, "//div[contains(@class, 'lane-head-items')]//span",
        "Занятость полосы")


class ShootersChoseForm(aqas.BaseForm):
    """
    Класс методов для проверки появления уведомления о неуспешном сохранении без оружия на странице выбора стрелков.
    """
    elements = ShootersChoseFormLocators()

    def __init__(self):
        super().__init__(By.XPATH, "//div[contains(text(),'Выбор стрелков на полосу 1')]",
                         "Выбор стрелков на полосу 1")

    def get_chosen_weapon_2(self):
        return self.elements.CHOSEN_WEAPON_2.text

    def get_chosen_ammo_2(self):
        return self.elements.CHOSEN_AMMO_2.text

    def back_to_lane1(self):
        self.elements.BACK.click()

    def is_notification_invisible(self):
        return self.elements.NOTIFICATION.state.wait_for_invisible()

    def is_notifications_invisible(self):
        return self.elements.NOTIFICATIONS.state.wait_for_invisible()

    def change_busy_lane(self):
        self.elements.BUSY_LANE_RADIO.click()
