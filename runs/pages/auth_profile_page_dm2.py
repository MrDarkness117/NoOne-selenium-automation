from .base.locator import Locator
from .base.base_page import BasePage
from .base.base_element import BaseElement
from selenium.webdriver.common.by import By


class AuthProfilePage(BasePage):

    url = "https://oneway:eehooXi8@dm2.noone.ru/"

    def ID(self, value):
        """
        ID wrapper
        :return:
        """
        locator = Locator(by=By.ID, value='{}'.format(value))
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def XPATH(self, value):
        """
        XPATH wrapper
        :return:
        """
        locator = Locator(by=By.XPATH, value='{}'.format(value))
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def CLASS(self, tag, value):
        """
        Pseudo CLASS_NAME wrapper
        :return:
        """
        locator = Locator(by=By.XPATH, value='//{}[@class="{}"]'.format(tag, value))
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def NAME(self, value):
        """
        NAME wrapper
        :return:
        """
        locator = Locator(by=By.NAME, value='{}'.format(value))
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    def TEXT(self, tag, value, n=''):
        """
        UNSAFE XPATH text() wrapper
        Может вызвать проблемы в поиске элемента, так как используется * для поиска конкретного элемента с id.
        :param n: нужен для указания id элемента
        :param tag: нужен для указания тэгов, либо более полных указателей
        :param value: нужен для указания текста для поиска
        :return:
        """
        locator = Locator(by=By.XPATH, value='//{}[contains(text(), "{}")]{}'.format(tag, value, n))
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def cookies(self):
        """
        Запуская тест через веб-драйвер всегда выскакивает окно подтверждения Cookies
        :return:
        """
        return self.ID('user-cookie-confirm-btn')

    @property
    def region_confirm(self):
        """
        Запуская тест через веб-драйвер всегда выскакивает окно подтверждения региона
        :return:
        """
        return self.ID('region-confirm')

    @property
    def auth_page(self):
        return self.XPATH('//li[@class="nav-item nav-item-auth"]')

    @property
    def auth_field_login(self):
        """
        Логин
        :return:
        """
        return self.XPATH('//fieldset[@class="form-fields"]//input[@name="USER_LOGIN"]')

    @property
    def auth_field_pass(self):
        """
        Пароль
        :return:
        """
        return self.XPATH('//fieldset[@class="form-fields"]//input[@name="USER_PASSWORD"]')

    @property
    def auth_field_button(self):
        """
        Кнопка аутентификации
        :return:
        """
        return self.XPATH('//button[@name="Login"]')

    # Личные данные

    @property
    def foot_size(self):
        """
        Выпадающий список размеров обуви
        :return:
        """
        return self.XPATH('//select[@name="UF_PREFERRED_SIZE"]/../div[@class="form-select-value"]')

    @property
    def foot_size_el(self):
        """
        Пункт 'Выберите размер' меню размера обуви
        :return:
        """
        return self.TEXT('li', 'Выберите размер', '[1]')

    @property
    def cloth_size(self):
        """
        Выпадающий список размеров обуви
        :return:
        """
        return self.XPATH('//select[@name="UF_PREFERRED_SIZE_CL"]/../div')

    @property
    def cloth_size_el(self):
        """
        Пункт 'Выберите размер' меню размера одежды
        :return:
        """
        return self.XPATH('//select[@name="UF_PREFERRED_SIZE_CL"]/../ul/li[1]')

    @property
    def agree_terms(self):
        """
        Выпадающий список размеров обуви
        :return:
        """
        return self.ID('agree')

    @property
    def save(self):
        """
        Сохранить изменения
        :return:
        """
        return self.TEXT('button', 'Сохранить')

    @property
    def save_checkbox(self):
        """
        Чекбокс для сохранения
        :return:
        """
        return self.XPATH('//input[@id="agree"]/../span')

    @property
    def save_accept(self):
        """
        Кнопка "ОК" после сохранения
        :return:
        """
        return self.CLASS('button', 'btn btn-primary bootbox-accept')


    # Пункты меню слева

    @property
    def personal_info(self):
        """
        Раздел личных данных
        :return:
        """
        return self.TEXT('a', 'Личные данные')

    @property
    def loyalty_programme(self):
        """
        Раздел программы лояльности
        :return:
        """
        return self.TEXT('a', 'Программа лояльности')

    @property
    def change_password(self):
        """
        Раздел изменения пароля
        :return:
        """
        return self.TEXT('a', 'Изменение пароля')

    @property
    def addresses(self):
        """
        Раздел мои адреса
        :return:
        """
        return self.TEXT('a', 'Мои адреса')

    @property
    def orders(self):
        """
        Раздел мои заказы
        :return:
        """
        return self.TEXT('a', 'Мои заказы')

    @property
    def favourites(self):
        """
        Раздел избранное
        :return:
        """
        return self.TEXT('a', 'Избранное')

    @property
    def recommendations(self):
        """
        Раздел рекомендации
        :return:
        """
        return self.TEXT('a', 'Рекомендации')

    @property
    def viewed(self):
        """
        Раздел просмотренное
        :return:
        """
        return self.TEXT('a', 'Просмотренное')

    @property
    def preferred_shop(self):
        """
        Раздел 'Любимый торговый центр'
        :return:
        """
        return self.TEXT('a', 'Любимый торговый центр')

    @property
    def feedback(self):
        """
        Раздел обратная связь
        :return:
        """
        return self.TEXT('a', 'Обратная связь')

    @property
    def items_frv(self):
        """
        Первый товар в разделе избранных (если есть)
        :return:
        """
        return self.XPATH("//div[@class='item js-item']/../../div[1]")

    @property
    def hover_block(self):
        """
        Третий блок hover
        :return:
        """
        return self.XPATH('//ul[@class="item-image-nav"][1]//li[@class="item-image-nav-link"][3]')

