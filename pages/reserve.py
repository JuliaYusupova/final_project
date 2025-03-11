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
    delivery = "(//label[@data-meta-name='RadioButton'])[2]"
    city = "//input[@name='city']"
    city_loc = "//*[@id='__next']/div/div[1]/div[2]/div/div/div/div[2]/div/div[2]/div[1]/button/span/span"
    street = "//input[@name='street']"
    str = "(//div[@class='rcs-outer-container'])[1]"
    house = "//input[@name='courier-delivery-new-address-form_house']"
    upon_receipt = "(//label[@class='eddme6n0 euonzdo0 css-1anqdz0-Label--Label-RadioButton--StyledRadioButton-RadioButton--StyledRadioButtonComponent-withRadioContext--isItemDisabled e1qcyipg0'])[1]"
    finish_button = "//button[@class='e1jq023s0 css-eb7y16-Button--StyledButton-Button--Button ekx3zbi0']"
    cit = "//div[@class='eqw7fo10 css-7asl3q-SelectListOption--StyledSelectListOption-SelectListOption--StyledSelectListOptionComponent e9d6jv80']"


    # Getters

    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_telephone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.telephone)))

    def get_delivery(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery)))

    def get_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city)))

    def get_street(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.street)))

    def get_str(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.str)))

    def get_cit(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cit)))

    def get_house(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.house)))

    def get_upon_receipt(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.upon_receipt)))

    def get_finish_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.finish_button)))

    def get_city_loc(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city_loc)))


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

    def click_delivery(self):
        self.get_delivery().click()
        print("Click delivery")

    def input_city(self, city):
        self.get_city().send_keys(city)
        print("Input city")

    def input_street(self, street):
        self.get_street().send_keys(street)
        print("Input street")

    def click_street(self):
        self.get_street().click()
        print("click street")

    def click_city(self):
        self.get_city().click()
        print("click city")

    def input_str(self):
        self.get_str().click()

    def input_cit(self):
        self.get_cit().click()

    def input_house(self, house):
        self.get_house().send_keys(house)
        print("Input house")

    def click_upon_receipt(self):
        self.get_upon_receipt().click()
        print("Click upon receipt")

    def click_finish_button(self):
        self.get_finish_button().click()
        print("Click finish button")

    def name_city_loc(self):
        name_city = self.get_city_loc().text
        return name_city

    # Methods
    def input_information(self):
        self.get_current_url()
        self.input_first_name("Тест")
        self.input_last_name("Тестович")
        self.input_telephone("+7 (979) 555-12-65")
        self.click_delivery()
        self.driver.execute_script("window.scrollTo(0, 1100);")
        self.input_city(self.name_city_loc())
        self.click_city()
        self.input_cit()
        self.input_street("Ленина")
        self.click_street()
        self.input_str()
        self.input_house("1")
        self.driver.execute_script("window.scrollTo(0, 1700);")
        self.click_upon_receipt()
        self.click_finish_button()

