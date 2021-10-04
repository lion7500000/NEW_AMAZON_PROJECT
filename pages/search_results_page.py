from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResults(Page):


    SERCH_RESULT=(By.XPATH,"//span[@class='a-color-state a-text-bold']")
    SIGN_IN_TEXT_ACTUAL = (By.CSS_SELECTOR, "h1.a-spacing-small")
    CART_PAGE_ACTUAL_TEXT= (By.CSS_SELECTOR,"h2.sc-your-amazon-cart-is-empty")
    BOOKS_DEPERTMENT = (By.CSS_SELECTOR,"div#nav-subnav[data-category='books'] a[href*='books']")

    def verify_serch_results(self,expected_text):
        self.verify_text(expected_text,*self.SERCH_RESULT)


    def verify_Sign_In_rezult_in_order (self,expected_text):
        self.verify_text(expected_text,*self.SIGN_IN_TEXT_ACTUAL)


    def verify_Cart_is_empty (self,expected_text):
        self.verify_text(expected_text,*self.CART_PAGE_ACTUAL_TEXT)

    def verify_department_selected (self,expected_text):
        self.verify_text(expected_text,*self.BOOKS_DEPERTMENT)
