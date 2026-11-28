###### Main ######

# Libraries
from fs_organiser import CompanyFinancials
from Finance2File import ReportExporter
from FinancialCalculations import *

print("Enter company ticker per line (Press Enter on a blank line when finished)")
companies = []

# Allows input of multiple tickers, processes them as they are entered, and stored in a list once completed
while True:
    ticker = input("> ").strip().upper()
    if ticker == "":    # Pressing enter stops loop
        break

    # Creates and uses CompanyFinancial Class
    comp = CompanyFinancials(ticker)
    if not comp.load_financial_data():
        continue


    # Creates and uses ReportExporter Class
    compOrganise = ReportExporter(comp)
    compOrganise.store_data_file()

    # Adds the current ticker to list of Companies
    companies.append(comp)

print([c.ticker for c in companies])

print("")

year = input("Enter year: ").strip()

for company in companies:
    ratios = Calculations(company)
    ratios.OutputRatios(year)
