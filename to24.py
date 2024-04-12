import pandas as pd
import os
import sys

# Function to reset global variables
def reset_globals():
    global pivot, pivotTwice, lock, passed7, passed24
    pivot = False
    pivotTwice = 0
    lock = False
    passed7 = False
    passed24 = False

# Function to convert 12-hour time to 24-hour time
def convert_to_24_hour(time_str):
    global pivot, passed7, lock, passed24, pivotTwice
    if isinstance(time_str, float):
        return time_str  # Return the original value if it's not a string
    if '-' in time_str:
        return time_str
    if '#' in time_str:
        time_str = time_str.replace("#", "")
    if '*' in time_str:
        time_str = time_str.replace("*", "")
    if '+' in time_str: 
        time_str = time_str.replace("+", "")# Return the original value if it contains special characters
    if ':' in time_str:
        hour, minute = map(int, time_str.split(':'))
    else:
        hour, minute = map(int, time_str.split('.'))
    if hour == 12:
        if not lock:
            pivot = not pivot
            lock = not lock
            pivotTwice += 1
            if pivotTwice == 2:
                passed24 = True
    if hour == 7 and lock:
        passed7 = True
        lock = not lock
    if pivot and hour != 12:
        return f'{hour+12:02d}:{minute:02d}'
    if passed24 and hour == 12:
        return f'{hour-12:02d}:{minute:02d}'
    return f'{hour:02d}:{minute:02d}'

# Iterate through each CSV file in the "transitcsvs" folder
for filename in os.listdir("transitcsvs"):
    if filename.endswith(".csv"):
        input_file = os.path.join("transitcsvs", filename)
        output_file = os.path.join("hr24", f"{filename}_converted.csv")
        try:
            # Read the CSV file
            df = pd.read_csv(input_file, header=1)

            # Reset global variables before processing each file
            reset_globals()

            # Apply the conversion function to each column
            for column in df.columns:
                reset_globals()
                df[column] = df[column].apply(convert_to_24_hour)

            # Write the output to a new CSV file in the "hr24" folder
            df.to_csv(output_file, index=False)
            print(f"Processed {filename} and saved as {output_file}")

        except pd.errors.ParserError as e:
            print(f"Error processing {filename}: {e}")

print("All files processed.")
