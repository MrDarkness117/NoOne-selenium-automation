from runs import \
    run_footer_dm2 as footer, \
    run_header_dm2 as header, \
    run_main_page_dm2 as mainpage, \
    run_catalog_dm2 as catalog, \
    run_auth_profile_dm2 as profile, \
    run_cart_dm2 as cart
from threading import Thread
from runs.pages.base.logging_report import Logging, LogReport

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

    def test_runs(self):

        log("=" * 28 + " Запуск глобального тестирования " + "=" * 29)
        Thread(target=f.RunFooterDM2().test_run()).start()
        Thread(target=h.RunHeaderDM2().test_run()).start()
        Thread(target=c.RunCatalogDM2().test_run()).start()
        Thread(target=p.RunAuthProfileDM2().test_run()).start()
        Thread(target=m.RunMainPageDM2().test_run()).start()
        Thread(target=ca.RunCartDM2().test_run()).start()
        for r in runs:
            log(r.logging.log)

        log("=" * 29 + " Конец глобального тестирования " + "=" * 29)

        LogReport(RunsDM2(), logs=logging.log).test_results()


if __name__ == '__main__':
    RunsDM2().test_runs()
