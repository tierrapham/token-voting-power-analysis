import csv
import pandas as pd
import glob
import streamlit as st

def get_files():
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
    return hip_files

def load_selected_data (hip_files, hip_selection):
    df = pd.read_csv(hip_files[hip_selection]) # Reads the HIP file chosen by the user
    retun df