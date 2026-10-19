import csv
import pandas as pd
import glob

path = 'hip_records/*.csv'  # Path to the folder containing CSV files
# Use glob to get all CSV files in the specified path
csv_files = glob.glob(path)
# print(csv_files)
total_files = len(csv_files)
# print(total_files)
data_files = []
for file in csv_files:
    # Read each CSV file and adds the information to a new list
    df = pd.read_csv(file)
    data_files.append(df)

# print(data_files)
# Concatenate all data into one DataFrame
big_frame = pd.concat (data_files, ignore_index=True)
print(big_frame)