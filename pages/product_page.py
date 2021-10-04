from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class Product(Page):


    ADD_TO_CART_BTN = (By.ID,'add-to-cart-button')
    SIZE_SELECTION_TOOLTIP = (By.ID,"a-popover-content-1")
    NEW_ARRIVALS_MENU = (By.CSS_SELECTOR,"a[href*='sr_hi_2']")
    NEW_ARRIVALS_TEXT = (By.CSS_SELECTOR,"img[alt*='New Arrivals']")


    def open_product (self, product_id):
        self.open_page(f'https://www.amazon.com/dp/{product_id}')


    def hover_add_to_cart(self):
        cart_btn = self.find_element(*self.ADD_TO_CART_BTN)
        actions = ActionChains(self.driver)
        actions.move_to_element(cart_btn).perform()


    def hover_new_arrivals(self):
        new_arrivals_menu = self.find_element(*self.NEW_ARRIVALS_MENU)
        actions = ActionChains(self.driver)
        actions.click(new_arrivals_menu).perform()


    def verify_size_tooltip(self):
        self.wait_for_element_appiar(*self.SIZE_SELECTION_TOOLTIP)


    def verify_new_arrivals_present(self,expected_text):
        self.verify_text(expected_text,*self.NEW_ARRIVALS_TEXT)

