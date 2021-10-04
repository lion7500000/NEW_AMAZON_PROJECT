from behave import given,when,then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

NAV_DESKTOP = (By.CSS_SELECTOR,"div#zg_header ul li" )


@given ("Open_BestSellers_Page {https}")
def Open_page (context,https):
    context.driver.get(https)


@when ("veryfy the page has {expected_links} links")
def verify_links(context,expected_links):
    menu= len(context.driver.find_elements(*NAV_DESKTOP))
    assert menu==int(expected_links), f'Expexted links is: {expected_links},but got: {menu}'