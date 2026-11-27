###### fs_organiser.py ######

# Libraries
import yfinance as yf
import sys

# Fetches and stores the financial statement data for a provided ticker
class CompanyFinancials:

    # Creates instance attributes for the ticker and its financial statemetns
    def __init__(self, ticker):
        self.ticker = ticker
        self.price = None
        self.marketCap = None
        self.cashFlow = {}
        self.balanceSheet = {}
        self.incomeStatement = {}

    # Scrapes data from Yahoo Finance and organizes it into nested dictionaries based by the year
    def load_financial_data(self):

        try:        # NOTE: Does not block invalid Tickers
            # Creates a yFinance Ticker object and scrapes the raw data frames
            tik = yf.Ticker(self.ticker)
            bs = tik.get_balance_sheet()
            ic = tik.get_income_stmt()
            cf = tik.get_cash_flow()

            self.price = tik.fast_info.last_price
            self.marketCap = tik.info.get("marketCap")

            # Checks if at least one statement contains data, otherwise it's an invalid Ticker
            if bs.empty and ic.empty and cf.empty:
                print(ValueError(f"{self.ticker} is an invalid ticker"))
                return False    # Incase someone types a bad ticker, it skips and asks again


        except ValueError:
            # Python requires an except block to handle the ValueError raised above
            print("Invalid company")

        # Converts Balance Sheet data frame into nested dictionary
        for y in bs.columns:
            myYear = str(y)[:4]     # Extracts the year from time stamp
            self.balanceSheet[myYear] = {}

            for x in bs.index:
                self.balanceSheet[myYear][x] = bs.loc[x, y]

        # Converts Cash Flow data frame into nested dictionary
        for y in cf.columns:
            myYear = str(y)[:4]
            self.cashFlow[myYear] = {}
            for x in cf.index:
                self.cashFlow[myYear][x] = cf.loc[x, y]

        # Converts Income Statement data frame into nested dictionary
        for y in ic.columns:
            myYear = str(y)[:4]
            self.incomeStatement[myYear] = {}
            for x in ic.index:
                self.incomeStatement[myYear][x] = ic.loc[x, y]





# --- Test Zone (this block will only run I execute this code directly) ---
if __name__ == "__main__":
    user_ticker = input("Enter ticker: ")

    #Creates the CompanyFinances object and fills the dictionaries
    company = CompanyFinancials(user_ticker)
    company.load_financial_data()

    # Check up to verify if program work
    print(company.balanceSheet["2025"]["NetDebt"])