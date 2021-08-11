from selenium import webdriver
from runs.pages.dm2_common_elements import CommonElements as CE
from runs.pages.common_elements import CommonElements as dm2CE
from selenium.webdriver.common.by import By
from runs.pages.base.logger_config_ import logger_config_
import time

"""
Программа для запуска главной страницы
Функции: Подтверждение работы домена, пароля и ручной работы со страницей
"""


def warn(msg): logger_config_().warn(msg)


def info(msg): logger_config_().info(msg)


def crit(msg): logger_config_().critical(msg)


def err(msg): logger_config_().error(msg)


def exc(msg): logger_config_().exception(msg)


def run_default():

    info("Running default page test")

    url = "https://noone.ru/"
    url_dm2 = "https://oneway:eehooXi8@dm2.noone.ru/"

    driver = webdriver.Chrome()
    driver.set_window_position(0, 0)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(url)

    noone = CE(driver=driver)

    # Команды для закрытия элементов кукис и выбора города

    region_confirmed = False
    cookies_accepted = False

    try:
        noone.region_confirm.click()
        info("Регион подтвержден")
        region_confirmed = True
        noone.cookies.click()
        info("Cookies приняты")
        cookies_accepted = True
        info("All commands passed")
    except:
        warn("Страница заблокирована всплывающим окном!")
        region_confirmed = False
        cookies_accepted = False
        subscribe = driver.find_element(By.XPATH, "fl-513145")
        driver.switch_to.frame(subscribe)
        driver.find_element(By.CLASS_NAME, "flocktory-widget-overlay").click()
        driver.switch_to.default_content()
        noone.region_confirm.click()
        info("Регион подтвержден")
        region_confirmed = True
        noone.cookies.click()
        info("Cookies приняты")
        cookies_accepted = True

    driver.close()
    driver_dm2 = webdriver.Chrome()
    driver_dm2.set_window_position(0, 0)
    driver_dm2.maximize_window()
    driver_dm2.implicitly_wait(10)
    driver_dm2.get(url_dm2)

    dm2_noone = dm2CE(driver=driver_dm2)

    dm2_noone.region_confirm.click()
    try:
        dm2_noone.cookies.click()
    except:
        time.sleep(2)
        dm2_noone.cookies.click()

    info("All tests passed")

    time.sleep(5)

    driver.quit()
    driver_dm2.quit()


if __name__ == '__main__':
    run_default()
