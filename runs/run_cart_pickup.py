#!/usr/bin/env python
# -*- coding: utf8 -*-
import re
import traceback
import datetime
import random
import time
import json
import glob
import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from pages.cart_page import CartPage as Page
from pages.base.logging_report import Logging, LogReport, TakeScreenshot

from telethon import TelegramClient

from logging import exception

logging = Logging()
log = logging.logger

tg_chat_zabbix = -444987572
tg_chat_autotest = -639744499
tg_chat_me = 374550034
chat = tg_chat_me

api_id = 16834116
api_hash = 'bb33295647d9d753684d3cf8850ab1ca'
api_bot_hash = '5660256779:AAG5Jtk7gCMxSG_gQCt13QKlvMipylm_ang'
# bot = Telegram
client = TelegramClient('me', api_id, api_hash)

test_complete = False


class RunCartPickup(object):
    # Настройки

    options = Options()
    # prefs = {"profile.managed_default_content_settings.images": 2}
    # options.add_experimental_option('prefs', prefs)
    # driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.set_window_position(-2000, 0)
    driver.maximize_window()
    driver.implicitly_wait(3)

    # Запуск

    noone = Page(driver=driver)
    noone.go()
    url = driver.current_url
    skipRR = True


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
            self.select_city()
            self.cart_click()

            # OLD

            if not self.skipRR:
                try:
                    self.product_recommended_hover()
                    self.preview_click()
                    try:
                        self.item_size_block_click()
                        self.item_size_click()
                        self.item_add_click()  # self.accept_click()
                    except Exception as e:
                        log("/" * 10 + "ОШИБКА: Не найдены блоки размеров предпросмотра! Возможна долгая загрузка сайта." + "\\" * 10)
                        try:
                            log('=' * 5 + "Закрываю модальное окно")
                            self.noone.close_modal_preview.click()
                        except:
                            log('/' * 10 + "Отсутствует модальное окно" + '\\' * 10)
                except:
                    log('/'*10 + "Не найден блок рекоммендаций Retail Rocket" + '\\'*10)

            with open('C:\\Users\\admin\\Documents\\GitHub\\NoOne-selenium-automation\\runs\\ids.json') as i:
                data = json.load(i)

            if len(data) > 0:
                for d in data:
                    self.search_item(str(d))
                    self.item_page()
                    self.noone.cart.click()
            elif len(data) == 0:  # Криво, но почему-то просто else работать не хочет :(
                self.add_shoes_from_catalog()
                # self.add_bags_from_catalog()  #FIXME: Андрей должен исправить резервы в карточке товара, тогда включу

            self.surname_enter()
            self.check_limits()
            # self.city_select_click()  #FIXME: Временно отключено
            # self.city_select_element_click()  #FIXME
            try:
                # self.driver.find_element_by_xpath('//div[contains(@class, "text-title-3") and contains(text(), "Пункт самовывоза")]//span[contains(text(), "Выбрать другой")]')
                # self.noone.form_address_change.click()
                self.noone.form_address_select.click()
                self.noone.select_all.click()
                time.sleep(10)
                # WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located((By.XPATH, '//div[@class="loader-overlay"]')))
                WebDriverWait(self.driver, 15).until(
                    EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Выбрать все")]'))).click()
                time.sleep(10)
            except:
                log("/" * 10 + "ВНИМАНИЕ: Невозможно выбрать адрес из истории!" + "\\" * 10)
                WebDriverWait(self.driver, 10).until(
                    EC.invisibility_of_element_located((By.XPATH, '//div[@class="loader-overlay"]')))
                log("Нажать \"Продолжить\"")
                self.noone.select_all.click()
                time.sleep(10)
                self.noone.select_all.click()
                time.sleep(10)
            time.sleep(1)
            self.label_pickup()
            self.select_pickup()
            self.select_atrium()
            self.select_map()
            self.payment_method_click()
            self.order_comment_click()
            self.order_comment_text()
            self.order_btn()
            global test_complete
            test_complete = True
            self.cancel_order()
        except Exception as e:
            log("/" * 10 + "ОШИБКА: Во время работы произошёл сбой!" + "\\" * 10 + "\nОшибка: {}".format(e))
            exception(e)

            # traceback.print_tb(e.__traceback__)
            TakeScreenshot(RunCartPickup()).take_screenshot()

        log("=" * 5 + "Завершение тестирования.")

        self.driver.quit()
        LogReport(testblock=RunCartPickup(), logs=logging.log).test_results()

    # Команды

    def auth(self):
        self.noone.auth_page.click()
        log("Открыть окно авторизации")
        self.noone.auth_email_login.click()
        log("Перейти на вход по email")

    def auth_fields(self):
        log("Ввести логин/пароль, нажать 'войти'")
        auth_info = {'login': 'm.romantsov@noone.ru', 'password': 'Mihailo117'}
        self.noone.auth_field_login.input_text(auth_info['login'])
        self.noone.auth_field_pass.input_text(auth_info['password'])
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            self.driver.find_element(By.XPATH, '//button[contains(text(), "Войти в аккаунт")]')))
        self.noone.auth_field_button.click()

    def select_city(self):
        log("="*5 + "Выбрать г. Москва")
        self.driver.execute_script("window.scrollBy(0, -2000)")
        self.noone.open_cities.click()
        self.noone.select_city_moscow.click()

    def logo(self):
        log("Перейти по логотипу на главную страницу")
        self.noone.header_logo.click()

    def cart_click(self):
        log("Нажать на кнопку корзины товаров")
        # WebDriverWait(self.driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, '//a[@class="nav-link js-basket-line"]')))
        self.noone.cart.click()

    def product_recommended_hover(self):
        try:
            log("Навести мышкой на товар снизу из списка")
            self.noone.dy_product_card.hover_center()
        except:
            log('=' * 5 + "(?) Корзина уже не пустая. Удаляем товары.")
            self.noone.item_delete.click()
            log("Навести мышкой на товар снизу из списка")
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//div[@data-swiper-slide-index="0"]')))
            self.noone.dy_product_card.hover_center()

    def preview_click(self):
        log("Нажать на появишвуюся кнопку предварительного просмотра товара")
        self.noone.dy_product_window.click()

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
        log("Нажать на окно размеров")
        self.noone.item_size_block.click()

    def item_size_click(self):
        try:
            random_size = random.randint(1, len(self.driver.find_elements(By.XPATH,
                '//div[@class="select item-size-list js-item-size-list select-open"]'
                '//ul[@class="select-list"]'
                '//li[@class="select-item item-size"]')))
            log("Выбрать случайный размер - size-id: {}".format(random_size))
            self.noone.item_size(random_size).click()
        except:
            log("=" * 5 + "Доступен только один размер, выбираю")
            self.noone.item_size_single.click()

    def item_preview_image(self):
        try:
            log("=" * 5 + "Пробую переключить изображение")
            self.noone.image_selection.click()
        except:
            log("=" * 5 + "Второе изображение недоступно, проверяю нажатие первого")
            self.driver.find_element_by_xpath(
                '//div[@class="bootbox-body"]//ul[@class="item-thumb-list js-item-thumb-list"]/li[1]').click()

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
            log("=" * 5 + "Проверка наличия резервирования, открыть окно")
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
            log("/" * 10 + "ОШИБКА ДОБАВЛЕНИЯ ТОВАРА В КОРЗИНУ!" + "\\" * 10)

    def add_shoes_from_catalog(self):
        log("=" * 5 + "Перехожу на страницу каталога")
        log("Перейти на страницу каталога")
        self.noone.logo.click()
        # self.noone.catalog_male.click()
        # WebDriverWait(self.driver, 10).until(EC.url_changes)
        self.noone.catalog_male_shoes.click()
        self.noone.catalog_first_item.hover_center()
        log("Открыть окно превью первого товара")
        self.noone.catalog_preview_btn.click()
        log("=" * 5 + "Товар: {}".format(
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                self.driver.find_element(By.XPATH, '//div[@class="item-gallery"]//a[@class="text-link"]'))).get_attribute(
                "href")))
        log("=" * 5 + "Проверить резервирование")
        try:
            log("Выбрать размер обуви")
            self.noone.catalog_preview_size_select.click()
        except:
            log('=' * 5 + "Не могу добавить размер - вероятно их для этого товара нет")
        log("=" * 5 + "Проверить резервирование")
        try:
            log("Открыть окно резервирования")
            self.noone.catalog_preview_reserve.click()
            try:
                log("Открыть выбрать первый доступный бутик")
                self.noone.catalog_preview_reserve_boutique.click()
                log("Проверить доступность кнопки \"Зарезервировать\"")
                self.noone.catalog_preview_reserve_reserve.find()
            except:
                log('/' * 10 + "CRITICAL: Ошибка функционала резервирования!!!")
            log("Закрыть окно резервирования")
            self.noone.catalog_preview_reserve_close.click()
        except:
            log("/" * 10 + "Нет кнопки зарезервировать! " + str(self.driver.current_url) + '\\' * 10)
        log("Нажать \"Добавить в корзину\"")
        self.noone.catalog_preview_add_to_cart.click()
        log("Перейти в корзину через кнопку появившегося модального окна")
        self.noone.catalog_preview_go_to_cart.click()

    def add_bags_from_catalog(self):
        log("=" * 5 + "Перехожу на страницу каталога")
        log("Перейти на страницу каталога")
        self.noone.logo.click()
        self.noone.catalog_male.click()
        time.sleep(0.5)
        self.noone.catalog_male_bags.click()
        self.noone.catalog_first_item.hover_center()
        log("Открыть окно превью первого товара")
        self.noone.catalog_preview_btn.click()
        log("=" * 5 + "Товар: {}".format(
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                self.driver.find_element(By.XPATH, '//div[@class="item-gallery"]//a[@class="text-link"]'))).get_attribute(
                "href")))
        log("=" * 5 + "Проверить резервирование")
        try:
            log("=" * 5 + "Проверить резервирование")
            log("Открыть окно резервирования")
            self.noone.catalog_preview_reserve.click()
            log("Открыть выбрать первый доступный бутик")
            self.noone.catalog_preview_reserve_boutique.click()
            log("Проверить доступность кнопки \"Зарезервировать\"")
            try:
                self.noone.catalog_preview_reserve_reserve.find()
            except:
                log('/' * 10 + "CRITICAL: Ошибка функционала резервирования!!!")
            log("Закрыть окно резервирования")
            self.noone.catalog_preview_reserve_close.click()
        except:
            log("/" * 10 + "Нет кнопки зарезервировать! " + str(self.driver.current_url) + '\\' * 10)
        log("Нажать \"Добавить в корзину\"")
        self.driver.find_element_by_xpath('//span[contains(text(), "Добавить в корзину")]').click()
        log("Перейти в корзину через кнопку появившегося модального окна")
        try:
            self.noone.catalog_preview_go_to_cart.click()
        except:
            log("=" * 5 + "Не нашел нужную кнопку, пробую другую")
            self.driver.find_element_by_xpath('//div[@class="item-checkout"]').click()

    def surname_enter(self):
        text = "Романцов"
        log("Ввести фамилию ({})".format(text))
        self.noone.surname.input_text(text)

    def check_limits(self):
        log("Проверить уведомления на ограничения по размеру")
        try:
            self.driver.find_element(By.XPATH, '//div[contains(text(), "Превышено количество товаров")]')
            log("=" * 5 + "Уведомление найдено, снимаю галочку на втором товаре")
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(
                (By.XPATH, '//div[@id="tab-available"]//div[@id="cart-items-avaliable"]/div[2]/label')))
            self.driver.find_element_by_xpath(
                '//div[@id="tab-available"]//div[@id="cart-items-avaliable"]/div[2]/label').click()
            log("=" * 5 + "Галочка снята")
            time.sleep(1)
        except:
            log("=" * 5 + "Уведомление отсутствует")

    def label_pickup(self):
        log("Выбрать самовывоз")
        self.noone.label_pickup.click()

    def select_pickup(self):
        log("Нажать кнопку выбрать пункт самовывоза")
        self.noone.select_pickup.click()

    def select_atrium(self):
        log("Выбрать магазин Атриум")
        self.noone.select_atrium.click()

    def select_map(self):
        log("Нажать на кнопку выбора пункта самовывоза на карте")
        time.sleep(10)
        self.noone.select_map.click()

    def payment_method_click(self):
        log("Выбрать метод оплаты")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                         '//div[@class="order-step"]//span[contains(text(), "Онлайн")]'))).click()  # self.noone.payment_method().click()

    def order_comment_click(self):
        log("Нажать на область ввода комментария к доставке")
        WebDriverWait(self.driver, 10).until(
            EC.invisibility_of_element_located((By.XPATH, '//div[@class="loader-overlay"]')))
        self.noone.order_comment_activate().click()

    def order_comment_text(self):
        comment = 'Это тестовый заказ от сотрудников NoOne. Он должен быть автоматически удалён. ' \
                  'В случае возникновения вопросов - звонить по номеру: +7 (916) 716-33-00'
        log("Ввести комментарий к доставке: '{}'".format(comment))
        self.noone.order_comment_box().input_text(comment)

    # def promo(self):
    #     self.noone.promocode().input_text()

    def order_btn(self):
        log("Нажать на кнопку оформления заказа.")
        # self.noone.order_btn.click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="checkout"]/div/div[2]/div/div[1]/div[2]/div[3]/div/button'))).click()
        cart_price = '//*[@class="cart-data cart-price-total"]//*[@class="cart-data-value"]'
        iframe = '//iframe[@class=" with-appled"]'
        cp_price = '//div[@class="header-component__cost"]/span'
        cart = re.sub("^[0-9]", '', self.driver.find_element(By.XPATH, cart_price).text)
        self.driver.switch_to.frame(WebDriverWait(self.driver, 10)
                                    .until(EC.visibility_of_element_located((By.XPATH, iframe))))
        cp = re.sub("^[0-9]", '', self.driver.find_element(By.XPATH, cp_price).text)
        self.driver.switch_to.default_content()
        assert cp == cart, "Ошибка соответствия цен товаров! CloudPayments != чекаут."

    def cancel_order(self):
        log("=" * 5 + "Отмена заказа")
        self.noone.go_refresh()
        # self.noone.header_logo.click()
        self.noone.logo.click()
        self.noone.profile.hover_center()
        log("Перейти в раздел отмены заказа")
        # self.noone.profile_personal_info.click()
        # self.noone.profile_my_orders.click()
        self.noone.profile_orders.click()
        log("Открыть окно заказа")
        try:
            for i in range(1, 150):
                self.noone.profile_my_orders_open_order.click()
                log("Удалить заказ")
                self.noone.order_delete.click()
                log("=" * 5 + "Подтвердить удаление заказа")
                self.noone.order_delete_confirm.click()
                log("=" * 5 + "Закрыть уведомление и вернуться")
                self.noone.order_post_delete_confirm.click()
                self.noone.go_back()
        except:
            log("=" * 5 + "Заказов нет, либо все отменены.")

    log('=' * 5 + "Проверка оформления заказа")


test_start = "=" * 5 + "Начало тестирования {}.".format(RunCartPickup().__class__.__name__)


async def send_telegram():
    from pathlib import Path

    report = glob.glob(
        str(Path.home()) + '\\Documents\\reports\\*.txt')  # * means all if need specific format then *.csv
    latest_file = max(report, key=os.path.getctime)
    screenshot = glob.glob(str(Path.home()) + '\\Documents\\screenshots\\*.png')
    latest_screenshot = max(screenshot, key=os.path.getctime)

    # if RunCart().test_complete:
    #     async with client:
    #         client.loop.run_until_complete(await client.send_message(tg_chat_zabbix,
    #                                                                  "Результаты автотеста на {}:\n\n".format(
    #                                                                      datetime.datetime.today()) /
    #                                                                  "Крит-автотест по сайту noone.ru (Авторизация, "
    #                                                                  "Каталог, Корзина (NO ONE; Онлайн), ЛК: Заказы) "
    #                                                                  "пройден успешно."))
    if not test_complete:
        with open(latest_file, 'r', encoding='utf8') as f:
            report_text = f.read()
            f.close()
        async with client:
            from telethon.errors.rpcerrorlist import MediaCaptionTooLongError
            try:
                await client.send_file(chat, latest_screenshot, caption="Результаты автотеста на {}:\n\n".format(
                    datetime.datetime.today()) + "Ошибка во время тестирования! \nШаги воспроизведения: \n\n{}"
                                       .format(report_text))

            except MediaCaptionTooLongError:
                await client.send_file(chat, latest_screenshot, caption="Результаты автотеста на {}:\n\n".format(
                    datetime.datetime.today()) + "Ошибка во время тестирования! \nЛог в файле ниже."
                                       .format(report_text))
            time.sleep(5)
            await client.send_file(chat, latest_file)


if __name__ == '__main__':
    RunCartPickup().test_run()
    test_start = "=" * 5 + "Начало тестирования."

    with client:
        client.loop.run_until_complete(send_telegram())
