import pytest
from selenium import webdriver
from faker import Faker
from CartPage import CartPage
from ChangeCurrency import ChangeCurrency
from LoginPage import LoginPage
from LogoutPage import LogoutPage
from MainPage import MainPage
from RegistrationPage import RegistrationPage


@pytest.fixture(scope="module")
def faker():
    # Create a Faker instance
    return Faker()


@pytest.fixture(scope="module")
def driver():
    # Create a WebDriver instance using Chrome
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"  # Specify the actual path to the Chrome executable

    driver = webdriver.Chrome(executable_path="E:\Загрузки\chromedriver_win32 (2)\chromedriver.exe",
                              chrome_options=chrome_options)
    yield driver


def test_registration(faker, driver):
    name = faker.name()
    surname = faker.last_name()
    email = faker.email()
    phone_number = faker.phone_number()
    password = faker.password()

    registration_page = RegistrationPage(driver)
    driver.get("http://127.0.0.1:8081/index.php?route=account/register")

    registration_page.fill_registration_form(name, surname, phone_number, email, password)
    registration_page.accept_terms_and_conditions()
    registration_page.submit_registration_form()


def test_currency_changes(driver):  # проверка изменения цен
    changeCurrencyPage = ChangeCurrency(driver)
    changeCurrencyPage.check_currency_changes()


def test_login_logout(driver):
    loginPage = LoginPage(driver)
    logoutPage = LogoutPage(driver)

    driver.get("http://127.0.0.1:8081/index.php?route=account/login")  # loginPage
    loginPage.login("user@email.com", "password123")
    driver.get("http://127.0.0.1:8081/index.php?route=account/account")  # logoutPage
    logoutPage.logOut()


def test_registration_and_checkout(faker, driver):
    main_page = MainPage(driver)
    driver.get("http://127.0.0.1:8081/index.php?route=common/home")

    main_page.add_to_cart()
    main_page.open_cart()
    main_page.checkout()

    cartPage = CartPage(driver, faker)
    driver.get("http://127.0.0.1:8081/index.php?route=checkout/checkout")
    cartPage.click_register_account()
    cartPage.fill_register_account()


def test_guest_checkout(driver, faker):
    main_page = MainPage(driver)
    driver.get("http://127.0.0.1:8081/index.php?route=common/home")

    main_page.add_to_cart()
    main_page.open_cart()
    main_page.checkout()

    cartPage = CartPage(driver, faker)
    driver.get("http://127.0.0.1:8081/index.php?route=checkout/checkout")
    cartPage.click_guest_checkout()
    cartPage.fill_guest_account()




