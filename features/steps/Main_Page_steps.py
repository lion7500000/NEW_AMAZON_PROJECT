from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from behave import given,then,when

AMAZON_MAIN_PAGE = "https://www.amazon.com/"
SIGH_IN_BTN = (By.CSS_SELECTOR,"#nav-signin-tooltip >a")



@given ("Open Amazon Main Page")
def Main_Page (context):
    context.app.main_page.open_amazon_page()


@then ("Input {text} into Amazon serch field")
def input_serch_word(context,text):
    context.app.main_page.input_serch_word("Dress")


@then ("Click on Amazon serch icon")
def click_serch_icon (context):
    context.app.main_page.click_serch_icon()


@then ("Search result Dress is shown")
def verify_serch_result (context):
    context.app.search_results_page.verify_serch_results('"Dress"')

@then ("Verify Sigh In is visible")
def Sigh_in_visible(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGH_IN_BTN))


@then ("Verify Sing In disappears")
def Sigh_in_disappears (context):
    context.driver.wait.until(EC.invisibility_of_element_located(SIGH_IN_BTN))


@then ("Verify Sign In page is opened")
def veriry_Sin_IN_pageopen(context):
    context.app.search_results_page.verify_Sign_In_rezult_in_order("Sign-In")


@then ("Verify 'Your Amazon Cart is empty' text present")
def veriry_Sin_IN_pageopen(context):
    context.app.search_results_page.verify_Cart_is_empty("Your Amazon Cart is empty")


@then ("Verify {select} department is selected")
def verify_department_selected (context,select):
    context.app.search_results_page.verify_department_selected(select)


@when ("Waite {time} sec")
def wait_time (contect,time):
    sleep(int(time))


@when ("Click to open Hamburger Menu")
def click_humburger_menu(context):
    context.app.main_page.click_humburger_menu()


@when ("Click Amazon Orders link")
def click_order_link (context):
    context.app.main_page.click_order_link()


@when ("Click on cart icon")
def Click_cart_icon(context):
    context.app.main_page.click_cart_icon()

@when ("Selected Books department")
def select_books_department (context):
    context.app.main_page.select_books_department()


@when ("Search for {text}")
def input_serch_word(context,text):
    context.app.main_page.input_serch_word(text)
    context.app.main_page.click_serch_icon()




