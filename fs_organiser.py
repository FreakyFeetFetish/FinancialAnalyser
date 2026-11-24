###### fs_organiser.py ######
import yfinance as yf
import pandas as pd

pd.set_option("display.max_rows", None)

ticker = input("Enter ticker: ")

#   Loads the data from Yahoo Finance and stores it in dictionaries
def load_financial_data(ticker):

    try:
        tik = yf.Ticker(ticker)

        bs = tik.get_balance_sheet()
        ic = tik.get_income_stmt()
        cf = tik.get_cash_flow()

        if bs.empty and ic.empty and cf.empty:
            raise ValueError(f"{ticker} is an invalid ticker")
    except ValueError:
        pass

    cashFlow = {}
    balanceSheet = {}
    incomeStatement = {}

    for y in bs.columns:            # selects an entire collum within the scraped balancesheet
        myYear = str(y)[:4]         # takes the first 4 letters of the collum, ex. 2024-12-31 and takes 2024
        balanceSheet[myYear] = {}   # creates an empty folder: balanceSheet["2025"] = {}

        for x in bs.index:          # Goes down the collum, and stores whatever vales
            balanceSheet[myYear][x] = bs.loc[x, y]

    for y in cf.columns:
        myYear = str(y)[:4]
        cashFlow[myYear] = {}
        for x in cf.index:
            cashFlow[myYear][x] = cf.loc[x, y]

    for y in ic.columns:
        myYear = str(y)[:4]
        incomeStatement[myYear] = {}
        for x in ic.index:
            incomeStatement[myYear][x] = ic.loc[x, y]

    return balanceSheet, cashFlow, incomeStatement, ticker

BalanceSheet, CashFlow, IncomeStatement, _ = load_financial_data(ticker)

print(BalanceSheet["2026"]["OrdinarySharesNumber"])





