###### fs_organiser.py ######
import yfinance as yf
import pandas as pd

pd.set_option("display.max_rows", None)


class CompanyFinancials:
    def __init__(self, ticker):
        self.ticker = ticker
        self.cashFlow = {}
        self.balanceSheet = {}
        self.incomeStatement = {}

    def load_financial_data(self):  #   Loads the data from Yahoo Finance and stores it in dictionaries

        try:
            tik = yf.Ticker(self.ticker)

            bs = tik.get_balance_sheet()
            ic = tik.get_income_stmt()
            cf = tik.get_cash_flow()

            if bs.empty and ic.empty and cf.empty:
                raise ValueError(f"{ticker} is an invalid ticker")
        except ValueError:
            print("Invalid company")

        for y in bs.columns:            # selects an entire collum within the scraped balance sheet
            myYear = str(y)[:4]         # takes the first 4 letters of the collum, ex. 2024-12-31 and takes 2024
            self.balanceSheet[myYear] = {}   # creates an empty folder: balanceSheet["2025"] = {}

            for x in bs.index:          # Goes down the collum, and stores whatever vales
                self.balanceSheet[myYear][x] = bs.loc[x, y]

        for y in cf.columns:
            myYear = str(y)[:4]
            self.cashFlow[myYear] = {}
            for x in cf.index:
                self.cashFlow[myYear][x] = cf.loc[x, y]

        for y in ic.columns:
            myYear = str(y)[:4]
            self.incomeStatement[myYear] = {}
            for x in ic.index:
                self.incomeStatement[myYear][x] = ic.loc[x, y]

user_ticker = input("Enter ticker: ")

company = CompanyFinancials(user_ticker)
company.load_financial_data()

print(company.balanceSheet["2025"]["NetDebt"])






