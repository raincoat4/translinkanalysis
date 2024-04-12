import pandas as pd

# Example DataFrame

df = pd.read_csv('merged.csv')
df1=pd.read_csv('stops.txt')
# Get unique values in the 'Name' column
unique_names = df['Name'].unique()

# Iterate over unique names
for name in unique_names:
    # Filter the DataFrame for the current name
    
    # Append Stop Code
    filtered_df=pd.merge(df, df1[['stop_id', 'stop_code']], on='stop_id', how='left')
    filtered_df['stop_code'] = filtered_df['stop_code'].astype(int)
    
    # Save the filtered DataFrame to a CSV file
    filtered_df = filtered_df[filtered_df['Name'] == name]
    output_file = 'busSchedule/'+f'{name}.csv'
    filtered_df.to_csv(output_file, index=False)
