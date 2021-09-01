import random
import datetime
from pytest import mark
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.wait import WebDriverWait
from runs.pages.main_page_dm2 import MainPage
# from runs.pages.base.logger_config_ import warn, info, err, exc
from runs.pages.base.logging_report import Logging, LogReport, TakeScreenshot

import time

# Настройки

logging = Logging()
log = logging.logger

options = Options()
# options.add_argument("--window-position=-2000,0")
driver = webdriver.Chrome(options=options)
driver.set_window_position(-2000, 0)
driver.maximize_window()
driver.implicitly_wait(3)

city_list = {
    "Москва": '77000000000',  # Москва
    "Красноярск": '24000001000',  # Красноярск
    "Ростов-на-Дону": '61000001000',  # Ростов-на-Дону
    "Самара": '63000001000',  # Самара
    "Екатеринбург": '66000001000',  # Екатеринбург
    "Краснодар": '23000001000',  # Краснодар
    "Уфа": '02000001000',  # Уфа
    "Новосибирск": '54000001000',  # Новосибирск
    "Волгоград": '34000001000',  # Волгоград
    "Санкт-Петербург": '78000000000',  # Санкт-Петербург
    "Казань": '16000001000',  # Казань
}
search_value = "зонт"

noone = MainPage(driver=driver)
noone.go()
url = driver.current_url


@mark.usefixtures('driver_init_header')
class RunHeaderDM2(object):

    def test_run(self):

        log(test_start + "Время: {}".format(str(datetime.datetime.now())))

        # Стандартные команды

        try:
            try:
                noone.region_confirm.click()
            except:
                log("="*5 + "No region requested")

            try:
                noone.cookies.click()
            except:
                log("="*5 + "No cookies requested")

            # Команды тестирования шапки

            log("Проверить загрузку городов")
            for city, code in city_list.items():
                log("="*5 + "Проверка загрузки города {}".format(city))
                try:
                    noone.city_menu.click()
                    log("="*5 + "Пробую код: {}".format(code))
                    noone.city_selector(code=code).click()
                    log("="*5 + "Город {}: Найден".format(city))
                    time.sleep(1)
                except:
                    log("/"*10 + "Город {}: Ошибка - элемент не найден!".format(city) + "\\"*10)

                # try:
                #     WebDriverWait(driver, 4).until(lambda driver: driver.current_url != url)
                # except:
                #     print("Ошибка загрузки страницы!")

            log("="*5 + "Проверка городов завершена!")
            try:
                log("Перейти на страницу авторизации")
                noone.auth_link.click()
            except:
                log("/"*10 + "Ошибка перехода на страницу авторизации!" + "\\"*10)
            log("Проверить загрузку страницы по логотипу")
            noone.logo.click()
            # WebDriverWait(driver, 15).until(lambda driver: driver.current_url == "https://noone.ru")
            log("Проверить поле ввода текста")
            noone.search_input.input_text(search_value)
            log("="*5 + "Поиск по '{}'".format(search_value))
            noone.search_btn.click()

            time.sleep(3)

            try:
                log("Проверить работу по переходу в корзину")
                noone.cart.click()
                time.sleep(3)
                log("="*5 + "Успех, возврат на главную страницу")
            except:
                log("/"*10 + "Ошибка перехода в корзину!" + "\\"*10)
            try:
                log("Вернуться на главную страницу")
                self.noone.logo_basket.click()
            except:
                log("=" * 5 + "Пробую закрыть всплывающие окна")
                self.driver.execute_script('document.querySelector(".flocktory-widget-overlay").click()')
                self.noone.logo_basket.click()

            try:
                log("Пробую перейти в каталог")
                log("=" * 5 + "Выбираю раздел полов")
                self.noone.gender_select(
                    random.randint(1, len(self.driver.find_elements_by_xpath('//ul[@class="nav-gender"]//li'))
                                   )).click()
                log("=" * 5 + "Выбираю раздел товаров")
                self.noone.category_select(
                    random.randint(1, len(self.driver.find_elements_by_xpath('//ul[@class="nav-primary"]/li'))
                                   )).click()
            except:
                log("=" * 5 + "Пробую закрыть всплывающие окна")
                self.driver.execute_script('document.querySelector(".flocktory-widget-overlay").click()')
                log("=" * 5 + "Окно закрыто.")

                self.noone.gender_select(
                    random.randint(1, len(self.driver.find_elements_by_xpath('//ul[@class="nav-gender"]//li'))
                                   )).click()
                time.sleep(1)
                self.noone.category_select(
                    random.randint(1, len(self.driver.find_elements_by_xpath('//ul[@class="nav-primary"]/li'))
                                   )).click()
        except Exception as e:
            log("/" * 10 + "ОШИБКА: Во время работы произошёл сбой!" + "\\" * 10 + "\nОшибка: {0}".format(str(e)))
            TakeScreenshot(RunHeaderDM2()).take_screenshot()

        log("="*5 + "Завершение тестирования.")
        time.sleep(2)
        driver.quit()
        LogReport(testblock=RunHeaderDM2(), logs=logging.log).test_results()


test_start = "=" * 5 + "Начало тестирования {}.".format(RunHeaderDM2().__class__.__name__)


if __name__ == '__main__':
    RunHeaderDM2().test_run()
    test_start = "=" * 5 + "Начало тестирования."
