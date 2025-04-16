import time

import self
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from base.base_class import Base


class Phone_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.actions = ActionChains(self.driver)

    # Locators

    slider = "(//div[@class='rc-slider-handle rc-slider-handle-2'])[2]"
    self_pickup = "(//div[@data-meta-name='FilterLabel'])[1]"
    installment_plan = "//span[contains(text(), 'Доступно в рассрочку')]"
    product_evaluation = "//span[contains(text(), '4,5 и выше')]"
    discount = "//span[contains(text(), '10% и больше')]"
    brand = "(//label[contains(@class, 'Label--Label')])[20]"
    cart_button = "(//button[@data-meta-name='Snippet__cart-button'])[1]"
    cart = "(//button[contains(@class, 'e11203e30 app-catalog-1w0ub5t-Button')])[2]"
    title_cart = "(//span[contains(@class, 'e9qk9yp0 e1a7a4n70')])[84]"

    # Getters

    def get_slider(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.slider)))

    def get_self_pickup(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.self_pickup)))

    def get_installment_plan(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.installment_plan)))

    def get_product_evaluation(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_evaluation)))

    def get_discount(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.discount)))

    def get_brand(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.brand)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_title_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, self.title_cart)))

    # Actions

    def click_slider(self):
        self.actions.click_and_hold(self.get_slider()).move_by_offset(-100, 0).release().perform()
        print("Click on slider")

    def click_self_pickup(self):
        self.get_self_pickup().click()
        print("Click on self pickup checkbox")

    def click_installment_plan(self):
        self.get_installment_plan().click()
        print("Click on installment plan")

    def click_product_evaluation(self):
        self.get_product_evaluation().click()
        print("Click on product evaluation")

    def click_discount(self):
        self.get_discount().click()
        print("Click on discount")

    def click_brand(self):
        self.get_brand().click()
        print("Click on brand")

    def click_cart_button(self):
        self.get_cart_button().click()
        print("Click on cart button")

    def click_cart(self):
        self.get_cart().click()
        print("Click on cart")

    # Methods
    def filters_1(self):
        self.get_current_url()
        self.driver.execute_script("window.scrollTo(0, 450);")
        time.sleep(3)
        self.click_slider()
        self.click_self_pickup()
        self.click_installment_plan()
        self.driver.execute_script("window.scrollTo(0, 1000);")
        self.click_product_evaluation()
        self.click_discount()
        self.click_brand()
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0, 300);")
        time.sleep(2)
        self.click_cart_button()
        time.sleep(3)
        self.click_cart()
        time.sleep(2)
        # self.assert_word(self.get_title_cart(), 'Корзина')





