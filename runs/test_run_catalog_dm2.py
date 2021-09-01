from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from runs.pages.catalog_page_dm2 import CatalogPage as Page
from runs.pages.base.logging_report import Logging, LogReport, TakeScreenshot
# from pytest import mark
import datetime
import random
import time
import re

logging = Logging()
log = logging.logger


# @mark.usefixtures('driver_init_catalog')
class RunCatalogDM2(object):
    # Настройки

    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.set_window_position(-2000, 0)
    driver.maximize_window()
    driver.implicitly_wait(4)

    # Запуск

    noone = Page(driver=driver)
    noone.go()
    url = driver.current_url

    # @mark.testrun
    def test_run(self):

        log(test_start + "Время: {}".format(str(datetime.datetime.now())))

        try:
            self.close_popups()
            self.open_category()
            self.catalog_view()
            self.select_filters()
            self.select_first_product()
            self.next_page()
            self.sort_test()
        except Exception as e:
            log("/" * 10 + "ОШИБКА: Во время работы произошёл сбой!" + "\\" * 10 + "\nОшибка: {}".format(str(e)))
            screenshot()

        log("=" * 5 + "Завершение тестирования.")
        self.driver.quit()
        LogReport(testblock=RunCatalogDM2(), logs=logging.log).test_results()

    def close_popups(self):
        log("=" * 5 + "Закрываю всплывающие окна")
        try:
            self.noone.cookies.click()
            self.noone.region_select.click()
            self.noone.region_select_moscow.click()
        except:
            log("=" * 5 + "Некоторые окна не были закрыты")

    def open_category(self):
        log("Перейти в произвольный раздел каталога.")
        # self.noone.gender_select_random(
        #     random.randrange(1, len(self.driver.find_elements_by_xpath('//ul[@class="nav-gender"]//li')))).click()
        self.noone.gender_select.click()
        time.sleep(1)
        self.noone.category_select.click()
        # self.noone.category_select_random(
        #     random.randrange(1, len(self.driver.find_elements_by_xpath('//ul[@class="nav-primary"]/li')))).click()
        log("=" * 5 + "URL: {}".format(self.driver.current_url))

    def catalog_view(self):
        log("Проверить работу сортировки каталога.")
        self.noone.button_grid_mode.click()
        try:
            test = self.driver.find_element_by_id('catalog-items')
            test_class = test.get_attribute('class')
            print(test_class, test.get_attribute('class') != test_class)
            # WebDriverWait(self.driver, 10).until(test.get_attribute('class') != test_class)  # Redundant
            if test.get_attribute('class') == 'catalog-view-2':
                log('=' * 5 + "Успех проверки работы сортировки каталога.")
            else:
                log("/" * 10 +
                    "Ошибка: Функция работает неправильно: div#catalog-items не поменял класс с 1 на 2!"
                    + "\\" * 10)
        except:
            log("/" * 10 + "Ошибка: Элемент не найден!" + "\\" * 10)
        log("=" * 5 + "Нажимаю ещё раз")
        self.noone.button_grid_mode.click()
        try:
            test = self.driver.find_element_by_id('catalog-items')
            WebDriverWait(self.driver, 10).until(test.get_attribute('class') == 'catalog-view-2')
            log("=" * 5 + "Успех повторной проверки работы сортировки каталога.")
        except:
            log("/" * 10 + "Ошибка: Функция работает неправильно, либо элемент не найден!" + "\\" * 10)

    def select_filters(self):
        log("Раскрыть фильтры меню")
        for i in self.driver.find_elements_by_xpath(
                '//div[@class="filter-secondary filter-panel filter-panel-collapse filter-panel-open"]/div/div'):
            try:
                i.click()
                log("=" * 5 + "Фильтр раскрыт")
            except:
                log("=" * 5 + "Проблема с поиском закрытых фильтров, пробую открыть ещё раз")
                self.driver.execute_script('window.scrollBy(0,100)')
                try:
                    i.click()
                    log("=" * 5 + "Фильтр раскрыт")
                except:
                    log("=" * 5 + "Все фильтры раскрыты")
        log("Выбрать произвольные фильтры")

        category = self.driver.find_element_by_xpath("//div[@id='block-CATEGORY']")
        brand = self.driver.find_element_by_xpath("//div[@id='block-BRAND']")
        try:
            category_elem = category.find_element_by_xpath(".//li[@class='filter-item filter-item-default'][{}]"
                                       .format(random.randrange(1, len(self.driver.find_elements_by_xpath(
            "//div[@id='block-CATEGORY']//li[@class='filter-item filter-item-default']")), 1)))
        except:
            category_elem = category.find_element_by_xpath(".//li[@class='filter-item filter-item-default']")
        try:
            brand_elem = brand.find_element_by_xpath(".//li[@class='filter-item filter-item-default'][{}]".format(
                random.randrange(1, len(brand.find_elements_by_xpath('.//li[@class="filter-item filter-item-default"]')))
            ))
        except:
            brand_elem = brand.find_element_by_xpath(".//li[@class='filter-item filter-item-default']")
        try:
            color = self.noone.filter_color(
                random.randrange(1, len(self.driver.find_elements_by_xpath(
                    "//div[@id='block-COLOR_GROUP']//li[@class='filter-item filter-item-color']")), 1)
            )
        except:
            color = self.noone.filter_color(1)

        filters = [
            category_elem,
            brand_elem,
            color
            # self.noone.filter_model(
            #     random.randrange(1, len(self.driver.find_elements_by_xpath(
            #         "//div[@id='block-MODEL']//li[@class='filter-item filter-item-default ']")), 1)
            # ),
            # self.noone.filter_basic_material(
            #     random.randrange(1, len(self.driver.find_elements_by_xpath(
            #         "//div[@id='block-BASIC_MATERIAL']//li[@class='filter-item filter-item-default ']")), 1)
            # ),
            # self.noone.filter_lining_material(
            #     random.randrange(1, len(self.driver.find_elements_by_xpath(
            #         "//div[@id='block-LINING_MATERIAL']//li[@class='filter-item filter-item-default ']")), 1)
            # ),
            # self.noone.filter_group(
            #     random.randrange(1, len(self.driver.find_elements_by_xpath(
            #         "//div[@id='block-GROUP_REF']//li[@class='filter-item filter-item-default ']")), 1)
            # )
        ]
        for el in filters:
            print(el)
            try:
                log("=" * 5 + "Тестирую {}".format(el))
                el.click()
                time.sleep(1)
            except:
                log("/" * 10 + "ОШИБКА: Один из фильтров не был найден ({})! См. по ссылке".format(el) + "\\" * 10)
                screenshot()

    def select_first_product(self):
        log("Добавить первый товар в корзину")
        try:
            log("=" * 5 + 'Навести мышкой на товар')
            self.noone.catalog_item.hover_center()
            log("=" * 5 + "Предпросмотр товара")
            self.noone.item_preview.click()
            time.sleep(1)
            self.driver.execute_script('document.querySelector(".modal-item-view").click()')
            self.noone.catalog_item.hover_center()
            log("=" * 5 + 'Добавить товар (нажать)')
            self.noone.catalog_item_add.click()
            log("=" * 5 + 'Выбрать размер')
            self.noone.size_select.click()
            log("=" * 5 + 'Добавить в корзину')
            self.noone.add_to_cart.click()
            self.noone.bootbox_accept.click()
        except:
            log("Товары не отобразились, пробую перезагрузить фильтры")
            self.driver.refresh()
            self.select_filters()
            self.noone.catalog_item.hover_center()
            self.noone.catalog_item_add.click()
            self.noone.bootbox_accept.click()

    def next_page(self):
        try:
            self.open_category()
            log("Проверить работу пагинации")
            self.noone.next_page.click()
            self.noone.go_back()
            log("=" * 5 + "Пагинация работает")
        except:
            log("/" * 10 + "Кнопки 'Вперед' нет, либо не работает пагинация" + "\\" * 10)

    def sort_test(self):
        self.open_category()
        log("Проверить сортировку товаров")
        self.noone.sort_button.click()
        self.noone.sort_option_grow.click()
        self._sort_compare('item-price', "span[@class='item-price-new text-data']")
        self.noone.sort_button.click()
        self.noone.sort_option_shrink.click()
        self._sort_compare('item-price', "span[@class='item-price-new text-data']")
        self.noone.sort_button.click()
        self.noone.sort_option_discount.click()
        self._sort_compare('item-label-list', "div[@class='item-label item-label-discount']")

    def favs(self):
        log("Проверить работу кнопки \"Добавить в избранное\"")
        self.open_category()
        self.noone.catalog_item.hover_center()
        log("=" * 5 + 'Добавить товар в избранное')
        self.noone.catalog_item_fav.click()
        log("=" * 5 + "Убрать товар из избранного")
        self.noone.catalog_item_fav.click()

    def _sort_compare(self, classinfo, item):
        """
        Сравнивает получаемые значения полей
        :param classinfo:
        :param item:
        :return:
        """
        compare = []
        n = 1
        for el in self.driver.find_elements_by_xpath('//div[@id="catalog-items"]//div[@class="col lg:col-4 xs:col-6"]'):
            element = self.driver.find_element_by_xpath(
                '//div[@id="catalog-items"]//div[@class="col lg:col-4 xs:col-6"][{}]//div[@class="{}"]//{}'
                    .format(n, classinfo, item))
            compare.append(int(re.sub('[^0-9]', '', element.text)))
            n += 1
        print(compare)
        return log("=" * 5 + 'Первый товар > последний: {}'.format(compare[0] > compare[-1]))


def screenshot():
    TakeScreenshot(RunCatalogDM2()).take_screenshot()


test_start = "=" * 5 + "Начало тестирования {}.".format(RunCatalogDM2().__class__.__name__)

if __name__ == '__main__':
    RunCatalogDM2().test_run()
    test_start = "=" * 5 + "Начало тестирования."
