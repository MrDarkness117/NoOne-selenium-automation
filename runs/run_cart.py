import datetime
import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from runs.pages.cart_page import CartPage as Page
from runs.pages.base.logging_report import Logging, LogReport, TakeScreenshot

logging = Logging()
log = logging.logger


class RunCart(object):

    # Настройки

    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.set_window_position(-2000, 0)
    driver.maximize_window()
    driver.implicitly_wait(3)

    # Запуск

    noone = Page(driver=driver)
    noone.go()
    url = driver.current_url

    def test_run(self):

        log(test_start + " Время: {}".format(str(datetime.datetime.now())))

        try:
            # Стандартные действия
            self.noone.region_confirm.click()
            self.noone.cookies.click()

            # Действия Cart Page
            self.auth()
            self.auth_fields()
            self.logo()
            self.cart_click()
            self.product_recommended_hover()
            self.preview_click()
            self.item_size_block_click()
            self.item_size_click()
            self.item_add_click()
            self.accept_click()
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
            TakeScreenshot(RunCart()).take_screenshot()

        log("="*5 + "Завершение тестирования.")

        self.driver.quit()
        LogReport(testblock=RunCart(), logs=logging.log).test_results()

    # Команды

    def auth(self):
        self.noone.auth_page.click()
        log("Открыть окно авторизации")

    def auth_fields(self):
        auth_info = {
            'login': 'm.romantsov@noone.ru',
            'password': 'mihailo'
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
            self.noone.dy_product_card.hover_center()
            log("Навести мышкой на товар снизу из списка")
        except:
            log('='*5 + "(?) Корзина уже не пустая. Удаляем товары.")
            self.noone.item_delete(1).click()
            # self.cart_click()
            log("Навести мышкой на товар снизу из списка")
            self.noone.dy_product_card.hover_center()

    def preview_click(self):
        self.noone.dy_product_window.click()
        log("Нажать на появишвуюся кнопку предварительного просмотра товара")

    def item_color_block(self):
        """
        Всегда выбирает неактивный элемент. Если это невозможно, то выбирает первый элемет из списка.
        :return:
        """
        log("Нажать на окно выбора цвета товара")
        self.noone.item_color_block.click()
        try:
            log("Выбрать цвет с без класса .is-active")
            self.noone.item_color_element.click()
        except:
            log("=" * 5 + "Не найдено более одного варианта, выбираю единственный возможный")
            self.noone.item_color_element_single.click()

    def item_size_block_click(self):
        self.noone.item_size_block.click()
        log("Нажать на окно размеров")

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
            log("="*5 + "Доступен только один размер, выбираю")
            self.noone.item_size_single.click()

    def item_preview_image(self):
        try:
            log("="*5 + "Пробую переключить изображение")
            self.noone.image_selection.click()
        except:
            log("="*5 + "Второе изображение недоступно, проверяю нажатие первого")
            self.driver.find_element_by_xpath('//div[@class="bootbox-body"]//ul[@class="item-thumb-list js-item-thumb-list"]/li[1]').click()

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
        checkbox_test = self.driver.execute_script("document.querySelector('.form-check-input').checked")
        log("Отключить чек-бокс \"Запомнить адрес\". Автоматическая проверка состояния чекбокса:")
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
        # self.noone.form_info("Улица и дом").input_text('д 37')  # TODO: Баг!!! http://proj.noone.ru/issues/124838
        self.noone.form_info("Улица и дом").input_text('д 3')
        time.sleep(3)
        self.driver.find_element_by_xpath('//div[@class="form-group form-autocomplete"]'
                                          '//li[1]').click()

    def delivery_click(self):
        log("Выбрать метод доставки")
        self.noone.form_delivery.click()

    def delivery_date_click(self):
        log("=" * 5 + "Выбираем дату доставки")
        try:
            log("Нажать на выбор даты доставки")
            self.noone.form_delivery_date().click()
        except:
            log("/"*10 + "ВНИМАНИЕ: Кнопка выбора даты отсутствует!" + '\\'*10)

    def delivery_date_select_click(self):
        try:
            log("Выбрать дату доставки")
            self.noone.form_delivery_date_element().click()
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
        self.noone.logo.click()
        self.noone.profile.hover_center()
        log("Перейти в раздел отмены заказа")
        self.noone.profile_personal_info.click()
        self.noone.profile_my_orders.click()
        log("Открыть окно заказа")
        try:
            for i in range(1, 100):
                self.noone.profile_my_orders_open_order.click()
                log("Удалить заказ")
                self.noone.order_delete.click()
                log("="*5 + "Подтвердить удаление заказа")
                self.noone.order_delete_confirm.click()
                log("="*5 + "Закрыть уведомление и вернуться")
                self.noone.order_post_delete_confirm.click()
                self.noone.go_back()
        except:
            log("="*5+"Заказов нет, либо все отменены.")

    log('='*5 + "Проверка оформления заказа")


test_start = "=" * 5 + "Начало тестирования {}.".format(RunCart().__class__.__name__)


if __name__ == '__main__':
    RunCart().test_run()
    test_start = "=" * 5 + "Начало тестирования."

    # try:
    #     RunCart().test_run()
    # except:
    #     print("Пробую закрыть всплывающие окна")
    #     RunCart().driver.execute_script('document.querySelector(".flocktory-widget-overlay").click()')
