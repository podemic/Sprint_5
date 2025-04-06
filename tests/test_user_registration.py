
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators import TestLocators
from conftest import chromeDriver
from creditsgenerator import generate_login, generate_valid_password,generate_invalid_password
from data import UserTestData
import time

class TestRegistration:
    #тустируем регу с валидными именем, мейлом, паролем > 6
    def test_success_registration_of_new_user(self,chromeDriver):
        random_email = generate_login()
        random_password = generate_valid_password()
        chromeDriver.find_element(*TestLocators.LOGIN_BTN_MAIN_PAGE).click()
        WebDriverWait(chromeDriver, 6).until(expected_conditions.visibility_of_element_located(
            TestLocators.REGISTRATION_BTN_AUTH))

        chromeDriver.find_element(*TestLocators.REGISTRATION_BTN_AUTH).click()
        WebDriverWait(chromeDriver, 6).until(expected_conditions.visibility_of_element_located(
            TestLocators.SUBMIT_BUTTON_REGISTRATION))
        chromeDriver.find_element(*TestLocators.NAME_INPUT_REGISTRATION).send_keys(UserTestData.username)
        chromeDriver.find_element(*TestLocators.EMAIL_INPUT_REGISTRATION).send_keys(random_email)
        chromeDriver.find_element(*TestLocators.PASSWORD_INPUT_REGISTRATION).send_keys(random_password)
        chromeDriver.find_element(*TestLocators.SUBMIT_BUTTON_REGISTRATION).click()
        assert chromeDriver.find_element(*TestLocators.SUBMIT_BUTTON_REGISTRATION).is_displayed()

    #тестируем регу с невалидным паролем <6 символов
    def test_registration_with_wrong_password(self,chromeDriver):
        random_email = generate_login()
        random_wrong_password = generate_invalid_password()
        chromeDriver.find_element(*TestLocators.LOGIN_BTN_MAIN_PAGE).click()
        WebDriverWait(chromeDriver, 6).until(expected_conditions.visibility_of_element_located(
            TestLocators.REGISTRATION_BTN_AUTH))

        chromeDriver.find_element(*TestLocators.REGISTRATION_BTN_AUTH).click()
        WebDriverWait(chromeDriver, 6).until(expected_conditions.visibility_of_element_located(
            TestLocators.SUBMIT_BUTTON_REGISTRATION))

        chromeDriver.find_element(*TestLocators.NAME_INPUT_REGISTRATION).send_keys(UserTestData.username)
        chromeDriver.find_element(*TestLocators.EMAIL_INPUT_REGISTRATION).send_keys(random_email)
        chromeDriver.find_element(*TestLocators.PASSWORD_INPUT_REGISTRATION).send_keys(random_wrong_password)
        chromeDriver.find_element(*TestLocators.SUBMIT_BUTTON_REGISTRATION).click()

        assert chromeDriver.find_element(*TestLocators.SUBMIT_BUTTON_REGISTRATION).is_displayed()

        # тестируем появление уведомления об ошибке при вводе неверного пароля
    def test_notification_after_registration_with_wrong_password(self, chromeDriver):
        random_email = generate_login()
        random_wrong_password = generate_invalid_password()
        chromeDriver.find_element(*TestLocators.LOGIN_BTN_MAIN_PAGE).click()
        WebDriverWait(chromeDriver, 6).until(expected_conditions.visibility_of_element_located(
        TestLocators.REGISTRATION_BTN_AUTH))

        chromeDriver.find_element(*TestLocators.REGISTRATION_BTN_AUTH).click()
        WebDriverWait(chromeDriver, 6).until(expected_conditions.visibility_of_element_located(
        TestLocators.SUBMIT_BUTTON_REGISTRATION))

        chromeDriver.find_element(*TestLocators.NAME_INPUT_REGISTRATION).send_keys(UserTestData.username)
        chromeDriver.find_element(*TestLocators.EMAIL_INPUT_REGISTRATION).send_keys(random_email)
        chromeDriver.find_element(*TestLocators.PASSWORD_INPUT_REGISTRATION).send_keys(random_wrong_password)
        chromeDriver.find_element(*TestLocators.SUBMIT_BUTTON_REGISTRATION).click()

        assert chromeDriver.find_element(*TestLocators.SUBMIT_BUTTON_REGISTRATION).is_displayed()

    #тест регистрации с правильными email и паролем, но без имени
    def test_registration_with_no_name(self,chromeDriver):
        random_email = generate_login()
        random_password = generate_valid_password()
        chromeDriver.find_element(*TestLocators.LOGIN_BTN_MAIN_PAGE).click()
        WebDriverWait(chromeDriver, 6).until(expected_conditions.visibility_of_element_located(
            TestLocators.REGISTRATION_BTN_AUTH))
        chromeDriver.find_element(*TestLocators.REGISTRATION_BTN_AUTH).click()
        WebDriverWait(chromeDriver, 6).until(expected_conditions.visibility_of_element_located(
            TestLocators.SUBMIT_BUTTON_REGISTRATION))
        chromeDriver.find_element(*TestLocators.NAME_INPUT_REGISTRATION).send_keys('')
        chromeDriver.find_element(*TestLocators.EMAIL_INPUT_REGISTRATION).send_keys(random_email)
        chromeDriver.find_element(*TestLocators.PASSWORD_INPUT_REGISTRATION).send_keys(random_password)
        chromeDriver.find_element(*TestLocators.SUBMIT_BUTTON_REGISTRATION).click()

        assert chromeDriver.find_element(*TestLocators.SUBMIT_BUTTON_REGISTRATION).is_displayed()

    #тест реги при незаполненном поле email и заполненых имени и пароле
    def test_registration_with_no_email(self,chromeDriver):
        random_email = generate_login()
        random_password = generate_valid_password()
        chromeDriver.find_element(*TestLocators.LOGIN_BTN_MAIN_PAGE).click()
        WebDriverWait(chromeDriver, 6).until(expected_conditions.visibility_of_element_located(
            TestLocators.REGISTRATION_BTN_AUTH))
        chromeDriver.find_element(*TestLocators.REGISTRATION_BTN_AUTH).click()
        WebDriverWait(chromeDriver, 6).until(expected_conditions.visibility_of_element_located(
            TestLocators.SUBMIT_BUTTON_REGISTRATION))
        chromeDriver.find_element(*TestLocators.NAME_INPUT_REGISTRATION).send_keys(UserTestData.username)
        chromeDriver.find_element(*TestLocators.EMAIL_INPUT_REGISTRATION).send_keys("")
        chromeDriver.find_element(*TestLocators.PASSWORD_INPUT_REGISTRATION).send_keys(random_password)
        time.sleep(2)
        chromeDriver.find_element(*TestLocators.SUBMIT_BUTTON_REGISTRATION).click()
        time.sleep(2)

        assert chromeDriver.find_element(*TestLocators.SUBMIT_BUTTON_REGISTRATION).is_displayed()
        time.sleep(2)






