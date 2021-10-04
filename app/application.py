from pages.main_page import MainPage
from pages.search_results_page import SearchResults
from pages.humburger_menu import Humburger_Menu
from pages.product_page import Product


class Application:


    def __init__(self,driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.search_results_page = SearchResults(self.driver)
        self.humburger_menu = Humburger_Menu(self.driver)
        self.product_page = Product(self.driver)