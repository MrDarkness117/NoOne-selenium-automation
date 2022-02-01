from .base.locator import Locator
from .base.base_element import BaseElement
from ._core import CoreLocators
from selenium.webdriver.common.by import By


class ItemIDPage(CoreLocators):

    url = 'https://noone.ru/catalog/'

    """
    Common Elements
    """

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

    """
    Item Search Elements
    """

    @property
    def search_field(self):
        """
        Строка поиска по каталогу
        :return:
        """
        return self.XPATH('//input[@id="search-input"]')

    @property
    def first_item(self):
        """
        Первый и единственный товар для данной реализации
        :return:
        """
        return self.XPATH('//div[@class="digi-products-grid digi-products-grid_horde"]/div')

    @property
    def search_submit(self):
        """
        Кнопка запроса поиска
        :return:
        """
        return self.XPATH('//span[@id="search-form"]//button')

    @property
    def item_page_sizes(self):
        return self.XPATH('//div[@class="item-info"]/ul[@class="item-size-list"]')

    @property
    def item_page_size(self):
        return self.XPATH('//div[@class="item-info"]/ul[@class="item-size-list"]/li[1]')

    @property
    def item_page_color_list(self):
        return self.XPATH('//div[@class="item-info"]/ul[@class="item-color-list"]')

    @property
    def item_page_color_option(self):
        return self.XPATH('//div[@class="item-info"]/ul[@class="item-color-list/li[1]"]')

    @property
    def item_page_add_to_cart(self):
        return self.XPATH('//span[contains(text(), "Добавить в корзину")]')

    @property
    def item_page_modal_size_list_item(self):
        return self.XPATH('//ul[@class="item-size-list js-item-size-list"]/li[1]')

    @property
    def item_page_preview_reserve(self):
        return self.XPATH('//span[contains(text(), "Наличие и резерв")]')

    @property
    def item_page_preview_reserve_boutique(self):
        return self.XPATH('//ul[@id="offer-shop-list"]/div[1]')

    @property
    def item_page_preview_reserve_reserve(self):
        return self.XPATH('//div[@class="btn btn-block btn-primary js-reserve-link"]')

    @property
    def item_page_preview_reserve_close(self):
        return self.XPATH('//div[@id="modal-offers"]//button[@class="close"]')
