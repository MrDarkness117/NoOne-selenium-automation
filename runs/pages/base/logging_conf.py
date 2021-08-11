import logging
import datetime


class LogReport(object):

    def __init__(self, testblock, logs):
        self.testblock = testblock
        self.logs = logs
        self.BASE_INFO = "SELENIUM ТЕСТИРОВАНИЕ - ДАТА/ВРЕМЯ: {} \n" \
                    "БЛОК ТЕСТИРОВАНИЯ - {}\n" \
                    "РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ: \n" \
                    "{}".format(datetime.datetime.now(), self.testblock, self.logs)

    logging.basicConfig(filename="selenium-'%(asctime)s-%(name)s.log", format='%(levelname)s:%(message)s')

    def test_results(self, logs):
        pass


