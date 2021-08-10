from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from pages.dm2_main_page import MainPage
from pages.main_page import MainPage
import time
import random

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
    noone.region_confirm.click()
except:
    print("No region requested")

try:
    noone.cookies.click()
except:
    print("No cookies requested")

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

noone.dy_product_window.click()
noone.item_buy.click()
noone.item_size.click()
noone.item_add.click()
noone.item_bootbox_accept.click()
# noone.item_bootbox_close.click()
noone.item_info_page.click()
WebDriverWait(browser, 10).until(lambda browser: browser.current_url != url)
time.sleep(2)
noone.go_back()  # после загрузки страницы товара
time.sleep(random.randint(0, 10))
noone.promo_banner.click()
WebDriverWait(browser, 10).until(lambda browser: browser.current_url != url)
time.sleep(2)
noone.go_back()
noone.journal.click()
time.sleep(2)

browser.quit()
