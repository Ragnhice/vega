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
