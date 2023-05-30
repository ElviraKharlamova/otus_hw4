import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class CartPage:  # оформление товара в корзине
    def __init__(self, driver, faker):
        self.driver = driver
        self.faker = faker

    def click_register_account(self):
        button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.driver.find_element(By.XPATH,'//*[@id="collapse-checkout-option"]/div/div/div[1]/div[1]/label')))
        button.click()
        self.driver.find_element(By.ID, 'button-account').click()

    def click_guest_checkout(self):
        self.driver.find_element(By.XPATH,
                                 '//input[@value="guest"]').click()
        self.driver.find_element(By.CLASS_NAME, 'btn btn-primary').click()

    def fill_register_account(self):
        password = self.faker.password()
        address = self.faker.address().split(",")
        self.driver.find_element(By.ID, "input-payment-firstname").send_keys(self.faker.name())
        self.driver.find_element(By.ID, "input-payment-lastname").send_keys(self.faker.last_name())
        self.driver.find_element(By.ID, "input-payment-email").send_keys(self.faker.email())
        self.driver.find_element(By.ID, "input-payment-telephone").send_keys(self.faker.phone_number())
        self.driver.find_element(By.ID, "input-payment-company").send_keys(self.faker.company())
        self.driver.find_element(By.ID, "input-payment-address-1").send_keys(address[0])
        self.driver.find_element(By.ID, "input-payment-address-2").send_keys(address[1])
        self.driver.find_element(By.ID, "input-payment-city").send_keys(self.faker.city())
        self.driver.find_element(By.ID, "input-payment-postcode").send_keys(self.faker.postcode())
        country = Select(self.driver.find_element_by_id('input-payment-country'))
        country.select_by_index(random.randint(1, 259))
        region = Select(self.driver.find_element_by_id('input-payment-zone'))
        region.select_by_index(random.randint(3513, 3612))
        self.driver.find_element(By.ID, "input-payment-password").send_keys(password)
        self.driver.find_element(By.ID, "input-payment-confirm").send_keys(password)
        self.driver.find_element(By.XPATH, '//*[@id="collapse-payment-address"]/div/div[3]/div/input[1]').click
        self.driver.find_element(By.ID, "button-register").click()

        def fill_guest_account(self):
            address = self.faker.address().split(",")
            self.driver.find_element(By.ID, "input-payment-firstname").send_keys(self.faker.name())
            self.driver.find_element(By.ID, "input-payment-lastname").send_keys(self.faker.last_name())
            self.driver.find_element(By.ID, "input-payment-email").send_keys(self.faker.email())
            self.driver.find_element(By.ID, "input-payment-telephone").send_keys(self.faker.phone_number())
            self.driver.find_element(By.ID, "input-payment-company").send_keys(self.faker.company())
            self.driver.find_element(By.ID, "input-payment-address-1").send_keys(address[0])
            self.driver.find_element(By.ID, "input-payment-address-2").send_keys(address[1])
            self.driver.find_element(By.ID, "input-payment-city").send_keys(self.faker.city())
            self.driver.find_element(By.ID, "input-payment-postcode").send_keys(self.faker.postcode())
            country = Select(self.driver.find_element_by_id('input-payment-country'))
            country.select_by_index(random.randint(1, 259))
            region = Select(self.driver.find_element_by_id('input-payment-zone'))
            region.select_by_index(random.randint(3513, 3612))
            self.driver.find_element(By.ID, "button-guest").click()

