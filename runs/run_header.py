import random
import time
import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from runs.pages.main_page import MainPage
from runs.pages.base.logging_report import Logging, LogReport, TakeScreenshot


# Настройки

logging = Logging()
log = logging.logger


class RunHeader(object):

    options = Options()
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
    search_value = "мокасины"

    noone = MainPage(driver=driver)
    noone.go()
    url = driver.current_url

    def test_run(self):

        # Стандартные команды

        log(test_start + "Время: {}".format(str(datetime.datetime.now())))

        try:
            try:
                self.noone.region_confirm.click()
            except:
                log("="*5 + "No region requested")

            try:
                self.noone.cookies.click()
            except:
                log("="*5 + "No cookies requested")

            # Команды тестирования шапки

            log("Проверить загрузку городов")
            for city, code in self.city_list.items():
                log("="*5 + "Проверка загрузки города {}".format(city))
                try:
                    self.noone.city_menu.click()
                    log("="*5 + "Пробую код: {}".format(code))
                    self.noone.city_selector(code=code).click()
                    log("="*5 + "Город {}: Найден".format(city))
                    time.sleep(0.5)
                except:
                    log("/"*10 + "Город {}: Ошибка - элемент не найден!".format(city) + "\\"*10)
                    try:
                        log("="*5 + "Пробую закрыть всплывающие окна")
                        self.driver.execute_script('document.querySelector(".flocktory-widget-overlay").click()')
                        self.noone.city_menu.click()
                        log("="*5 + "Пробую код: {}".format(code))
                        self.noone.city_selector(code=code).click()
                        log("="*5 + "Город {}: Найден".format(city))

                    except:
                        log("/"*10 + "Критическая ошибка." + "\\"*10)

            log("="*5 + "Проверка городов завершена!")
            log("Проверить скроллинг и закрепление шапки сайта (.header -> .header.header-fixed)")
            self.driver.execute_script('window.scrollTo(0, 400);')
            if self.driver.find_element_by_tag_name('header').get_attribute('class') == 'header header-fixed':
                log("="*5 + "Скроллинг работает правильно, шапка сайта закрепилась!")
            else:
                log("/"*10 + "Ошибка работы скроллинга!" + "\\"*10)
            self.driver.execute_script('window.scrollTo(0, -400);')
            try:
                log("Перейти на страницу авторизации")
                self.noone.auth_link.click()
            except:
                log("/"*10 + "Ошибка перехода на страницу авторизации!" + "\\"*10)
            log("Проверить загрузку страницы по логотипу")
            self.noone.logo.click()
            log("Проверить поле ввода текста")
            self.noone.search_input.input_text(self.search_value)
            log("="*5 + "Поиск по '{}'".format(self.search_value))
            self.noone.search_btn.click()

            time.sleep(3)

            try:
                log("Проверить работу по переходу в корзину")
                self.noone.cart.click()
                time.sleep(3)
                log("="*5 + "Успех, возврат на главную страницу")
            except:
                log("/"*10 + "Ошибка перехода в корзину!" + "\\"*10)
            try:
                log("Вернуться на главную страницу")
                self.noone.logo_basket.click()
            except:
                log("="*5 + "Пробую закрыть всплывающие окна")
                self.driver.execute_script('document.querySelector(".flocktory-widget-overlay").click()')
                self.noone.logo_basket.click()

            try:
                log("Пробую перейти в каталог")
                log("="*5 + "Выбираю раздел полов")
                self.noone.gender_select(random.randint(1, len(self.driver.find_elements_by_xpath('//ul[@class="nav-gender"]//li'))
                                                   )).click()
                log("="*5 + "Выбираю раздел товаров")
                self.noone.category_select(random.randint(1, len(self.driver.find_elements_by_xpath('//ul[@class="nav-primary"]/li'))
                                                     )).click()
            except:
                log("="*5 + "Пробую закрыть всплывающие окна")
                self.driver.execute_script('document.querySelector(".flocktory-widget-overlay").click()')
                log("="*5 + "Окно закрыто.")

                self.noone.gender_select(random.randint(1, len(self.driver.find_elements_by_xpath('//ul[@class="nav-gender"]//li'))
                                                   )).click()
                time.sleep(1)
                self.noone.category_select(random.randint(1, len(self.driver.find_elements_by_xpath('//ul[@class="nav-primary"]/li'))
                                                     )).click()
        except Exception as e:
            log("/" * 10 + "ОШИБКА: Во время работы произошёл сбой!" + "\\" * 10 + "\nОшибка: {0}".format(str(e)))
            TakeScreenshot(RunHeader()).take_screenshot()

        log("="*5 + "Завершение тестирования.")
        time.sleep(2)
        self.driver.quit()
        LogReport(testblock=RunHeader(), logs=logging.log).test_results()


test_start = "=" * 5 + "Начало тестирования {}.".format(RunHeader().__class__.__name__)


if __name__ == '__main__':
    RunHeader().test_run()
    test_start = "=" * 5 + "Начало тестирования."
