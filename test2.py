from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#init set
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

#locators and text
MAIN_PAGE = "https://www.amazon.com"
EXPECTED_TEXT = "Sign-In"
ORDER_BTN = (By.ID, 'nav-orders')
SEARCH_TEXT = (By.XPATH, "//h1[@class='a-spacing-small']")


#Actions
driver.get(MAIN_PAGE)
driver.find_element(*ORDER_BTN).click()
actual_text = driver.find_element(*SEARCH_TEXT).text

#assertion
assert actual_text in EXPECTED_TEXT, f"Expected text: {EXPECTED_TEXT}, but got {actual_text}"

driver.quit()