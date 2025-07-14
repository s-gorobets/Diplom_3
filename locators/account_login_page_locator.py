from selenium.webdriver.common.by import By

class PersonalAccountLocators:
    RESTORE_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
    EMAIL_FIELD = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
    PASSWORD_FIELD = (By.XPATH, '//input[@type="password"]')
    ENTER_BTN = (By.XPATH, '//button[text()="Войти"]')
    ORDER_HISTORY_BTN = (By.XPATH, '//*[@href="/account/order-history"]')
    LOGOUT_BTN = (By.XPATH, '//*[contains(@class, "Account_button")]')
    PROFILE_BTN = (By.XPATH, "//p[text()='Личный Кабинет']")


