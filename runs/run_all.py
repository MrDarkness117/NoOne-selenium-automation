from runs import \
    run_footer as footer, \
    run_header as header, \
    run_main_page as mainpage, \
    run_catalog as catalog, \
    run_auth_profile as profile, \
    run_cart as cart
from threading import Thread
from runs.pages.base.logging_report import Logging, LogReport
import datetime

logging = Logging()
log = logging.logger

f = footer
h = header
c = catalog
p = profile
m = mainpage
ca = cart
runs = [f, h, c, p, m]
logs = [f.log, h.log, c.log, p.log, m.log]


# TODO: Имплементировать параллельное тестирование
class Runs(object):

    def testruns(self):

        log("=" * 5 + "Время: {}".format(str(datetime.datetime.now())))
        log("=" * 10 + " Запуск глобального тестирования " + "=" * 10)
        # Thread(target=f.RunFooter().test_run()).start()
        # Thread(target=h.RunHeader().test_run()).start()
        # Thread(target=c.RunCatalog().test_run()).start()
        # Thread(target=p.RunAuthProfile().test_run()).start()
        # Thread(target=m.RunMainPage().test_run()).start()
        # Thread(target=ca.RunCart().test_run()).start()
        f.RunFooter().test_run()
        h.RunHeader().test_run()
        c.RunCatalog().test_run()
        p.RunAuthProfile().test_run()
        m.RunMainPage().test_run()
        ca.RunCart().test_run()
        for r in runs:
            log(r.logging.log)

        log("=" * 10 + " Конец глобального тестирования " + "=" * 10)

        LogReport(Runs(), logs=logging.log).test_results()


if __name__ == '__main__':
    Runs().testruns()
