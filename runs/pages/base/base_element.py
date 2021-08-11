from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BaseElement(object):
    def __init__(self, driver, locator):
        self.driver = driver
        self.url = ''
        self.locator = locator

        self.web_element = None
        self.find()

    def find(self):
        # self.driver.find_element(by=self.by, value=self.locator)  # Unsophisticated way, implicit way
        element = WebDriverWait(self.driver, 10)\
            .until(EC.visibility_of_element_located(locator=self.locator))
        self.web_element = element
        return None

    def input_text(self, txt):
        self.web_element.send_keys(txt)
        return None

    def attribute(self, attr_name):
        attribute = self.web_element.get_attribute(attr_name)
        return attribute

    def click(self):
        element = WebDriverWait(self.driver, 10)\
            .until(EC.element_to_be_clickable(locator=self.locator))
        element.click()
        return None

    def hover_center(self):
        element = WebDriverWait(self.driver, 10)\
            .until(EC.visibility_of_element_located(locator=self.locator))
        actions = ActionChains(driver=self.driver)
        actions.move_to_element(element).perform()  # set the cursor to be in the middle

    def hover_offset(self, x=0, y=0):
        actions = ActionChains(driver=self.driver)
        actions.move_by_offset(x, y).perform()

    def hover_center_and_click(self):
        element = WebDriverWait(self.driver, 10) \
            .until(EC.visibility_of_element_located(locator=self.locator))
        actions = ActionChains(driver=self.driver)
        actions.move_to_element(element).click().perform()  # set the cursor to be in the middle

    def hover_center_offset_and_click(self, x=0, y=0):
        element = WebDriverWait(self.driver, 10)\
            .until(EC.visibility_of_element_located(locator=self.locator))
        actions = ActionChains(driver=self.driver)
        actions.move_to_element(element).move_by_offset(x, y).click().perform()

    @property
    def text(self):
        text = self.web_element.text
        return text
