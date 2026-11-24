from hip_data import *
from analysis import *
from interface import *

display_intro_message()
hip_files = get_files()
hip_selection, top_n = get_user_selection()
df = load_selected_data(hip_files, hip_selection)
df, top_n_df, top_percent = top_n_voting_power (df, top_n)
display_results(top_n, top_n_df, top_percent)


# # Not necessarily a part of the project but this is used to determine if there are duplicate owners within data sets
# st.subheader("Duplicate Owner Check:") 
# duplicates = df.duplicated(subset=["Owner"]) # Checks the 'Owner' column for duplicate values and returns booleans, False if it is the first occurence of the owner and True if it has appeared in an earlier row

# duplicates = duplicates.replace(False, 'No') # Replaces the boolean values with strings, as it appears that booleans cannot print to/do not appear on the website

# st.dataframe(duplicates) #Creates a visualization to allow for easier review of the duplicate analysis information