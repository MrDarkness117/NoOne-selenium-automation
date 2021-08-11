from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from runs.pages.auth_profile_page import AuthProfilePage as Page
from runs.pages.base.logger_config_ import warn, info, err, exc


class RunAuthProfile(object):

    # Настройки

    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.set_window_position(0, 0)
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
        self.open_sections()
        self.section_favs()
        self.section_recs()
        self.section_views()

    # Команды

    def auth(self):
        info("Открыть окно авторизации")
        self.noone.auth_page.click()

    def auth_fields(self):
        auth_info = {
            'login': 'm.romantsov@noone.ru',
            'password': 'mihailo'
        }
        info("Ввести логин/пароль, нажать 'войти'")
        self.noone.auth_field_login.input_text(auth_info['login'])
        self.noone.auth_field_pass.input_text(auth_info['password'])
        self.noone.auth_field_button.click()

    def foot_size_select(self):
        info("Выбрать размер обуви")
        self.noone.foot_size.click()
        self.noone.foot_size_el.click()

    def cloth_size_select(self):
        info("Выбрать размер одежды")
        self.noone.cloth_size.click()
        self.noone.cloth_size_el.click()

    def accept_and_save(self):
        info("Принять условия и сохранить")
        self.noone.save_accept.click()
        self.noone.save.click()

    def open_sections(self):
        info("Проверка на открытие разделов")
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
            info("Все разделы успешно открываются")
        except:
            err("Один или более разделов не открывается!")

    def section_favs(self):
        info("Проверка раздела избранных")

    def section_recs(self):
        info("Проверка раздела рекомендаций")

    def section_views(self):
        info("Проверка раздела просмотренное")


if __name__ == '__main__':
    RunAuthProfile().test_run()
