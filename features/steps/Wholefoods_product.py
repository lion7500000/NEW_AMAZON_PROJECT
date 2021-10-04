from behave import given,then
from selenium.webdriver.common.by import By


ITEMS = (By.CSS_SELECTOR,"#wfm-pmd_deals_section div:nth-of-type(5) li")
PRODUCTS = (By.CSS_SELECTOR,"#wfm-pmd_deals_section div:nth-of-type(5) li")

@given ("Open Wholefoods")
def Open_product_page (contect):
    contect.driver.get("https://www.amazon.com/fmc/storedeals/?_encoding=UTF8&almBrandId=VUZHIFdob2xlIEZvb2Rz")


@then ("Each item has Regular filed and Product name")
def Check_items(context):
    all_item = context.driver.find_elements(*ITEMS)
    for item in all_item:
        assert "Regular" in item.text, f"Expected 'Regular' in {item.text}"
        assert context.driver.find_element(*PRODUCTS)