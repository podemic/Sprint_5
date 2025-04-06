from time import sleep

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from conftest import chromeDriver
from conftest import login
from locators import TestLocators
import time

#пробую залогиниться , перейти в ЛК и оттуда на страницу Конструктора
class TestNavigationToConstructorPage:
    def test_navigation_to_constructor_page(self,chromeDriver,login):
        chromeDriver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(chromeDriver, 7).until(expected_conditions.visibility_of_element_located(
            TestLocators.ORDERS_HISTORY_PERSONAL_ACCOUNT))
        chromeDriver.find_element(*TestLocators.COSTRUCTOR_BUTTON_HEADER).click()
        WebDriverWait(chromeDriver,7).until(expected_conditions.visibility_of_element_located(
            TestLocators.BUNS_BLOCK))
        assert chromeDriver.find_element(*TestLocators.MAKE_ORDER_BUTTON).is_displayed()

    def test_navigation_to_constructor_from_persnal_account_by_click_logo(self,chromeDriver,login):
        chromeDriver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(chromeDriver, 7).until(expected_conditions.visibility_of_element_located(
            TestLocators.ORDERS_HISTORY_PERSONAL_ACCOUNT))
        WebDriverWait(chromeDriver,7).until(expected_conditions.visibility_of_element_located(
            TestLocators.LOGO))
        chromeDriver.find_element(*TestLocators.LOGO).click()
        assert chromeDriver.find_element(*TestLocators.MAKE_ORDER_BUTTON).is_displayed()





