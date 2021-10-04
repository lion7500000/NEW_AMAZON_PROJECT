from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import Given,When,Then

#locators and text
MAIN_PAGE = "https://www.amazon.com"
EXPECTED_TEXT = "Sign-In"
ORDER_BTN = (By.ID, 'nav-orders')
SEARCH_TEXT = (By.XPATH, "//h1[@class='a-spacing-small']")

@Given ("Open Amazon site {link}")
def Open_Amazon_Page(context,link):
    context.driver.get(link)

@When ("Click Orders")
def Click_Order_Btn (context):
    context.driver.find_element(*ORDER_BTN).click()
    actual_text = context.driver.find_element(*SEARCH_TEXT).text

@Then ("Verify {text} page opened")
def Verify_Page (context,text):
    actual_text = context.driver.find_element(*SEARCH_TEXT).text
    assert actual_text in text, f"Expected text: {text}, but got {actual_text}"


