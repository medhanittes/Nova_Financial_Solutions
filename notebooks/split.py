import pandas as pd 

df = pd.read_csv('data/raw_analyst_ratings.csv')

df['date'] = pd.to_datetime(df['date']) 
df['day_of_week'] = df['date'].dt.day_name() 
day_of_week_counts = df['day_of_week'].value_counts() 
total_publications = len(df) 
day_of_week_percentages = (day_of_week_counts / total_publications) * 100 
print("Day of the Week Counts:") 
print(day_of_week_counts) 
print("\nDay of the Week Percentages:") 
print(day_of_week_percentages)
