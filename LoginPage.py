from selenium.webdriver.common.by import By



class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):
        self.driver.find_element(By.ID, "input-email").send_keys(email)
        self.driver.find_element(By.ID, "input-password").send_keys(password)
        self.driver.find_element(By.CLASS_NAME, "btn btn-primary").click()
