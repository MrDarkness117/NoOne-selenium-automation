import random

from .base.locator import Locator
from .base.base_page import BasePage
from .base.base_element import BaseElement
from selenium.webdriver.common.by import By
from ._core import CoreElems

core = CoreElems(BasePage)
XPATH = core.XPATH
TEXT = core.TEXT
CLASS = core.CLASS
NAME = core.NAME
ID = core.ID


class CatalogPage(BasePage):

    url = 'https://noone.ru'

    @property
    def gender_select(self):
        """
        Категории продуктов (женская, мужская, т.д.)
        :param num:
        :return:
        """

        return XPATH('//ul[@class="nav-gender"]//li[1]')

    @property
    def gender_select_random(self):
        """
        Категории продуктов (женская, мужская, т.д.)
        :param num:
        :return:
        """

        return XPATH('//ul[@class="nav-gender"]//li[{}]'.format(random.randrange(len('//ul[@class="nav-gender"]//li'))))

    @property
    def category_select(self):
        """
        Выбор под-категории продуктов
        :return:
        """

        return XPATH('//ul[@class="nav-primary"]/li[1]')

    @property
    def category_select_random(self):
        """
        Выбор под-категории продуктов
        :return:
        """

        return XPATH('//ul[@class="nav-primary"]/li[{}]'.format(random.randrange(len('//ul[@class="nav-primary"]//li'))))
