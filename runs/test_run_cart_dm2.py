import random
import time
import datetime
from pytest import mark
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from runs.pages.cart_page_dm2 import CartPage
from runs.pages.base.logging_report import Logging, LogReport, TakeScreenshot

logging = Logging()
log = logging.logger


@mark.usefixtures('driver_init_cart')
class RunCartDM2(object):

    # Настройки

    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.set_window_position(-2000, 0)
    driver.maximize_window()
    driver.implicitly_wait(3)

    # Запуск

    noone = CartPage(driver=driver)
    noone.go()
    url = driver.current_url

    def test_run(self):

        log(test_start + "Время: {}".format(str(datetime.datetime.now())))

        try:
            # Стандартные действия
            try:
                self.noone.region_confirm.click()
                self.noone.cookies.click()
            except Exception as e:
                log("=" * 5 + "Ошибка покиска элементов: \n{}".format(e))

            # Действия Cart Page
            self.auth()
            self.auth_fields()
            self.logo()
            self.cart_click()
            self.product_recommended_hover()  # Отличается от стабильной версии
            # self.preview_click()  # эти действия не нужны в случае dm2
            # self.item_size_block_click()
            # self.item_size_click()
            # self.item_add_click()
            # self.accept_click()
            self.surname_enter()
            self.city_select_click()
            self.city_select_element_click()
            self.form_check_deselect()
            self.form_info()
            self.delivery_click()
            self.delivery_date_click()
            self.delivery_date_select_click()
            self.payment_method_click()
            self.order_comment_click()
            self.order_comment_text()
            self.order_btn()
            self.cancel_order()
        except Exception as e:
            log("/" * 10 + "ОШИБКА: Во время работы произошёл сбой!" + "\\" * 10 + "\nОшибка: {}".format(str(e)))
            TakeScreenshot(RunCartDM2()).take_screenshot()

        log("="*5 + "Завершение тестирования.")

        self.driver.quit()
        LogReport(testblock=RunCartDM2(), logs=logging.log).test_results()

    # Команды

    def auth(self):
        self.noone.auth_page.click()
        log("Открыть окно авторизации")

    def auth_fields(self):
        auth_info = {
            'login': 'm.romantsov@noone.ru',
            'password': 'qK4%j8Wqy*'
        }
        self.noone.auth_field_login.input_text(auth_info['login'])
        self.noone.auth_field_pass.input_text(auth_info['password'])
        self.noone.auth_field_button.click()
        log("Ввести логин/пароль, нажать 'войти'")

    def logo(self):
        self.noone.logo.click()
        log("Перейти по логотипу на главную страницу")

    def cart_click(self):
        self.noone.cart.click()
        log("Нажать на кнопку корзины товаров")

    def product_recommended_hover(self):
        try:
            log('='*5 + "Проверка наличия товаров в корзине. Удаляем товары если есть.")
            self.noone.item_delete(1).click()
        except:
            # self.cart_click()
            log("=" * 5 + "DM2: Нет рекомендаций на странице, добавить товары самостоятально.")
            self.noone.go_back()
            self.driver.find_element_by_xpath('//ul[contains(@class, "nav-primary") and contains(@data-gender, "F")]/li[1]').click()
            self.noone.alt_buy_item_hover.hover_center()
            self.driver.find_element_by_xpath('//div[@class="btn btn-primary js-add-to-cart"]').click()
            self.driver.find_element_by_xpath('//ul[@id="size-list"]/li[1]').click()
            self.driver.find_element_by_xpath('//div[@id="add-to-cart"]').click()
            self.driver.find_element_by_xpath('//button[@class="btn btn-primary bootbox-accept"]').click()
            self.noone.cart.click()

    def preview_click(self):
        log("Нажать на появишвуюся кнопку предварительного просмотра товара")
        self.noone.dy_product_window.click()

    def item_color_block(self):
        log("Нажать на окно выбора цвета товара")
        self.noone.item_color_block.click()

    def item_color_element(self):
        """
        Всегда выбирает неактивный элемент. Если это невозможно, то выбирает первый элемет из списка.
        :return:
        """
        try:
            log("Выбрать цвет с без класса .is-active")
            self.noone.item_color_element.click()
        except Exception as e:
            log("=" * 5 + "Не найдено более одного варианта, выбираю единственный возможный")
            self.noone.item_color_element_single.click()

    def item_size_block_click(self):
        log("Нажать на окно размеров")
        self.noone.item_size_block.click()

    def item_size_click(self):
        try:
            random_size = random.randint(1, len(self.driver.find_elements_by_xpath(
                '//div[@class="select item-size-list js-item-size-list select-open"]'
                '//ul[@class="select-list"]'
                '//li[@class="select-item item-size"]'
            )))
            log("Выбрать случайный размер - size-id: {}".format(random_size))
            self.noone.item_size(random_size).click()
        except:
            log("=" * 5 + "Доступен только один размер, выбираю")
            self.noone.item_size_single.click()

    def item_add_click(self):
        log("Нажать на 'добавить в корзину'")
        self.noone.item_add.click()

    def accept_click(self):
        log("Нажать на 'Перейти в корзину'")
        self.noone.item_bootbox_accept.click()

    def surname_enter(self):
        text = "Романцов"
        log("Ввести фамилию ({})".format(text))
        self.noone.surname.input_text(text)

    def city_select_click(self):
        log("Кнопка выбора города")
        self.noone.city_select.click()

    def city_select_element_click(self):
        city = '1'  # г Москва
        log("Выбрать первый из выпадающего списка город (г Москва)")
        self.noone.city_select_element(city).click()

    def form_check_deselect(self):
        log("Отключить чек-бокс \"Запомнить адрес\". Автоматическая проверка состояния чекбокса:")
        checkbox_test = self.driver.execute_script("document.querySelector('.form-check-input').checked")
        if str(checkbox_test) != 'false':
            self.noone.form_check_save.click()
            log('='*5 + "Чекбокс не был отключен.")
        else:
            log('='*5 + "Чекбокс уже отключен.")

    def form_info(self):
        # if self.noone.form_info("Улица и дом").text != 'г Москва, ул Профсоюзная, д 37':
        #     self.driver.find_elements_by_xpath('//ul[@class="form-autocomplete-list"]/li[1]').click()
        log("Заполнить информацию адреса доставки")
        self.noone.form_info("Квартира").input_text('43')
        self.noone.form_info("Подъезд").input_text('3')
        self.noone.form_info("Этаж").input_text('1')
        self.noone.form_info("Код домофона").input_text('43к0000')
        self.noone.form_info("Улица и дом").click()
        self.noone.form_info("Улица и дом").hover_center_and_click()
        self.noone.form_info("Улица и дом").input_text('г Москва, ')
        time.sleep(1)
        self.noone.form_info("Улица и дом").input_text('ул Профсоюзная, ')
        time.sleep(1)
        self.noone.form_info("Улица и дом").input_text('д 37')
        time.sleep(3)
        self.driver.find_element_by_xpath('//div[@class="form-group form-autocomplete"]'
                                          '//li[1]').click()

    def delivery_click(self):
        log("Выбрать метод доставки")
        self.noone.form_delivery.click()

    def delivery_date_click(self):
        log("=" * 5 + "Выбираем дату доставки")
        try:
            self.noone.form_delivery_date().click()
            log("Нажать на выбор даты доставки")
        except:
            log("/"*10 + "ВНИМАНИЕ: Кнопка выбора даты отсутствует!" + '\\'*10)

    def delivery_date_select_click(self):
        try:
            log("Выбрать дату доставки")
            self.noone.form_delivery_date_element()
        except:
            log("/"*10 + "ВНИМАНИЕ: Выбрать дату невозможно" + '\\'*10)

    def payment_method_click(self):
        log("Выбрать метод оплаты")
        self.noone.payment_method().click()

    def order_comment_click(self):
        log("Нажать на область ввода комментария к доставке")
        self.noone.order_comment_activate().click()

    def order_comment_text(self):
        comment = 'Это тестовый заказ от сотрудников NoOne. Он должен быть автоматически удалён. ' \
                  'В случае возникновения вопросов - звонить по номеру: +7 (916) 716-33-00'
        log("Ввести комментарий к доставке: '{}'".format(comment))
        self.noone.order_comment_box().input_text(
            comment
        )

    # def promo(self):
    #     self.noone.promocode().input_text()

    def order_btn(self):
        log("Нажать на кнопку оформления заказа.")
        self.noone.order_btn().click()

    def cancel_order(self):
        log("="*5 + "Отмена заказа")
        log("Перейти в раздел отмены заказа")
        self.noone.logo.click()
        self.noone.profile.hover_center()
        self.noone.profile_personal_info.click()
        self.noone.profile_my_orders.click()
        log("Открыть окно заказа, удалить Новые")
        try:
            for i in range(1, 10):
                self.noone.profile_my_orders_open_order.click()
                log("=" * 5 + "Удалить заказ")
                self.noone.order_delete.click()
                log("="*5 + "Подтвердить удаление заказа")
                self.noone.order_delete_confirm.click()
                log("="*5 + "Закрыть уведомление и вернуться")
                self.noone.order_post_delete_confirm.click()
                self.noone.go_back()
        except:
            log("="*5+"Заказов нет, либо все отменены.")
        log("=" * 5 + "Игнорировать DM2, заказы удаляются только через администрирование")


test_start = "=" * 5 + "Начало тестирования {}.".format(RunCartDM2().__class__.__name__)


if __name__ == '__main__':
    RunCartDM2().test_run()
    test_start = "=" * 5 + "Начало тестирования."
