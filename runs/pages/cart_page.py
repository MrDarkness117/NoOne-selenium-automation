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
        Автормзация необходима для дальнейших тестов
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
    def auth_field_login(self):
        """
        Логин
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            value='//fieldset[@class="form-fields"]//input[@name="USER_LOGIN"]'
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
            value='//fieldset[@class="form-fields"]//input[@name="USER_PASSWORD"]'
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
            value='//button[@name="Login"]'
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def logo(self):
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
            value='//div[contains(text(), "Способ получения")]//span[contains(@class, "form-select-dropdown")]'
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

    def item_delete(self, num):
        """
        Удалить предмет из корзины
        :return:
        """
        # btn btn-action btn-delete js-item-delete
        locator = Locator(
            by=By.XPATH,
            value='//button[contains(@class, "btn btn-action btn-delete js-item-delete")][{}]'.format(num)
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
            # value='//div[@class="table-row js-order-row"][1]//div[@class="table-cell table-cell-action text-right"]'
            #       '/span[@class="btn-collapse"]'
            value='//div[@class="table-body"]/div[@class="table-row js-order-row"][1]/div[contains(text(), "Новый")]'
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
            value='//a[@class="btn btn-default js-btn js-btn-order-cancel"]'
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
            value='//div[@class="bootbox modal bootbox-confirm in"]//button[@class="btn btn-primary bootbox-accept"]'
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
            value='//div[@class="bootbox modal bootbox-alert in"]//button[@class="btn btn-primary bootbox-accept"]'
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )


