
class LogoutPage:
    def __init__(self, driver):
        self.driver = driver

    def logout(self, driver):
        driver.get("http://127.0.0.1:8081/index.php?route=account/logout")
