import random

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from pages.cart_page import CartPage


class RunCart(object):

    # Настройки

    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.set_window_position(0, 0)
    driver.maximize_window()
    driver.implicitly_wait(3)

    # Запуск

    noone = CartPage(driver=driver)
    noone.go()
    url = driver.current_url

    def test_run(self):

        # Стандартные действия
        self.noone.cookies.click()
        # self.noone.region_confirm.click()

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

    # Команды

    def auth(self):
        self.noone.auth_page.click()
        print("Открыть окно авторизации")

    def auth_fields(self):
        auth_info = {
            'login': 'm.romantsov@noone.ru',
            'password': 'mihailo'
        }
        self.noone.auth_field_login.input_text(auth_info['login'])
        self.noone.auth_field_pass.input_text(auth_info['password'])
        self.noone.auth_field_button.click()
        print("Ввести логин/пароль, нажать 'войти'")

    def logo(self):
        self.noone.logo.click()
        print("Перейти по логотипу на главную страницу")

    def cart_click(self):
        self.noone.cart.click()
        print("Нажать на кнопку корзины товаров")

    def product_recommended_hover(self):
        try:
            self.noone.dy_product_card.hover_center()
            print("Навести мышкой на товар")
        except:
            print("Корзина уже не пустая. Удаляем.")
            self.noone.item_delete(1).click()
            # self.cart_click()
            self.noone.dy_product_card.hover_center()

    def preview_click(self):
        self.noone.dy_product_window.click()
        print("Нажать на появишвуюся кнопку предварительного просмотра товара")

    def item_size_block_click(self):
        self.noone.item_size_block.click()
        print("Нажать на окно размеров")

    def item_size_click(self):
        random_size = random.randint(1, len(self.driver.find_elements_by_xpath(
            '//div[@class="select item-size-list js-item-size-list select-open"]'
            '//ul[@class="select-list"]'
            '//li[@class="select-item item-size"]'
        )))
        print("Выбрать случайный размер - size-id: {}".format(random_size))
        self.noone.item_size(random_size).click()

    def item_add_click(self):
        self.noone.item_add.click()
        print("Нажать на 'добавить в корзину'")

    def accept_click(self):
        self.noone.item_bootbox_accept.click()
        print("Нажать на 'Перейти в корзину'")

    def surname_enter(self):
        text = "Романцов"
        self.noone.surname.input_text(text)
        print("Ввести фамилию ({})".format(text))

    def city_select_click(self):
        self.noone.city_select.click()
        print("Кнопка выбора города")

    def city_select_element_click(self):
        city = '1'  # г Москва
        self.noone.city_select_element(city).click()
        print("Выбрать первый из выпадающего списка город (г Москва)")

    def form_check_deselect(self):
        checkbox_test = self.driver.execute_script("document.querySelector('.form-check-input').checked")
        print("Отключить чек-бокс \"Запомнить адрес\". Автоматическая проверка состояния чекбокса:")
        if str(checkbox_test) != 'false':
            self.noone.form_check_save.click()
            print("Чекбокс не был отключен.")
        else:
            print("Чекбокс уже отключен.")

    def form_info(self):
        self.noone.form_info("Улица и дом").input_text('г Москва, ул Профсоюзная, д 37')
        self.driver.find_element_by_xpath('//ul[@class="form-autocomplete-list"]/li[1]').click()
        self.noone.form_info("Квартира").input_text('43')
        self.noone.form_info("Подъезд").input_text('3')
        self.noone.form_info("Этаж").input_text('1')
        self.noone.form_info("Код домофона").input_text('43к0000')
        print("Заполнить информацию адреса доставки")

    def delivery_click(self):
        self.noone.form_delivery.click()
        print("Выбрать метод доставки")

    def delivery_date_click(self):
        self.noone.form_delivery_date().click()
        print("Нажать на выбор даты доставки")

    def delivery_date_select_click(self):
        self.noone.form_delivery_date_element()
        print("Выбрать дату доставки")

    def payment_method_click(self):
        self.noone.payment_method().click()
        print("Выбрать метод оплаты")

    def order_comment_click(self):
        self.noone.order_comment_activate().click()
        print("Нажать на область ввода комментария к доставке")

    def order_comment_text(self):
        comment = 'Это тестовый заказ от сотрудников NoOne. Он должен быть автоматически удалён. ' \
                  'В случае возникновения вопросов - звонить по номеру: +7 (916) 716-33-00'
        self.noone.order_comment_box().input_text(
            comment
        )
        print("Ввести комментарий к доставке: '{}'".format(comment))

    # def promo(self):
    #     self.noone.promocode().input_text()

    def order_btn(self):
        self.noone.order_btn().click()
        print("Нажать на кнопку оформления заказа.")

    print("Проверка оформления заказа")
    try:
        WebDriverWait(driver, 15).until(lambda driver: driver.current_url == "https://noone.ru")
        print("Заказ успешно оформлен!")
    except:
        print("Заказ не был оформлен, либо страница выдала ошибку")


if __name__ == '__main__':
    RunCart().test_run()
    # try:
    #     RunCart().test_run()
    # except:
    #     print("Пробую закрыть всплывающие окна")
    #     RunCart().driver.execute_script('document.querySelector(".flocktory-widget-overlay").click()')
