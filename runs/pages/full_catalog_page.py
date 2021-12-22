from .base.locator import Locator
from .base.base_element import BaseElement
from ._core import CoreLocators
from selenium.webdriver.common.by import By


class FullCatalog(CoreLocators):

    url = "https://noone.ru/"

    """
    Priority Elements
    """

    @property
    def cookies(self):
        """
        Подтвердить кукисы
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
        Подтвердить регион
        :return:
        """
        locator = Locator(by=By.ID, value='region-confirm')
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    """
    Common Page Elements
    """

    @property
    def auth_page(self):
        return self.XPATH('//li[@class="nav-item nav-item-auth"]')

    @property
    def auth_email_login(self):
        return self.XPATH('//a[@href="#modal-auth-email"]')

    @property
    def auth_field_login(self):
        return self.XPATH('//input[@name="USER_LOGIN"]')

    @property
    def auth_field_pass(self):
        return self.XPATH('//input[@name="USER_PASSWORD"]')

    @property
    def auth_field_button(self):
        return self.XPATH('//button[@name="Login"]')

    @property
    def header_logo(self):
        return self.XPATH('//a[@class="header-logo"]')

    @property
    def logo(self):
        return self.XPATH('//a[@class="logo"]')

    """
    Main
    """

    @property
    def catalog_first_item(self):
        return self.XPATH('//div[@id="catalog"]//div[@class="col lg:col-4 xs:col-6"][1]')

    def catalog_nth_item(self, num):
        return self.XPATH('//div[@id="catalog"]//div[@class="col lg:col-4 xs:col-6"][{}]'.format(num))

    @property
    def catalog_preview_btn(self):
        return self.XPATH('//div[@class="btn-item-view js-item-view"]')

    @property
    def catalog_preview_size_select(self):
        return self.XPATH('//div[@class="bootbox modal modal-item-view in"]//ul[@class="item-size-list"]/li[1]')

    @property
    def catalog_preview_reserve(self):
        return self.XPATH('//span[contains(text(), "Наличие и резерв")]')

    @property
    def catalog_preview_reserve_boutique(self):
        return self.XPATH('//ul[@id="offer-shop-list"]/div[1]')

    @property
    def catalog_preview_reserve_reserve(self):
        return self.XPATH('//div[@class="btn btn-block btn-primary js-reserve-link"]')

    @property
    def catalog_preview_reserve_close(self):
        return self.XPATH('//div[@id="modal-offers"]//button[@class="close"]')

    @property
    def catalog_preview_add_to_cart(self):
        return self.XPATH('//a[contains(text(), "Добавить в корзину")]')

    @property
    def catalog_preview_go_to_cart(self):
        return self.XPATH('//button[@class="btn btn-primary bootbox-accept"]')

    @property
    def catalog_preview_go_to_item(self):
        return self.XPATH('//article[@id="item-details"]//a[@class="text-link"]')
