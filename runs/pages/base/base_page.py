class BasePage(object):
    """
    Pass in the URL for go()
    Передача URL в метод go()
    """

    url = None

    def __init__(self, driver):
        self.driver = driver

    def go(self):
        self.driver.get(self.url)

    def go_back(self):
        """
        На прошлую страницу, шаг назад
        :return:
        """
        self.driver.execute_script("window.history.go(-1)")

    def go_forward(self):
        """
        На прошлую страницу, шаг вперёд
        :return:
        """
        self.driver.execute_script("window.history.go(1)")

    def go_to(self, num):
        """
        На страницу num (индекс страницы в истории браузера)
        :param num:
        :return:
        """
        self.driver.execute_script("window.history.go({})").format(num)

    def go_refresh(self):
        """
        Обновить страницу методом JS window.history.go()
        :return:
        """
        self.driver.execute_script("window.history.go(0)")
