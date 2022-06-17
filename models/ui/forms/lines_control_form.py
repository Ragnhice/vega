from selenium.webdriver.common.by import By
from aqas.element_factory import ElementFactory
from aqas.forms.base_form import BaseForm, BaseFormElements


class LinesControlFormElements(BaseFormElements):
    """
    Класс, который содержит элементы, используемые при проверке страницы управления полосами
    """
    LINE1 = ElementFactory.Labels(
        locator_type=By.XPATH,
        locator_value="//tbody/tr[1]/td[1]",
        name_prefix="Переход к полосе №1",
        )

    PLAY_LINE1 = ElementFactory.Button(
        By.XPATH, ".//span[@class='p-ml-2'][normalize-space()='1']/span[contains('play_arrow')]",
        "Запустить упражнение на полосе №1")

    STOP_LINE1 = ElementFactory.Button(
        By.XPATH, ".//span[@class='p-ml-2'][normalize-space()='1']/span[contains('stop')] ",
        "Остановить упражнение на полосе №1")

    PAUSE_LINE1 = ElementFactory.Button(
        By.XPATH, ".//span[@class='p-ml-2'][normalize-space()='1']/span[contains('pause')] ",
        "Приостановить упражнение на полосе №1")

    EDIT_LINE1 = ElementFactory.Button(
        By.XPATH, "//span[@class='p-ml-2'][normalize-space()='1']",
        "Редактирвоать 1 полосу")

    NOTIFICATIONS = ElementFactory.Labels(
        By.XPATH, "//div[contains(@class, 'p-toast-top-right')]",
        "Все уведомления")

    EDIT_LINE2 = ElementFactory.Button(
        By.XPATH, "//span[@class='p-ml-2'][normalize-space()='2']",
        "Редактирвоать 2 полосу")


class LinesControlForm(BaseForm):
    """
        Класс, который содержит методы, используемые при проверке страницы управления полосами
        """
    elements = LinesControlFormElements()

    def __init__(self):
        super().__init__(By.XPATH,
                         "//div[contains(text(),'Управление полосами')]",
                         "Страница управления полосами")

    def go_to_line1(self):
        self.elements.LINE1.wait_and_click()

    def wait_for_invisible_notifications(self):
        return self.elements.NOTIFICATIONS.state.wait_for_invisible()
