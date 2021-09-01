import pytest

from runs import \
    test_run_footer_dm2 as footer, \
    test_run_header_dm2 as header, \
    test_run_main_page_dm2 as mainpage, \
    test_run_catalog_dm2 as catalog, \
    test_run_auth_profile_dm2 as profile, \
    test_run_cart_dm2 as cart


@pytest.fixture(scope='session')
def test_run_footer():
    footer.RunFooterDM2().test_run()


@pytest.fixture(scope='session')
def test_run_header():
    header.RunHeaderDM2().test_run()


@pytest.fixture(scope='session')
def test_run_main_page():
    mainpage.RunMainPageDM2().test_run()


@pytest.fixture(scope='session')
def test_run_catalog():
    catalog.RunCatalogDM2().test_run()


@pytest.fixture(scope='session')
def test_run_profile():
    profile.RunAuthProfileDM2().test_run()


@pytest.fixture(scope='session')
def test_run_cart():
    cart.RunCartDM2().test_run()
