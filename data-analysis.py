import csv
import pandas as pd
import glob

path = 'hip_records/*.csv'  # Path to the folder containing CSV files
# Use glob to get all CSV files in the specified path
csv_files = glob.glob(path)
total_files = len(csv_files)
for file in csv_files:
    # Read each CSV file into a DataFrame
    df = pd.read_csv(file)
    # Perform data analysis on the DataFrame
    print(df['Vote Power']) 
    print("\n")  # Print a newline for better readability between files