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
        Меняет отображение div#catalog-items с .catalog-view-1 (по умолчанию) на .catalog-view-2
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

    def filter_color(self, num):
        """
        Фильтр цвета (если доступен)
        :param num:
        :return:
        """

        return XPATH("//div[@id='block-COLOR_GROUP']//ul[@class='filter-list filter-list-colors']//li[{}]".format(num))

    def filter_season(self, num):
        """
        Фильтр сезонов (если доступен)
        :param num:
        :return:
        """

        return XPATH("//div[@id='block-SEASONALITY']//li[{}]".format(num))

    def filter_collection(self, num):
        """
        Фильтр коллекции (если доступен)
        :param num:
        :return:
        """

        return XPATH("//div[@id='block-COLLECTION']//li[{}]".format(num))

    def filter_model(self, num):
        """
        Фильтр моделей (если доступен)
        :param num:
        :return:
        """

        return XPATH("//div[@id='block-MODEL']//li[{}]".format(num))

    def filter_basic_material(self, num):
        """
        Фильтр базового материала (если доступен)
        :param num:
        :return:
        """

        return XPATH("//div[@id='block-BASIC_MATERIAL']//li[{}]".format(num))

    def filter_lining_material(self, num):
        """
        Фильтр материала подкладки (если доступен)
        :param num:
        :return:
        """

        return XPATH("//div[@id='block-LINING_MATERIAL']//li[{}]".format(num))

    def filter_group(self, num):
        """
        Фильтр группы (если доступен)
        :param num:
        :return:
        """

        return XPATH("//div[@id='block-GROUP_REF']//li[{}]".format(num))


