from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from runs.pages.catalog_page import CatalogPage as Page
from runs.pages.base.logging_report import Logging, LogReport, TakeScreenshot
import random

logging = Logging()
log = logging.logger


class RunCatalog(object):
    # Настройки

    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.set_window_position(-2000, 0)
    driver.maximize_window()
    driver.implicitly_wait(3)
    screenshot = TakeScreenshot(driver).take_screenshot()

    # Запуск

    noone = Page(driver=driver)
    noone.go()
    url = driver.current_url

    def test_run(self):

        log("=" * 5 + "Начало тестирования.")

        try:
            self.open_category()
            self.catalog_view()

        except:
            log("/" * 10 + "ОШИБКА: Во время работы произошёл сбой!" + "\\" * 10)

        log("=" * 5 + "Завершение тестирования.")

        self.driver.quit()

    def open_category(self):
        log("Перейти в произвольный раздел каталога.")
        self.noone.gender_select_random.click()
        self.noone.category_select_random.click()
        log("=" * 5 + "URL: {}".format(self.driver.current_url))

    def catalog_view(self):
        log("Проверить работу сортировки каталога.")
        self.noone.button_grid_mode.click()
        try:
            test = self.driver.find_element_by_id('catalog-items')
            test_class = test.get_attribute('class')
            WebDriverWait(self.driver, 10).until(test.get_attribute('class') != test_class)
            if test.get_attribute('class') == 'catalog-view-2':
                log('=' * 5 + "Успех проверки работы сортировки каталога.")
            else:
                log("/" * 10 +
                    "Ошибка: Функция работает неправильно: div#catalog-items не поменял класс с 1 на 2!"
                    + "\\" * 10)
        except:
            log("/" * 10 + "Ошибка: Элемент не найден!" + "\\" * 10)
        self.noone.button_grid_mode.click()
        try:
            test = self.driver.find_element_by_id('catalog-items')
            test_class = test.get_attribute('class')
            WebDriverWait(self.driver, 10).until(test.get_attribute('class') != test_class)
            log("=" * 5 + "Успех повторной проверки работы сортировки каталога.")
        except:
            log("/" * 10 + "Ошибка: Функция работает неправильно, либо элемент не найден!" + "\\" * 10)

    def select_filters(self):
        log("Выбрать произвольные фильтры")
        try:
            for el in [
                self.noone.filter_category(
                    random.randrange(1, len(self.driver.find_elements_by_xpath("//div[@id='block-CATEGORY']//li")), 1)
                ),
                self.noone.filter_brand(
                    random.randrange(1, len(self.driver.find_elements_by_xpath("//div[@id='block-BRAND']//li")), 1)
                ),
                self.noone.filter_size(
                    random.randrange(1, len(self.driver.find_elements_by_xpath("//div[@id='block-RAZMER']//li")), 1)
                ),
                self.noone.filter_color(
                    random.randrange(1, len(self.driver.find_elements_by_xpath(
                        "//div[@id='block-COLOR_GROUP']//ul[@class='filter-list filter-list-colors']//li")), 1)
                ),
                self.noone.filter_season(
                    random.randrange(1, len(self.driver.find_elements_by_xpath("//div[@id='block-SEASONALITY']//li")),
                                     1)
                ),
                self.noone.filter_collection(
                    random.randrange(1, len(self.driver.find_elements_by_xpath("//div[@id='block-COLLECTION']//li")), 1)
                ),
                self.noone.filter_model(
                    random.randrange(1, len(self.driver.find_elements_by_xpath("//div[@id='block-MODEL']//li")), 1)
                ),
                self.noone.filter_basic_material(
                    random.randrange(1,
                                     len(self.driver.find_elements_by_xpath("//div[@id='block-BASIC_MATERIAL']//li")),
                                     1)
                ),
                self.noone.filter_lining_material(
                    random.randrange(1,
                                     len(self.driver.find_elements_by_xpath("//div[@id='block-LINING_MATERIAL']//li")),
                                     1)
                ),
                self.noone.filter_group(
                    random.randrange(1, len(self.driver.find_elements_by_xpath("//div[@id='block-GROUP_REF']//li")), 1)
                )]: el.click()
        except:
            log("/" * 10 + "ОШИБКА: Один из фильтров не был найден! См. по ссылке" + "\\" * 10)
            TakeScreenshot(self.driver, RunCatalog()).take_screenshot()


if __name__ == '__main__':
    try:
        RunCatalog().test_run()
        LogReport(testblock=RunCatalog(), logs=logging.log).test_results()
    except:
        LogReport(testblock=RunCatalog(), logs=logging.log).test_results()
