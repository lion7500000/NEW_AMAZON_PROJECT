from behave import given,when,then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

BENEFIT_BOXSES = (By.CSS_SELECTOR,"div.benefit-box")

@given ('Open Amazon Prime Page')
def Open_Prime_Page (context):
    context.driver.get('https://www.amazon.com/amazonprime')

@then ("Verify {expected_count} benefit boxses are displaed")
def Verify_boxses(context,expected_count):
    boxses=len(context.driver.find_elements(*BENEFIT_BOXSES))
    assert boxses == int(expected_count),f'Expected boxses {expected_count}, but got {boxses}'