# The content of this file was generated using the Python profile of libCellML 0.6.3.

from enum import Enum
from math import *


__version__ = "0.6.0"
LIBCELLML_VERSION = "0.6.3"

STATE_COUNT = 15
CONSTANT_COUNT = 55
COMPUTED_CONSTANT_COUNT = 4
ALGEBRAIC_VARIABLE_COUNT = 34

VOI_INFO = {"name": "time", "units": "second", "component": "environment"}

STATE_INFO = [
    {"name": "Gs_alpha_GTP", "units": "uM", "component": "caveolar_G_s_protein_activation_module"},
    {"name": "Gs_beta_gamma", "units": "uM", "component": "caveolar_G_s_protein_activation_module"},
    {"name": "Gs_alpha_GDP", "units": "uM", "component": "caveolar_G_s_protein_activation_module"},
    {"name": "Gi_alpha_GTP", "units": "uM", "component": "caveolar_G_i_protein_activation_module"},
    {"name": "Gi_beta_gamma", "units": "uM", "component": "caveolar_G_i_protein_activation_module"},
    {"name": "Gi_alpha_GDP", "units": "uM", "component": "caveolar_G_i_protein_activation_module"},
    {"name": "Gs_alpha_GTP", "units": "uM", "component": "extracaveolar_G_s_protein_activation_module"},
    {"name": "Gs_beta_gamma", "units": "uM", "component": "extracaveolar_G_s_protein_activation_module"},
    {"name": "Gs_alpha_GDP", "units": "uM", "component": "extracaveolar_G_s_protein_activation_module"},
    {"name": "Gi_alpha_GTP", "units": "uM", "component": "extracaveolar_G_i_protein_activation_module"},
    {"name": "Gi_beta_gamma", "units": "uM", "component": "extracaveolar_G_i_protein_activation_module"},
    {"name": "Gi_alpha_GDP", "units": "uM", "component": "extracaveolar_G_i_protein_activation_module"},
    {"name": "cAMP_cav", "units": "uM", "component": "cAMP_flux_module"},
    {"name": "cAMP_ecav", "units": "uM", "component": "cAMP_flux_module"},
    {"name": "cAMP_cyt", "units": "uM", "component": "cAMP_flux_module"}
]

CONSTANT_INFO = [
    {"name": "K_H", "units": "uM", "component": "beta_1_adrenergic_parameters"},
    {"name": "K_L", "units": "uM", "component": "beta_1_adrenergic_parameters"},
    {"name": "K_C", "units": "uM", "component": "beta_1_adrenergic_parameters"},
    {"name": "K_H", "units": "uM", "component": "muscarinic_parameters"},
    {"name": "K_L", "units": "uM", "component": "muscarinic_parameters"},
    {"name": "K_C", "units": "uM", "component": "muscarinic_parameters"},
    {"name": "k_PDE2", "units": "per_sec", "component": "PDE_parameters"},
    {"name": "Km_PDE2", "units": "uM", "component": "PDE_parameters"},
    {"name": "k_PDE3", "units": "per_sec", "component": "PDE_parameters"},
    {"name": "Km_PDE3", "units": "uM", "component": "PDE_parameters"},
    {"name": "k_PDE4", "units": "per_sec", "component": "PDE_parameters"},
    {"name": "Km_PDE4", "units": "uM", "component": "PDE_parameters"},
    {"name": "k_act1", "units": "per_sec", "component": "G_s_parameters"},
    {"name": "k_act2", "units": "per_sec", "component": "G_s_parameters"},
    {"name": "k_hydr", "units": "per_sec", "component": "G_s_parameters"},
    {"name": "k_reas", "units": "per_uM_per_sec", "component": "G_s_parameters"},
    {"name": "k_act1", "units": "per_sec", "component": "G_i_parameters"},
    {"name": "k_act2", "units": "per_sec", "component": "G_i_parameters"},
    {"name": "k_hydr", "units": "per_sec", "component": "G_i_parameters"},
    {"name": "k_reas", "units": "per_uM_per_sec", "component": "G_i_parameters"},
    {"name": "R_Total", "units": "uM", "component": "caveolar_beta_1_adrenergic_receptor_module"},
    {"name": "R_Total", "units": "uM", "component": "caveolar_muscarinic_receptor_module"},
    {"name": "Gs_Total", "units": "uM", "component": "caveolar_G_s_protein_activation_module"},
    {"name": "Gi_Total", "units": "uM", "component": "caveolar_G_i_protein_activation_module"},
    {"name": "R_Total", "units": "uM", "component": "extracaveolar_beta_1_adrenergic_receptor_module"},
    {"name": "R_Total", "units": "uM", "component": "extracaveolar_muscarinic_receptor_module"},
    {"name": "Gs_Total", "units": "uM", "component": "extracaveolar_G_s_protein_activation_module"},
    {"name": "Gi_Total", "units": "uM", "component": "extracaveolar_G_i_protein_activation_module"},
    {"name": "MW_AC56", "units": "kDa", "component": "AC56_module"},
    {"name": "ATP", "units": "uM", "component": "AC56_module"},
    {"name": "Km_ATP", "units": "uM", "component": "AC56_module"},
    {"name": "AF56", "units": "dimensionless", "component": "AC56_module"},
    {"name": "AC_56", "units": "uM", "component": "AC56_module"},
    {"name": "MW_AC47", "units": "kDa", "component": "AC47_ecav_module"},
    {"name": "ATP", "units": "uM", "component": "AC47_ecav_module"},
    {"name": "Km_ATP", "units": "uM", "component": "AC47_ecav_module"},
    {"name": "AF47", "units": "dimensionless", "component": "AC47_ecav_module"},
    {"name": "AC_47_ecav", "units": "uM", "component": "AC47_ecav_module"},
    {"name": "ATP", "units": "uM", "component": "AC47_cyt_module"},
    {"name": "Km_ATP", "units": "uM", "component": "AC47_cyt_module"},
    {"name": "AF47", "units": "dimensionless", "component": "AC47_cyt_module"},
    {"name": "AC_47_cyt", "units": "uM", "component": "AC47_cyt_module"},
    {"name": "k_AC47_cyt", "units": "per_sec", "component": "AC47_cyt_module"},
    {"name": "PDE2", "units": "uM", "component": "caveolar_PDE_module"},
    {"name": "PDE3", "units": "uM", "component": "caveolar_PDE_module"},
    {"name": "PDE4", "units": "uM", "component": "caveolar_PDE_module"},
    {"name": "PDE2", "units": "uM", "component": "extracaveolar_PDE_module"},
    {"name": "PDE4", "units": "uM", "component": "extracaveolar_PDE_module"},
    {"name": "PDE2", "units": "uM", "component": "bulk_cytoplasmic_PDE_module"},
    {"name": "PDE3", "units": "uM", "component": "bulk_cytoplasmic_PDE_module"},
    {"name": "PDE4", "units": "uM", "component": "bulk_cytoplasmic_PDE_module"},
    {"name": "V_cell", "units": "litre", "component": "cAMP_flux_module"},
    {"name": "J_cav_cyt", "units": "liters_per_second", "component": "cAMP_flux_module"},
    {"name": "J_cav_ecav", "units": "liters_per_second", "component": "cAMP_flux_module"},
    {"name": "J_ecav_cyt", "units": "liters_per_second", "component": "cAMP_flux_module"}
]

COMPUTED_CONSTANT_INFO = [
    {"name": "dcAMP_AC_47_cyt_dt", "units": "uM_per_sec", "component": "AC47_cyt_module"},
    {"name": "V_cav", "units": "litre", "component": "cAMP_flux_module"},
    {"name": "V_ecav", "units": "litre", "component": "cAMP_flux_module"},
    {"name": "V_cyt", "units": "litre", "component": "cAMP_flux_module"}
]

ALGEBRAIC_INFO = [
    {"name": "L_iso", "units": "uM", "component": "beta_1_adrenergic_parameters"},
    {"name": "L_ach", "units": "uM", "component": "muscarinic_parameters"},
    {"name": "RG", "units": "uM", "component": "caveolar_beta_1_adrenergic_receptor_module"},
    {"name": "LRG", "units": "uM", "component": "caveolar_beta_1_adrenergic_receptor_module"},
    {"name": "LR", "units": "uM", "component": "caveolar_beta_1_adrenergic_receptor_module"},
    {"name": "R", "units": "uM", "component": "caveolar_beta_1_adrenergic_receptor_module"},
    {"name": "G", "units": "uM", "component": "caveolar_beta_1_adrenergic_receptor_module"},
    {"name": "RG", "units": "uM", "component": "caveolar_muscarinic_receptor_module"},
    {"name": "LRG", "units": "uM", "component": "caveolar_muscarinic_receptor_module"},
    {"name": "LR", "units": "uM", "component": "caveolar_muscarinic_receptor_module"},
    {"name": "R", "units": "uM", "component": "caveolar_muscarinic_receptor_module"},
    {"name": "G", "units": "uM", "component": "caveolar_muscarinic_receptor_module"},
    {"name": "RG", "units": "uM", "component": "extracaveolar_beta_1_adrenergic_receptor_module"},
    {"name": "LRG", "units": "uM", "component": "extracaveolar_beta_1_adrenergic_receptor_module"},
    {"name": "LR", "units": "uM", "component": "extracaveolar_beta_1_adrenergic_receptor_module"},
    {"name": "R", "units": "uM", "component": "extracaveolar_beta_1_adrenergic_receptor_module"},
    {"name": "G", "units": "uM", "component": "extracaveolar_beta_1_adrenergic_receptor_module"},
    {"name": "RG", "units": "uM", "component": "extracaveolar_muscarinic_receptor_module"},
    {"name": "LRG", "units": "uM", "component": "extracaveolar_muscarinic_receptor_module"},
    {"name": "LR", "units": "uM", "component": "extracaveolar_muscarinic_receptor_module"},
    {"name": "R", "units": "uM", "component": "extracaveolar_muscarinic_receptor_module"},
    {"name": "G", "units": "uM", "component": "extracaveolar_muscarinic_receptor_module"},
    {"name": "k_AC56", "units": "per_sec", "component": "AC56_module"},
    {"name": "dcAMP_AC_56_dt", "units": "uM_per_sec", "component": "AC56_module"},
    {"name": "k_AC47_ecav", "units": "per_sec", "component": "AC47_ecav_module"},
    {"name": "dcAMP_AC_47_ecav_dt", "units": "uM_per_sec", "component": "AC47_ecav_module"},
    {"name": "dcAMP_cav_PDE2_dt", "units": "uM_per_sec", "component": "caveolar_PDE_module"},
    {"name": "dcAMP_cav_PDE3_dt", "units": "uM_per_sec", "component": "caveolar_PDE_module"},
    {"name": "dcAMP_cav_PDE4_dt", "units": "uM_per_sec", "component": "caveolar_PDE_module"},
    {"name": "dcAMP_ecav_PDE2_dt", "units": "uM_per_sec", "component": "extracaveolar_PDE_module"},
    {"name": "dcAMP_ecav_PDE4_dt", "units": "uM_per_sec", "component": "extracaveolar_PDE_module"},
    {"name": "dcAMP_cyt_PDE2_dt", "units": "uM_per_sec", "component": "bulk_cytoplasmic_PDE_module"},
    {"name": "dcAMP_cyt_PDE3_dt", "units": "uM_per_sec", "component": "bulk_cytoplasmic_PDE_module"},
    {"name": "dcAMP_cyt_PDE4_dt", "units": "uM_per_sec", "component": "bulk_cytoplasmic_PDE_module"}
]


def leq_func(x, y):
    return 1.0 if x <= y else 0.0


def gt_func(x, y):
    return 1.0 if x > y else 0.0


def and_func(x, y):
    return 1.0 if bool(x) & bool(y) else 0.0


def create_states_array():
    return [nan]*STATE_COUNT


def create_constants_array():
    return [nan]*CONSTANT_COUNT


def create_computed_constants_array():
    return [nan]*COMPUTED_CONSTANT_COUNT


def create_algebraic_variables_array():
    return [nan]*ALGEBRAIC_VARIABLE_COUNT


def initialise_arrays(states, rates, constants, computed_constants, algebraic_variables):
    states[0] = 0.041983438
    states[1] = 0.042634499
    states[2] = 0.000651061
    states[3] = 0.012644961
    states[4] = 0.013274751
    states[5] = 0.00062979
    states[6] = 0.083866891
    states[7] = 0.084522918
    states[8] = 0.000656025
    states[9] = 0.001018705
    states[10] = 0.001475253
    states[11] = 0.000456548
    states[12] = 0.11750433
    states[13] = 1.092200547
    states[14] = 0.992583576
    constants[0] = 0.035
    constants[1] = 0.386
    constants[2] = 8.809
    constants[3] = 0.16
    constants[4] = 11.0
    constants[5] = 30.0
    constants[6] = 20.0
    constants[7] = 50.0
    constants[8] = 1.25
    constants[9] = 0.08
    constants[10] = 2.5
    constants[11] = 2.2
    constants[12] = 5.0
    constants[13] = 0.1
    constants[14] = 0.8
    constants[15] = 1.21e3
    constants[16] = 2.5
    constants[17] = 0.05
    constants[18] = 0.8
    constants[19] = 1.21e3
    constants[20] = 0.633
    constants[21] = 0.633
    constants[22] = 10.0
    constants[23] = 20.0
    constants[24] = 0.633
    constants[25] = 0.633
    constants[26] = 10.0
    constants[27] = 1.0
    constants[28] = 130.0
    constants[29] = 5000.0
    constants[30] = 315.0
    constants[31] = 500.0
    constants[32] = 3.379
    constants[33] = 130.0
    constants[34] = 5000.0
    constants[35] = 315.0
    constants[36] = 130.0
    constants[37] = 0.2
    constants[38] = 5000.0
    constants[39] = 315.0
    constants[40] = 130.0
    constants[41] = 0.136
    constants[42] = 1.08e-3
    constants[43] = 4.5
    constants[44] = 5.6
    constants[45] = 2.0
    constants[46] = 0.02
    constants[47] = 0.16
    constants[48] = 5.0e-3
    constants[49] = 7.5e-3
    constants[50] = 5.0e-3
    constants[51] = 38.0e-12
    constants[52] = 7.5e-14
    constants[53] = 7.5e-15
    constants[54] = 1.5e-17


def compute_computed_constants(states, rates, constants, computed_constants, algebraic):
    computed_constants[0] = constants[42]*constants[41]*constants[40]*constants[38]/(constants[39]+constants[38])
    computed_constants[1] = 0.01*constants[51]
    computed_constants[2] = 0.02*constants[51]
    computed_constants[3] = 0.5*constants[51]


def compute_rates(voi, states, rates, constants, computed_constants, algebraic_variables):
    algebraicVariables[0] = 1.0 if and_func(gt_func(voi, 120.0), leq_func(voi, 720.0)) else 1.0
    algebraicVariables[6] = constants[22]-states[0]-states[2]
    algebraicVariables[5] = constants[1]*constants[0]*constants[2]*pow(constants[1]*constants[0]*constants[2]-(constants[0]*(-constants[2]*algebraicVariables[0]-constants[1]*(constants[22]+-states[0]-states[2]))-pow(constants[1], 2.0)*algebraicVariables[0]*(constants[22]+-states[0]-states[2])), -1.0)*constants[20]
    algebraicVariables[3] = algebraicVariables[0]*algebraicVariables[5]*algebraicVariables[6]/(constants[0]*constants[2]/constants[1])
    algebraicVariables[2] = algebraicVariables[5]*algebraicVariables[6]/constants[2]
    rates[0] = algebraicVariables[2]*constants[13]+algebraicVariables[3]*constants[12]-states[0]*constants[14]
    rates[1] = algebraicVariables[2]*constants[13]+algebraicVariables[3]*constants[12]-states[2]*states[1]*constants[15]
    rates[2] = states[0]*constants[14]-states[2]*states[1]*constants[15]
    algebraicVariables[1] = 0.0 if and_func(gt_func(voi, 240.0), leq_func(voi, 540.0)) else 0.0
    algebraicVariables[11] = constants[23]-states[3]-states[5]
    algebraicVariables[10] = constants[3]*constants[4]*constants[5]*pow(constants[3]*constants[4]*constants[5]-(constants[4]*(-constants[3]*(constants[23]+-states[3]-states[5])-constants[4]*algebraicVariables[1]*(constants[23]+-states[3]-states[5]))-constants[3]*constants[5]*algebraicVariables[1]), -1.0)*constants[21]
    algebraicVariables[8] = algebraicVariables[1]*algebraicVariables[10]*algebraicVariables[11]/(constants[3]*constants[5]/constants[4])
    algebraicVariables[7] = algebraicVariables[10]*algebraicVariables[11]/constants[5]
    rates[3] = algebraicVariables[7]*constants[17]+algebraicVariables[8]*constants[16]-states[3]*constants[18]
    rates[4] = algebraicVariables[7]*constants[17]+algebraicVariables[8]*constants[16]-states[5]*states[4]*constants[19]
    rates[5] = states[3]*constants[18]-states[5]*states[4]*constants[19]
    algebraicVariables[16] = constants[26]-states[6]-states[8]
    algebraicVariables[15] = constants[1]*constants[0]*constants[2]*pow(constants[1]*constants[0]*constants[2]-(constants[0]*(-constants[2]*algebraicVariables[0]-constants[1]*(constants[26]+-states[8]-states[6]))-pow(constants[1], 2.0)*algebraicVariables[0]*(constants[26]+-states[8]-states[6])), -1.0)*constants[24]
    algebraicVariables[13] = algebraicVariables[0]*algebraicVariables[15]*algebraicVariables[16]/(constants[0]*constants[2]/constants[1])
    algebraicVariables[12] = algebraicVariables[15]*algebraicVariables[16]/constants[2]
    rates[6] = algebraicVariables[12]*constants[13]+algebraicVariables[13]*constants[12]-states[6]*constants[14]
    rates[7] = algebraicVariables[12]*constants[13]+algebraicVariables[13]*constants[12]-states[8]*states[7]*constants[15]
    rates[8] = states[6]*constants[14]-states[8]*states[7]*constants[15]
    algebraicVariables[21] = constants[27]-states[9]-states[11]
    algebraicVariables[20] = constants[3]*constants[4]*constants[5]*pow(constants[3]*constants[4]*constants[5]-(-constants[3]*constants[5]*algebraicVariables[1]+-pow(constants[4], 2.0)*algebraicVariables[1]*(-states[9]+constants[27]-states[11])-constants[3]*constants[4]*(-states[9]+constants[27]-states[11])), -1.0)*constants[25]
    algebraicVariables[18] = algebraicVariables[1]*algebraicVariables[20]*algebraicVariables[21]/(constants[3]*constants[5]/constants[4])
    algebraicVariables[17] = algebraicVariables[20]*algebraicVariables[21]/constants[5]
    rates[9] = algebraicVariables[17]*constants[17]+algebraicVariables[18]*constants[16]-states[9]*constants[18]
    rates[10] = algebraicVariables[17]*constants[17]+algebraicVariables[18]*constants[16]-states[11]*states[10]*constants[19]
    rates[11] = states[9]*constants[18]-states[11]*states[10]*constants[19]
    algebraicVariables[22] = (0.7+3.8234*pow(states[0]/1.0, 0.9787)/(0.1986+pow(states[0]/1.0, 0.9787)))*(1.0+1.0/1.4432*-1.0061*pow(states[3]/1.0, 0.8356)/(0.1918+pow(states[3]/1.0, 0.8356)))*constants[28]/60.0*0.001
    algebraicVariables[23] = algebraicVariables[22]*constants[32]*constants[31]*constants[29]/(constants[30]+constants[29])
    algebraicVariables[26] = constants[6]*constants[43]*states[12]/(constants[7]+states[12])
    algebraicVariables[27] = constants[8]*constants[44]*states[12]/(constants[9]+states[12])
    algebraicVariables[28] = constants[10]*constants[45]*states[12]/(constants[11]+states[12])
    rates[12] = algebraicVariables[23]-(algebraicVariables[26]+algebraicVariables[27]+algebraicVariables[28])-constants[53]*(states[12]-states[13])/computed_constants[1]-constants[52]*(states[12]-states[14])/computed_constants[1]
    algebraicVariables[24] = (0.063+2.01*pow(states[6]*1000.0, 1.0043)/(31.544+pow(states[6]*1000.0, 1.0043)))*(1.0+1.0/3.01*49.1*pow(states[10]*1000.0, 0.8921)/(25.44+pow(states[10]*1000.0, 0.8921)))*constants[33]/60.0*0.001
    algebraicVariables[25] = algebraicVariables[24]*constants[37]*constants[36]*constants[34]/(constants[35]+constants[34])
    algebraicVariables[29] = constants[6]*constants[46]*states[13]/(constants[7]+states[13])
    algebraicVariables[30] = constants[10]*constants[47]*states[13]/(constants[11]+states[13])
    rates[13] = algebraicVariables[25]-(algebraicVariables[29]+algebraicVariables[30])+constants[53]*(states[12]-states[13])/computed_constants[2]-constants[54]*(states[13]-states[14])/computed_constants[2]
    algebraicVariables[31] = constants[6]*constants[48]*states[14]/(constants[7]+states[14])
    algebraicVariables[32] = constants[8]*constants[49]*states[14]/(constants[9]+states[14])
    algebraicVariables[33] = constants[10]*constants[50]*states[14]/(constants[11]+states[14])
    rates[14] = computed_constants[0]-(algebraicVariables[31]+algebraicVariables[32]+algebraicVariables[33])+constants[52]*(states[12]-states[14])/computed_constants[3]+constants[54]*(states[13]-states[14])/computed_constants[3]


def compute_variables(voi, states, rates, constants, computed_constants, algebraic_variables):
    algebraicVariables[5] = constants[1]*constants[0]*constants[2]*pow(constants[1]*constants[0]*constants[2]-(constants[0]*(-constants[2]*algebraicVariables[0]-constants[1]*(constants[22]+-states[0]-states[2]))-pow(constants[1], 2.0)*algebraicVariables[0]*(constants[22]+-states[0]-states[2])), -1.0)*constants[20]
    algebraicVariables[4] = algebraicVariables[0]*algebraicVariables[5]/constants[1]
    algebraicVariables[6] = constants[22]-states[0]-states[2]
    algebraicVariables[3] = algebraicVariables[0]*algebraicVariables[5]*algebraicVariables[6]/(constants[0]*constants[2]/constants[1])
    algebraicVariables[2] = algebraicVariables[5]*algebraicVariables[6]/constants[2]
    algebraicVariables[10] = constants[3]*constants[4]*constants[5]*pow(constants[3]*constants[4]*constants[5]-(constants[4]*(-constants[3]*(constants[23]+-states[3]-states[5])-constants[4]*algebraicVariables[1]*(constants[23]+-states[3]-states[5]))-constants[3]*constants[5]*algebraicVariables[1]), -1.0)*constants[21]
    algebraicVariables[9] = algebraicVariables[1]*algebraicVariables[10]/constants[4]
    algebraicVariables[11] = constants[23]-states[3]-states[5]
    algebraicVariables[8] = algebraicVariables[1]*algebraicVariables[10]*algebraicVariables[11]/(constants[3]*constants[5]/constants[4])
    algebraicVariables[7] = algebraicVariables[10]*algebraicVariables[11]/constants[5]
    algebraicVariables[15] = constants[1]*constants[0]*constants[2]*pow(constants[1]*constants[0]*constants[2]-(constants[0]*(-constants[2]*algebraicVariables[0]-constants[1]*(constants[26]+-states[8]-states[6]))-pow(constants[1], 2.0)*algebraicVariables[0]*(constants[26]+-states[8]-states[6])), -1.0)*constants[24]
    algebraicVariables[14] = algebraicVariables[0]*algebraicVariables[15]/constants[1]
    algebraicVariables[16] = constants[26]-states[6]-states[8]
    algebraicVariables[13] = algebraicVariables[0]*algebraicVariables[15]*algebraicVariables[16]/(constants[0]*constants[2]/constants[1])
    algebraicVariables[12] = algebraicVariables[15]*algebraicVariables[16]/constants[2]
    algebraicVariables[20] = constants[3]*constants[4]*constants[5]*pow(constants[3]*constants[4]*constants[5]-(-constants[3]*constants[5]*algebraicVariables[1]+-pow(constants[4], 2.0)*algebraicVariables[1]*(-states[9]+constants[27]-states[11])-constants[3]*constants[4]*(-states[9]+constants[27]-states[11])), -1.0)*constants[25]
    algebraicVariables[19] = algebraicVariables[1]*algebraicVariables[20]/constants[4]
    algebraicVariables[21] = constants[27]-states[9]-states[11]
    algebraicVariables[18] = algebraicVariables[1]*algebraicVariables[20]*algebraicVariables[21]/(constants[3]*constants[5]/constants[4])
    algebraicVariables[17] = algebraicVariables[20]*algebraicVariables[21]/constants[5]
    algebraicVariables[22] = (0.7+3.8234*pow(states[0]/1.0, 0.9787)/(0.1986+pow(states[0]/1.0, 0.9787)))*(1.0+1.0/1.4432*-1.0061*pow(states[3]/1.0, 0.8356)/(0.1918+pow(states[3]/1.0, 0.8356)))*constants[28]/60.0*0.001
    algebraicVariables[23] = algebraicVariables[22]*constants[32]*constants[31]*constants[29]/(constants[30]+constants[29])
    algebraicVariables[24] = (0.063+2.01*pow(states[6]*1000.0, 1.0043)/(31.544+pow(states[6]*1000.0, 1.0043)))*(1.0+1.0/3.01*49.1*pow(states[10]*1000.0, 0.8921)/(25.44+pow(states[10]*1000.0, 0.8921)))*constants[33]/60.0*0.001
    algebraicVariables[25] = algebraicVariables[24]*constants[37]*constants[36]*constants[34]/(constants[35]+constants[34])
    algebraicVariables[26] = constants[6]*constants[43]*states[12]/(constants[7]+states[12])
    algebraicVariables[27] = constants[8]*constants[44]*states[12]/(constants[9]+states[12])
    algebraicVariables[28] = constants[10]*constants[45]*states[12]/(constants[11]+states[12])
    algebraicVariables[29] = constants[6]*constants[46]*states[13]/(constants[7]+states[13])
    algebraicVariables[30] = constants[10]*constants[47]*states[13]/(constants[11]+states[13])
    algebraicVariables[31] = constants[6]*constants[48]*states[14]/(constants[7]+states[14])
    algebraicVariables[32] = constants[8]*constants[49]*states[14]/(constants[9]+states[14])
    algebraicVariables[33] = constants[10]*constants[50]*states[14]/(constants[11]+states[14])
