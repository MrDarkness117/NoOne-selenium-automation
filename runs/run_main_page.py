from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
# from pages.dm2_main_page import MainPage
from runs.pages.main_page import MainPage
from runs.pages.base.logging_report import Logging, LogReport, TakeScreenshot
import time
import random
import datetime

logging = Logging()
log = logging.logger

options = Options()
browser = webdriver.Chrome(options=options)
browser.set_window_position(-2000, 0)
browser.maximize_window()
browser.implicitly_wait(3)
url = browser.current_url

noone = MainPage(driver=browser)
noone.go()

# Команды


class RunMainPage(object):

    driver = browser

    def test_run(self):

        log(test_start + "Время: {}".format(str(datetime.datetime.now())))

        try:
            try:
                log("Выбрать регион")
                noone.region_confirm.click()
            except:
                log("=" * 5 + "No region requested")

            try:
                log("Принять Cookies")
                noone.cookies.click()
            except:
                log("=" * 5 + "No cookies requested")

            log("Навести мышкой на карточку продукта")
            noone.dy_product_card.hover_center()
            browser.execute_script("window.scrollBy(0, 80)")

            try:
                log("Принять Cookies")
                noone.cookies.click()
            except:
                log("=" * 5 + "No cookies requested")
            log("Нажать на кнопку быстрого просмотра продукта")
            noone.dy_product_window.click()
            log("Нажать на кнопку покупки")
            noone.item_buy.click()
            log("Получить уведомление, нажать ОК")
            noone.modal_ok.click()
            log("Выбрать размер продукта")
            # try:
            #     noone.item_size(len(self.driver.find_elements_by_xpath('//ul[@id="size-list"]//li[contains(@class, "item-size")]'))).click()
            # except:
            #     try:
            #         noone.item_size_single.click()
            #     except:
            #         log("="*5 + "Нет доступных размеров")
            noone.item_size.click()
            log("Добавить продукт в корзину")
            noone.item_buy.click()
            log("Нажать на кнопку 'Принять'")
            noone.item_bootbox_accept.click()
            # noone.item_bootbox_close.click()
            log("Перейти на страницу товара, дождаться загрузки")
            noone.go_back()
            time.sleep(random.randint(0, 10))
            log("Нажать на промо-баннер, дождаться загрузки")
            time.sleep(1)
            noone.promo_banner.click()
            WebDriverWait(browser, 10).until(lambda browser: browser.current_url != url)
            log("Вернуться на одну страницу назад")
            noone.go_back()
            log("Нажать на первый источник журнала, дождаться загрузки")
            noone.journal.click()
            time.sleep(2)
        except Exception as e:
            log("/" * 10 + "ОШИБКА: Во время работы произошёл сбой!" + "\\" * 10 + "\nОшибка: {}".format(str(e)))
            TakeScreenshot(RunMainPage()).take_screenshot()

        log("=" * 5 + "Завершение тестирования.")
        browser.quit()

        LogReport(testblock=RunMainPage(), logs=logging.log).test_results()


test_start = "=" * 5 + "Начало тестирования {}.".format(RunMainPage().__class__.__name__)


if __name__ == '__main__':
    RunMainPage().test_run()
    test_start = "=" * 5 + "Начало тестирования."
