a =1 
print(a)
import pandas as pd
import yfinance as yf

STOCK_TICKER = 'MSFT' # Example: Microsoft

try:
    ticker_obj = yf.Ticker(STOCK_TICKER)

    # --- Get Financial Statements ---
    income_statement_annual = ticker_obj.financials # Annual
    balance_sheet_annual = ticker_obj.balance_sheet
    cash_flow_annual = ticker_obj.cashflow

    

    # Save to CSV
    df = pd.DataFrame(income_statement_annual)
    df.to_csv('income_statement_annual.csv', index=False)
    # Save to CSV
    df = pd.DataFrame(balance_sheet_annual)
    df.to_csv('balance_sheet_annual.csv', index=False)
    # Save to CSV
    df = pd.DataFrame(cash_flow_annual)
    df.to_csv('cash_flow_annual.csv', index=False)

    # These are already pandas DataFrames
    print(f"\n--- {STOCK_TICKER} Annual Financial Statements Downloaded and Saved as csv---")
    

    # You can also get quarterly data
    # income_statement_quarterly = ticker_obj.quarterly_financials
    # print(f"\n--- {STOCK_TICKER} Quarterly Income Statement (from yfinance) ---")
    # print(income_statement_quarterly.head())

except Exception as e:
    print(f"An error occurred with yfinance: {e}")