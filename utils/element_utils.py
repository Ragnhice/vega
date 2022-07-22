import aqas
from aqas.elements.base.base_element import BaseElement
from selenium.common import TimeoutException


def is_located(element: BaseElement) -> bool:
    try:
        element.state.wait_for_located(timeout=3)
        return True
    except TimeoutException:
        return False
    except Exception as error:
        aqas.logger.error(error)
        raise AssertionError from error
