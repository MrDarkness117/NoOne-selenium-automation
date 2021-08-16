import datetime
import os


class LogReport(object):

    def __init__(self, testblock, logs):
        self.testblock = testblock
        self.logs = logs
        self.BASE_INFO = "SELENIUM ТЕСТИРОВАНИЕ - ДАТА/ВРЕМЯ: {} \n" \
                         "БЛОК ТЕСТИРОВАНИЯ - {}\n" \
                         "РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ: \n" \
                         "{}".format(datetime.datetime.now(), self.testblock, self.logs)

    def return_testblock(self, cls_name):
        return cls_name.__class__.__name__

    def test_results(self):
        newpath = '.\\reports'
        if not os.path.exists(newpath):
            os.makedirs(newpath)

        with open(".\\reports\\" + self.return_testblock(self.testblock) + ' ' +
                  str(datetime.datetime.now()).replace(':', '-')[:-7] + "_" +
                  '_report.txt', 'w') as report:
            report.write(self.BASE_INFO)
        report.close()


class Logging(object):
    log = '=' * 90 + "\n"
    n = 0

    def logger(self, report):
        if report[0] != '=':
            if report[0] != '/':
                self.n += 1
                self.log += str(self.n) + '. ' + report + "\n"
            else:
                self.log += report + '\n'
        else:
            self.log += report + '\n'
