import datetime
import random
import time
import json

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from runs.pages.item_id_page import ItemIDPage as Page
from runs.pages.base.logging_report import Logging, LogReport, TakeScreenshot

logging = Logging()
log = logging.logger


class RunItemID(object):

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

        with open('../ids.json') as i:
            data = json.load(i)

        try:
            self.noone.region_confirm.click()
            time.sleep(1)
            self.noone.cookies.click()

            for d in data:
                self.search_item(d)
                self.item_page()

        except Exception as e:
            log("/" * 10 + "ОШИБКА: Во время работы произошёл сбой!" + "\\" * 10 + "\nОшибка: {}".format(e))
            print(e)
            TakeScreenshot(RunItemID()).take_screenshot()

        log("=" * 5 + "Завершение тестирования.")

        self.driver.quit()
        LogReport(testblock=RunItemID(), logs=logging.log).test_results()

    def search_item(self, n):
        self.noone.search_field.click()
        self.noone.search_field.input_text(str(n))
        self.noone.search_submit.click()

        self.noone.first_item.click()

    def item_page(self):
        try:
            log("="*5 + "Проверка выбора размера (обуви/одежды)")
            self.noone.item_page_sizes.find()
            self.noone.item_page_size.click()
        except Exception as e:
            log("/"*10 + "У товара нет размеров" + "\\"*10)

        try:
            log("="*5 + "Проверка наличия выбора вариантов цвета")
            self.noone.item_page_color_list.find()
            self.noone.item_page_color_option.find()
        except:
            log("/"*10 + "У товара нет выбора вариантов цвета" + "\\"*10)

        try:
            log("="*5 + "Проверка резервирования")
            self.noone.item_page_preview_reserve.click()
        except:
            log("/"*10 + "У товара нет вариантов резервирования" + "\\"*10)

        try:
            self.noone.item_page_preview_reserve_boutique.click()
            self.noone.item_page_preview_reserve_reserve.find()
            self.noone.item_page_preview_reserve_close.click()
        except:
            log('/'*10 + "ОШИБКА РАБОТЫ РЕЗЕРВИРОВАНИЯ!" + "\\"*10)


test_start = "=" * 5 + "Начало тестирования {}.".format(RunItemID().__class__.__name__)


if __name__ == '__main__':
    RunItemID().test_run()
    test_start = "=" * 5 + "Начало тестирования."