import datetime
import time
from pytest import mark
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from runs.pages.footer_main_page_dm2 import FooterMainPage as Page
from runs.pages.base.logging_report import LogReport, Logging, TakeScreenshot

logging = Logging()
log = logging.logger


@mark.usefixtures('driver_init_footer')
class RunFooterDM2(object):
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

    @mark.testrun
    def test_run(self):
        if __name__ == '__main__':
            log("=" * 5 + "Начало тестирования.")
        else:
            log("=" * 5 + "Начало тестирования {}".format(RunFooterDM2().__class__.__name__) +
                "Время: {}".format(datetime.datetime.now()))

        try:
            self.noone.cookies.click()
            self.nav_links()
        except Exception as e:
            log("/" * 10 + "ОШИБКА: Во время работы произошёл сбой!" + "\\" * 10 + "\nОшибка: {}".format(str(e)))
            TakeScreenshot(RunFooterDM2()).take_screenshot()

        log('='*5 + "Завершение тестирования.")
        # self.driver.quit()
        LogReport(logs=logging.log, testblock=RunFooterDM2()).test_results()

    def nav_links(self):
        # for i in self.driver.find_elements_by_xpath("//footer//a[@class='nav-item']"):
        for i in range(1, len(self.driver.find_elements_by_xpath("//footer//li[@class='nav-item']")), 1):
            log("Перехожу по ссылке элемента: " + str(i))
            self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            # i.click()
            self.driver.find_element_by_xpath("//footer//li[@class='nav-item'][{}]".format(str(i))).click()
            log("Возвращаюсь на одну страницу назад")
            self.noone.go_back()


if __name__ == '__main__':
    RunFooterDM2().test_run()
