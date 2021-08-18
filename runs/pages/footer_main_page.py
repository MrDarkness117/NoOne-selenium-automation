from .base.locator import Locator
from .base.base_page import BasePage
from .base.base_element import BaseElement
from selenium.webdriver.common.by import By
from ._core import CoreLocators

core = CoreLocators(BasePage)
XPATH = core.XPATH
TEXT = core.TEXT
CLASS = core.CLASS
NAME = core.NAME
ID = core.ID


class FooterMainPage(BasePage):

    url = 'https://noone.ru'

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

    def footer_navlinks(self, val):
        """
        Элементы nav-link футера страницы
        :param val:
        :return:
        """
        return XPATH("//footer//a[@class='nav-link'][{}]".format(val))
