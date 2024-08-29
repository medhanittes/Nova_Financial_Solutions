"""to calculate basic statistics"""
import pandas as pd
df = pd.read_csv('data/raw_analyst_ratings.csv')
column_lengths = df['headline'].str.len()
print(f"Minimum length: {column_lengths.min()}")
print(f"Maximum length: {column_lengths.max()}")
print(f"Mean length: {column_lengths.mean()}")
print(f"Median length: {column_lengths.median()}")
print(f"Standard deviation: {column_lengths.std()}")
"""to calculate number of articles per publisher"""
publisher_counts = df['publisher'].value_counts()
print(publisher_counts)
