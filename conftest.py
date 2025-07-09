import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from pages.account_page import AccountPage
from pages.constructor_page import ConstructorPage
from locators.account_login_page_locator import PersonalAccountLocators
from data.urls import *
import requests
import uuid

@pytest.fixture(params=['Chrome', 'Firefox'])
def driver(request):
    if request.param == 'Chrome':
        options = ChromeOptions()
        browser = webdriver.Chrome(options=options)
    else:
        options = FirefoxOptions()
        browser = webdriver.Firefox(options=options)

    yield browser
    browser.quit()

@pytest.fixture(scope='function')
def create_user_and_delete():
    email = f"test_{uuid.uuid4().hex[:8]}@example.com"
    password = "test123"
    name = "Test User"

    payload = {"email": email, "password": password, "name": name}
    response = requests.post(REGISTER_URL, json=payload)
    assert response.status_code == 200

    tokens = response.json()
    access_token = tokens["accessToken"]
    refresh_token = tokens["refreshToken"]

    yield {
        "email": email,
        "password": password,
        "name": name,
        "access_token": access_token,
        "refresh_token": refresh_token,
    }

    headers = {"Authorization": access_token}
    delete_response = requests.delete(DELETE_USER_URL, headers=headers)
    assert delete_response.status_code in [200, 202]

@pytest.fixture
def login_user(driver, create_user_and_delete):
    user_email = create_user_and_delete["email"]
    user_password = create_user_and_delete["password"]

    page = AccountPage(driver)
    page.go_to_base_url()
    page.click_profile_button()
    page.login_in_account(user_email, user_password)

    yield



@pytest.fixture
def create_order(driver, login_user):
    page = ConstructorPage(driver)
    return page.create_an_order()