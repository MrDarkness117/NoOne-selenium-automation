import datetime
import random
import time
import json
import re

from os import path
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from runs.pages.full_catalog_page import FullCatalog as Page
from runs.pages.base.logging_report import Logging, LogReport, TakeScreenshot

logging = Logging()
log = logging.logger


class RunFullCatalog(object):

    # Настройки

    options = Options()
    # driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.set_window_position(-2000, 0)
    driver.maximize_window()
    driver.implicitly_wait(3)

    # Запуск

    noone = Page(driver=driver)
    noone.go()
    url = driver.current_url

    shoes_f_url = 'https://www.noone.ru/catalog/zhenskoe/obuv/'
    bags_f_url = 'https://www.noone.ru/catalog/zhenskoe/sumki/'
    accessories_f_url = 'https://www.noone.ru/catalog/zhenskoe/aksessuary/'
    shoes_m_url = 'https://www.noone.ru/catalog/muzhskoe/obuv/'
    bags_m_url = 'https://www.noone.ru/catalog/muzhskoe/sumki/'
    accessories_m_url = 'https://www.noone.ru/catalog/muzhskoe/aksessuary/'

    product_url = 'https://www.noone.ru/product/'

    sizes_catalog = {}
    sizes_product = {}
    errors = {}

    def test_run(self):

        log(test_start + " Время: {}".format(str(datetime.datetime.now())))
        sizes_list_catalog = {}

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

            # Открытие URL, собираем информацию по размерам (и др., по необходимости добавим)
            sizes_list_catalog['female'].append(self.run_catalog_shoes_f())
            sizes_list_catalog['male'].append(self.run_catalog_shoes_m())

            # Далее нужно чтобы он сравнивал собранные данные
            self.data_compare()
            self.create_report()

        except Exception as e:
            log("/" * 10 + "ОШИБКА: Во время работы произошёл сбой!" + "\\" * 10 + "\nОшибка: {}".format(e))
            print(e)
            TakeScreenshot(RunFullCatalog()).take_screenshot()

        log("="*5 + "Завершение тестирования.")

        self.driver.quit()
        LogReport(testblock=RunFullCatalog(), logs=logging.log).test_results()

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

    def run_catalog_sizes(self):
        global sizes_catalog
        items = self.driver.find_elements_by_xpath('//div[@id="catalog"]//div[@class="col lg:col-4 xs:col-6"]')
        for item in items:
            item_id = item.get_attribute('href').replace('/', '').replace('product', '')
            for size_info in item.find_elements_by_xpath('//ul[@class="item-sizes"]'):
                for size in size_info:
                    sizes_catalog[item_id].append(size.get_attribute('data-text'))

    def run_product_sizes(self):
        global sizes_product
        sizes = self.driver.find_elements_by_xpath('//div[@class="item-info"]//ul[@class="item-size-list"]/li')
        item_id = re.sub('[^0-9]', '', self.driver.current_url)
        for size in sizes:
            sizes_product[item_id].append(size)
            sizes_product['url'].append(self.driver.current_url)

    # def run_item_page(self, item_id):
    #     self.driver.get(item_id)

    def scroll_through_page_and_switch(self):
        last_page = self.driver.find_element_by_xpath('//ul[@class="pagination-list"]/li[last()]/a').get_attribute('data-page')
        current_page = re.sub('[^0-9]', '', self.driver.current_url)
        while self.driver.find_element_by_xpath('//ul[@class="pagination-list"]/li[@class="is-active"]').text != last_page:
            self.run_catalog_sizes()
            items = self.driver.find_elements_by_xpath('//div[@id="catalog"]//div[@class="col lg:col-4 xs:col-6"]')
            for item in items:
                item.click()
                self.run_product_sizes()
                self.noone.go_back()
            try:
                self.noone.next_page.click()
            except:
                break
            WebDriverWait(self.driver, 10).until(EC.url_contains(current_page))

    def run_catalog_shoes_f(self):
        self.driver.get(self.shoes_f_url)
        self.scroll_through_page_and_switch()

    # def run_catalog_bags_f(self):
    #     self.driver.get(self.bags_f_url)
    #     pass
    #
    # def run_catalog_accessories_f(self):
    #     self.driver.get(self.accessories_f_url)
    #     pass

    def run_catalog_shoes_m(self):
        self.driver.get(self.shoes_m_url)
        self.scroll_through_page_and_switch()

    # def run_catalog_bags_m(self):
    #     self.driver.get(self.bags_m_url)
    #     pass
    #
    # def run_catalog_accessories_m(self):
    #     self.driver.get(self.accessories_m_url)
    #     pass

    def data_compare(self):
        for k, v in self.sizes_catalog.items():
            if v != self.sizes_product[k]:
                global errors
                errors['item_id'].append(k)
                errors['link'].append(sizes_product['url'])

    def create_report(self):
        with open('{}.json'.format(str(datetime.datetime.now())), 'w') as t:
            json.dump(self.errors, t, ensure_ascii=False, indent=4)
            t.close()

    # TODO: Ниже находятся методы для будущих доработок

    @staticmethod
    def scan(params=1):
        if params == 1:
            pass
        if params == 2:
            pass
        if params == 3:
            pass

    def scan_shoes(self):
        # //article[@id='item_details']//li[@class='item-size'] ? must always be clickable
        # //div[@class='item-checkout']/a ? must always be clickable
        try:
            self.noone.catalog_preview_size_select.find()
            self.noone.catalog_preview_add_to_cart.find()
        except:
            self.go_to_page_exception()

    def scan_unsized(self):
        try:
            # WebDriverWait(self.driver, 1).until(EC.invisibility_of_element_located((
            #     By.XPATH, '//div[@class="bootbox modal modal-item-view in"]//ul[@class="item-size-list"]/li[1]')))
            self.noone.catalog_preview_add_to_cart.find()
        except:
            self.go_to_page_exception()

    def scan_simple(self):
        try:
            WebDriverWait(self.driver, 1).until(EC.invisibility_of_element_located((
                By.XPATH, '//div[@class="bootbox modal modal-item-view in"]//ul[@class="item-size-list"]/li[1]')))
            self.noone.catalog_preview_add_to_cart.find()
        except:
            self.go_to_page_exception(params=2)
        pass

    def go_to_page_exception(self, params=1):
        self.noone.catalog_preview_go_to_item.click()
        if params == 1:
            log("/" * 5 + "Ошибка! Отсутствует размер у товара: " + "{} ".format(self.driver.current_url) + "\\" * 5)
            self.noone.go_back()
        if params == 2:
            log("/" * 5 + "Ошибка с товаром: " + "{} ".format(self.driver.current_url) + "\\" * 5)
            self.noone.go_back()
        if params == 3:
            item_list = []

            log("="*10 + "Размеры: {}".format(str(item_list)))

    def preview_items_on_page(self):
        for el in range(1, len(self.driver.find_elements_by_xpath(
                '//div[@id="catalog"]//div[@class="col lg:col-4 xs:col-6"]'))):
            self.noone.catalog_nth_item(el).hover_center()
            self.noone.catalog_preview_btn.click()


test_start = "=" * 5 + "Начало тестирования {}.".format(RunFullCatalog().__class__.__name__)


if __name__ == '__main__':
    RunFullCatalog().test_run()
    test_start = "=" * 5 + "Начало тестирования."
