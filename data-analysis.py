import csv
import pandas as pd
import glob
import streamlit as st

hip98 = 'hip_records/hip_98__mobile_subdao_quality_of_service_requirements_vote_breakdown.csv'
hip101 = 'hip_records/hip_101__equalizing_poc_rewards_across_wi-fi_and_cbrs_vote_breakdown.csv'
hip102 = 'hip_records/hip_102__helium_educational_lns_-_unrewarded_trial_network_vote_breakdown.csv'
hip103 = 'hip_records/hip_103__mobile_oracle_hex_boosting_vote_breakdown.csv'
hip104 = 'hip_records/hip_104__finetune_hip-17_parameters_to_tackle_density_vote_breakdown.csv'
hip105 = 'hip_records/hip_105__modification_of_mobile_subdao_hex_limits_vote_breakdown.csv'
hip106 = 'hip_records/hip_106__hotspot_bidirectional_coverage_requirement_vote_breakdown.csv'
hip107 = 'hip_records/hip_107__preventing_gaming_within_the_mobile_network_vote_breakdown.csv'
hip109 = 'hip_records/hip_109__hex_boosting_by_deployment_vote_breakdown.csv'
hip110 = 'hip_records/hip_110__proxy_voting_vote_breakdown.csv'
hip112 = 'hip_records/hip_112__scaling_iot_hotspot_assert_fees_vote_breakdown.csv'
hip113 = 'hip_records/hip_113__reward_cbrs_as_experimental_vote_breakdown.csv'
hip114 = 'hip_records/hip_114__incentive_escrow_fund_for_subscriber_referrals_vote_breakdown.csv'
hip116 = 'hip_records/hip_116__lorawan_device_address_price_adjustment_vote_breakdown.csv'
hip117 = 'hip_records/hip_117__add_mntd._as_a_hotspot_vendor_to_the_helium_mobile_subnetwork_vote_breakdown.csv'
hip118 = 'hip_records/hip_118__verification_mapping_for_mobile_network_vote_breakdown.csv'
hip119 = 'hip_records/hip_119__closing_gaming_loopholes_within_the_mobile_network_vote_breakdown.csv'
hip122 = 'hip_records/hip_122__amend_service_provider_hex_boosting_vote_breakdown.csv'
hip123 = 'hip_records/hip_123__redefining_iot_data-only_hotspot_onboarding_and_assertion_fees__vote_breakdown.csv'
hip124 = 'hip_records/hip_124__securing_iot_governance_through_staking_rewards_vote_breakdown.csv'
hip125 = 'hip_records/hip_125__temporary_anti-gaming_measures_for_boosted_hexes_vote_breakdown.csv'
hip129 = 'hip_records/hip_129__mobile_carrier_beta_vote_breakdown.csv'
hip130 = 'hip_records/hip_130__data-only_mobile_hotspots_vote_breakdown.csv'
hip131 = 'hip_records/hip_131__bridging_gap_between_verification_mappers_and_anti-gaming_measures_vote_breakdown.csv'
hip132 = 'hip_records/hip_132__scaling_mobile_mappers_vote_breakdown.csv'
hip133 = 'hip_records/hip_133__bridging_gap_for_anti-gaming_measures_phase_2_vote_breakdown.csv'
hip134 = 'hip_records/hip_134__reward_mobile_carrier_offload_hotspots_vote_breakdown.csv'
hip137 = 'hip_records/hip_137__remove_cn470_from_iot_poc_vote_breakdown.csv'
hip138 = 'hip_records/hip_138__return_to_hnt_vote_breakdown.csv'
hip139 = 'hip_records/hip_139__phase_out_cbrs_vote_breakdown.csv'
hip140 = 'hip_records/hip_140__adjust_service_provider_boost_qualifiers_vote_breakdown.csv'
hip141 = 'hip_records/hip_141__single-token_governance_and_helium_release_proposals_vote_breakdown.csv'
hip142 = 'hip_records/hip_142__add_inversion_capital_as_an_international_service_provider_to_the_helium_mobile_network_vote_breakdown (1).csv'
hip143 = 'hip_records/hip_143__decoupling_service_provider_pricing_from_governance_vote_breakdown.csv'
hip144 = 'hip_records/hip_144__mobile_hotspot_rewards_escrow_vote_breakdown.csv'
hip147 = 'hip_records/hip_147__mobile_data_eats_first_vote_breakdown.csv'
hip148 = 'hip_records/hip_148__reallocate_mobile_mapping_rewards_vote_breakdown.csv'
hip149 = 'hip_records/hip-149__helium_utility_and_emissions_realignment_vote_breakdown (1).csv'
hip150 = 'hip_records/hip-150__mobile_deployer_prioritization_vote_breakdown (1).csv'


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

hip_selection = st.selectbox("Select one:", ["HIP 98", "HIP 101", "HIP 102", "HIP 103", "HIP 104", "HIP 105", "HIP 106", "HIP 107", "HIP 109", "HIP 110", "HIP 112", "HIP 113", "HIP 114", "HIP 116", "HIP 117", "HIP 118", "HIP 119", "HIP 122", "HIP 123", "HIP 124", "HIP 125", "HIP 129", "HIP 130", "HIP 131", "HIP 132", "HIP 133", "HIP 134", "HIP 137", "HIP 138", "HIP 139", "HIP 140", "HIP 141", "HIP 142", "HIP 143", "HIP 144", "HIP 147", "HIP 148", "HIP 149", "HIP 150"])
top_n = st.number_input("Select the number N of top wallets to display:", 0, 100)