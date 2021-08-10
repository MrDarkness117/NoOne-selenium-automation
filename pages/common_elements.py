from .base.locator import Locator
from .base.base_page import BasePage
from .base.base_element import BaseElement
from selenium.webdriver.common.by import By


class CommonElements(BasePage):

    # url = "https://noone.ru/"

    @property
    def cookies(self):
        """
        In WebDriver you always get a cookies confirm
        :return:
        """
        locator = Locator(by=By.ID, value='user-cookie-confirm-btn')
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
    def subscribe(self):
        """
        In WebDriver you always get a region confirmation
        :return:
        """
        locator = Locator(by=By.ID, value='fl-513145')
        return BaseElement(
            driver=self.driver,
            locator=locator
        )
