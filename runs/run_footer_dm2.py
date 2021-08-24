from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from runs.pages.footer_main_page_dm2 import FooterMainPage as Page
from runs.pages.base.logging_report import LogReport, Logging
import time

logging = Logging()
log = logging.logger


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

    def test_run(self):
        if __name__ == '__main__':
            log("=" * 5 + "Начало тестирования.")
        else:
            log("=" * 5 + "Начало тестирования {}".format(RunFooterDM2().__class__.__name__))

        self.noone.cookies.click()
        self.nav_links()

        log('='*5 + "Завершение тестирования.")
        self.driver.quit()
        LogReport(logs=logging.log, testblock=RunFooterDM2()).test_results()

    def nav_links(self):
        # for i in self.driver.find_elements_by_xpath("//footer//a[@class='nav-item']"):
        for i in range(1, 12, 1):
            log("Перехожу по ссылке элемента: " + str(i))
            self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            # i.click()
            self.driver.find_element_by_xpath("//footer//li[@class='nav-item'][{}]".format(str(i))).click()
            log("Возвращаюсь на одну страницу назад")
            self.noone.go_back()


if __name__ == '__main__':
    RunFooterDM2().test_run()