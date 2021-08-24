import random

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.wait import WebDriverWait
from runs.pages.main_page import MainPage
# from runs.pages.base.logger_config_ import warn, info, err, exc
from runs.pages.base.logging_report import Logging, LogReport, TakeScreenshot

import time

# Настройки

logging = Logging()
log = logging.logger

options = Options()
driver = webdriver.Chrome(options=options)
driver.set_window_position(0, 0)
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
search_value = "мокасины"

noone = MainPage(driver=driver)
noone.go()
url = driver.current_url


class RunHeader(object):

    def test_run(self):

        # Стандартные команды

        log(test_start)
        
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
                except:
                    log("/"*10 + "Город {}: Ошибка - элемент не найден!".format(city) + "\\"*10)
                    try:
                        log("="*5 + "Пробую закрыть всплывающие окна")
                        driver.execute_script('document.querySelector(".flocktory-widget-overlay").click()')

                        # driver.switch_to.frame(driver.find_elements_by_css_selector("iframe[id='fl-513145']"))
                        # print("Переключен на iframe")
                        # driver.find_elements_by_xpath('//div[@class="widget__close js-collapse-login"]').click()
                        # print("iframe закрыт")
                        # driver.switch_to.default_content()

                        noone.city_menu.click()
                        log("="*5 + "Пробую код: {}".format(code))
                        noone.city_selector(code=code).click()
                        log("="*5 + "Город {}: Найден".format(city))

                    except:
                        log("/"*10 + "Критическая ошибка." + "\\"*10)

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
                noone.logo_basket.click()
            except:
                log("="*5 + "Пробую закрыть всплывающие окна")
                driver.execute_script('document.querySelector(".flocktory-widget-overlay").click()')
                noone.logo_basket.click()

            try:
                noone.gender_select(random.randint(1, len(driver.find_elements_by_xpath('//ul[@class="nav-gender"]//li'))
                                                   )).click()
                noone.category_select(random.randint(1, len(driver.find_elements_by_tag_name('ul.nav-primary > li'))
                                                     )).click()
            except:
                log("="*5 + "Пробую закрыть всплывающие окна")
                driver.execute_script('document.querySelector(".flocktory-widget-overlay").click()')
                log("="*5 + "Окно закрыто.")

                noone.gender_select(random.randint(1, len(driver.find_elements_by_xpath('//ul[@class="nav-gender"]//li'))
                                                   )).click()
                time.sleep(1)
                noone.category_select(random.randint(1, len(driver.find_elements_by_tag_name('ul.nav-primary > li'))
                                                     )).click()
        except Exception as e:
            log("/" * 10 + "ОШИБКА: Во время работы произошёл сбой!" + "\\" * 10 + "\nОшибка: {}".format(e))
            TakeScreenshot(RunHeader()).take_screenshot()

        log("="*5 + "Завершение тестирования.")
        time.sleep(2)
        driver.quit()
        LogReport(testblock=RunHeader(), logs=logging.log).test_results()


test_start = "=" * 5 + "Начало тестирования {}.".format(RunHeader().__class__.__name__)


if __name__ == '__main__':
    RunHeader().test_run()
    test_start = "=" * 5 + "Начало тестирования."
