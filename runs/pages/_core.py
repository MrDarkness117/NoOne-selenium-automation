from .base.locator import Locator
from .base.base_page import BasePage
from .base.base_element import BaseElement
from selenium.webdriver.common.by import By


class CoreLocators(BasePage):

    def __init__(self, driver, url='https://noone.ru'):
        super().__init__(driver)
        self.url = url

    def ID(self, value):
        """
        ID wrapper
        :return:
        """
        locator = Locator(by=By.ID, value='{}'.format(value))
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def XPATH(self, value):
        """
        XPATH wrapper
        :return:
        """
        locator = Locator(by=By.XPATH, value='{}'.format(value))
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def CLASS(self, value, tag='*'):
        """
        Pseudo CLASS_NAME wrapper
        :param tag: нужен для указания тэгов, либо более полных указателей
        :param value: нужен для указания полного класса для поиска
        :return:
        """
        locator = Locator(by=By.XPATH, value='//{}[@class="{}"]'.format(tag, value))
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def NAME(self, value):
        """
        NAME wrapper
        :return:
        """
        locator = Locator(by=By.NAME, value='{}'.format(value))
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def TEXT(self, tag, value, n=''):
        """
        UNSAFE XPATH text() wrapper
        Может вызвать проблемы в поиске элемента, так как используется * для поиска конкретного элемента с id.
        :param n: нужен для указания id элемента
        :param tag: нужен для указания тэгов, либо более полных указателей
        :param value: нужен для указания текста для поиска
        :return:
        """
        locator = Locator(by=By.XPATH, value='//{}[contains(text(), "{}")]{}'.format(tag, value, n))
        return BaseElement(
            driver=self.driver,
            locator=locator
        )
