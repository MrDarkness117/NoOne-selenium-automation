import random

from .base.locator import Locator
from .base.base_page import BasePage
from .base.base_element import BaseElement
from selenium.webdriver.common.by import By
from ._core import CoreLocators

# core = CoreLocators(BasePage)
# XPATH = core.XPATH
# TEXT = core.TEXT
# CLASS = core.CLASS
# NAME = core.NAME
# ID = core.ID


class CatalogPage(CoreLocators):

    url = 'https://noone.ru'

    @property
    def cookies(self):
        """
        In WebDriver you always get a cookies confirm
        :return:
        """
        return self.ID('user-cookie-confirm-btn')

    @property
    def region_confirm(self):
        """
        In WebDriver you always get a region confirmation
        :return:
        """
        return self.ID('region-confirm')

    @property
    def open_filters(self):
        """
        Панели для раскрытия фильтров
        :return:
        """
        return self.XPATH('//div[@class="filter-secondary filter-panel filter-panel-collapse filter-panel-open"]/div')

    @property
    def gender_select(self):
        """
        Категории продуктов (женская, мужская, т.д.)
        :return:
        """

        return self.XPATH('//ul[@class="nav-gender"]//li[1]')

    def gender_select_random(self, num):
        """
        Категории продуктов (женская, мужская, т.д.)
        :return:
        """

        return self.XPATH('//ul[@class="nav-gender"]//li[{}]'.format(num))

    @property
    def category_select(self):
        """
        Выбор под-категории продуктов
        :return:
        """

        return self.XPATH('//ul[@class="nav-primary"]/li[1]')

    def category_select_random(self, num):
        """
        Выбор под-категории продуктов
        :return:
        """

        return self.XPATH('//ul[@class="nav-primary"]/li[{}]'.format(num))

    @property
    def button_grid_mode(self):
        """
        Кнопка смены отображения сетки товаров
        Меняет отображение div#catalog-items с .catalog-view-1 (по умолчанию) на .catalog-view-2
        :return:
        """

        return self.XPATH('//div[@id="catalog-view-toggle"]')

    def filter_category(self, num):
        """
        Фильтр категории
        :return:
        """
        return self.XPATH("//div[@id='block-CATEGORY']//li[{}]".format(num))

    def filter_brand(self, num):
        """
        Фильтр бренда (если доступен)
        :return:
        """
        return self.XPATH("//div[@id='block-BRAND']//li[{}]".format(num))

    def filter_size(self, num):
        """
        Фильтр размера (если доступен)
        :return:
        """
        return self.XPATH("//div[@id='block-RAZMER']//li[{}]".format(num))

    def filter_color(self, num):
        """
        Фильтр цвета (если доступен)
        :param num:
        :return:
        """

        return self.XPATH("//div[@id='block-COLOR_GROUP']//ul[@class='filter-list filter-list-colors']//li[{}]".format(num))

    def filter_season(self, num):
        """
        Фильтр сезонов (если доступен)
        :param num:
        :return:
        """

        return self.XPATH("//div[@id='block-SEASONALITY']//li[{}]".format(num))

    def filter_collection(self, num):
        """
        Фильтр коллекции (если доступен)
        :param num:
        :return:
        """

        return self.XPATH("//div[@id='block-COLLECTION']//li[{}]".format(num))

    def filter_model(self, num):
        """
        Фильтр моделей (если доступен)
        :param num:
        :return:
        """

        return self.XPATH("//div[@id='block-MODEL']//li[{}]".format(num))

    def filter_basic_material(self, num):
        """
        Фильтр базового материала (если доступен)
        :param num:
        :return:
        """

        return self.XPATH("//div[@id='block-BASIC_MATERIAL']//li[{}]".format(num))

    def filter_lining_material(self, num):
        """
        Фильтр материала подкладки (если доступен)
        :param num:
        :return:
        """

        return self.XPATH("//div[@id='block-LINING_MATERIAL']//li[{}]".format(num))

    def filter_group(self, num):
        """
        Фильтр группы (если доступен)
        :param num:
        :return:
        """

        return self.XPATH("//div[@id='block-GROUP_REF']//li[{}]".format(num))

    @property
    def catalog_item(self):
        """
        Товар из списка предложенных на странице
        :return:
        """
        return self.XPATH("//div[@id='catalog-items']//div[@class='col lg:col-4 xs:col-6'][1]")

    @property
    def catalog_item_fav(self):
        """
        Кнопка "Добавить в избранное"
        :return:
        """
        return self.XPATH("//div[@id='catalog-items']//div[@class='col lg:col-4 xs:col-6'][1]"
                          "//div[@class='btn btn-action btn-item-favorite js-item-favorite']")

    @property
    def item_preview(self):

        return self.XPATH('//div[@id="catalog-items"]//div[@class="col lg:col-4 xs:col-6"][1]'
                          '//div[@class="btn-item-view js-item-view"]')

    @property
    def catalog_item_add(self):
        """
        Кнопка добавления товара в корзину
        :return:
        """
        return self.XPATH(
            "//div[@id='catalog-items']"
            "//div[@class='col lg:col-4 xs:col-6'][1]"
            "//div[@class='btn btn-primary js-add-to-cart']"
        )

    @property
    def size_select(self):
        """
        Выбор размера
        :return:
        """
        return self.XPATH('//ul[@id="size-list"]/li[1]')

    @property
    def add_to_cart(self):
        """
        Кнопка добавить в корзину
        :return:
        """
        return self.ID('add-to-cart')

    @property
    def bootbox_accept(self):

        return self.CLASS(tag='button', value='btn btn-primary bootbox-accept')

    @property
    def next_page(self):
        """
        Пагинация страниц, кнопка Вперед (если есть)
        :return:
        """
        return self.XPATH(
            "//div[@class='pagination js-pagination']//ul[@class='pagination-list']//li//a[contains(text(), 'Вперед')]"
        )

    @property
    def sort_button(self):
        """
        Кнопка сортировки товаров
        :return:
        """
        return self.XPATH('//div[@class="catalog-control catalog-control-sort"]//div[@class="dropdown"]/div/span')

    @property
    def sort_option_grow(self):
        """
        Опция возрастание
        :return:
        """
        return self.XPATH('//div[@class="catalog-control catalog-control-sort"]//ul[@class="dropdown-menu-list"]//li[3]')

    @property
    def sort_option_shrink(self):
        """
        Опция возрастание
        :return:
        """
        return self.XPATH('//div[@class="catalog-control catalog-control-sort"]//ul[@class="dropdown-menu-list"]//li[4]')

    @property
    def sort_option_discount(self):
        """
        Опция возрастание
        :return:
        """
        return self.XPATH('//div[@class="catalog-control catalog-control-sort"]//ul[@class="dropdown-menu-list"]//li[5]')
