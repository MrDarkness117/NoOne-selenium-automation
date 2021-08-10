from .base.locator import Locator
from .base.base_page import BasePage
from .base.base_element import BaseElement
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    url = "https://oneway:eehooXi8@dm2.noone.ru/"

    '''
    Static Buttons
    '''

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
