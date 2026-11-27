from fs_organiser import CompanyFinancials

class Calculations:
    def __init__(self, company):
        self.company = company

    def NetProfitMargin(self, year):
        return round((self.company.incomeStatement[year]["NetIncome"] / self.company.incomeStatement[year]["TotalRevenue"]) * 100)

    def EPS(self, year):
        return round(self.company.incomeStatement[year]["NetIncome"] / self.company.incomeStatement[year]["BasicAverageShares"], 2)

    def WorkingCapitalRatio(self, year):
        return round(self.company.balanceSheet[year]["CurrentAssets"] / self.company.balanceSheet[year]["CurrentLiabilities"], 2)

    def ROE(self, year):
        return round(self.company.incomeStatement[year]["NetIncome"] / self.company.balanceSheet[year]["StockholdersEquity"], 2)

    def DebtToEquityRatio(self, year):
        return round(self.company.balanceSheet[year]["TotalDebt"] / self.company.balanceSheet[year]["StockholdersEquity"], 2)

    def FreeCashFlow(self, year):
        return round(self.company.cashFlow[year]["FreeCashFlow"])





# --- Test Zone ---
if __name__ == "__main__":
    ticker = input("Enter ticker : ")
    year = str(input("Enter year : "))
    company = CompanyFinancials(ticker)
    company.load_financial_data()

    ratios = Calculations(company)
    print(f"Net Profit Margin ({year}): {ratios.NetProfitMargin(year)}%")
    print(f"EPS ({year}): {ratios.EPS(year)}")
    print(f"Working Capital Ratio ({year}): {ratios.WorkingCapitalRatio(year)}")
    print(f"ROE ({year}): {ratios.ROE(year)}")
    print(f"Debt-To-Equity Ratio ({year}): {ratios.DebtToEquityRatio(year)}")
    print(f"Free Cash Flow ({year}): {ratios.FreeCashFlow(year)}")

