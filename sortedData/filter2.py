import pandas as pd
import re
def removeUntilTo(input):
    pattern = r'^(.*?)\bTo\b'
    number = r'^(.*\d)'
    # Search for the pattern in the input string
    match = re.search(pattern, input)
    num=re.search(number, input)
    if match:
        # Replace the matched substring with an empty string
        cutString = num.group(0)+input.replace(match.group(0),  '').strip()
        return cutString
    else:
        # Return the original string if no match found
        return input


df=pd.read_csv('filteredSort.csv')
df['trip_headsign']=df['trip_headsign'].apply(removeUntilTo)
print(df)
df.to_csv('headsignFix.csv')