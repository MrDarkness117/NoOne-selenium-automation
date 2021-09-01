from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from runs.pages.main_page_dm2 import MainPage as Page
from runs.pages.base.logging_report import Logging, LogReport, TakeScreenshot
import time
import random
from pytest import mark
import datetime

logging = Logging()
log = logging.logger

options = Options()
browser = webdriver.Chrome(options=options)
browser.set_window_position(-2000, 0)
browser.maximize_window()
browser.implicitly_wait(3)
url = browser.current_url

noone = Page(driver=browser)
noone.go()


@mark.usefixtures('driver_init_main_page')
class RunMainPageDM2(object):

    def test_run(self):

        # Команды

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

            # FIXME: для dm2 данный функционал нужно переделать
            # log("Навести мышкой на карточку продукта")
            # noone.dy_product_card.hover_center()
            # browser.execute_script("window.scrollBy(0, 80)")

            """try:
                print("looking for ribbon...")
                WebDriverWait(browser, 10).until(
                    EC.frame_to_be_available_and_switch_to_it(browser.find_element_by_xpath("//iframe[@id='fl-450213']"))
                )
                # ribbon = browser.find_element(value='fl-450213')
                # browser.switch_to.frame(ribbon)
                print("iframe found")
                # print(ribbon)
                # noone.footer_ribbon.click()
                browser.find_element_by_id('Ribbon-close').click()
                print("closed iframe")
                browser.switch_to.default_content()
            except:
                print("No ribbon appeared")"""

            # log("Нажать на кнопку окна продукта")
            # noone.dy_product_window.click()
            # log("Нажать на кнопку покупки")
            # noone.item_buy.click()
            # log("Выбрать размер продукта")
            # try:
            #     noone.item_size(len(self.driver.find_elements_by_xpath('//ul[@id="size-list"]//li[contains(@class, "item-size")]'))).click()
            # except:
            #     try:
            #         noone.item_size_single.click()
            #     except:
            #         log("="*5 + "Нет доступных размеров")
            # noone.item_add.click()
            # log("Нажать на кнопку 'Приинять'")
            # noone.item_bootbox_accept.click()
            # # noone.item_bootbox_close.click()
            # log("Перейти на страницу товара, дождаться загрузки")
            # noone.item_info_page.click()
            # WebDriverWait(browser, 10).until(lambda browser: browser.current_url != url)
            # time.sleep(2)
            # log("Вернуться на одну страницу назад")
            # noone.go_back()  # после загрузки страницы товара
            # time.sleep(random.randint(0, 10))
            log("Нажать на промо-баннер, дождаться загрузки")
            time.sleep(1)
            # WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="promo"]//div[@class="carousel"]')))
            # Удивительно, но WebDriverWait не помогает. Time.sleep помогает. Как??
            noone.promo_banner.click()
            WebDriverWait(browser, 10).until(lambda browser: browser.current_url != url)
            time.sleep(2)
            log("Вернуться на одну страницу назад")
            noone.go_back()
            log("Нажать на первый источник журнала, дождаться загрузки")
            noone.journal.click()
            time.sleep(2)
        except Exception as e:
            log("/" * 10 + "ОШИБКА: Во время работы произошёл сбой!" + "\\" * 10 + "\nОшибка: {}".format(str(e)))
            TakeScreenshot(RunMainPageDM2()).take_screenshot()

        log("=" * 5 + "Завершение тестирования.")
        browser.quit()
        LogReport(testblock=RunMainPageDM2(), logs=logging.log).test_results()


test_start = "=" * 5 + "Начало тестирования {}.".format(RunMainPageDM2().__class__.__name__)


if __name__ == '__main__':
    RunMainPageDM2().test_run()
    test_start = "=" * 5 + "Начало тестирования."
