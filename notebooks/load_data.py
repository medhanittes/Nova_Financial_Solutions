import pandas as pd

# Load the CSV file
df1 = pd.read_csv('data/AAPL_historical_data.csv')
print(df1.columns)

df2 = pd.read_csv('data/AMZN_historical_data.csv')
print(df2.columns)

df3 = pd.read_csv('data/AMZN_historical_data.csv')
print(df3.columns)

df4 = pd.read_csv('data/GOOG_historical_data.csv')
print(df4.columns)

df5 = pd.read_csv('data/MSFT_historical_data.csv')
print(df5.columns)

df6 = pd.read_csv('data/NVDA_historical_data.csv')
print(df6.columns)

df7 = pd.read_csv('data/TSLA_historical_data.csv')
print(df7.columns)
