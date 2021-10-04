from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#init set
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

AMAZON_HELP_PAGE = 'https://www.amazon.com/gp/help/customer/display.html'
TEXT = 'Cancel order'
EXPEXTED_TEXT = 'Cancel Items or Orders'
HELP_SEARCH_FIELD = (By.ID, "helpsearch")
SEARCH_TEXT = (By.XPATH, "//*[text()='Cancel Items or Orders']")

#actions
driver.get(AMAZON_HELP_PAGE)
search = driver.find_element(*HELP_SEARCH_FIELD)
search.clear()
search.send_keys(TEXT, Keys.ENTER)

#assertion
actual_text = driver.find_element(*SEARCH_TEXT).text

assert actual_text in EXPEXTED_TEXT,f'Expected text:{EXPEXTED_TEXT}, bot got: {actual_text}'

driver.quit()