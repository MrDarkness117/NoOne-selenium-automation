import pytest
from selenium import webdriver


@pytest.fixture()
def driver_init_footer(request):
    web_driver = webdriver.Chrome()
    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.fixture()
def driver_init_header(request):
    web_driver = webdriver.Firefox()
    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.fixture()
def driver_init_main_page(request):
    web_driver = webdriver.Firefox()
    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.fixture()
def driver_init_profile(request):
    web_driver = webdriver.Firefox()
    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.fixture()
def driver_init_catalog(request):
    web_driver = webdriver.Firefox()
    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.fixture()
def driver_init_cart(request):
    web_driver = webdriver.Firefox()
    request.cls.driver = web_driver
    yield
    web_driver.close()
