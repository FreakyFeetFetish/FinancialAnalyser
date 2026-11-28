###### FinancialCalculations.py ######

# Libraries
from fs_organiser import CompanyFinancials

# Calculates the profitability, liquididy, leverage, and valuation for CompanyFinancials object
class Calculations:
    def __init__(self, company):
        self.company = company


    # --- Profitability Ratios ---

    # The percentage of Revenue kept as net profit after all expenses and taxes
    def NetProfitMargin(self, year):
        return round((self.company.incomeStatement[year]["NetIncome"] / self.company.incomeStatement[year]["TotalRevenue"]) * 100, 2)

    # Percentage of revenue remaining after subtracting production costs (COGS)
    def GrossProfitMargin(self, year):
        return round((self.company.incomeStatement[year]["GrossProfit"] / self.company.incomeStatement[year]["TotalRevenue"]) * 100, 2)

    # Percentage of revenue generated as profit from core business operations before interest and taxes
    def OperatingProfitMargin(self, year):
        return round((self.company.incomeStatement[year]["OperatingIncome"] / self.company.incomeStatement[year]["TotalRevenue"]) * 100, 2)

    # Return on Equity (%): Measures how efficiently shareholder equity is used to generate net profit
    def ROE(self, year):
        return round((self.company.incomeStatement[year]["NetIncome"] / self.company.balanceSheet[year]["StockholdersEquity"]) *100, 2)

    # Return on Assets (%): Measures how efficiently total company assets generate net profit
    def ROA(self, year):
        return round((self.company.incomeStatement[year]["NetIncome"] / self.company.balanceSheet[year]["TotalAssets"]) * 100, 2)

# --- Liquidity & Leverage Ratios ---

    # Measures short term liquidity
    def WorkingCapitalRatio(self, year):
        return round(self.company.balanceSheet[year]["CurrentAssets"] / self.company.balanceSheet[year]["CurrentLiabilities"], 2)

    # Measures financial leverage by comparing total debt to stockholder equity
    def DebtToEquityRatio(self, year):
        try:
            return round(self.company.balanceSheet[year]["TotalDebt"] / self.company.balanceSheet[year]["StockholdersEquity"], 2)
        except(KeyError, ZeroDivisionError, TypeError):
            return "N/A"

# --- Cash FLow & Valuation ---

    # Earnings Per Share ($): Net profit allocated to each outstanding share of common stock
    def EPS(self, year):
        return round(
            self.company.incomeStatement[year]["NetIncome"] / self.company.incomeStatement[year]["BasicAverageShares"],2)

    # Actual cash remaining after operating expenses and capital expenditures
    def FreeCashFlow(self, year):
        return round(self.company.cashFlow[year]["FreeCashFlow"])

    # Total market value of the company's outstanding shares
    def MarketCapitalisation(self):
        return round(self.company.marketCap)

    # Price-to-Earnings Ratio: Compares current share price against Earnings Per Share (reuses self.EPS)
    def PEratio(self, year):
        return round (self.company.price / self.EPS(year), 2)

    # Price-to-Book Ratio: Compares market capitalisation against net book value (Stockholders Equity)
    def PBratio(self, year):
        return round(self.company.marketCap / self.company.balanceSheet[year]["StockholdersEquity"], 2)

    # Price-to-Sales Ratio: Compares market capitalisation against annual total revenue
    def PSratio(self, year):
        return round(self.company.marketCap / self.company.incomeStatement[year]["TotalRevenue"], 2)

    # --- Year by year Comparison ---

    # loops through all years from oldest to newest for any ratio method
    def Get_Metric_over_time(self, metric_function):
        years = sorted(self.company.incomeStatement.keys())
        history = {}

        for y in years:
            try:
                history[y] = float(metric_function(y))
            except(KeyError, ZeroDivisionError, TypeError):
                history[y] = None   # Deals with missing years
        return history

    def OutputRatios(self, year):
        print( f"\n====== {self.company.ticker} ({year}) ======")
        print(f"Net Profit Margin ({year}): {self.NetProfitMargin(year)}%")
        print(f"Gross Profit Margin ({year}): {self.GrossProfitMargin(year)}%")
        print(f"Operating Profit Margin ({year}): {self.OperatingProfitMargin(year)}%")
        print(f"ROE ({year}): {self.ROE(year)}%")
        print(f"ROA ({year}): {self.ROA(year)}%")
        print(f"Working Capital Ratio ({year}): {self.WorkingCapitalRatio(year)}")
        print(f"Debt-To-Equity Ratio ({year}): {self.DebtToEquityRatio(year)}")
        print(f"EPS ({year}): {self.EPS(year)}")
        print(f"Free Cash Flow ({year}): {self.FreeCashFlow(year)}")
        print(f"Market Cap: {self.MarketCapitalisation()}")
        print(f"PEratio ({year}): {self.PEratio(year)}")
        print(f"Price-to-Book ratio ({year}): {self.PBratio(year)}")
        print(f"Price-to-Shares ratio ({year}): {self.PSratio(year)}")
        print(f"Metric over time :{self.Get_Metric_over_time(self.NetProfitMargin)}\n")




# --- Test Zone ---
if __name__ == "__main__":
    ticker = input("Enter ticker : ")
    year = str(input("Enter year : "))
    company = CompanyFinancials(ticker)
    company.load_financial_data()

    ratios = Calculations(company)
    ratios.OutputRatios(year)

