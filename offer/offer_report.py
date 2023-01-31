from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from prettytable import PrettyTable
import xlsxwriter
import csv
import os

class OfferReport:
    def __init__(self, driver:WebDriver):
        self.driver = driver
        self.offer_boxes = []
        self.offer_box_attributes = []
        self.nombre_total_offres = 0

    def pull_offer_boxes(self):
        self.offer_boxes = self.driver.find_elements(By.CSS_SELECTOR, 'li[class~="tw-mb-6"]')
        self.nombre_total_offres = self.nombre_total_offres + len(self.offer_boxes)
        self.pull_offer_box_attributes()

    def pull_offer_box_attributes(self):
        for offer_box in self.offer_boxes:
            company_name = offer_box.find_element(By.CSS_SELECTOR, 'span[data-cy="companyName"] > span').get_attribute("innerHTML").strip()
            offer_title = offer_box.find_element(By.CSS_SELECTOR, 'div[class~="offer--maininfo"]  a').get_attribute("title").strip()
            offer_location = offer_box.find_element(By.CSS_SELECTOR, 'div[data-cy="loc"] > span > span').get_attribute("innerHTML").strip()

            self.offer_box_attributes.append(
                [company_name,offer_title,offer_location]
            )

    def get_offer_console_report(self):
        table = PrettyTable(
            field_names = ["Nom Entreprise","Intitulé Poste","Lieu"]
        )
        table.add_rows(self.offer_box_attributes)
        print(f"\nNombre total d'offres: {self.nombre_total_offres}")
        print(table)

    def get_offer_xlsx_report(self):
        wb = xlsxwriter.Workbook("Scrapped_offers.xlsx")
        ws = wb.add_worksheet()
        row = 0
        col = 0
        for line in self.offer_box_attributes:
            for item in line:
                ws.write(row, col, item)
                col += 1
            row += 1
            col = 0

        wb.close()
        os.system("Scrapped_offers.xlsx")

    def get_offer_csv_report(self):
        self.offer_box_attributes.insert(0, ["Nom Entreprise", "Intitulé Poste", "Lieu"])
        with open("Scrapped_offers.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(self.offer_box_attributes)

