from .base.locator import Locator
from .base.base_page import BasePage
from .base.base_element import BaseElement
from selenium.webdriver.common.by import By
import random


class MainPage(BasePage):

    url = "https://noone.ru/"

    '''
    Static Buttons
    '''

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

    @property
    def footer_ribbon(self):
        """
        Элемент внизу экрана, который можно зкарыть
        :return:
        """
        # Ribbon-close
        locator = Locator(by=By.CLASS_NAME, value='Ribbon-close')
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
            value='//div[@data-retailrocket-markup-block="5f6c550197a52513c056be77"]'
                  '//div[@data-swiper-slide-index="0"]'
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
            value='//div[@data-retailrocket-markup-block="5f6c550197a52513c056be77"]'
                  '//div[@data-swiper-slide-index="0"]'
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

    def item_size(self, num):
        """
        Выбрать размер обуви (случайное значение)
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            value='//li[contains(@class, "item-size")][{}]'.format(random.randint(1, num))
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
            value='//li[contains(@class, "item-size")]'
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
            by=By.ID,
            value='add-to-cart'
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
    def item_info_page(self):
        """
        Открыть полную страницу товара
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            value='//a[@class="btn btn-block btn-default"]'
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def promo_banner(self):
        """
        Промо-баннер с коллекциями
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            value='//div[@class="carousel"]'
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def journal(self):
        """
        Элемент журнала NoOne
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            value='//a[contains(text(), "No one журнал")]'
                  '/..'
                  '/..'
                  '/div[@class="carousel"]//li[contains(@class, "carousel-item")][1]'

        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    """
    Шапка сайта
    """

    @property
    def city_menu(self):
        """
        Элемент выбора города
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            value='//li[@class="nav-item nav-item-region"]'
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def city_selector(self, code='77000000000'):
        """
        Города, предлагаемые на выбор
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            value='//li[@data-code="{}"]'.format(code)
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
    def logo_basket(self):
        """
        Логотип страницы
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            value='//a[@class="logo"]'
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )


    @property
    def auth_link(self):
        """
        Кнопка авторизации
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            value='//li[@class="nav-item nav-item-auth"]'
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def search_input(self):
        """
        Поле ввода для поиска
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            value='//input[@id="search-input"]'
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def search_btn(self):
        """
        Кнопка для поиска
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            value='//form[@class="search-form"]//button[@class="btn"]'
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

    def gender_select(self, num):
        """
        Категории продуктов (женская, мужская, т.д.)
        :param num:
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            value='//ul[@class="nav-gender"]//li[{}]'.format(num)
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def category_select(self, num):
        """
        Выбор под-категории продуктов
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            value='//ul[@class="nav-primary"]/li[{}]'.format(num)
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )
