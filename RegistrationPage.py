from selenium.webdriver.common.by import By

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver

    def fill_registration_form(self, firstname, lastname, telephone, email, password):
        self.driver.find_element(By.ID, "input-firstname").send_keys(firstname)
        self.driver.find_element(By.ID, "input-lastname").send_keys(lastname)
        self.driver.find_element(By.ID, "input-telephone").send_keys(telephone)
        self.driver.find_element(By.ID, "input-email").send_keys(email)
        self.driver.find_element(By.ID, "input-password").send_keys(password)
        self.driver.find_element(By.ID, "input-confirm").send_keys(password)

    def accept_terms_and_conditions(self):
        checkbox = self.driver.find_element(By.NAME, "agree")
        checkbox.click()

    def submit_registration_form(self):
        self.driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
