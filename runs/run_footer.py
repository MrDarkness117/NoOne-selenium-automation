from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from runs.pages.footer_main_page import FooterMainPage as Page
from runs.pages.base.logging_report import LogReport, Logging, TakeScreenshot
import datetime
import time

logging = Logging()
log = logging.logger


class RunFooter(object):
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
        log(test_start + "Время: {}".format(str(datetime.datetime.now())))

        try:
            self.noone.cookies.click()
            self.nav_links()
        except Exception as e:
            log("/" * 10 + "ОШИБКА: Во время работы произошёл сбой!" + "\\" * 10 + "\nОшибка: {}".format(e))
            TakeScreenshot(RunFooter()).take_screenshot()

        log('='*5 + "Завершение тестирования.")
        self.driver.quit()
        LogReport(logs=logging.log, testblock=RunFooter()).test_results()

    def nav_links(self):
        # for i in self.driver.find_elements_by_xpath("//footer//a[@class='nav-item']"):
        for i in range(1, 12, 1):
            log("Перейти по ссылке элемента: " + str(i))
            self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            # i.click()
            self.driver.find_element_by_xpath("//footer//li[@class='nav-item'][{}]".format(str(i))).click()
            log("=" * 5 + "Возвращаюсь на одну страницу назад")
            self.noone.go_back()


test_start = "=" * 5 + "Начало тестирования {}.".format(RunFooter().__class__.__name__)


if __name__ == '__main__':
    RunFooter().test_run()
    test_start = "=" * 5 + "Начало тестирования."

