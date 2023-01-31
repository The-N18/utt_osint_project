import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from offer.offer_filtration import OfferFiltration
from offer.offer_report import OfferReport


class Offer(webdriver.Chrome):
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Offer, self).__init__(options=chrome_options)
        self.implicitly_wait(50)
        self.maximize_window()

    def land_first_page(self):
        self.get("https://www.hellowork.com/fr-fr/stage.html")
        try:
            self.find_element(By.ID,"hw-cc-notice-accept-btn").click()
        except:
            print('Pas de bouton "Tout accepter"')

    def select_offer_field(self, offer_field):
        search_field = self.find_element(By.CSS_SELECTOR,'input[class="autocomplete-innerinput-k"]')
        search_field.clear()
        search_field.send_keys(offer_field)

    def select_offer_place(self, offer_place):
        search_field = self.find_element(By.CSS_SELECTOR,'input[class="autocomplete-innerinput-l"]')
        search_field.clear()
        search_field.send_keys(offer_place)
        self.find_element(By.CSS_SELECTOR, 'span[class="cross-input"] ~ ul > li:first-child > span').click()

    def apply_filtration(self):
        filtration = OfferFiltration(driver=self)
        filtration.select_period('w')

    def report_offers(self):

        report = OfferReport(driver=self)

        pagination_section = self.find_element(By.ID, 'pagin')
        max_page_num = pagination_section.find_element(By.CSS_SELECTOR, 'ul > li:nth-last-child(2)').get_attribute("data-value")

        print("max_page_num",max_page_num)
        print("page", 1)
        report.pull_offer_boxes()

        for i in range(2,int(max_page_num)+1):
            print("page",i)
            page_num = pagination_section.find_element(By.CSS_SELECTOR, f'ul > li[data-value="{i}"')
            page_num.click()
            time.sleep(10)
            report.pull_offer_boxes()


        report.get_offer_console_report()
        report.get_offer_xlsx_report()






