from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from app.logger import logger


class Page:


    def __init__(self,driver):
        self.driver = driver
        self_base_url = 'https://www.amazon.com/'
        self.wait = WebDriverWait(self.driver,15)


    def click(self,*locator):
        self.driver.find_element(*locator).click()


    def input_text (self,text,*locator):
        i= self.find_element(*locator)
        i.clear()
        logger.info(f'Input text: {text}')
        i.send_keys(text)
        i.click()


    def open_page (self,url):
        self.driver.get(url)


    def find_element(self,*locator):
        return self.driver.find_element(*locator)


    def find_elements(self,*locator):
        return self.driver.find_elements(*locator)


    def wait_for_element_appiar (self,*locator):
        self.driver.wait.until(EC.presence_of_element_located(locator))


    def wait_for_element_disappiar (self,*locator):
        self.driver.wait.until(EC.invisibility_of_element_located(locator))


    def wait_for_element_click (self,*locator):
        element= self.driver.wait.until(EC.element_to_be_clickable(locator))
        element.click()


    def verify_text(self,expected_text,*locator):
        """
        Search for webelement, get it text
        :param expected_text: text wich in webelement
        :param locator:locator of webelement(ex.(By,'Id'))
        :return:expected text in actual text(locator of webelement)
        """
        actual_text = self.driver.find_element(*locator).text
        assert actual_text in expected_text,f"Error, Expected {expected_text}, but got {actual_text}"