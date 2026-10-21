import csv
import pandas as pd
import glob
import streamlit as st

# A dictionary to associate each HIP selection with the correct file pathway
hip_files = {"HIP 98": 'hip_records/hip_98__mobile_subdao_quality_of_service_requirements_vote_breakdown.csv',
             "HIP 101": 'hip_records/hip_101__equalizing_poc_rewards_across_wi-fi_and_cbrs_vote_breakdown.csv',
             "HIP 102": 'hip_records/hip_102__helium_educational_lns_-_unrewarded_trial_network_vote_breakdown.csv',
             "HIP 103": 'hip_records/hip_103__mobile_oracle_hex_boosting_vote_breakdown.csv',
             "HIP 104": 'hip_records/hip_104__finetune_hip-17_parameters_to_tackle_density_vote_breakdown.csv',
             "HIP 105": 'hip_records/hip_105__modification_of_mobile_subdao_hex_limits_vote_breakdown.csv',
             "HIP 106": 'hip_records/hip_106__hotspot_bidirectional_coverage_requirement_vote_breakdown.csv',
             "HIP 107": 'hip_records/hip_107__preventing_gaming_within_the_mobile_network_vote_breakdown.csv',
             "HIP 109": 'hip_records/hip_109__hex_boosting_by_deployment_vote_breakdown.csv',
             "HIP 110": 'hip_records/hip_110__proxy_voting_vote_breakdown.csv',
             "HIP 112": 'hip_records/hip_112__scaling_iot_hotspot_assert_fees_vote_breakdown.csv',
             "HIP 113": 'hip_records/hip_113__reward_cbrs_as_experimental_vote_breakdown.csv',
             "HIP 114": 'hip_records/hip_114__incentive_escrow_fund_for_subscriber_referrals_vote_breakdown.csv',
             "HIP 116": 'hip_records/hip_116__lorawan_device_address_price_adjustment_vote_breakdown.csv',
             "HIP 117": 'hip_records/hip_117__add_mntd._as_a_hotspot_vendor_to_the_helium_mobile_subnetwork_vote_breakdown.csv',
             "HIP 118": 'hip_records/hip_118__verification_mapping_for_mobile_network_vote_breakdown.csv',
             "HIP 119": 'hip_records/hip_119__closing_gaming_loopholes_within_the_mobile_network_vote_breakdown.csv',
             "HIP 122": 'hip_records/hip_122__amend_service_provider_hex_boosting_vote_breakdown.csv',
             "HIP 123": 'hip_records/hip_123__redefining_iot_data-only_hotspot_onboarding_and_assertion_fees__vote_breakdown.csv',
             "HIP 124": 'hip_records/hip_124__securing_iot_governance_through_staking_rewards_vote_breakdown.csv',
             "HIP 125": 'hip_records/hip_125__temporary_anti-gaming_measures_for_boosted_hexes_vote_breakdown.csv',
             "HIP 129": 'hip_records/hip_129__mobile_carrier_beta_vote_breakdown.csv',
             "HIP 130": 'hip_records/hip_130__data-only_mobile_hotspots_vote_breakdown.csv',
             "HIP 131": 'hip_records/hip_131__bridging_gap_between_verification_mappers_and_anti-gaming_measures_vote_breakdown.csv',
             "HIP 132": 'hip_records/hip_132__scaling_mobile_mappers_vote_breakdown.csv',
             "HIP 133": 'hip_records/hip_133__bridging_gap_for_anti-gaming_measures_phase_2_vote_breakdown.csv',
             "HIP 134": 'hip_records/hip_134__reward_mobile_carrier_offload_hotspots_vote_breakdown.csv',
             "HIP 137": 'hip_records/hip_137__remove_cn470_from_iot_poc_vote_breakdown.csv',
             "HIP 138": 'hip_records/hip_138__return_to_hnt_vote_breakdown.csv',
             "HIP 139": 'hip_records/hip_139__phase_out_cbrs_vote_breakdown.csv',
             "HIP 140": 'hip_records/hip_140__adjust_service_provider_boost_qualifiers_vote_breakdown.csv',
             "HIP 141": 'hip_records/hip_141__single-token_governance_and_helium_release_proposals_vote_breakdown.csv',
             "HIP 142": 'hip_records/hip_142__add_inversion_capital_as_an_international_service_provider_to_the_helium_mobile_network_vote_breakdown (1).csv',
             "HIP 143": 'hip_records/hip_143__decoupling_service_provider_pricing_from_governance_vote_breakdown.csv',
             "HIP 144": 'hip_records/hip_144__mobile_hotspot_rewards_escrow_vote_breakdown.csv',
             "HIP 147": 'hip_records/hip_147__mobile_data_eats_first_vote_breakdown.csv',
             "HIP 148": 'hip_records/hip_148__reallocate_mobile_mapping_rewards_vote_breakdown.csv',
             "HIP 149": 'hip_records/hip-149__helium_utility_and_emissions_realignment_vote_breakdown (1).csv',
             "HIP 150": 'hip_records/hip-150__mobile_deployer_prioritization_vote_breakdown (1).csv'
}

# Each row represents a voting record
# Column 1: Owner
# Coulmn 2: Choices
# Column 3: Vote Power
# Column 4: Percentage
# Column 5: Proxy Name
# Column 6: Voted Via

# Website title and introduction message
st.title("Top N Wallet Voting Power Analyzer")
st.write("Welcome to the Top N Wallet Voting Power Analyzer.")
st.write("This application will analyze wallet-level voting data, rank wallets according to their voting power, and calculate the percentage of total voting power represented by the top N wallets.")

# Describes the data included in each file to the user
st.header("About the Data:")
st.markdown("""
Each row represents **one voting record**
The columns are as follows:
- *owner* -- The wallet address or the account that cast the vote
- *choices* -- The voting option selected by the owner
- *vote power* -- The amount of voting power the owner's vote holds
- *percentage* -- The percentage of total voting power represented by the owner's vote
- *proxy name* -- The name of the proxy
- *voted via* -- The method by which the owner cast the vote
""")
st.divider() # Divides sections on the website


st.subheader("Top N Wallets:") # A subheader for the Top N Wallets section
hip_selection = st.selectbox("Select one:", ["HIP 98", "HIP 101", "HIP 102", "HIP 103", "HIP 104", "HIP 105", "HIP 106", "HIP 107", "HIP 109", "HIP 110", "HIP 112", "HIP 113", "HIP 114", "HIP 116", "HIP 117", "HIP 118", "HIP 119", "HIP 122", "HIP 123", "HIP 124", "HIP 125", "HIP 129", "HIP 130", "HIP 131", "HIP 132", "HIP 133", "HIP 134", "HIP 137", "HIP 138", "HIP 139", "HIP 140", "HIP 141", "HIP 142", "HIP 143", "HIP 144", "HIP 147", "HIP 148", "HIP 149", "HIP 150"]) # Creates a selection box for the user to select the proposal voting data they wish to analyze
top_n = st.number_input("Select the number N of top wallets to display:", 1, 100) # Creates a number input feature to allow the user to determine the top N wallets for their chosen proposal they wish to analyze

df = pd.read_csv(hip_files[hip_selection]) # Reads the HIP file chosen by the user
df["Vote Power"] = df["Vote Power"].str.replace(',', '') # Replaces the ',' characters in the 'Vote Power' data column with white space (removes them) to allow the data to be converted to numbers and evaluated
df["Vote Power"] = pd.to_numeric(df["Vote Power"], errors="coerce") # Converts the data in the 'Vote Power' column into numeric values

total_vote_power = df["Vote Power"].sum() # Sums the voting power of all owners/voting records
top_n_df = df.nlargest(top_n, "Vote Power") # Sorts the data from largest to smallest by the 'Vote Power'
top_n_vote_power = top_n_df["Vote Power"].sum() # Sums the voting power of the top N wallets (chosen by the user)

top_percent = (top_n_vote_power/total_vote_power)*100 #Determines the total percentage of voting power that belongs to the top N wallets (there is also a 'Percentage' column that is very helpful in simply expressing the percentage of total voting power belonging to each voting record. However, after comparing the two methods (using the sum of the 'Percentage' column; and manually calculating the percentage by summing the top N wallets voting power, the total overall voting power, and dividing the two) it was observed that the two values were not always exact equivalents. It seems that the 'Percentage' column may be filled with pre-rounded decimals causing slight value differences. Therefore, to ensure the most accurate values and findings, the manual calculation method was chosen)

st.dataframe(top_n_df) #Showcase a dataframe visualization of the top N wallets

# Alters the verbage of the total percentage message depending on the number of top wallets chosen by the user
st.subheader("Top N Voting Power Share:")
if top_n == 1:
    st.write(f"{top_percent:.2f}% of total voting power belongs to the top wallet.")
else:
    st.write(f"{top_percent:.2f}% of total voting power belongs to the top {top_n} wallets.")

# Not necessarily a part of the project but this is used to determine if there are duplicate owners within data sets
st.subheader("Duplicate Owner Check:") 
duplicates = df.duplicated(subset=["Owner"]) # Checks the 'Owner' column for duplicate values and returns booleans, False if it is the first occurence of the owner and True if it has appeared in an earlier row

duplicates = duplicates.replace(False, 'No') # Replaces the boolean values with strings, as it appears that booleans cannot print to/do not appear on the website

st.dataframe(duplicates) #Creates a visualization to allow for easier review of the duplicate analysis information