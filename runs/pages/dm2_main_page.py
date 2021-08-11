from .base.locator import Locator
from .base.base_page import BasePage
from .base.base_element import BaseElement
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    url = "https://oneway:eehooXi8@dm2.noone.ru/"

    '''
    Static Buttons
    '''

    def _ID(self, func):
        """
        ID wrapper
        :return:
        """
        locator = Locator(by=By.ID, value='{}'.format(func))
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def _XPATH(self, func):
        """
        XPATH wrapper
        :return:
        """
        locator = Locator(by=By.XPATH, value='{}'.format(func))
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def _CLASS(self, func):
        """
        CLASS_NAME wrapper
        :return:
        """
        locator = Locator(by=By.CLASS_NAME, value='{}'.format(func))
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def region_confirm(self):
        """
        In WebDriver you always get a region confirmation
        :return:
        """
        locator = Locator(by=By.ID, value='region-confirm')
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def cookies(self):
        return self._ID('cookies-confirm')
