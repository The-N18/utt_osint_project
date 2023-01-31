from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time


class OfferFiltration:
    def __init__(self,driver:WebDriver):
        self.driver = driver

    def select_period(self,period):
        drop_down = self.driver.find_element(By.CSS_SELECTOR,'div[data-cypress-d]')

        self.driver.execute_script("arguments[0].scrollIntoView({'block':'center','inline':'center'})", drop_down)
        drop_down.click()

        selected_period = self.driver.find_element(By.CSS_SELECTOR,f'li[data-value="{period}"] > label')
        selected_period.click()
        time.sleep(10)

