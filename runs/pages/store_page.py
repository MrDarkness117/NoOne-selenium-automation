from .base.locator import Locator
from .base.base_page import BasePage
from .base.base_element import BaseElement
from selenium.webdriver.common.by import By


class Footwear(BasePage):

    url = 'https://www.noone.ru/catalog/muzhskoe/obuv/'

    '''
    Static Buttons
    '''

    @property
    def region_confirm(self):
        """
        In WebDriver you always get a region confirmation
        :return:
        """
        locator = Locator(by=By.ID, value='region-confirm')
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def region_confirm_manual(self):
        """

        :return:
        """
        locator = Locator(by=By.CLASS_NAME, value="btn btn-default js-region-popup-open")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def region_confirm_manual_rus(self):
        """

        :return:
        """
        locator = Locator(by=By.XPATH, value="//li[contains(@data-code, '77000000000')]")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def store_ads(self):
        """
        Ad element
        :return:
        """
        locator = Locator(by=By.XPATH, value="//div[contains(@class, 'flocktory-widget-overlay')[1]]")
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def store_filter(self):
        """

        :return:
        """
        locator = Locator(by=By.CLASS_NAME, value='catalog-control-label')
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def store_filter_close(self):
        """

        :return:
        """
        locator = Locator(by=By.CLASS_NAME, value='catalog-control catalog-control-shops')
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def store_filter_show_filtered(self):
        """

        :return:
        """
        locator = Locator(by=By.ID, value='set_filter_trigger')
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def store_filter_remove_filtered(self):
        """

        :return:
        """
        locator = Locator(by=By.ID, value='modal-reservation-reset')
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    '''
    Map elements
    '''

    @property
    def store_map(self):
        """
        Can pass x, y coords for setting the hover offset
        :return:
        """
        locator = Locator(by=By.ID, value='tab-map')
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    '''
    Checkboxes
    '''

    def checkbox(self, nth=1):
        """
        Checkbox list
        :param nth: must be 1 or greater
        :return:
        """
        locator = Locator(
            by=By.XPATH,
            value="//ul[contains(@class, 'filter-list')]/li[contains(@class, 'filter-item-level-1')][%s]" % nth)
        return BaseElement(
            driver=self.driver,
            locator=locator
        )

    @property
    def checkbox_last(self):
        """
        Last checkbox element
        :return:
        """
        count = Locator(
            by=By.XPATH,
            value="count(//ul[contains(@class, 'filter-list')]/li[contains(@class, 'filter-item-level-1')])"
        )
        locator = Locator(
            by=By.XPATH,
            value="//ul[contains(@class, 'filter-list')]/li[contains(@class, 'filter-item-level-1')[%s]]" % count
        )
        return BaseElement(
            driver=self.driver,
            locator=locator
        )
