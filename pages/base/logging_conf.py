import logging
import datetime


class LogReport:

    def __init__(self, testblock):
        self.testblock = testblock

        self.logs = ''

    def test_results(self):

        BASE_INFO = "SELENIUM ТЕСТИРОВАНИЕ - ДАТА/ВРЕМЯ: {} \n" \
                    "БЛОК ТЕСТИРОВАНИЯ - {}\n" \
                    "РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ: \n" \
                    "{}".format(datetime.datetime.now(), self.testblock, self.logs)

    logging.basicConfig(filename="selenium-'%(asctime)s-%(name)s.log", format='%(levelname)s:%(message)s')

