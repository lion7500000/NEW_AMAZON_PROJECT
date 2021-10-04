from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import Page


class Humburger_Menu(Page):


    AMAZON_MUSIC_MENU = (By.XPATH,"//ul[contains(@class,'hmenu-visible')]//div[contains(text(),'Amazon Music')]")
    AMAZON_MUSIC_MENU_RESULL = (By.CSS_SELECTOR,"ul.hmenu-visible a:not(.hmenu-back-button)")


    def click_amazon_music(self):
        self.click(*self.AMAZON_MUSIC_MENU)


    def verify_amount_of_item(self,item_count: int):
        items=self.driver.wait.until(
            lambda driver: len(driver.find_elements(*self.AMAZON_MUSIC_MENU_RESULL))
        )
        assert items == item_count, f'result {items}'