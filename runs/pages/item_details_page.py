from ._core import CoreLocators

class ItemDetailsPage(CoreLocators):

    url = "https://dm1.noone.ru/catalog/muzhskoe/obuv/"

    def catalog_item(self):
        """Произвольный товар на странице каталога"""
        return self.XPATH('//div[@id="catalog-items"]/div/div[3]/a')

    def item_subscribe(self):
        return self.XPATH('//a[contains(text(), "Не нашли свой размер?")]')

    def item_size_list_item(self):
        return self.XPATH('//ul[@class="ite,-size-list"]/li[1]')

    def item_add(self):
        return self.XPATH('//span[contains(text(), "Добавить в корзину")]')

    # TODO: Добавить кнопку "Купить одним кликом" когда она будет доработана
    def item_add_1_click(self):
        return self.XPATH('')

    def item_info_extend(self):
        return self.XPATH('//p/a[contains(text(), "Показать все")]')

    def item_info_block(self):
        return self.XPATH('//div[@id="features"]')  # check for style *or* collapse in / collapse

    def item_info_delivery(self):
        return self.XPATH('//li/a[@href="#item-delivery"]')

    def item_info_city(self):
        return self.XPATH('//div[contains(text(), "Способы доставки")]//span[@class="text-link-color"]')

    def header_city(self):
        return self.XPATH('//span[@id="region-name"][1]')

    
