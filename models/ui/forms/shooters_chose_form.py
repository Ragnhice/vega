import aqas
from selenium.webdriver.common.by import By

from models.ui.common_elements import CommonElements, SettingsElements, StateLaneElements


class ShootersChoseFormLocators(CommonElements, SettingsElements, StateLaneElements):
    """
    Класс, который содержит элементы, используемые при проверке появления уведомления о неуспешном сохранении
    без оружия на странице выбора стрелков.
    """

    EDIT_EXERCISE_BTN = aqas.element_factory.button(
        By.XPATH, "//a[@href='/lines/1/exercises']/div/span",
        "Открыть окно  Выбора упражнения на полосу")

    ADD_SHOOTER_BTN = aqas.element_factory.button(
        By.XPATH, ".//div[@class='section-block__content']//button",
        "Добавить стрелка")

    SHOOTER_TO_CHOSE_LIST_1_BTN = aqas.element_factory.button(
        By.XPATH, ".//div[@id='shooterId']",
        "Открыть список для выбора 1-го стрелка")

    CHOSEN_AMMO_2_DRDW = aqas.element_factory.dropdown(
        By.XPATH, "//*[@id='newAmmoId']/span",
        "Поле выбранного боеприпаса")

    CHOSEN_WEAPON_2_DRDW = aqas.element_factory.dropdown(
        By.XPATH, "//*[@id='newWeaponId']/span",
        "Поле выбранного оружия")

    ADD_WEAPON_DRDW = aqas.element_factory.button(
        By.XPATH,
        "//button[contains(text(),'добавить')]",
        "Добавить выбранное оружия")


class ShootersChoseForm(aqas.BaseForm):
    """
    Класс методов для проверки появления уведомления о неуспешном сохранении без оружия на странице выбора стрелков.
    """

    elements = ShootersChoseFormLocators()

    def __init__(self):
        super().__init__(By.XPATH, "//div[contains(text(),'Выбор стрелков на полосу 1')]",
                         "Выбор стрелков на полосу 1")

    def wait_for_notification_invisible(self):
        self.elements.NOTIFICATION_LBL.state.wait_for_invisible()

    def wait_for_notifications_invisible(self):
        self.elements.NOTIFICATIONS_LBL.state.wait_for_invisible()
