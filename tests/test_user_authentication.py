from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators import TestLocators
from conftest import chromeDriver
from data import UserTestData
import time

#тест успешной аутентификации на странице, ассерт по появлению кнопки "сделать заказ"
class TestAuthentication:
    def test_success_auth_at_main_page(self,chromeDriver):
         chromeDriver.find_element(*TestLocators.LOGIN_BTN_MAIN_PAGE).click()

         chromeDriver.find_element(*TestLocators.EMAIL_INPUT_AUTH).send_keys(UserTestData.email)
         chromeDriver.find_element(*TestLocators.PASSWORD_INPUT_AUTH).send_keys(UserTestData.password)
         chromeDriver.find_element(*TestLocators.LOGIN_BTN_AUTH).click()
         WebDriverWait(chromeDriver, 7).until(expected_conditions.visibility_of_element_located(
             TestLocators.MAKE_ORDER_BUTTON))
         assert chromeDriver.find_element(*TestLocators.MAKE_ORDER_BUTTON).is_displayed()

# тест успешной аутентификации на странице через кнопку ЛК, ассерт по появлению кнопки "сделать заказ"
    def test_success_auth_by_click_button_personal_account(self,chromeDriver):
        chromeDriver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()

        chromeDriver.find_element(*TestLocators.EMAIL_INPUT_AUTH).send_keys(UserTestData.email)
        chromeDriver.find_element(*TestLocators.PASSWORD_INPUT_AUTH).send_keys(UserTestData.password)
        chromeDriver.find_element(*TestLocators.LOGIN_BTN_AUTH).click()
        WebDriverWait(chromeDriver, 7).until(expected_conditions.visibility_of_element_located(
            TestLocators.MAKE_ORDER_BUTTON))
        assert chromeDriver.find_element(*TestLocators.MAKE_ORDER_BUTTON).is_displayed()

# вход через кнопку "войти" на странице регистрации

    def test_success_auth_by_click_login_button_on_registration_page(self,chromeDriver):
        chromeDriver.find_element(*TestLocators.LOGIN_BTN_MAIN_PAGE).click()
        WebDriverWait(chromeDriver, 9).until(expected_conditions.visibility_of_element_located(
            TestLocators.REGISTRATION_BTN_AUTH))
        chromeDriver.find_element(*TestLocators.REGISTRATION_BTN_AUTH).click() #нажили кнопку "зарегестрироваться" на странице реги
        WebDriverWait(chromeDriver,7).until(expected_conditions.visibility_of_element_located(
            TestLocators.LOGIN_BTN_REGISTRATION_FORM))

        chromeDriver.find_element(*TestLocators.LOGIN_BTN_REGISTRATION_FORM).click()
        WebDriverWait(chromeDriver,7).until(expected_conditions.visibility_of_element_located(
            TestLocators.LOGIN_BTN_AUTH))
        chromeDriver.find_element(*TestLocators.EMAIL_INPUT_AUTH).send_keys(UserTestData.email)
        chromeDriver.find_element(*TestLocators.PASSWORD_INPUT_AUTH).send_keys(UserTestData.password)
        chromeDriver.find_element(*TestLocators.LOGIN_BTN_AUTH).click()
        WebDriverWait(chromeDriver, 7).until(expected_conditions.visibility_of_element_located(
            TestLocators.MAKE_ORDER_BUTTON))

        assert chromeDriver.find_element(*TestLocators.MAKE_ORDER_BUTTON).is_displayed()

    #вход через кнопку "войти" на странице восстановления пароля

    def test_success_auth_by_click_login_button_on_forgot_password_page(self,chromeDriver):
        chromeDriver.find_element(*TestLocators.LOGIN_BTN_MAIN_PAGE).click()
        WebDriverWait(chromeDriver, 7).until(expected_conditions.visibility_of_element_located(
        TestLocators.PASSWORD_RECOVER_BUTTON_AUTH))
        chromeDriver.find_element(*TestLocators.PASSWORD_RECOVER_BUTTON_AUTH).click()

        WebDriverWait(chromeDriver,7).until(expected_conditions.visibility_of_element_located(
            TestLocators.LOGIN_BTN_PASSWORD_RECOVERY_FORM))
        chromeDriver.find_element(*TestLocators.LOGIN_BTN_PASSWORD_RECOVERY_FORM).click()

        chromeDriver.find_element(*TestLocators.EMAIL_INPUT_AUTH).send_keys(UserTestData.email)
        chromeDriver.find_element(*TestLocators.PASSWORD_INPUT_AUTH).send_keys(UserTestData.password)
        chromeDriver.find_element(*TestLocators.LOGIN_BTN_AUTH).click()
        WebDriverWait(chromeDriver, 7).until(expected_conditions.visibility_of_element_located(
            TestLocators.MAKE_ORDER_BUTTON))
        assert chromeDriver.find_element(*TestLocators.MAKE_ORDER_BUTTON).is_displayed()














