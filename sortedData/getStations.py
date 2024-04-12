import os
import csv

def extract_second_row_values(folder_path, output_file):
    # List all CSV files in the folder
    csv_files = [file for file in os.listdir(folder_path) if file.endswith('.csv')]
    
    # Open the output file for writing
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        
        # Write header
        writer.writerow(['File Name', 'Second Row Values'])
        
        # Iterate over each CSV file
        for csv_file in csv_files:
            # Open the current CSV file
            with open(os.path.join(folder_path, csv_file), 'r') as file:
                reader = csv.reader(file)
                # Skip the first row (header)
                next(reader)
                # Read the second row
                second_row = next(reader)
                # Write the file name and second row values to the output file
                writer.writerow([csv_file.replace('-mf.csv', ''), ','.join(second_row)])


folder_path = '../transitcsvs'  # Specify the folder path containing CSV files
output_file = 'stations.csv'  # Specify the output file name

extract_second_row_values(folder_path, output_file)
