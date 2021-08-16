from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from runs.pages.auth_profile_page import AuthProfilePage as Page
from runs.pages.base.logging_report import LogReport

log = '=' * 90 + "\n"
n = 0


def logger(report):
    global log
    global n
    if report[0] != '=':
        if report[0] != '/':
            n += 1
            log += str(n) + '. ' + report + "\n"
        else:
            log += report + '\n'
    else:
        log += report + '\n'


class RunAuthProfile(object):
    # Настройки

    options = Options()
    options.add_argument("--window-position=-2000,0")
    driver = webdriver.Chrome(options=options)
    driver.set_window_position(-2000, 0)
    driver.maximize_window()
    driver.implicitly_wait(3)

    # Запуск

    noone = Page(driver=driver)
    noone.go()
    url = driver.current_url

    def test_run(self):

        # Стандартные действия
        self.noone.cookies.click()
        # self.noone.region_confirm.click()

        # Действия Cart Page
        self.auth()
        self.auth_fields()
        self.foot_size_select()
        self.cloth_size_select()
        self.accept_and_save()
        self.section_favs()
        self.section_recs()
        self.section_views()
        self.open_sections()

        logger('=' * 5 + "Завершение теста.")
        self.driver.quit()

    # Команды

    def auth(self):
        logger("Открыть окно авторизации")
        self.noone.auth_page.click()

    def auth_fields(self):
        auth_info = {
            'login': 'm.romantsov@noone.ru',
            'password': 'mihailo'
        }
        logger("Ввести логин/пароль, нажать 'войти'")
        self.noone.auth_field_login.input_text(auth_info['login'])
        self.noone.auth_field_pass.input_text(auth_info['password'])
        self.noone.auth_field_button.click()

    def foot_size_select(self):
        logger("Выбрать размер обуви")
        self.noone.foot_size.click()
        self.noone.foot_size_el.click()

    def cloth_size_select(self):
        logger("Выбрать размер одежды")
        self.noone.cloth_size.click()
        self.noone.cloth_size_el.click()

    def accept_and_save(self):
        logger("Принять условия и сохранить")
        self.noone.save_checkbox.click()
        self.noone.save.click()
        self.noone.save_accept.click()

    def open_sections(self):
        logger("Проверка на открытие разделов")
        try:
            self.noone.personal_info.click()
            self.noone.loyalty_programme.click()
            self.noone.change_password.click()
            self.noone.addresses.click()
            self.noone.orders.click()
            self.noone.favourites.click()
            self.noone.recommendations.click()
            self.noone.viewed.click()
            self.noone.preferred_shop.click()
            self.noone.feedback.click()
            logger('=' * 5 + "Все разделы успешно открываются")
        except:
            logger('/' * 10 + "ОШИБКА: Один или более разделов не открывается!" + '\\' * 10)

    def section_favs(self):
        self.noone.favourites.click()
        self.section_tests()
        self.action_hover(
            '//div[@class="item js-item"][1]//li[@class="slider-item"][3]',
            '//ul[@class="item-image-nav"][1]//li[@class="item-image-nav-link"][3]'
        )

    def section_recs(self):
        self.noone.recommendations.click()
        self.section_tests()
        self.action_hover(
            '//div[@class="item js-item"][1]//img[contains(@class, "js-image-lazy")][3]',
            '//ul[@class="item-image-nav"][1]//li[@class="item-image-nav-link"][3]'
        )

    def section_views(self):
        self.noone.viewed.click()
        self.section_tests()
        self.action_hover(
            '//div[@class="item js-item"][1]//img[contains(@class, "js-image-lazy")][3]',
            '//ul[@class="item-image-nav"][1]//li[@class="item-image-nav-link"][3]'
        )

    # Команды для повторного использования

    def section_tests(self):
        logger("Проверить раздел с товарами")
        self.noone.items_frv.hover_center()

    def action_hover(self, img_el, find_el):
        logger("Проверить блоки hover")
        self.noone.hover_block.hover_center()
        logger("Проверить логику соответствия номера изображения и блока hover")
        self.perform_compare(img_el, find_el)

    def perform_compare(self, img_el, find_el):
        logger('=' * 5 + "Поиск картинки")
        img_compare = self.driver.find_element_by_xpath(img_el)
        logger("=" * 5 + "Картинка найдена")
        logger("Проверить соответствие с блоком наведения")
        if int(self.driver.find_element_by_xpath(find_el).get_attribute('data-image')) == 2 \
                and img_compare.is_displayed():
            logger('=' * 5 + "Изображение соответствует элементу при наведении мышью")
        else:
            logger('/' * 10 + "ОШИБКА: Ошибка работы элемента!" + '\\' * 10)
            print("Ошибка работы элемента!")


if __name__ == '__main__':
    RunAuthProfile().test_run()
    LogReport(logs=log, testblock=RunAuthProfile()).test_results()
else:
    LogReport(logs=log, testblock=RunAuthProfile()).test_results()
