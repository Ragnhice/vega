import aqas
from selenium.webdriver.common.by import By
from models.ui.forms.common_elements import CommonFormElements, CommonForm


class Lane1ControlFormElements(aqas.BaseFormElements,CommonFormElements):
    """Класс, который содержит элементы, используемые при проверке управления первой полосой."""

    CHOSEN_WEAPON_LBL = aqas.element_factory.label(
        By.XPATH, "//div[@id='weaponId']//span",
        "Поле выбранного оружия")

    CHOSEN_AMMO_LBL = aqas.element_factory.label(
        By.XPATH, "//div[@id='ammoId']//span",
        "Поле выбранного боеприпаса")

    CLOSE_CHOSE_WEAPON_BTN = aqas.element_factory.button(
        By.XPATH, "//span[contains(text(),'Закрыть')]",
        "Закрыть выбор оружия")

    CONFIRM_CHOSEN_WEAPON_BTN = aqas.element_factory.button(
        By.XPATH, "//span[contains(text(),'Подтвердить')]",
        "Подтвердить выбор оружия")

    TIME_LBL = aqas.element_factory.label(
        By.XPATH, ".//div[contains(text(),'Резульат')/div/div[5]/div[1]",
        "Значение времени от начала")

    PRINT_QUICK_BTN = aqas.element_factory.button(
        By.XPATH, "//a[@href='/lines/1/stats']",
        "Распечатать отчет")

    STOP_DISABLED_LBL = aqas.element_factory.label(
        By.XPATH, "//button[contains(@class, 'p-disabled')]/span[contains(text(),'stop')]",
        "Кнопка остановки упражнения в НЕКЛИКАБЕЛЬНОМ СОСТОЯНИИ")

    PLAY_DISABLED_LBL = aqas.element_factory.label(
        By.XPATH, "//button[contains(@class, 'p-disabled')]/span[contains(text(),'play_arrow')]",
        "Кнопка запуска упражнения в НЕКЛИКАБЕЛЬНОМ СОСТОЯНИИ")

    PAUSE_DISABLED_LBL = aqas.element_factory.label(
        By.XPATH, "//button[contains(@class, 'p-disabled')]/span[contains(text(),'pause')]",
        "Кнопка паузы в НЕКЛИКАБЕЛЬНОМ СОСТОЯНИИ, упр. либо приостановлено либо оставновлено")


class Lane1ControlForm(aqas.BaseForm, CommonForm):
    """Класс, который содержит методы, используемые при проверке страницы управления первой полосой."""
    elements = Lane1ControlFormElements()

    def __init__(self):
        super().__init__(By.XPATH, "//div[contains(text(),'Управление полосой')]",
                         "Страница управления первой полосой")

    def change_busy_lane(self):
        self.elements.BUSY_LANE_BTN.click()

    def go_shooters_menu(self):
        self.elements.SHOOTERS_MENU_BTN.state.wait_for_visible()
        self.elements.SHOOTERS_MENU_BTN.click()

    def press_play(self):
        self.elements.PLAY_BTN.click()

    def get_chosen_weapon(self):
        return self.elements.CHOSEN_WEAPON_LBL.text

    def get_chosen_ammo(self):
        return self.elements.CHOSEN_AMMO_LBL.text

    def close_chose_weapon_tab(self):
        self.elements.CLOSE_CHOSE_WEAPON_BTN.click()

    def confirm_chosen_weapon(self):
        self.elements.CONFIRM_CHOSEN_WEAPON_BTN.click()

    def press_stop(self):
        self.elements.STOP_BTN.click()

    def go_exercise_menu(self):
        self.elements.EX_MENU_BTN.click()

    def go_conditions_menu(self):
        self.elements.CONDITIONS_MENU_BTN.click()
