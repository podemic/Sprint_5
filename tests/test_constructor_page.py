from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from conftest import login, chromeDriver
from locators import TestLocators
import time


class TestSwitchBetweenBlocksConstructor:
    #проверка, что при переходе в ЛК, выбран раздел булки
    def test_block_buns_is_opened_when_joined_personal_account(self,chromeDriver,login):
        WebDriverWait(chromeDriver,7).until(expected_conditions.visibility_of_element_located(
            TestLocators.MAKE_ORDER_BUTTON))

        assert chromeDriver.find_element(*TestLocators.SELECTED_BUTTON).text == 'Булки'

    #переход из блока Булки в блок Начинки
    def test_switch_from_but_to_sauce(self,chromeDriver,login):
        WebDriverWait(chromeDriver,7).until(expected_conditions.visibility_of_element_located(
            TestLocators.MAKE_ORDER_BUTTON))
        chromeDriver.find_element(*TestLocators.FILLINGS_BLOCK).click()
        assert chromeDriver.find_element(*TestLocators.SELECTED_BUTTON).text == 'Начинки'

    #переход из блока Начинки в блок Соусы
    def test_switch_from_fillings_block_to_sauce(self,chromeDriver,login):
        WebDriverWait(chromeDriver,7).until(expected_conditions.visibility_of_element_located(
            TestLocators.MAKE_ORDER_BUTTON))
        chromeDriver.find_element(*TestLocators.FILLINGS_BLOCK).click() #клик по Начинки , переход в них из Булок
        chromeDriver.find_element(*TestLocators.SAUCES_BLOCK).click() #rkbr по блоку Соусы, переход в них
        assert chromeDriver.find_element(*TestLocators.SELECTED_BUTTON).text == 'Соусы'# проверка, што мы на Соусах
    #переход из блока соусы в блок булки
    def test_switch_from_sauces_block_to_buns_block(self,chromeDriver,login):
        WebDriverWait(chromeDriver,7).until(expected_conditions.visibility_of_element_located(
            TestLocators.MAKE_ORDER_BUTTON))
        chromeDriver.find_element(*TestLocators.SAUCES_BLOCK).click()

        chromeDriver.find_element(*TestLocators.BUNS_BLOCK).click()

        assert chromeDriver.find_element(*TestLocators.SELECTED_BUTTON).text == 'Булки'









