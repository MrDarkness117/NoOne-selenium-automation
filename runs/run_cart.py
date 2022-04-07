import datetime
import random
import time
import json

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from pages.cart_page import CartPage as Page
from pages.base.logging_report import Logging, LogReport, TakeScreenshot

logging = Logging()
log = logging.logger


class RunCart(object):

    # Настройки

    options = Options()
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option('prefs', prefs)
    # driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.set_window_position(-2000, 0)
    driver.maximize_window()
    driver.implicitly_wait(3)

    # Запуск

    noone = Page(driver=driver)
    noone.go()
    url = driver.current_url
    skipCollection = False

    def test_run(self):

        log(test_start + " Время: {}".format(str(datetime.datetime.now())))

        try:
            # Стандартные действия
            # time.sleep(2)
            self.noone.region_confirm.click()
            time.sleep(1)
            self.noone.cookies.click()

            # Действия Cart Page
            self.auth()
            self.auth_fields()
            WebDriverWait(self.driver, 10).until(EC.invisibility_of_element((By.XPATH, '//a[@id="modal-auth-phone"]')))
            self.cart_click()

            # OLD

            if not self.skipCollection:
                self.product_recommended_hover()
                self.preview_click()
                try:
                    self.item_size_block_click()
                    self.item_size_click()
                    self.item_add_click()
                    # self.accept_click()
                except Exception as e:
                    log("/"*10 + "ОШИБКА: Не найдены блоки предпросмотра в корзине!" + "\\"*10 + str(e))
                    try:
                        log('='*5 + "Закрываю модальное окно")
                        self.noone.close_modal_preview.click()
                    except:
                        log('/'*10 + "Отсутствует модальное окно" + '\\'*10)

                with open('C:\\Users\\admin\\Documents\\GitHub\\NoOne-selenium-automation\\runs\\ids.json') as i:
                    data = json.load(i)

                if len(data) > 0:
                    for d in data:
                        self.search_item(str(d))
                        self.item_page()
                        self.noone.cart.click()
                elif len(data) == 0:
                    self.add_shoes_from_catalog()
                    self.add_bags_from_catalog()

            self.surname_enter()
            self.check_limits()
            self.city_select_click()
            self.city_select_element_click()
            try:
                # self.driver.find_element_by_xpath('//div[contains(@class, "text-title-3") and contains(text(), "Пункт самовывоза")]//span[contains(text(), "Выбрать другой")]')
                # self.noone.form_address_change.click()
                self.noone.form_address_select.click()
                self.noone.select_all.click()
                time.sleep(0.5)
                self.noone.select_all.click()
            except:
                log("/"*10 + "ВНИМАНИЕ: Невозможно выбрать адрес из истории!" + "\\"*10)
                self.noone.form_address_change.click()  # TODO: Внедрить проверку "Выбрать другой"
                self.form_info()
                self.form_check_deselect()
                log("Нажать \"Продолжить\"")
                self.noone.form_continue().click()
                self.noone.form_address_show_all().click()
                if self.noone.form_address_label_text.text == "Россия, Москва, ул Профсоюзная, 37, кв 43":  # FIXME:   В строке отображается без "Россия" и "кв 43", а также вместо "37" - "д 37"
                    log("="*5 + "Адреса соответствуют")
                # try:
                #     log("="*5 + "Проверка зависания")
                #     self.driver.find_element_by_xpath("//ul[@class='form-autocomplete-list']")
                #     log('/'*10 + "Список адресов завис!!" + "\\"*10)
                # except:
                #     log("="*5 + "Зависания не произошло")
                self.noone.select_all.click()
                time.sleep(0.5)
                self.noone.select_all.click()
            self.delivery_click()
            self.delivery_date_click()
            self.delivery_date_select_click()
            time.sleep(1)
            self.payment_method_click()
            self.order_comment_click()
            self.order_comment_text()
            self.order_btn()
            self.cancel_order()
        except Exception as e:
            log("/" * 10 + "ОШИБКА: Во время работы произошёл сбой!" + "\\" * 10 + "\nОшибка: {}".format(e))
            print(e)
            TakeScreenshot(RunCart()).take_screenshot()

        log("="*5 + "Завершение тестирования.")

        self.driver.quit()
        LogReport(testblock=RunCart(), logs=logging.log).test_results()

    # Команды

    def auth(self):
        self.noone.auth_page.click()
        log("Открыть окно авторизации")
        self.noone.auth_email_login.click()
        log("Перейти на вход по email")

    def auth_fields(self):
        auth_info = {
            'login': 'm.romantsov@noone.ru',
            'password': 'Mihailo117'
        }
        self.noone.auth_field_login.input_text(auth_info['login'])
        self.noone.auth_field_pass.input_text(auth_info['password'])
        self.noone.auth_field_button.click()
        log("Ввести логин/пароль, нажать 'войти'")

    def logo(self):
        self.noone.header_logo.click()
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
            self.noone.item_delete.click()
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

    def search_item(self, n):
        log("Поиск товара по запросу: " + str(n))
        self.noone.search_field.click()
        self.noone.search_field.input_text(str(n))
        self.noone.search_submit.click()

        self.noone.first_item.click()

    def item_page(self):
        try:
            log("=" * 5 + "Проверка выбора размера (обуви/одежды)")
            self.noone.item_page_size.click()
        except Exception as e:
            log("/" * 10 + "У товара нет размеров" + "\\" * 10)

        try:
            log("=" * 5 + "Проверка наличия выбора вариантов цвета")
            self.noone.item_page_color_list.find()
            self.noone.item_page_color_option.find()
        except:
            log("/" * 10 + "У товара нет выбора вариантов цвета" + "\\" * 10)

        try:
            log("="*5 + "Проверка наличия резервирования, открыть окно")
            self.noone.catalog_preview_reserve.click()
            try:
                log("Открыть выбрать первый доступный бутик")
                self.noone.catalog_preview_reserve_boutique.click()
                self.noone.catalog_preview_reserve_reserve.find()
                log("Проверить доступность кнопки \"Зарезервировать\"")
                self.noone.catalog_preview_reserve_close.click()
            except:
                log('/' * 10 + "ОШИБКА РАБОТЫ РЕЗЕРВИРОВАНИЯ!" + "\\" * 10)
                self.noone.catalog_preview_reserve_close.click()
        except:
            log("/" * 10 + "У товара нет вариантов резервирования" + "\\" * 10)

        try:
            log("Нажать \"Добавить в корзину\"")
            self.noone.catalog_preview_add_to_cart.click()
            log("Перейти в корзину через кнопку появившегося модального окна")
            self.noone.catalog_preview_go_to_cart.click()
        except:
            log("/"*10 + "ОШИБКА ДОБАВЛЕНИЯ ТОВАРА В КОРЗИНУ!" + "\\"*10)

    def add_shoes_from_catalog(self):
        log("="*5 + "Перехожу на страницу каталога")
        log("Перейти на страницу каталога")
        self.noone.logo.click()
        # self.noone.catalog_male.click()
        # WebDriverWait(self.driver, 10).until(EC.url_changes)
        self.noone.catalog_male_shoes.click()
        self.noone.catalog_first_item.hover_center()
        log("Открыть окно превью первого товара")
        self.noone.catalog_preview_btn.click()
        try:
            log("Выбрать размер обуви")
            self.noone.catalog_preview_size_select.click()
        except:
            log('='*5 + "Не могу добавить размер - вероятно их для этого товара нет")
        log("="*5 + "Проверить резервирование")
        try:
            log("Открыть окно резервирования")
            self.noone.catalog_preview_reserve.click()
            log("Открыть выбрать первый доступный бутик")
            self.noone.catalog_preview_reserve_boutique.click()
            log("Проверить доступность кнопки \"Зарезервировать\"")
            try:
                self.noone.catalog_preview_reserve_reserve.find()
            except:
                log('/'*10 + "CRITICAL: Ошибка функционала резервирования!!!")
            log("Закрыть окно резервирования")
            self.noone.catalog_preview_reserve_close.click()
        except:
            log("/"*10 + "Нет кнопки зарезервировать! " + str(self.driver.current_url) + '\\'*10)
        log("Нажать \"Добавить в корзину\"")
        self.noone.catalog_preview_add_to_cart.click()
        log("Перейти в корзину через кнопку появившегося модального окна")
        self.noone.catalog_preview_go_to_cart.click()

    def add_bags_from_catalog(self):
        log("="*5 + "Перехожу на страницу каталога")
        log("Перейти на страницу каталога")
        self.noone.logo.click()
        self.noone.catalog_male.click()
        time.sleep(0.5)
        self.noone.catalog_male_bags.click()
        self.noone.catalog_first_item.hover_center()
        log("Открыть окно превью первого товара")
        self.noone.catalog_preview_btn.click()
        log("="*5 + "Проверить резервирование")
        try:
            log("Открыть окно резервирования")
            self.noone.catalog_preview_reserve.click()
            log("Открыть выбрать первый доступный бутик")
            self.noone.catalog_preview_reserve_boutique.click()
            log("Проверить доступность кнопки \"Зарезервировать\"")
            try:
                self.noone.catalog_preview_reserve_reserve.find()
            except:
                log('/'*10 + "CRITICAL: Ошибка функционала резервирования!!!")
            log("Закрыть окно резервирования")
            self.noone.catalog_preview_reserve_close.click()
        except:
            log("/"*10 + "Нет кнопки зарезервировать! " + str(self.driver.current_url) + '\\'*10)
        log("Нажать \"Добавить в корзину\"")
        self.driver.find_element_by_xpath('//span[contains(text(), "Добавить в корзину")]').click()
        log("Перейти в корзину через кнопку появившегося модального окна")
        try:
            self.noone.catalog_preview_go_to_cart.click()
        except:
            log("="*5 + "Не нашел нужную кнопку, пробую другую")
            self.driver.find_element_by_xpath('//div[@class="item-checkout"]').click()

    def surname_enter(self):
        text = "Романцов"
        log("Ввести фамилию ({})".format(text))
        self.noone.surname.input_text(text)

    def check_limits(self):
        log("Проверить уведомления на ограничения по размеру")
        try:
            self.driver.find_element_by_xpath('//div[contains(text(), "Превышено количество товаров")]')
            log("="*5 + "Уведомление найдено, снимаю галочку на втором товаре")
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@id="tab-available"]//div[@id="cart-items-avaliable"]/div[2]/label')))
            self.driver.find_element_by_xpath('//div[@id="tab-available"]//div[@id="cart-items-avaliable"]/div[2]/label').click()
            log("="*5 + "Галочка снята")
            time.sleep(1)
        except:
            log("Уведомление отсутствует")

    def city_select_click(self):
        log("Кнопка выбора города")
        self.noone.city_select.click()

    def city_select_element_click(self):
        city = 1  # г Москва
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
        self.noone.form_info("Улица и дом").input_text('д 37')  # TODO: Баг!!! http://proj.noone.ru/issues/124838
        # self.noone.form_info("Улица и дом").input_text('д 3')
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
        self.noone.go_refresh()
        # self.noone.header_logo.click()
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
