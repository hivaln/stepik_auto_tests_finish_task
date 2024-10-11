from selenium.webdriver.common.by import By
from .pages.main_page import MainPage
from .pages.locators import MainPageLocators


link = "http://selenium1py.pythonanywhere.com/" 

# def go_to_login_page(browser):
#     login_link = browser.find_element(*MainPageLocators.LOGIN_LINK)
#     login_link.click()

# def test_guest_can_go_to_login_page(browser):
#     page = MainPage(browser, link)   
#     page.open()                      
#     page.go_to_login_page()

# def test_guest_should_see_login_link(browser):
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_login_link()

def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()