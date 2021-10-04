from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class MainPage(Page):


    SERCH_FILD = (By.ID,"twotabsearchtextbox")
    SERCH_ICON = (By.CSS_SELECTOR,"#nav-search-submit-button")
    ORDER_LINK = (By.ID, "nav-orders")
    CART = (By.ID, "nav-cart")
    HUMBURGER_MENU = (By.ID,"nav-hamburger-menu")
    SELECT_MENU = (By.ID,"searchDropdownBox")



    def open_amazon_page(self):
        self.open_page('https://www.amazon.com/')

    def input_serch_word (self,text):
        self.input_text(text,*self.SERCH_FILD)


    def click_humburger_menu(self):
        self.click(*self.HUMBURGER_MENU)


    def click_serch_icon(self):
        self.click(*self.SERCH_ICON)

    def click_order_link(self):
        self.click(*self.ORDER_LINK)


    def click_cart_icon(self):
        self.click(*self.CART)


    def select_books_department(self):
        select = Select(self.find_element(*self.SELECT_MENU))
        select.select_by_value("search-alias=stripbooks")