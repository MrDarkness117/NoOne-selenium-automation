import datetime
import random
import time
import json
import re
import schedule
import logging as exceptions

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
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(options=options)
    # driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.set_window_position(-2000, 0)
    driver.maximize_window()
    driver.implicitly_wait(3)

    # Запуск

    noone = Page(driver=driver)
    noone.go()
    url = driver.current_url

    actions = ActionChains(driver)

    shoes_f_url = 'https://www.noone.ru/catalog/zhenskoe/obuv/?PAGE=1'
    # shoes_f_url_test = 'https://oneway:eehooXi8@dm1.noone.ru/catalog/zhenskoe/obuv/'
    bags_f_url = 'https://www.noone.ru/catalog/zhenskoe/sumki/'
    accessories_f_url = 'https://www.noone.ru/catalog/zhenskoe/aksessuary/'
    shoes_m_url = 'https://www.noone.ru/catalog/muzhskoe/obuv/?PAGE=1'
    bags_m_url = 'https://www.noone.ru/catalog/muzhskoe/sumki/'
    accessories_m_url = 'https://www.noone.ru/catalog/muzhskoe/aksessuary/'

    product_url = 'https://www.noone.ru/product/'

    project_url = 'http://proj.noone.ru/issues/137780'
    login = 'm.romantsov'
    password = 'KwMuP7UXcC'

    mail_url = 'https://mail.noone.ru/'
    login_mail = 'm.romantsov@noone.ru'
    pass_mail = 'Test_001'

    sizes_catalog = {}
    sizes_product = {}
    errors = {}

    page_number = 1

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
            print("Opened auth")
            self.auth_fields()
            print("Auth completed")
            WebDriverWait(self.driver, 10).until(EC.invisibility_of_element((By.XPATH, '//a[@id="modal-auth-phone"]')))

            # Открытие URL, собираем информацию по размерам (и др., по необходимости добавим)
            print("Beginning catalog")
            try:
                self.run_catalog_shoes_f()
            except:
                print("Error: ")
                exceptions.exception("message")
            try:
                self.run_catalog_shoes_m()
            except:
                print("Error: ")
                exceptions.exception("message")

            # Далее нужно чтобы он сравнивал собранные данные
            self.data_compare()
            self.create_report()
            self.post_report()
            if json.dumps(self.errors) != '{}':
                self.send_report()

        except Exception as e:
            exceptions.exception('message')
            log("/" * 10 + "ОШИБКА: Во время работы произошёл сбой!" + "\\" * 10 + "\nОшибка: {}".format(e))
            print("/" * 10 + "ОШИБКА: Во время работы произошёл сбой!" + "\\" * 10 + "\nОшибка: {}".format(e))
            TakeScreenshot(RunFullCatalog()).take_screenshot()

        log("="*5 + "Завершение тестирования.")

        self.driver.quit()
        LogReport(testblock=RunFullCatalog(), logs=logging.log).test_results()

    def item(self, item):
        self.driver.find_element(By.XPATH, item).click()

    def auth(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//li[@class="nav-item nav-item-auth"]')))
        self.noone.auth_page.click()
        log("Открыть окно авторизации")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="#modal-auth-email"]')))
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
        """
        Сохраняет инфу о товарах в переменную self.sizes_catalog
        :return:
        """
        items = self.driver.find_elements(By.XPATH, '//div[@id="catalog"]//div[@class="col lg:col-4 xs:col-6"]')
        count = 0
        for item in items:
            count += 1
            item_id = re.sub('[^0-9]', '', str(self.driver.find_element(
                By.XPATH,
                '//div[@id="catalog"]//div[@class="col lg:col-4 xs:col-6"][{}]/div/a'.format(count)
            ).get_attribute('href')))
            for size_info in self.driver.find_elements(
                    By.XPATH,
                    '//div[@id="catalog"]//div[@class="col lg:col-4 xs:col-6"][{}]'
                    '//ul[@class="item-sizes"]/li'.format(count)
            ):
                self.sizes_catalog.setdefault(item_id, []).append(size_info.get_attribute('data-text'))

    def run_product_sizes(self):
        """
        Считывает инфу со страницы/предпросмотра товара.
        :return:
        """
        sizes = self.driver.find_elements(By.XPATH, '//div[@class="item-info"]//ul[@class="item-size-list"]/li')

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((
            By.XPATH, '//div[@class="item-gallery"]/a[@class="text-link"]'
        )))
        item_id = re.sub('[^0-9]', '', self.driver.find_element(
            By.XPATH, '//div[@class="item-gallery"]/a[@class="text-link"]').get_attribute('href'))

        self.sizes_product[item_id] = {'sizes': [], 'url': ''}
        for size in sizes:
            self.sizes_product[item_id]['sizes'].append(size.get_attribute('data-size'))
        if self.driver.find_element(By.XPATH, '//div[@class="item-gallery"]/a[@class="text-link"]').get_attribute('href') == '':
            self.sizes_product[item_id]['url'] = "Отсуствтует ссылка"
        else:
            self.sizes_product[item_id]['url'] = self.driver.find_element(
                By.XPATH, '//div[@class="item-gallery"]/a[@class="text-link"]').get_attribute('href')

    # def run_item_page(self, item_id):
    #     self.driver.get(item_id)

    def scroll_through_page_and_switch(self):
        """
        Пролистывает страницу, собирает инфу, потом открывает отдельные вкладки, вытаскивает из них инфу, сохраняет
        инфу каталога и инфу со страниц товаров в разные переменные.
        :return:
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//ul[@class="pagination-list"]/li[last()]/a')))
        last_page = self.driver.find_element(By.XPATH, '//ul[@class="pagination-list"]/li[last()]/a').get_attribute('data-page')
        while self.driver.find_element(By.XPATH, '//ul[@class="pagination-list"]/li[@class="is-active"]').text != last_page:
            self.run_catalog_sizes()
            items = self.driver.find_elements(By.XPATH, '//div[@id="catalog"]//div[@class="col lg:col-4 xs:col-6"]')
            for n in range(1, len(items)+1):
                preview_btn = '//div[@id="catalog"]//div[@class="col lg:col-4 xs:col-6"][{}]' \
                              '//div[@class="btn-item-view js-item-view"]'.format(n)
                preview_close = '//div[@class="modal-body"]//button[@class="bootbox-close-button close"]'
                try:
                    self.actions.move_to_element(self.driver.find_element(
                        By.XPATH,
                        '//div[@id="catalog"]//div[@class="col lg:col-4 xs:col-6"][{}]'.format(n))).perform()
                    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                        (By.XPATH, '//div[@id="catalog"]//div[@class="col lg:col-4 xs:col-6"][{}]'
                                   '//div[@class="btn-item-view js-item-view"]'.format(n))
                    ))
                    self.noone.catalog_nth_item(n).hover_center()
                    try:
                        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, preview_btn)))
                        self.item(preview_btn)
                    except:
                        self.actions.move_to_element(self.driver.find_element(By.XPATH, preview_btn)).perform()
                        self.item(preview_btn)
                    self.run_product_sizes()
                    WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, preview_close)))
                    self.item(preview_close)
                except Exception as e:
                    self.noone.go_refresh()
                    exceptions.exception(e)
            self.next_page()

    def next_page(self):
        current_page = re.sub('[^0-9]', '', self.driver.current_url)
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, '//ul[@class="pagination-list"]//a[contains(text(), "Вперед")]')))
            self.noone.next_page.click()
        except:
            return
        self.page_number = current_page
        print("Page " + current_page + " completed.")

    def run_catalog_shoes_f(self):
        self.driver.get(self.shoes_f_url)
        print("Opened url")
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
            try:
                self.sizes_product[k]['sizes'] = list(dict.fromkeys(self.sizes_product[k]['sizes']))
                self.sizes_catalog[k] = list(dict.fromkeys(self.sizes_catalog['item_id']))
                if v != self.sizes_product[k]['sizes']:
                    print(v, self.sizes_product[k]['sizes'], self.sizes_product[k]['url'])
                    self.errors.setdefault('item_id', []).append(
                        [k, self.sizes_product[k]['url'], self.page_number,
                         {'s_cat': v, 's_prod': self.sizes_product[k]['sizes']}])
            except:
                pass

    def create_report(self):
        with open('{}.json'.format(str(datetime.datetime.now())[:-7].replace(':', '-')), 'w') as t:
            if json.dumps(self.errors) == '{}':
                json.dump({"errors": 'Всё отлично! Ошибок нет.'}, t, ensure_ascii=False, indent=4)
            else:
                json.dump(self.errors, t, ensure_ascii=False, indent=4)
            t.close()

    def post_report(self):
        self.driver.get(self.project_url)
        self.driver.find_element(By.XPATH, '//input[@id="username"]').send_keys(self.login)
        self.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(self.password)
        self.driver.find_element(By.XPATH, '//input[@id="login-submit"]').click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((
            By.XPATH, '//span[contains(text(), "Редактировать")][1]')))
        self.driver.find_element(By.XPATH, '//span[contains(text(), "Редактировать")][1]').click()
        time.sleep(0.3)
        self.driver.find_element(By.XPATH, '//textarea[@id="issue_notes"]')\
            .send_keys("Данный пост создан автоматически по завершению автотеста. \n")
        self.driver.find_element(By.XPATH, '//textarea[@id="issue_notes"]').send_keys('<pre><code class="json">\n')
        self.driver.find_element(By.XPATH, '//textarea[@id="issue_notes"]')\
            .send_keys(json.dumps(self.errors, ensure_ascii=False, indent=4))
        self.driver.find_element(By.XPATH, '//textarea[@id="issue_notes"]').send_keys('\n<pre><code>')
        self.driver.find_element(By.XPATH, '//input[@name="commit" and contains(@value, "Принять")]').click()
        time.sleep(5)

    def send_report(self):
        self.driver.get(self.mail_url)
        self.driver.find_element(By.XPATH, '//input[@id="name"]').send_keys(self.login_mail)
        self.driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(self.pass_mail)
        self.driver.find_element(By.XPATH, '//input[@type="submit"]').click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//td[@id="zb__NEW_MENU_title"]')))
        self.driver.find_element(By.XPATH, '//td[@id="zb__NEW_MENU_title"]').click()
        for p in ["Анастасия Боева", "Алексей Юн", "Сергей Журавлев"]:
            address = self.driver.find_element(By.XPATH, '//div[@id="DWT52"]')
            address.click()
            address.send_keys(p)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
                (By.XPATH, '//td[contains(text(), "{}")]'.format(p))
            ))
            self.driver.find_element(By.XPATH, '//td[contains(text(), "{}")]'.format(p)).click()
        self.driver.find_element(By.XPATH, '//input[@id="zv__COMPOSE-1_subject_control"]')\
            .send_keys("Автотест размеры {}".format(datetime.date.today()))
        self.driver.find_element(By.XPATH, '//body[@id="tinymce"]').send_keys(self.errors)
        self.driver.find_element(By.XPATH, '//div[@id="zb__COMPOSE-1__SEND_MENU"]').click()

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
        for el in range(1, len(self.driver.find_elements(By.XPATH,
                '//div[@id="catalog"]//div[@class="col lg:col-4 xs:col-6"]'))):
            self.noone.catalog_nth_item(el).hover_center()
            self.noone.catalog_preview_btn.click()


test_start = "=" * 5 + "Начало тестирования {}.".format(RunFullCatalog().__class__.__name__)


if __name__ == '__main__':
    schedule.every().day.at("01:00").do(RunFullCatalog().test_run())
    while True:
        schedule.run_pending()
