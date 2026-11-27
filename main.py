###### Main ######

# Libraries
from fs_organiser import CompanyFinancials
from Finance2File import ReportExporter
from FinancialCalculations import *

print("Enter company ticker per line (Press Enter on a blank line when finished)")
Companies = []

# Allows input of multiple tickers, processes them as they are entered, and stored in a list once completed
while True:
    ticker = input("> ").strip().upper()
    if ticker == "":    # Pressing enter stops loop
        break

    # Creates and uses CompanyFinancial Class
    comp = CompanyFinancials(ticker)
    comp.load_financial_data()

    # Creates and uses ReportExporter Class
    compOrganise = ReportExporter(comp)
    compOrganise.store_data_file()

    # Adds the current ticker to list of Companies
    Companies.append(ticker)

print(Companies)
