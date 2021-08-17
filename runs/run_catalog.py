from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from runs.pages.catalog_page import CatalogPage as Page
from runs.pages.base.logging_report import Logging, LogReport

logging = Logging()
log = logging.logger


class RunCatalog(object):

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

        log("=" * 5 + "Начало тестирования.")

        try:
            self.open_category()

        except:
            log("/"*10 + "ОШИБКА: Во время работы произошёл сбой!" + "\\"*10)

        log("="*5 + "Завершение тестирования.")

        self.driver.quit()

    def open_category(self):

        self.noone.gender_select_random.click()
        self.noone.category_select_random.click()


if __name__ == '__main__':
    try:
        RunCatalog().test_run()
        LogReport(testblock=RunCatalog(), logs=logging.log).test_results()
    except:
        LogReport(testblock=RunCatalog(), logs=logging.log).test_results()
