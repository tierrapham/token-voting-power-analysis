# Each row represents a voting record
# Column 1: Owner
# Coulmn 2: Choices
# Column 3: Vote Power
# Column 4: Percentage
# Column 5: Proxy Name
# Column 6: Voted Via

def top_n_voting_power (df, top_n):
    df["Vote Power"] = df["Vote Power"].str.replace(',', '') # Replaces the ',' characters in the 'Vote Power' data column with white space (removes them) to allow the data to be converted to numbers and evaluated

    df["Vote Power"] = pd.to_numeric(df["Vote Power"], errors="coerce") # Converts the data in the 'Vote Power' column into numeric values

    total_vote_power = df["Vote Power"].sum() # Sums the voting power of all owners/voting records
    top_n_df = df.nlargest(top_n, "Vote Power") # Sorts the data from largest to smallest by the 'Vote Power'
    top_n_vote_power = top_n_df["Vote Power"].sum() # Sums the voting power of the top N wallets (chosen by the user)

    top_percent = (top_n_vote_power/total_vote_power)*100 #Determines the total percentage of voting power that belongs to the top N wallets (there is also a 'Percentage' column that is very helpful in simply expressing the percentage of total voting power belonging to each voting record. However, after comparing the two methods (using the sum of the 'Percentage' column; and manually calculating the percentage by summing the top N wallets voting power, the total overall voting power, and dividing the two) it was observed that the two values were not always exact equivalents. It seems that the 'Percentage' column may be filled with pre-rounded decimals causing slight value differences. Therefore, to ensure the most accurate values and findings, the manual calculation method was chosen)

    return