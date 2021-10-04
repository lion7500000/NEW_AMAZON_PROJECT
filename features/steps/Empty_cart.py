from behave import given,when,then
from selenium.webdriver.common.by import By

CART = (By.ID,"nav-cart")
CART_MSG_EMP = (By.CSS_SELECTOR,".sc-your-amazon-cart-is-empty")


@then ("Shopping cart is empty")
def Verify_emp_cart (context):
    result_msg = context.driver.find_element(*CART_MSG_EMP).text
    assert 'empty' in result_msg, f"Expected to be empty cart, but it is not"