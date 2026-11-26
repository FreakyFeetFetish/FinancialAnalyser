###### Finance2File.py ######

# Libraries
import pandas as pd
import yfinance as yf
import os

# Core Variables
ticker = yf.Ticker("NVDA")

# This block of code allows all the data to get printed into its file
# Otherwise there is a cap to the num of columns and rows
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.max_colwidth", None)
pd.set_option("display.width", None)

# Reason for this class is to create multiple recorded finance documents of different companies. 1 object per company
# NOTE: within 'outputs' have program create new folder named ofter the ticker containing its unique finances
class ReportExporter:
    def __init__(self, tik, company = None):
        self.company = company      # Receives the CompanyFinancials object
        self.tik = tik

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


        bs = self.tik.balance_sheet
        cf = self.tik.cash_flow
        inc = self.tik.income_stmt

        with open(pathBS, "w") as myFile:   # Opens an instance where balance_sheet.csv can be edited
            myFile.write(str(bs))           # Writes all data from bs into balance_sheet.csv
            print("Wrote to balance sheet")

        with open(pathCS, "w") as myFile:   # Opens an instance where cash_flow.csv can be edited
            myFile.write(str(cf))           # Writes all data from bs into cash_flow.csv
            print("Wrote to cash flow")

        with open(pathIC, "w") as myFile:   # Opens an instance where income_statement.csv can be edited
            myFile.write(str(inc))          # Writes all data from bs into income_statement.csv
            print("Wrote to income statement")

companyDocs1 = ReportExporter(ticker)       # Creates an object from the library
companyDocs1.store_data_file()              # Uses the store Data method within the class


# This code looks so clean
# Cleanest code ive ever writen