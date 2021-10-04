from behave import given,then,when
from selenium.webdriver.common.by import By
from time import sleep


@given ("Open amazon product {product_id}")
def open_amazon_product_page (context,product_id):
    context.app.product_page.open_product(product_id)


@when ("Hover over Add to Cart button")
def hover_over_add_to_cart (context):
    context.app.product_page.hover_add_to_cart()
    sleep(1)


@when ("Hover over New Arrivals")
def hover_to_new_arrivels(context):
    context.app.product_page.hover_new_arrivals()
    sleep(1)


@then ("Verify Size selection tooltip is show")
def verify_size_tooltip (context):
    context.app.product_page.verify_size_tooltip()


@then ("Verify New Arrivals is show")
def verify_new_arrivals(context):
    context.app.product_page.verify_new_arrivals_present("New Arivals")