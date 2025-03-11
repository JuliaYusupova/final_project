import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):

    url = 'https://www.citilink.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    phone_main = "//span[contains(text(), 'Смартфоны')]"

    # Getters

    def get_phone_main(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_main)))

    # Actions

    def click_phone_main(self):
        self.get_phone_main().click()
        print("Click on phone section in Main page")

    # Methods
    def select_phone_section(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.driver.execute_script("window.scrollTo(0, 300);")
        self.click_phone_main()
        self.assert_url('https://www.citilink.ru/catalog/smartfony/?ref=mainpage_popular')