###### Finance2File.py ######

# Libraries
import pandas as pd
import yfinance as yf
import os
from fs_organiser import CompanyFinancials

# This block of code allows all the data to get printed into its file
# Otherwise there is a cap to the num of columns and rows
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.max_colwidth", None)
pd.set_option("display.width", None)

# Reason for this class is to create multiple recorded finance documents of different companies. 1 object per company
# NOTE: within 'outputs' have program create new folder named ofter the ticker containing its unique finances
class ReportExporter:
    def __init__(self, company):
        self.company = company      # Receives the CompanyFinancials object

    def store_data_file(self):

        # Automatically detects current directory so program know where to create files no matter where the project is stored
        # Finds the location of this exact file (Finance2File.py) in my case E:\Financial_Analysis\modules\Finance2File.py
        # then os.path.dirname() cuts off the last item, resulting in the location of Finance2File.py 's parents folder
        current_file_dir = os.path.dirname(os.path.abspath(__file__))
        base_dir = os.path.dirname(current_file_dir)              # Cuts off the last item again to get E:\Financial_Analysis

        output_dir = os.path.join(base_dir, "outputs")            # adds the outputs folder to the end, so E:\Financial_Analysis\outputs
        os.makedirs(output_dir, exist_ok=True)                    # Creates outputs folder incase it isn't downloaded

        pathBS = os.path.join(output_dir, "balance_sheet.csv")
        pathCS = os.path.join(output_dir, "cash_flow.csv")
        pathIC = os.path.join(output_dir, "income_statement.csv")

        # Converts nested dictionary -> Data Frame -> .csv file
        pd.DataFrame.from_dict(self.company.balanceSheet).to_csv(pathBS)
        print(f"Wrote {self.company.ticker} to balance sheet")

        # Converts nested dictionary -> Data Frame -> .csv file
        pd.DataFrame.from_dict(self.company.cashFlow).to_csv(pathCS)
        print(f"Wrote {self.company.ticker} to cash flow")

        # Converts nested dictionary -> Data Frame -> .csv file
        pd.DataFrame.from_dict(self.company.incomeStatement).to_csv(pathIC)
        print(f"Wrote {self.company.ticker} to income statement")



# --- Hooking up the 2 classes ---
if __name__ == "__main__":
    user_ticker = input("Enter a Ticker: ")

    # Creates an object from CompanyFinancials
    company = CompanyFinancials(user_ticker)
    company.load_financial_data()

    # Creates and object from ReportExporter
    companyDocs1 = ReportExporter(company)
    companyDocs1.store_data_file()