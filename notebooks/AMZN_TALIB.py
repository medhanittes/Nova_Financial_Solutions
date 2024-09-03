import pandas as pd
import talib

# Load the CSV file
df = pd.read_csv('data/AMZN_historical_data.csv')

# Remove rows with NaN values from all columns
df_cleaned = df.dropna()

# Save the cleaned data to a new CSV file
df_cleaned.to_csv('data/AMZN_historical_data_cleaned.csv', index=False)

# Load the cleaned data
df = pd.read_csv('data/AMZN_historical_data_cleaned.csv')

# Calculate a TA-Lib indicator Simple Moving Average
df['SMA'] = talib.SMA(df['Close'], timeperiod=200)  # 200 days

# Calculate a TA-Lib indicator Relative Strength Index
df['RSI'] = talib.RSI(df['Close'], timeperiod=200)  # 200 days

# Calculate MACD
df['MACD'], df['MACD_Signal'], df['MACD_Hist'] = talib.MACD(df['Close'], 
                                                               fastperiod=12, 
                                                               slowperiod=26, 
                                                               signalperiod=9)

# Remove rows with NaN values after calculations
df1 = df.dropna()

# Display the last few rows of the DataFrame
print(df1[['Close', 'SMA', 'RSI', 'MACD', 'MACD_Signal', 'MACD_Hist']])