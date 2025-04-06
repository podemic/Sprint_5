from selenium.webdriver.common.by import By

class TestLocators:
    # Кнопки на главной tps://stellarburgers.nomoreparties.site
    LOGIN_BTN_MAIN_PAGE = By.XPATH, '//button[text() = "Войти в аккаунт"]' # кнопка "Войти в аккаунт"
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, '//p[text() = "Личный Кабинет"]' # кнопка "Личный кабинет" в хедере
    COSTRUCTOR_BUTTON_HEADER = By.XPATH, '//p[text() = "Конструктор"]'

    # Страница Аутентификации https://stellarburgers.nomoreparties.site/login
    EMAIL_INPUT_AUTH = By.XPATH, '//label[text() = "Email"]/following-sibling::input'  # Поле ввода имейла на странице
    PASSWORD_INPUT_AUTH = By.XPATH, '//input[@name = "Пароль"]'  # Поле ввода пароля
    LOGIN_BTN_AUTH = By.XPATH, '//button[text()="Войти"]'  # Кнопка войти
    REGISTRATION_BTN_AUTH = By.XPATH, '//a[text()="Зарегистрироваться"]'  # Кнопка регистрации
    PASSWORD_RECOVER_BUTTON_AUTH = By.XPATH, '//a[text()= "Восстановить пароль"]'  # Кнопка восстановить пароль

    #Страница регистрации
    NAME_INPUT_REGISTRATION = By.XPATH, '//label[text()="Имя"]/following-sibling::input'
    EMAIL_INPUT_REGISTRATION = By.XPATH, './/label[text()="Email"]/following-sibling::input'
    PASSWORD_INPUT_REGISTRATION = By.XPATH, './/input[@name="Пароль"]'
    SUBMIT_BUTTON_REGISTRATION = By.XPATH, '//button[text() = "Зарегистрироваться"]'
    PASSWORD_VALIDATION_ERROR_REGISTRATION = By.XPATH, '//p[text() = "Некорректный пароль"]'
    LOGIN_BTN_REGISTRATION_FORM = By.XPATH, '//a[text() = "Войти"]'

    #Личный кабинет
    MAKE_ORDER_BUTTON = By.XPATH, '//button[text()="Оформить заказ"]'
    ORDERS_HISTORY_PERSONAL_ACCOUNT = By.XPATH, '//a[@href = "/account/order-history"]'
    USER_LOGOUT_BTN_FROM_PERSONAL_ACCOUNT = By.XPATH, '//button[@type = "button"]'

    #Страница восстановления пароля
    LOGIN_BTN_PASSWORD_RECOVERY_FORM = By.XPATH, '//a[text() = "Войти"]'
    #Внутри конструктора
    # Селектор
    SELECTED_BUTTON = By.XPATH, ('//div[@class = ''"tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]')
    # "Булки" в меню конструктора
    BUNS_BLOCK = By.XPATH, '//span[text() = "Булки"]'
    #"Соусы" в меню конструктора
    SAUCES_BLOCK = By.XPATH, '//span[text() = "Соусы"]'
    #"Начинки" в меню конструктора
    FILLINGS_BLOCK = By.XPATH, '//span[text() = "Начинки"]'
    #logo в хедере
    LOGO = By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]'
    #уведомление "некорректный пароль"
    WRONG_PASSWORD = By.XPATH, '//p[text() = "Некорректный пароль"]'




















