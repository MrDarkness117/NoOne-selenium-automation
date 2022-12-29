from .base.locator import Locator
from .base.base_element import BaseElement
from ._core import CoreLocators
from selenium.webdriver.common.by import By


class PDBSmokePage(CoreLocators):

    def __init__(self, driver):
        url = "https://principedibologna.it/?ignore-country=true"
        super().__init__(driver, url=url)

    @property
    def change_country(self):
        return self.XPATH('//span[@class="header__toolbar-link header__lang-link js-country-modal-open"]')

    @property
    def select_country(self):
        return self.XPATH('//div[contains(@class, "country-name") and contains(text(), "Belgium")]')

    @property
    def auth_button(self):
        return self.XPATH('//div[@class="header__user"]')

    @property
    def auth_email(self):
        return self.XPATH('//div[@id="sign-in-form"]//input[@placeholder="E-mail"]')

    @property
    def auth_password(self):
        return self.XPATH('//div[@id="sign-in-form"]//input[@placeholder="Password"]')

    @property
    def auth_sign_in(self):
        return self.XPATH('//div[@id="sign-in-btn"]')

    @property
    def catalog_button(self):
        return self.XPATH('//span[contains(text(), "Catalog")]')

    @property
    def catalog_item(self):
        # TODO: Взять цену, сверить с чекаутом
        return self.XPATH('//a[@class="catalog-item"][1]')

    @property
    def item_size(self):
        return self.XPATH('//li[contains(@class, "sizes-list__link")][1]')

    @property
    def add_to_cart(self):
        return self.XPATH('//button[@class="add-to-cart js-add-to-cart"]')

    @property
    def item_price(self):
        return self.XPATH('//div[@class="product-info__price"]')

    @property
    def cart_button(self):
        return self.XPATH('//div[@class="header__cart"]')

    @property
    def input_phone(self):
        return self.XPATH('//input[@placeholder="Phone"]')

    @property
    def input_name(self):
        return self.XPATH('//input[@placeholder="Name"]')

    @property
    def input_surname(self):
        return self.XPATH('//input[@placeholder="Surname"]')

    @property
    def input_city(self):
        return self.XPATH('//input[@placeholder="City"]')

    @property
    def input_state(self):
        return self.XPATH('//input[@placeholder="State"]')

    @property
    def input_address(self):
        return self.XPATH('//input[@placeholder="Address"]')

    @property
    def input_postal_code(self):
        return self.XPATH('//input[@placeholder="Postal or zip code"]')

    @property
    def price_total(self):
        return self.XPATH('//dl[@class="cart-price cart-price__total"]/dd')

    @property
    def delivery_cost(self):
        return self.XPATH('//dl[@class="cart-price"]/dd')

    def cart_item(self, n):
        return self.XPATH(f'//div[@class="cart-item"][{n}]')

    def cart_item_price(self, n):
        return self.XPATH(f'//div[@class="cart-item"][{n}]//div[@class="cart-item__price--new"]')

    def payment_button(self):
        return self.XPATH('//div[@class="btn btn-block btn-primary"]')

    def item_count(self):
        return self.XPATH('//input[@class="cart-item__quantity--input"]')

