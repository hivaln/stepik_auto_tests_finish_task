from selenium.webdriver.common.by import By
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.locators import MainPageLocators

link = "http://selenium1py.pythonanywhere.com/" 

def test_should_be_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)
    login_page.open()
    
    login_page.should_be_login_page()