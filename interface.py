import streamlit as st

def display_intro_message():
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

def get_user_selection():
    st.subheader("Top N Wallets:") # A subheader for the Top N Wallets section
    hip_selection = st.selectbox("Select one:", ["HIP 98", "HIP 101", "HIP 102", "HIP 103", "HIP 104", "HIP 105", "HIP 106", "HIP 107", "HIP 109", "HIP 110", "HIP 112", "HIP 113", "HIP 114", "HIP 116", "HIP 117", "HIP 118", "HIP 119", "HIP 122", "HIP 123", "HIP 124", "HIP 125", "HIP 129", "HIP 130", "HIP 131", "HIP 132", "HIP 133", "HIP 134", "HIP 137", "HIP 138", "HIP 139", "HIP 140", "HIP 141", "HIP 142", "HIP 143", "HIP 144", "HIP 147", "HIP 148", "HIP 149", "HIP 150"]) # Creates a selection box for the user to select the proposal voting data they wish to analyze
    top_n = st.number_input("Select the number N of top wallets to display:", 1, 100) # Creates a number input feature to allow the user to determine the top N wallets for their chosen proposal they wish to analyze

    return hip_selection, top_n

def display_results(top_n, top_n_df, top_percent):
    st.dataframe(top_n_df) #Showcase a dataframe visualization of the top N wallets

    # Alters the verbage of the total percentage message depending on the number of top wallets chosen by the user
    st.subheader("Top N Voting Power Share:")
    if top_n == 1:
        st.write(f"{top_percent:.2f}% of total voting power belongs to the top wallet.")
    else:
        st.write(f"{top_percent:.2f}% of total voting power belongs to the top {top_n} wallets.")

    st.divider() # Divides sections on the website