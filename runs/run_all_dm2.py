from runs import \
    test_run_footer_dm2 as footer, \
    test_run_header_dm2 as header, \
    test_run_main_page_dm2 as mainpage, \
    test_run_catalog_dm2 as catalog, \
    test_run_auth_profile_dm2 as profile, \
    test_run_cart_dm2 as cart
from threading import Thread
from runs.pages.base.logging_report import Logging, LogReport
import datetime
# import pytest

logging = Logging()
log = logging.logger

f = footer
h = header
c = catalog
p = profile
m = mainpage
ca = cart
runs = [f, h, c, p, m, ca]
logs = [f.log, h.log, c.log, p.log, m.log]


# TODO: Имплементировать параллельное тестирование для быстрых тестов
class RunsDM2(object):

    # @pytest.fixture(scope='session')
    def testruns(self):

        log("=" * 5 + "Время: {}".format(str(datetime.datetime.now())))
        log("=" * 28 + " Запуск глобального тестирования " + "=" * 29)
        Thread(target=f.RunFooterDM2().test_run()).start()
        Thread(target=h.RunHeaderDM2().test_run()).start()
        Thread(target=c.RunCatalogDM2().test_run()).start()
        Thread(target=p.RunAuthProfileDM2().test_run()).start()
        Thread(target=m.RunMainPageDM2().test_run()).start()
        Thread(target=ca.RunCartDM2().test_run()).start()
        # f.RunFooterDM2().test_run()
        # h.RunHeaderDM2().test_run()
        # c.RunCatalogDM2().test_run()
        # p.RunAuthProfileDM2().test_run()
        # m.RunMainPageDM2().test_run()
        # ca.RunCartDM2().test_run()
        for r in runs:
            log(r.logging.log)

        log("=" * 29 + " Конец глобального тестирования " + "=" * 29)

        LogReport(RunsDM2(), logs=logging.log).test_results()
        # return logging.log


if __name__ == '__main__':
    RunsDM2().testruns()
