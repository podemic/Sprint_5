import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from locators import TestLocators
from data import UserTestData


@pytest.fixture(scope="function")
def chromeDriver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()


@pytest.fixture
def login(chromeDriver):
    chromeDriver.find_element(*TestLocators.LOGIN_BTN_MAIN_PAGE).click()
    chromeDriver.find_element(*TestLocators.EMAIL_INPUT_AUTH).send_keys(UserTestData.email)
    chromeDriver.find_element(*TestLocators.PASSWORD_INPUT_AUTH).send_keys(UserTestData.password)
    chromeDriver.find_element(*TestLocators.LOGIN_BTN_AUTH).click()

