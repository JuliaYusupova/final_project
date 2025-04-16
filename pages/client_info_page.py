import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Client_info_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    first_name = "//input[@name='contact-form_firstName']"
    last_name = "//input[@name='contact-form_lastName']"
    telephone = "//input[@name='contact-form_phone']"
    self_pickup = "(//label[@data-meta-name='RadioButton'])[1]"
    upon_receipt = "//span[contains(text(), 'Наличными')]"
    finish_button = "(//span[contains(text(), 'Оформить')])[1]"
    pick_up_point = "//span[contains(text(), 'Выбрать пункт')]"
    shop_button = "(//span[contains(text(), 'Выбрать')])[1]"



    # Getters

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_telephone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.telephone)))

    def get_self_pickup(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.self_pickup)))
    def get_upon_receipt(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.upon_receipt)))

    def get_finish_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.finish_button)))

    def get_pick_up_point(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pick_up_point)))

    def get_shop_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.shop_button)))




    # Actions

    def input_first_name(self, name):
        self.get_first_name().send_keys(name)
        print("Input first_name")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("Input last_name")

    def input_telephone(self, telephone):
        self.get_telephone().send_keys(telephone)
        print("Input telephone")

    def click_self_pickup(self):
        self.get_self_pickup().click()
        print("Click self_pickup")

    def click_upon_receipt(self):
        self.get_upon_receipt().click()
        print("Click upon receipt")

    def click_pick_up_point(self):
        self.get_pick_up_point().click()
        print("Click pick_up_point")

    def click_finish_button(self):
        self.get_finish_button().click()
        print("Click finish button")

    def click_shop_button(self):
        self.get_shop_button().click()
        print("Click shop_button")

    # Methods
    def input_information(self):
        self.get_current_url()
        self.input_first_name("Петруша")
        self.input_last_name("Тестович")
        self.input_telephone("+7 (979) 555-12-65")
        self.click_self_pickup()
        self.driver.execute_script("window.scrollTo(0, 1200);")
        self.click_pick_up_point()
        time.sleep(2)
        self.click_shop_button()
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, 1800);")
        self.click_upon_receipt()
        self.driver.execute_script("window.scrollTo(0, 1300);")
        time.sleep(2)
        self.click_finish_button()

