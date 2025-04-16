import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Finish_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    title_finish = "//span[contains(@class, 'css-13eo1xz-StyledTypography')]"

    # Getters

    def get_title_finish(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.title_finish)))

    # Actions


    # Methods
    def finish(self):
        self.get_current_url()
        time.sleep(2)
        self.assert_word(self.get_title_finish(), 'Заказ успешно создан!')
        self.get_screenshot()

