from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from runs.pages.auth_profile_page import AuthProfilePage as Page
from runs.pages.base.logging_report import LogReport, Logging, TakeScreenshot
import datetime

logging = Logging()
log = logging.logger


class RunAuthProfile(object):
    # Настройки

    options = Options()
    options.add_argument("--window-position=-2000,0")
    driver = webdriver.Chrome(options=options)
    driver.set_window_position(-2000, 0)
    driver.maximize_window()
    driver.implicitly_wait(3)

    # Запуск

    noone = Page(driver=driver)
    noone.go()
    url = driver.current_url

    def test_run(self):
        pass


test_start = "=" * 5 + "Начало тестирования {}.".format(RunAuthProfile().__class__.__name__)


if __name__ == '__main__':
    RunAuthProfile().test_run()
    test_start = "=" * 5 + "Начало тестирования"
