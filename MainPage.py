
from selenium.webdriver.common.by import By



class MainPage:  # положить товар в корзину
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self):
        self.driver.find_element(By.XPATH, '//*[@id="content"]/div[2]/div[2]/div/div[3]/button[1]').click()

    def open_cart(self):
        self.driver.find_element(By.XPATH, '//*[@id="cart"]/button').click()

    def checkout(self):
        self.driver.get("http://127.0.0.1:8081/index.php?route=checkout/checkout")
