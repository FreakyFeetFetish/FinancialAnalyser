from fs_organiser import CompanyFinancials

class Calculations:
    def __init__(self, company):
        self.company = company

    def NetProfitMargin(self, year):
        return round((self.company.incomeStatement[year]["NetIncome"] / self.company.incomeStatement[year]["TotalRevenue"]) * 100)

    def EPS(self, year):
        return round(self.company.incomeStatement[year]["NetIncome"] / self.company.incomeStatement[year]["BasicAverageShares"])

    def WorkingCapitalRatio(self, year):
        return round(self.company.balanceSheet[year]["CurrentAssets"] / self.company.balanceSheet[year]["CurrentLiabilities"])





# --- Test Zone ---
if __name__ == "__main__":
    ticker = input("Enter ticker : ")
    year = str(input("Enter year : "))
    company = CompanyFinancials(ticker)
    company.load_financial_data()

    ratios = Calculations(company)
    print(ratios.EPS(year))
