from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from conftest import chromeDriver
from conftest import login
from locators import TestLocators
import time
#логин -> переход в ЛК -> клик по Выход -> ассерт что есть кнопка Войти
class TestUserLogout:
    def test_success_user_logout(self,chromeDriver,login):
        chromeDriver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(chromeDriver, 7).until(expected_conditions.visibility_of_element_located(
            TestLocators.ORDERS_HISTORY_PERSONAL_ACCOUNT))

        chromeDriver.find_element(*TestLocators.USER_LOGOUT_BTN_FROM_PERSONAL_ACCOUNT).click()
        WebDriverWait(chromeDriver,7).until(expected_conditions.visibility_of_element_located(
            TestLocators.LOGIN_BTN_AUTH))
        assert chromeDriver.find_element(*TestLocators.LOGIN_BTN_AUTH).is_displayed()

