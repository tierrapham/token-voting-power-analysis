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
#print(big_frame)

# Each row represents a voting record
# Column 1: Owner
# Coulmn 2: Choices
# Column 3: Vote Power
# Column 4: Percentage
# Column 5: Proxy Name
# Column 6: Voted Via

# Next: Determine if an owner appears more than once to determine whether each row in a data set represents one wallet

owners = big_frame["Owner"]
print(owners)

owner_check = []
repeat_owners = False
for owner in owners:
    if owner not in owner_check:
        owner_check.append(owner)
    else:
        repeat_owners = True
        break
if repeat_owners == True:
    print("There are repeat owners")
else:
    print("There arent repeat owners")