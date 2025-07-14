from selenium.webdriver.common.by import By

class RecoverPass:
    RECOVER_PASS_BTN = (By.XPATH, "//a[text() = 'Восстановить пароль']")
    EMAIL_INPUT = (By.XPATH, '//label[text()="Email"]/following-sibling::input')
    RECOVER_BTN = (By.XPATH, "//button[text()='Восстановить']")
    SHOW_PASS_TOGGLE = (By.XPATH, '//div[contains(@class,"icon-action")]')
    PASSWORD_FIELD_IS_ACTIVE = (By.CSS_SELECTOR, ".input.input_status_active")


