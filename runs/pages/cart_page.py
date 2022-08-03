from .base.locator import Locator
from .base.base_element import BaseElement
from ._core import CoreLocators
from selenium.webdriver.common.by import By
import random


class CartPage(CoreLocators):

    url = "https://noone.ru/"
    # url_dm2 = "https://dm2.noone.ru/"

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
    Cart Page Elements
    """

    @property
    def auth_page(self):
        """
        Автормиация необходима для дальнейших тестов
        :return:
        """
        #
        locator = Locator(
            by=By.XPATH,
            value='//li[@class="nav-item nav-item-auth"]'
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def auth_email_login(self):
        # return self.XPATH('//a[@href="#modal-auth-email"]')
        return self.XPATH('//a[contains(text(), "По email")]')

    @property
    def auth_field_login(self):
        """
        Логин
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            value='//input[@name="USER_LOGIN"]'
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def auth_field_pass(self):
        """
        Пароль
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            value='//input[@name="USER_PASSWORD"]'
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def auth_field_button(self):
        """
        Пароль
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            # value='//button[@name="Login"]'
            value='//button[contains(text(), "Войти в аккаунт")]'
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def header_logo(self):
        """
                Логотип страницы
                :return:
                """
        locator = Locator(
            by=By.XPATH,
            value='//a[@class="header-logo"]'
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def logo(self):
        return self.XPATH('//a[@class="logo"]')

    @property
    def cart(self):
        """
        Кнопка корзины
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            value='//a[@class="nav-link js-basket-line"]'
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def dy_product_card(self):
        """
        Карточка товара (index 0) из списка.
        Для методов Hover и Click
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            value='//div[@data-swiper-slide-index="0"]'
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def dy_product_window(self):
        """
        Кнопка предпросмотра товара с index 0 из каталога DY
        Для метода Click
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            value='//div[@data-swiper-slide-index="0"]'
                  '//div[@class="rr-item__view"]'
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def item_buy(self):
        """
        Добавить в корзину по нажатию на открывшееся окно
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            value='//div[contains(@class, "item-checkout")]'
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )


    @property
    def item_color_block(self):
        """
        Блок выбора цвета товара
        :return:
        """
        return self.XPATH('//div[@class="select item-color-list js-item-list"]//div[@class="select-value"]')

    @property
    def item_color_element(self):
        """
        Блок выбора цвета товара
        :return:
        """
        return self.XPATH('//div[@class="select item-color-list js-item-list select-open"]//ul[@class="select-list"]/li[@class="select-item"][1]')

    @property
    def item_color_element_single(self):
        """
        Блок выбора цвета товара
        :return:
        """
        return self.XPATH('//div[@class="select item-color-list js-item-list select-open"]//ul[@class="select-list"]/li[1]')

    @property
    def item_size_block(self):
        """
        Выпадающий список обуви
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            value='//div[contains(@class, "item-size-block")]/div'
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def item_size(self, num):
        """
        Выбрать размер обуви (случайное значение)
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            value='//li[@class="select-item item-size"][{}]'.format(num)
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def item_size_single(self):
        """
        Выбрать размер обуви (случайное значение)
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            value='//li[@class="select-item item-size"]'
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def image_selection(self):
        """
        Открыть предпросмотр другого изображения из списка
        :return:
        """
        return self.XPATH('//div[@class="bootbox-body"]//ul[@class="item-thumb-list js-item-thumb-list"]/li[2]')

    @property
    def item_add(self):
        """
        Добавить в корзиру
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            value='//div[@class="item-checkout"]'
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def item_bootbox_accept(self):
        """
        Принять и закрыть уведомление
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            value='//button[contains(@class, "bootbox-accept")]'
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def item_bootbox_close(self):
        """
        Закрыть окно предпросмотра товара
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            value='//div[@class="modal-dialog modal-lg"]//button[contains(@class, "bootbox-close-button")]'
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def surname(self):
        """
        Поле ввода фамилии
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            value='//input[@name="LAST_NAME"]'
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def city_select(self):
        """
        Кнопка выбора города в способе получения
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            value='//div[contains(text(), "Способ получения")]//span[contains(@class, "form-select-dropdown")]/span'
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def city_select_element(self, city):
        """
        Вариант выбора города
        :return:
        """
        # form-select-item
        locator = Locator(
            by=By.XPATH,
            value='//div[@class="text-title-2"]//li[contains(@class, "form-select-item")][{}]'.format(city)
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def form_check_save(self):
        """
        Флажок сохранения адреса
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            value='//div[@class="order-address-service"]//label[@class="form-check"]'
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def form_address_change(self):
        """
        Кнопка "Выбрать другой" адрес
        :return:
        """
        return self.XPATH('//div[contains(text(), "Адрес доставки")]//span[contains(text(), "Выбрать другой")]')

    @property
    def form_address_select(self):
        """
        Кнопка выбора адреса из предложенного ниже
        :return:
        """
        return self.XPATH('//div[contains(@class, "text-title-3")]/../div[@class="form-card-list"]/label')

    @property
    def form_address_label_text(self):
        """
        Адрес указанный в чекбоксе
        :return:
        """
        return self.XPATH('//div[contains(text(), "Адрес доставки")]/..'
                          '/div[@class="form-card-list"]/label[2]//span[@class="form-check-label"]')

    def form_address_show_all(self):
        """
        Кнопка "показать все" в адресах
        :return:
        """
        return self.XPATH('//div[contains(text(), "Адрес доставки")]/..//span[contains(text(), "Показать все")]')

    @property
    def select_all(self):
        """
        Флажок для выбора всех товаров на странице
        :return:
        """
        return self.XPATH('//span[contains(text(), "Выбрать все")]')

    def form_info(self, info):
        """
        Ввод адреса, подъезда, этажа, кода домофона
        :param info:
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            value='//label[contains(text(), "{}")]/../input'.format(info)
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def form_continue(self):
        """
        Кнопка "Продолжить"
        :return:
        """
        return self.XPATH('//div[@class="modal-footer"]/div[contains(text(), "Продолжить")]')

    @property
    def form_delivery(self):
        """
        Выбор метода доставки
        :return:
        """
        # order-block
        locator = Locator(
            by=By.XPATH,
            value='//div[@class="order-block"]/div[@class="row row-gap-20"][1]/div[1]'
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def form_delivery_date(self):
        """
        Список даты доставки
        :return:
        """
        # row row-gap-20
        locator = Locator(
            by=By.XPATH,
            # value='//div[contains(class, "order-block")]'
            #       '/..'
            #       '/div[@class="row row-gap-20"]'
            #       '/div[@class="form-select"]'
            value='//div[contains(text(), "Дата и время доставки")]/../div[@class="row row-gap-20"]/div'
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def form_delivery_date_element(self):
        """
        Выбор даты из списка
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            value='//div[contains(text(), "Дата и время доставки")]'
                  '/..'
                  '/div[@class="row row-gap-20"]'
                  '/div'
                  '//ul[@class="form-select-list"]'
                  '/li[5]'
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def payment_method(self):
        """
        Выбор метода оплаты
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            value='//div[@class="order-step"]//span[contains(text(), "Онлайн")]'
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def order_comment_activate(self):
        """
        Комментарий для фирмы (на всякий случай)
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            value='//a[contains(text(), "Добавить комментарий к заказу")]'
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def order_comment_box(self):
        """
        Форма для комментария
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            value='//textarea[@name="COMMENTS"]'
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def promocode(self):
        """
        Поле для промокодов
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            value='//input[@id="coupon"]'
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def order_btn(self):
        """
        Кнопка оформления заказа
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            value='//div[@id="cart-checkout-button"]//button'
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def item_delete(self):
        """
        Удалить предмет из корзины
        :return:
        """
        # btn btn-action btn-delete js-item-delete
        locator = Locator(
            by=By.XPATH,
            value='//span[contains(text(), "Очистить корзину")]'
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def profile(self):
        """
        Кнопка профиля
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            value='//li[@class="nav-item nav-item-profile"]'
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def profile_personal_info(self):
        """
        Удалить заказ
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            value='//ul[@class="nav-item-dropdown"]/li[1]'
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def profile_orders(self):
        return self.XPATH('//div[@class="nav-item-dropdown"]//li[3]')

    @property
    def profile_my_orders(self):
        """
        Удалить заказ
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            value='//a[contains(text(), "Мои заказы")]'
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def profile_my_orders_open_order(self):
        """
        Удалить заказ
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            # value='//div[@class="table-body"]/div[@class="table-row js-order-row"][1]/div[contains(text(), "Новый")]'
            value='//div[contains(@class, "table-cell table-cell-status")]//text()[contains(.,"Принят")]/../../..'
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def order_delete(self):
        """
        Удалить заказ
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            # value='//a[@class="btn btn-default js-btn js-btn-order-cancel"]'
            value='//span[contains(text(), "Отменить")]'
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def order_delete_confirm(self):
        """
        Удалить заказ
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            # value='//div[@class="bootbox modal bootbox-confirm in"]//button[@class="btn btn-primary bootbox-accept"]'
            value='//div[@class="modal-footer"]/button[contains(text(), "Да")]'
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def order_post_delete_confirm(self):
        """
        Удалить заказ
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            # value='//div[@class="bootbox modal bootbox-alert in"]//button[@class="btn btn-primary bootbox-accept"]'
            value='//button[contains(@class, "btn btn-primary bootbox-accept")]'
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def close_modal_preview(self):
        return self.XPATH('//button[@class="bootbox-close-button close"]')

    @property
    def catalog_male(self):
        return self.XPATH('//span[@data-gender-target="M"]')

    @property
    def catalog_male_shoes(self):
        return self.XPATH('//ul[@class="nav-primary"]/li/a[@class="nav-link js-link-to-level2"'
                          ' and contains(text(), "Обувь")]')

    @property
    def catalog_male_bags(self):
        return self.XPATH('//ul[@class="nav-primary"]/li/a[@class="nav-link js-link-to-level2"'
                          ' and contains(text(), "Сумки")]')

    @property
    def catalog_first_item(self):
        return self.XPATH('//div[@id="catalog"]//div[@class="col lg:col-4 xs:col-6"][1]')

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
