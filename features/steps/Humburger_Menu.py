from behave import given,then,when
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@then ("Click on Music Menu item")
def click_click_amazon_music(context):
    context.app.humburger_menu.click_amazon_music()


@then ("Check {item_count} Menue items are present")
def verify_amount_of_item(context,item_count):
    context.app.humburger_menu.verify_amount_of_item(item_count)