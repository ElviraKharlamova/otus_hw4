
from selenium.webdriver.common.by import By



class ChangeCurrency:
    def __init__(self, driver):
        self.driver = driver

    def check_currency_changes(self):
        self.driver.find_element(By.CLASS_NAME, "btn btn-link dropdown-toggle").click()
        self.driver.find_element(By.XPATH, '//*[@id="form-currency"]/div/ul/li[1]/button').click()
        price1 = self.driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[2]/p[2]/text()')
        self.driver.find_element(By.CLASS_NAME, "btn btn-link dropdown-toggle").click()
        self.driver.find_element(By.XPATH, '//*[@id="form-currency"]/div/ul/li[2]/button').click()
        price2 = self.driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[2]/p[2]/text()')
        self.driver.find_element(By.CLASS_NAME, "btn btn-link dropdown-toggle").click()
        self.driver.find_element(By.XPATH, '//*[@id="form-currency"]/div/ul/li[3]/button').click()
        price3 = self.driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[2]/p[2]/text()')
        assert price1 != price2
        assert price1 != price3
