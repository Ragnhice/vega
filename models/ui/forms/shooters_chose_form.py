import aqas

from selenium.webdriver.common.by import By
from models.ui.forms.common_elements import CommonFormElements, CommonForm


class ShootersChoseFormLocators(aqas.BaseFormElements,CommonFormElements):
    """
    Класс, который содержит элементы, используемые при проверке появления уведомления о неуспешном сохранении
    без оружия на странице выбора стрелков.
    """

    CHOSEN_AMMO_2_DRDW = aqas.element_factory.dropdown(
        By.XPATH, "//*[@id='newAmmoId']/span",
        "Поле выбранного боеприпаса")

    CHOSEN_WEAPON_2_DRDW  = aqas.element_factory.dropdown(
        By.XPATH, "//*[@id='newWeaponId']/span",
        "Поле выбранного оружия")

    ADD_WEAPON_DRDW = aqas.element_factory.button(
        By.XPATH,
        "//button[contains(text(),'добавить')]",
        "Добавить выбранное оружия")

    EDIT_EXERCISE_BTN = aqas.element_factory.button(
        By.XPATH, "//a[@href='/lines/1/exercises']/div/span",
        "Открыть окно  Выбора упражнения на полосу")

    ADD_SHOOTER_BTN = aqas.element_factory.button(
        By.XPATH, ".//div[@class='section-block__content']//button",
        "Добавить стрелка")

    SHOOTER_TO_CHOSE_LIST_1_BTN = aqas.element_factory.button(
        By.XPATH, ".//div[@id='shooterId']",
        "Открыть список для выбора 1-го стрелка")

class ShootersChoseForm(aqas.BaseForm, CommonForm):
    """
    Класс методов для проверки появления уведомления о неуспешном сохранении без оружия на странице выбора стрелков.
    """
    elements = ShootersChoseFormLocators()

    def __init__(self):
        super().__init__(By.XPATH, "//div[contains(text(),'Выбор стрелков на полосу 1')]",
                         "Выбор стрелков на полосу 1")

    def get_chosen_weapon_2(self):
        return self.elements.CHOSEN_WEAPON_2_DRDW.text

    def get_chosen_ammo_2(self):
        return self.elements.CHOSEN_AMMO_2_DRDW.text

    def back_to_lane1(self):
        self.elements.BACK_BTN.click()

    def is_notification_invisible(self):
        return self.elements.NOTIFICATION_LBL.state.wait_for_invisible()

    def is_notifications_invisible(self):
        return self.elements.NOTIFICATIONS_LBL.state.wait_for_invisible()

    def change_busy_lane(self):
        self.elements.BUSY_LANE_DRDN.click()
