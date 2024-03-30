import pandas as pd
import re

# Example DataFrames
data1 = pd.read_csv('../names.csv')
data2 = pd.read_csv('sorted.csv')
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Create a regex pattern to match whole words
pattern = '|'.join(r'\b{}\b'.format(re.escape(name)) for name in df1['File Name'])

# Filter df2 based on whether 'trip_headsign' contains any of the values in df1['name']
filtered_df2 = df2[df2['trip_headsign'].str.contains(pattern)].reset_index(drop=True)
filtered_df2=filtered_df2.drop(columns=['Unnamed: 0'])
filtered_df2.to_csv('filteredSort.csv')
