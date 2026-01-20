# The content of this file was generated using the Python profile of libCellML 0.6.3.

from enum import Enum
from math import *


__version__ = "0.6.0"
LIBCELLML_VERSION = "0.6.3"

STATE_COUNT = 9
CONSTANT_COUNT = 34
COMPUTED_CONSTANT_COUNT = 15
ALGEBRAIC_VARIABLE_COUNT = 10

VOI_INFO = {"name": "time", "units": "second", "component": "environment"}

STATE_INFO = [
    {"name": "v", "units": "m3_per_s", "component": "input_vessel_module"},
    {"name": "q_C", "units": "m3", "component": "input_vessel_module"},
    {"name": "q_C_d", "units": "m3", "component": "input_vessel_module"},
    {"name": "v", "units": "m3_per_s", "component": "capillary_0_module"},
    {"name": "q_C", "units": "m3", "component": "pericyte_0_module"},
    {"name": "v", "units": "m3_per_s", "component": "capillary_1_module"},
    {"name": "q_C", "units": "m3", "component": "pericyte_1_module"},
    {"name": "q_C", "units": "m3", "component": "capillary_0_module"},
    {"name": "q_C", "units": "m3", "component": "capillary_1_module"}
]

CONSTANT_INFO = [
    {"name": "E_input_vessel", "units": "J_per_m3", "component": "parameters"},
    {"name": "l_input_vessel", "units": "metre", "component": "parameters"},
    {"name": "r_input_vessel", "units": "metre", "component": "parameters"},
    {"name": "theta_input_vessel", "units": "dimensionless", "component": "parameters"},
    {"name": "u_ext_input_vessel", "units": "J_per_m3", "component": "parameters"},
    {"name": "v_in_input_vessel", "units": "m3_per_s", "component": "parameters"},
    {"name": "u_ext_pericyte_0", "units": "J_per_m3", "component": "parameters"},
    {"name": "R_pericyte_0", "units": "Js_per_m6", "component": "parameters"},
    {"name": "C_pericyte_0", "units": "m6_per_J", "component": "parameters"},
    {"name": "u_ext_pericyte_1", "units": "J_per_m3", "component": "parameters"},
    {"name": "R_pericyte_1", "units": "Js_per_m6", "component": "parameters"},
    {"name": "C_pericyte_1", "units": "m6_per_J", "component": "parameters"},
    {"name": "q_C_init_capillary_0", "units": "m3", "component": "parameters"},
    {"name": "E_capillary_0", "units": "J_per_m3", "component": "parameters"},
    {"name": "l_capillary_0", "units": "metre", "component": "parameters"},
    {"name": "r_capillary_0", "units": "metre", "component": "parameters"},
    {"name": "u_ext_capillary_0", "units": "J_per_m3", "component": "parameters"},
    {"name": "v_out_1_capillary_0", "units": "m3_per_s", "component": "parameters"},
    {"name": "v_out_2_capillary_0", "units": "m3_per_s", "component": "parameters"},
    {"name": "q_C_init_capillary_1", "units": "m3", "component": "parameters"},
    {"name": "E_capillary_1", "units": "J_per_m3", "component": "parameters"},
    {"name": "l_capillary_1", "units": "metre", "component": "parameters"},
    {"name": "r_capillary_1", "units": "metre", "component": "parameters"},
    {"name": "u_ext_capillary_1", "units": "J_per_m3", "component": "parameters"},
    {"name": "v_out_1_capillary_1", "units": "m3_per_s", "component": "parameters"},
    {"name": "v_out_2_capillary_1", "units": "m3_per_s", "component": "parameters"},
    {"name": "beta_g", "units": "dimensionless", "component": "parameters_global"},
    {"name": "rho", "units": "kg_per_m3", "component": "parameters_global"},
    {"name": "mu", "units": "Js_per_m3", "component": "parameters_global"},
    {"name": "g", "units": "m_per_s2", "component": "parameters_global"},
    {"name": "a_vessel", "units": "dimensionless", "component": "parameters_global"},
    {"name": "b_vessel", "units": "per_m", "component": "parameters_global"},
    {"name": "c_vessel", "units": "dimensionless", "component": "parameters_global"},
    {"name": "d_vessel", "units": "per_m", "component": "parameters_global"}
]

COMPUTED_CONSTANT_INFO = [
    {"name": "h", "units": "metre", "component": "input_vessel_module"},
    {"name": "I", "units": "Js2_per_m6", "component": "input_vessel_module"},
    {"name": "C", "units": "m6_per_J", "component": "input_vessel_module"},
    {"name": "R", "units": "Js_per_m6", "component": "input_vessel_module"},
    {"name": "R_v", "units": "Js_per_m6", "component": "input_vessel_module"},
    {"name": "h", "units": "metre", "component": "capillary_0_module"},
    {"name": "I", "units": "Js2_per_m6", "component": "capillary_0_module"},
    {"name": "C", "units": "m6_per_J", "component": "capillary_0_module"},
    {"name": "R", "units": "Js_per_m6", "component": "capillary_0_module"},
    {"name": "v_out_total", "units": "m3_per_s", "component": "capillary_0_module"},
    {"name": "h", "units": "metre", "component": "capillary_1_module"},
    {"name": "I", "units": "Js2_per_m6", "component": "capillary_1_module"},
    {"name": "C", "units": "m6_per_J", "component": "capillary_1_module"},
    {"name": "R", "units": "Js_per_m6", "component": "capillary_1_module"},
    {"name": "v_out_total", "units": "m3_per_s", "component": "capillary_1_module"}
]

ALGEBRAIC_INFO = [
    {"name": "u_d", "units": "J_per_m3", "component": "input_vessel_module"},
    {"name": "u", "units": "J_per_m3", "component": "input_vessel_module"},
    {"name": "u_C", "units": "J_per_m3", "component": "input_vessel_module"},
    {"name": "v_out_2", "units": "m3_per_s", "component": "input_vessel_module"},
    {"name": "v_out_1", "units": "m3_per_s", "component": "input_vessel_module"},
    {"name": "u_C_d", "units": "J_per_m3", "component": "input_vessel_module"},
    {"name": "u", "units": "J_per_m3", "component": "pericyte_0_module"},
    {"name": "u", "units": "J_per_m3", "component": "pericyte_1_module"},
    {"name": "u", "units": "J_per_m3", "component": "capillary_0_module"},
    {"name": "u", "units": "J_per_m3", "component": "capillary_1_module"}
]


def create_states_array():
    return [nan]*STATE_COUNT


def create_constants_array():
    return [nan]*CONSTANT_COUNT


def create_computed_constants_array():
    return [nan]*COMPUTED_CONSTANT_COUNT


def create_algebraic_variables_array():
    return [nan]*ALGEBRAIC_VARIABLE_COUNT


def initialise_arrays(states, rates, constants, computed_constants, algebraic_variables):
    states[0] = 0.0
    states[1] = 0.0
    states[2] = 0.0
    states[3] = 0.0
    states[4] = 0.0
    states[5] = 0.0
    states[6] = 0.0
    constants[12] = 1.0e-18
    states[7] = constants[12]
    constants[19] = 1.0e-18
    states[8] = constants[19]
    constants[0] = 400000.0
    constants[1] = 2.0e-05
    constants[2] = 4.0e-06
    constants[3] = 0.0
    constants[4] = 0.0
    constants[5] = 1.0e-07
    constants[6] = 0.0
    constants[7] = 1.0
    constants[8] = 1.0
    constants[9] = 0.0
    constants[10] = 1.0
    constants[11] = 1.0
    constants[13] = 400000.0
    constants[14] = 2.0e-05
    constants[15] = 2.0e-06
    constants[16] = 0.0
    constants[17] = 0.25e-7
    constants[18] = 0.25e-7
    constants[20] = 400000.0
    constants[21] = 2.0e-05
    constants[22] = 2.0e-06
    constants[23] = 0.0
    constants[24] = 0.25e-7
    constants[25] = 0.25e-7
    constants[26] = 0.0
    constants[27] = 1050.0
    constants[28] = 0.004
    constants[29] = 9.81
    constants[30] = 0.2802
    constants[31] = -505.3
    constants[32] = 0.1324
    constants[33] = -11.14
    computed_constants[0] = constants[2]*(constants[30]*exp(constants[31]*constants[2])+constants[32]*exp(constants[33]*constants[2]))
    computed_constants[1] = constants[27]*constants[1]/(3.14159265358979*pow(constants[2], 2.0))
    computed_constants[3] = 8.0*constants[28]*constants[1]/(3.14159265358979*pow(constants[2], 4.0))
    computed_constants[5] = constants[15]*(constants[30]*exp(constants[31]*constants[15])+constants[32]*exp(constants[33]*constants[15]))
    computed_constants[6] = constants[27]*constants[14]/(3.14159265358979*pow(constants[15], 2.0))
    computed_constants[8] = 8.0*constants[28]*constants[14]/(3.14159265358979*pow(constants[15], 4.0))
    computed_constants[9] = constants[17]+constants[18]
    computed_constants[10] = constants[22]*(constants[30]*exp(constants[31]*constants[22])+constants[32]*exp(constants[33]*constants[22]))
    computed_constants[11] = constants[27]*constants[21]/(3.14159265358979*pow(constants[22], 2.0))
    computed_constants[13] = 8.0*constants[28]*constants[21]/(3.14159265358979*pow(constants[22], 4.0))
    computed_constants[14] = constants[24]+constants[25]


def compute_computed_constants(states, rates, constants, computed_constants, algebraic):
    computed_constants[2] = 2.0*3.14159265358979*pow(constants[2], 3.0)*constants[1]/(constants[0]*computed_constants[0])
    computed_constants[4] = 0.01/computed_constants[2]
    computed_constants[7] = 2.0*3.14159265358979*pow(constants[15], 3.0)*constants[14]/(constants[13]*computed_constants[5])
    computed_constants[12] = 2.0*3.14159265358979*pow(constants[22], 3.0)*constants[21]/(constants[20]*computed_constants[10])


def compute_rates(voi, states, rates, constants, computed_constants, algebraic_variables):
    algebraic_variables[2] = states[1]/(computed_constants[2]/2.0)+constants[4]
    algebraic_variables[1] = algebraic_variables[2]+2.0*computed_constants[4]*(constants[5]-states[0])
    algebraic_variables[0] = (0.01*(pow(2.71828182845905, constants[31]*constants[2])*constants[30]+pow(2.71828182845905, constants[33]*constants[2])*constants[32])*constants[0]*((states[4]+constants[6]*constants[8]+states[0]*constants[8]*constants[7])*constants[11]*constants[10]+(states[6]+constants[9]*constants[11])*constants[8]*constants[7])+3.14159265358979*sin(10000*voi)*constants[1]*constants[8]*constants[11]*constants[7]*constants[10]*pow(constants[2], 2.0)+3.14159265358979*constants[1]*constants[4]*constants[8]*constants[11]*constants[7]*constants[10]*pow(constants[2], 2.0)+states[2]*(pow(2.71828182845905, constants[31]*constants[2])*constants[30]+pow(2.71828182845905, constants[33]*constants[2])*constants[32])*constants[0]*constants[8]*constants[11]*constants[7]*constants[10])*pow(-0.01*(-constants[8]*constants[11]*constants[10]-constants[8]*constants[11]*constants[7])*(pow(2.71828182845905, constants[31]*constants[2])*constants[30]+pow(2.71828182845905, constants[33]*constants[2])*constants[32])*constants[0]+3.14159265358979*constants[1]*constants[8]*constants[11]*constants[7]*constants[10]*pow(constants[2], 2.0), -1.0)
    rates[0] = (algebraic_variables[1]-algebraic_variables[0]-computed_constants[3]*states[0]-constants[26]*constants[27]*constants[29]*constants[1]*cos(constants[3]*3.14159265358979/180.0))/computed_constants[1]
    rates[1] = constants[5]-states[0]
    algebraic_variables[7] = states[6]/constants[11]+constants[9]
    algebraic_variables[3] = (algebraic_variables[0]-algebraic_variables[7])/constants[10]
    algebraic_variables[6] = states[4]/constants[8]+constants[6]
    algebraic_variables[4] = (algebraic_variables[0]-algebraic_variables[6])/constants[7]
    rates[2] = states[0]-algebraic_variables[4]-algebraic_variables[3]
    rates[4] = algebraic_variables[4]-states[3]
    rates[6] = algebraic_variables[3]-states[5]
    algebraic_variables[8] = states[7]/computed_constants[7]+constants[16]
    rates[3] = (algebraic_variables[6]-algebraic_variables[8]-computed_constants[8]*states[3])/computed_constants[6]
    rates[7] = states[3]-computed_constants[9]
    algebraic_variables[9] = states[8]/computed_constants[12]+constants[23]
    rates[5] = (algebraic_variables[7]-algebraic_variables[9]-computed_constants[13]*states[5])/computed_constants[11]
    rates[8] = states[5]-computed_constants[14]


def compute_variables(voi, states, rates, constants, computed_constants, algebraic_variables):
    algebraic_variables[5] = states[2]/(computed_constants[2]/2.0)+constants[4]
    algebraic_variables[0] = (0.01*(pow(2.71828182845905, constants[31]*constants[2])*constants[30]+pow(2.71828182845905, constants[33]*constants[2])*constants[32])*constants[0]*((states[4]+constants[6]*constants[8]+states[0]*constants[8]*constants[7])*constants[11]*constants[10]+(states[6]+constants[9]*constants[11])*constants[8]*constants[7])+3.14159265358979*sin(100*voi)*constants[1]*constants[8]*constants[11]*constants[7]*constants[10]*pow(constants[2], 2.0)+3.14159265358979*constants[1]*constants[4]*constants[8]*constants[11]*constants[7]*constants[10]*pow(constants[2], 2.0)+states[2]*(pow(2.71828182845905, constants[31]*constants[2])*constants[30]+pow(2.71828182845905, constants[33]*constants[2])*constants[32])*constants[0]*constants[8]*constants[11]*constants[7]*constants[10])*pow(-0.01*(-constants[8]*constants[11]*constants[10]-constants[8]*constants[11]*constants[7])*(pow(2.71828182845905, constants[31]*constants[2])*constants[30]+pow(2.71828182845905, constants[33]*constants[2])*constants[32])*constants[0]+3.14159265358979*constants[1]*constants[8]*constants[11]*constants[7]*constants[10]*pow(constants[2], 2.0), -1.0)
    algebraic_variables[4] = (algebraic_variables[0]-algebraic_variables[6])/constants[7]
    algebraic_variables[3] = (algebraic_variables[0]-algebraic_variables[7])/constants[10]
