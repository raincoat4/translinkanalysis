import pandas as pd
from fuzzywuzzy import process

filtered=pd.read_csv('headsignFix.csv')
names=pd.read_csv('../names.csv')

# Function to perform fuzzy matching and find the best match
def find_best_match(row, choices):
    match = process.extractOne(row['Name'], choices)
    return match[0]

# Get unique values from df2
choices = filtered['trip_headsign'].unique()

# Apply fuzzy matching to find the best match for each row in df1
names['Best Match'] = names.apply(find_best_match, axis=1, args=(choices,))

# Merge the two dataframes on the best match column
merged = pd.merge(names, filtered, left_on='Best Match', right_on='trip_headsign')
merged.drop(columns=['Unnamed: 0.1'], inplace=True)
merged.drop(columns=['Unnamed: 0'], inplace=True)
merged.drop(columns=['Best Match'], inplace=True)

merged.to_csv('merged.csv')