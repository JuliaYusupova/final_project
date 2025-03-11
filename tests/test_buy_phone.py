import time

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

from pages.cart_page import Cart_page
from pages.client_info_page import Client_info_page
from pages.finish_page import Finish_page
from pages.main_page import Main_page
from pages.phone_page import Phone_page
from base.base_class import Base


def test_buy_phone_1():

    options = webdriver.FirefoxOptions()
    options.page_load_strategy = 'eager'
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)

    mp = Main_page(driver)
    mp.select_phone_section()

    pp = Phone_page(driver)
    pp.filters_1()

    cp = Cart_page(driver)
    cp.order()

    cip = Client_info_page(driver)
    cip.input_information()

    fp = Finish_page(driver)
    fp.finish()
    driver.quit()


    # driver.quit()
    print("Start test 1")
