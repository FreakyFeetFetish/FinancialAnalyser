###### Finance2File.py ######

import pandas as pd
import yfinance as yf

ticker = yf.Ticker("AAPL")

class reportExporter:
    def __init__(self, tik, comapny = None):
        self.company = company      # Recieves the CompanyFinancials object
        self.tik = tik
    def store_data_file(self):

        self.pathBS = "E:\Financial_Analysis\outputs\BalanceSheet.txt"
        self.pathCS = "E:\Financial_Analysis\outputs\CashFlow.txt"
        self.pathIC = "E:\Financial_Analysis\outputs\IncomeStatement.txt"

        bs = self.tik.balance_sheet
        cf = self.tik.cash_flow
        inc = self.tik.income_stmt

        with open(self.pathBS, "w") as myFile:
            myFile.write(str(bs))
            print("Wrote to balance sheet")

        with open(self.pathCS, "w") as myFile:
            myFile.write(str(cf))
            print("Wrote to cash flow")

        with open(self.pathIC, "w") as myFile:
            myFile.write(str(inc))
            print("Wrote to income statement")

companyDocs1 = reportExporter(ticker)
companyDocs1.store_data_file()


