from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators import TestLocators
from conftest import chromeDriver






class TestNavigationToPersonalAccountPage:
 def test_success_navigation_to_personal_account_page(self,chromeDriver,login):
     chromeDriver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()

     WebDriverWait(chromeDriver, 7).until(expected_conditions.visibility_of_element_located(
     TestLocators.ORDERS_HISTORY_PERSONAL_ACCOUNT))

     assert chromeDriver.find_element(*TestLocators.ORDERS_HISTORY_PERSONAL_ACCOUNT).is_displayed()
     #должен произойти логин на главной, -> переход в ЛК. проверка по локатору История заказов







