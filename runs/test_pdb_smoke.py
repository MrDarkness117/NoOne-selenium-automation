import datetime
import random
import time
import json
import re
# import schedule
import logging as exceptions
import smtplib

from email import message

from os import path
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from pages.pdb_smoke_page import PDBSmokePage as Page
from pages.base.logging_report import Logging, LogReport, TakeScreenshot

logging = Logging()
log = logging.logger



class PDBSmokeTest(object):
    # Настройки

    login = 'm.romantsov@noone.ru'
    password = 'mihailo117'

    options = Options()
    options.add_argument("--window-position=-2000,0")
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option('prefs', prefs)
    # driver = webdriver.Chrome(options=options)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.set_window_position(-2000, 0)
    driver.maximize_window()
    driver.implicitly_wait(3)

    wait = WebDriverWait(driver, 10)

    # Запуск

    pdb = Page(driver=driver)
    pdb.go()
    url = driver.current_url

    def test_run(self):

        log(test_start + "Время: {}".format(str(datetime.datetime.now())))

        try:
            self.change_country()
            self.auth()
            self.catalog()
            self.item()
            self.cart()

        except Exception as e:
            exceptions.exception('message')
            log("/" * 10 + "ОШИБКА: Во время работы произошёл сбой!" + "\\" * 10 + "\nОшибка: {}".format(e))
            print("/" * 10 + "ОШИБКА: Во время работы произошёл сбой!" + "\\" * 10 + "\nОшибка: {}".format(e))
            TakeScreenshot(PDBSmokeTest()).take_screenshot()

        log("=" * 5 + "Завершение тестирования.")

        self.driver.quit()
        LogReport(testblock=PDBSmokeTest(), logs=logging.log).test_results()

    def change_country(self):
        self.pdb.change_country.click()
        self.pdb.select_country.click()

    def auth(self):
        self.pdb.auth_button.click()
        self.pdb.auth_email.input_text(self.login)
        self.pdb.auth_password.input_text(self.password)
        self.pdb.auth_sign_in.click()

    def catalog(self):
        time.sleep(3)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="https://principedibologna.it/catalog"]/..')))\
            .click()
        # self.pdb.catalog_button.click()
        self.pdb.catalog_item.click()

    def item(self):
        self.pdb.item_size.click()
        self.pdb.add_to_cart.click()

    def cart(self):
        self.pdb.cart_button.click()
        time.sleep(3)
        current_price = int(re.sub('[^0-9]', '', self.pdb.cart_item_price(1).text))
        print(current_price)
        delivery_cost = int(re.sub('[^0-9]', '', self.pdb.delivery_cost.text))
        print(delivery_cost)
        total_price = int(re.sub('[^0-9]', '', self.pdb.price_total.text))
        print(total_price)
        item_amount = int(self.pdb.item_count().text)
        assert total_price == (current_price * item_amount) + delivery_cost


test_start = "=" * 5 + "Начало тестирования {}.".format(PDBSmokeTest().__class__.__name__)


if __name__ == '__main__':
    PDBSmokeTest().test_run()
