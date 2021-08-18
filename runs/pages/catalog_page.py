import random

from .base.locator import Locator
from .base.base_page import BasePage
from .base.base_element import BaseElement
from ._core import CoreLocators

core = CoreLocators(BasePage)
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
        :return:
        """

        return XPATH('//ul[@class="nav-gender"]//li[1]')

    @property
    def gender_select_random(self):
        """
        Категории продуктов (женская, мужская, т.д.)
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

    @property
    def button_grid_mode(self):
        """
        Кнопка смены отображения сетки товаров
        :return:
        """

        return XPATH('//div[@class="btn-view btn-view-2"]')

    def filter_category(self, num):
        """
        Фильтр категории
        :return:
        """
        return XPATH("//div[@id='block-CATEGORY']//li[{}]".format(num))

    def filter_brand(self, num):
        """
        Фильтр бренда (если доступен)
        :return:
        """
        return XPATH("//div[@id='block-BRAND']//li[{}]".format(num))

    def filter_size(self, num):
        """
        Фильтр размера (если доступен)
        :return:
        """
        return XPATH("//div[@id='block-RAZMER']//li[{}]".format(num))

