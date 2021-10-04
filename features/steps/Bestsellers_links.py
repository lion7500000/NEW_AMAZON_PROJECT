from behave import given,then
from selenium.webdriver.common.by import By

BESTSELLERS_LINKS = (By.CSS_SELECTOR,"#zg_tabs a")
HEADERS= (By.XPATH,"//div[@id='zg_banner_text_wrapper']")


@given ("Open Amazon Bestsellers Page")
def Amazon_bestsellers(context):
    context.driver.get('https://www.amazon.com/Best-Sellers/zgbs/ref=zg_bs_tab')


@then ("User can click through top links and verify it")
def veryfi_bestseller_links(context):
    links_header=context.driver.find_elements(*BESTSELLERS_LINKS)

    for i in range(len(links_header)):
        links = context.driver.find_elements(*BESTSELLERS_LINKS)[i]

        link_text = links.text
        links.click()

        header_text = context.driver.find_element(*HEADERS).text

        assert link_text in header_text, f"Expected {link_text} not in {heade_text}"