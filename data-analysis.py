import csv
import pandas as pd
import glob
import streamlit as st

hip98 = 'hip_98__mobile_subdao_quality_of_service_requirements_vote_breakdown.csv'


# Each row represents a voting record
# Column 1: Owner
# Coulmn 2: Choices
# Column 3: Vote Power
# Column 4: Percentage
# Column 5: Proxy Name
# Column 6: Voted Via

st.title("Top N Wallet Voting Power Analyzer")
st.write("Welcome to the Top N Wallet Voting Power Analyzer.")
st.write("This application will analyze wallet-level voting data, rank wallets according to their voting power, and calculate the percentage of total voting power represented by the top N wallets.")

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
st.divider()

st.selectbox("Select one:", ["HIP 98", "HIP 101", "HIP 102", "HIP 103", "HIP 104", "HIP 105", "HIP 106", "HIP 107", "HIP 109", "HIP 110", "HIP 112", "HIP 113", "HIP 114", "HIP 116", "HIP 117", "HIP 118", "HIP 119", "HIP 122", "HIP 123", "HIP 124", "HIP 125", "HIP 129", "HIP 130", "HIP 131", "HIP 132", "HIP 133", "HIP 134", "HIP 137", "HIP 138", "HIP 139", "HIP 140", "HIP 141", "HIP 142", "HIP 143", "HIP 144", "HIP 147", "HIP 148", "HIP 149", "HIP 150"])