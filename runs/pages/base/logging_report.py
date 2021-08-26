import datetime
import os


def return_testblock(cls_name):
    """
    Статический метод возвращающий имя класса для сохранения файлов
    :param cls_name: Класс, имя которого мы должны получить
    :return:
    """
    return cls_name.__class__.__name__


class LogReport(object):
    """
    Составление отчетов о тестах. Действия сохраняются пошагово при помощи метода Logging().logger()
    testblock - Имя класса теста. Как правило RunНазваниеБлока
    logs - Вся сохраняемая информация о действиях драйвера
    """

    def __init__(self, testblock, logs, mode='s'):
        self.testblock = testblock
        self.logs = logs
        self.BASE_INFO = "SELENIUM ТЕСТИРОВАНИЕ - ДАТА/ВРЕМЯ: {} \n" \
                         "БЛОК ТЕСТИРОВАНИЯ - {}\n" \
                         "РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ: \n" \
                         "{}".format(datetime.datetime.now(), self.testblock, self.logs)
        self.mode = mode
        if mode == 'g':
            self.BASE_INFO = ''

    def test_results(self):
        """
        Сохранение результатов тестирования в отдельный файл с информацией сохраненной в __init__()

        Использовать в блоке каждого тест кейса в самом конце:
            LogReport(testblock=RunClass(), logs=logging.log).test_results()

        где RunClass() - пример передаваемого название класса self.testblock для отчётов
        :return:
        """
        newpath = '.\\reports'
        if not os.path.exists(newpath):
            os.makedirs(newpath)

        with open(".\\reports\\" + return_testblock(self.testblock) + ' ' +
                  str(datetime.datetime.now()).replace(':', '-')[:-7] + "_" +
                  '_report.txt', 'w') as report:
            report.write(self.BASE_INFO)
        report.close()


class Logging(object):
    """
    Логгирование информации для блока LogReport().test_results()
    """
    log = '=' * 90 + "\n"
    n = 0
    start_message = ''

    def start_msg(self, testblock):
        if __name__ == '__main__':
            self.start_message = "=" * 5 + "Начало тестирования."
        else:
            self.start_message = "=" * 5 + "Начало тестирования {}.".format(return_testblock(testblock))
        return self.start_message

    def logger(self, report):
        """
        Сохранение информации в виде пошаговых логов
        Символы '/' и '=' говорят программе не сохранять эти логи как действия для воспроизведения,
        а носят исключительно информативный характер. Знак = для информации и предупреждений, / для ошибок

        Рекомендуется в начале файла run после импорта ставить следующие строки:
            logging = Logging()
            log = logging.logger
        где log - метод для логгирования шагов, информации и ошибок
        :param report: передаваемая информация
        :return:
        """
        if report[0] != '=':
            if report[0] != '/':
                self.n += 1
                self.log += str(self.n) + '. ' + report + "\n"
            else:
                self.log += report + '\n'
        else:
            self.log += report + '\n'


class TakeScreenshot(object):
    """
    Сохранение скриншотов
    """

    def __init__(self, testblock):
        self.testblock = testblock
        self.driver = testblock.driver

    def take_screenshot(self):
        """
        Использовать только с Selenium WebDriver
        Сохранить скриншот с именем self.testblock
        :return:
        """
        newpath = '.\\screenshots'
        if not os.path.exists(newpath):
            os.makedirs(newpath)
        self.driver.save_screenshot('.\\screenshots\\' + return_testblock(self.testblock) + ' ' +
                                    str(datetime.datetime.now()).replace(':', '-')[:-7] + "_" +
                                    '_screenshot.png')

