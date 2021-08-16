import random

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support.wait import WebDriverWait
from runs.pages.main_page import MainPage
from runs.pages.base.logger_config_ import warn, info, err, exc
from runs.pages.base.logging_report import Logging, LogReport

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

        try:
            noone.region_confirm.click()
        except:
            warn("No region requested")

        try:
            noone.cookies.click()
        except:
            warn("No cookies requested")

        # Команды тестирования шапки

        for city, code in city_list.items():
            info("Тестирую загрузку города {}".format(city))
            try:
                noone.city_menu.click()
                info("Пробую код: {}".format(code))
                noone.city_selector(code=code).click()
                info("Город {}: Найден".format(city))
            except:
                warn("Город {}: Ошибка - элемент не найден!".format(city))
                try:
                    info("Пробую закрыть всплывающие окна")
                    driver.execute_script('document.querySelector(".flocktory-widget-overlay").click()')

                    # driver.switch_to.frame(driver.find_elements_by_css_selector("iframe[id='fl-513145']"))
                    # print("Переключен на iframe")
                    # driver.find_elements_by_xpath('//div[@class="widget__close js-collapse-login"]').click()
                    # print("iframe закрыт")
                    # driver.switch_to.default_content()

                    noone.city_menu.click()
                    info("Пробую код: {}".format(code))
                    noone.city_selector(code=code).click()
                    info("Город {}: Найден".format(city))

                except:
                    err("Failed.")

            # try:
            #     WebDriverWait(driver, 4).until(lambda driver: driver.current_url != url)
            # except:
            #     print("Ошибка загрузки страницы!")

        info("Проверка городов завершена!")
        try:
            info("Переход на страницу авторизации")
            noone.auth_link.click()
        except:
            err("Ошибка перехода на страницу авторизации!")
        info("Проверка загрузки страницы по логотипу")
        noone.logo.click()
        # WebDriverWait(driver, 15).until(lambda driver: driver.current_url == "https://noone.ru")
        info("Проверка поля ввода текста")
        noone.search_input.input_text(search_value)
        info("Поиск по '{}'".format(search_value))
        noone.search_btn.click()

        time.sleep(3)

        try:
            info("Проверка работы по переходу в корзину")
            noone.cart.click()
            time.sleep(3)
            info("Успех, возврат на главную страницу")
        except:
            err("Ошибка перехода в корзину!")
        try:
            noone.logo_basket.click()
        except:
            info("Пробую закрыть всплывающие окна")
            driver.execute_script('document.querySelector(".flocktory-widget-overlay").click()')
            noone.logo_basket.click()

        try:
            noone.gender_select(random.randint(1, len(driver.find_elements_by_xpath('//ul[@class="nav-gender"]//li'))
                                               )).click()
            noone.category_select(random.randint(1, len(driver.find_elements_by_tag_name('ul.nav-primary > li'))
                                                 )).click()
        except:
            info("Пробую закрыть всплывающие окна")
            driver.execute_script('document.querySelector(".flocktory-widget-overlay").click()')
            info("Окно закрыто.")

            noone.gender_select(random.randint(1, len(driver.find_elements_by_xpath('//ul[@class="nav-gender"]//li'))
                                               )).click()
            time.sleep(1)
            noone.category_select(random.randint(1, len(driver.find_elements_by_tag_name('ul.nav-primary > li'))
                                                 )).click()

        info("Завершение тестирования.")


time.sleep(4)
driver.quit()
LogReport(testblock=RunHeader(), logs=logging.log).test_results()
