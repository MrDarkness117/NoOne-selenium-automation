from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
# from pages.dm2_main_page import MainPage
from runs.pages.main_page import MainPage
from runs.pages.base.logger_config_ import warn, info, err, exc
from runs.pages.base.logging_report import Logging, LogReport
import time
import random

logging = Logging()
log = logging.logger

options = Options()
browser = webdriver.Chrome(options=options)
browser.set_window_position(0, 0)
browser.maximize_window()
browser.implicitly_wait(3)
url = browser.current_url

noone = MainPage(driver=browser)
noone.go()

# Команды

try:
    info("Выбрать регион")
    noone.region_confirm.click()
except:
    info("No region requested")

try:
    info("Принять Cookies")
    noone.cookies.click()
except:
    info("No cookies requested")

info("Навести мышкой на карточку продукта")
noone.dy_product_card.hover_center()
browser.execute_script("window.scrollBy(0, 80)")

"""try:
    print("looking for ribbon...")
    WebDriverWait(browser, 10).until(
        EC.frame_to_be_available_and_switch_to_it(browser.find_element_by_xpath("//iframe[@id='fl-450213']"))
    )
    # ribbon = browser.find_element(value='fl-450213')
    # browser.switch_to.frame(ribbon)
    print("iframe found")
    # print(ribbon)
    # noone.footer_ribbon.click()
    browser.find_element_by_id('Ribbon-close').click()
    print("closed iframe")
    browser.switch_to.default_content()
except:
    print("No ribbon appeared")"""

info("Нажать на кнопку окна продукта")
noone.dy_product_window.click()
info("Нажать на кнопку покупки")
noone.item_buy.click()
info("Выбрать размер продукта")
noone.item_size.click()
info("Добавить продукт в корзину")
noone.item_add.click()
info("Нажать на кнопку 'Приинять'")
noone.item_bootbox_accept.click()
# noone.item_bootbox_close.click()
info("Перейти на страницу товара, дождаться загрузки")
noone.item_info_page.click()
WebDriverWait(browser, 10).until(lambda browser: browser.current_url != url)
time.sleep(2)
info("Вернуться на одну страницу назад")
noone.go_back()  # после загрузки страницы товара
time.sleep(random.randint(0, 10))
info("Нажать на промо-баннер, дождаться загрузки")
noone.promo_banner.click()
WebDriverWait(browser, 10).until(lambda browser: browser.current_url != url)
time.sleep(2)
info("Вернуться на одну страницу назад")
noone.go_back()
info("Нажать на первый источник журнала, дождаться загрузки")
noone.journal.click()
time.sleep(2)
info("Успех, завершение теста")

browser.quit()
