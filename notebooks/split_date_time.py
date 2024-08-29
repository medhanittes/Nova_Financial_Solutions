import pandas as pd

# Read the CSV file
df = pd.read_csv('data/raw_analyst_ratings.csv')

# Print the columns of the DataFrame
print(df.columns)

# Convert 'date' column to datetime 

df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Separate valid and invalid dates
valid_dates = df[df['date'].notna()].copy()
invalid_dates = df[df['date'].isna()].copy()

if not invalid_dates.empty:
    print("Some dates could not be converted:")
    print(invalid_dates[['headline', 'date']])

# Process valid dates
valid_dates['time'] = valid_dates['date'].dt.time
valid_dates['date_only'] = valid_dates['date'].dt.date

# Save valid and invalid dates to separate CSV files
valid_dates.to_csv('data/valid_dates.csv', index=False)
invalid_dates['original_date'] = df['date'].where(df['date'].isna())
invalid_dates.to_csv('data/invalid_dates.csv', index=False)
