from behave import given,then,when
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


Sign_In_btn = (By.CSS_SELECTOR,"#nav-signin-tooltip >a")


@then ("Sign_In popup is present and clickable")
def Sign_In_present_clickable(context):
    context.driver.wait.until(EC.presence_of_element_located(Sign_In_btn))
    context.driver.wait.until(EC.element_to_be_clickable(Sign_In_btn))

@when("Sign_in popup disappears")
def Sign_In_disappears(context):
    context.driver.wait.until(EC.invisibility_of_element_located(Sign_In_btn))


