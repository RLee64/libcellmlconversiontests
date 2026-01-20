# The content of this file was generated using the Python profile of libCellML 0.6.3.

from enum import Enum
from math import *


__version__ = "0.6.0"
LIBCELLML_VERSION = "0.6.3"

STATE_COUNT = 9
CONSTANT_COUNT = 32
COMPUTED_CONSTANT_COUNT = 15
ALGEBRAIC_VARIABLE_COUNT = 12

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
    {"name": "C_pericyte_0", "units": "m6_per_J", "component": "parameters"},
    {"name": "u_ext_pericyte_1", "units": "J_per_m3", "component": "parameters"},
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
    {"name": "R", "units": "Js_per_m6", "component": "pericyte_0_module"},
    {"name": "R", "units": "Js_per_m6", "component": "pericyte_1_module"},
    {"name": "u_in", "units": "J_per_m3", "component": "pericyte_1_module"},
    {"name": "u", "units": "J_per_m3", "component": "input_vessel_module"},
    {"name": "u_C", "units": "J_per_m3", "component": "input_vessel_module"},
    {"name": "v", "units": "m3_per_s", "component": "pericyte_1_module"},
    {"name": "v", "units": "m3_per_s", "component": "pericyte_0_module"},
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


from common import nla_solve


def objective_function_0(u, f, data):
    voi = data[0]
    states = data[1]
    rates = data[2]
    constants = data[3]
    computed_constants = data[4]
    algebraic_variables = data[5]

    algebraic_variables[5] = u[0]
    algebraic_variables[6] = u[1]
    algebraic_variables[2] = u[2]

    f[0] = algebraic_variables[2]-(algebraic_variables[7]+2.0*computed_constants[4]*(states[0]-algebraic_variables[6]-algebraic_variables[5]))
    f[1] = algebraic_variables[6]-(algebraic_variables[2]-algebraic_variables[8])/algebraic_variables[0]
    f[2] = algebraic_variables[5]-(algebraic_variables[2]-algebraic_variables[9])/algebraic_variables[1]


def find_root_0(voi, states, rates, constants, computed_constants, algebraic_variables):
    u = [nan]*3

    u[0] = algebraic_variables[5]
    u[1] = algebraic_variables[6]
    u[2] = algebraic_variables[2]

    u = nla_solve(objective_function_0, u, 3, [voi, states, rates, constants, computed_constants, algebraic_variables])

    algebraic_variables[5] = u[0]
    algebraic_variables[6] = u[1]
    algebraic_variables[2] = u[2]


def initialise_arrays(states, rates, constants, computed_constants, algebraic_variables):
    states[0] = 0.0
    states[1] = 0.0
    states[2] = 0.0
    states[3] = 0.0
    states[4] = 0.0
    states[5] = 0.0
    states[6] = 0.0
    constants[10] = 1.0e-18
    states[7] = constants[10]
    constants[17] = 1.0e-18
    states[8] = constants[17]
    constants[0] = 400000.0
    constants[1] = 2.0e-05
    constants[2] = 4.0e-06
    constants[3] = 0.0
    constants[4] = 0.0
    constants[5] = 1.0e-07
    constants[6] = 0.0
    constants[7] = 1.0
    constants[8] = 0.0
    constants[9] = 1.0
    constants[11] = 400000.0
    constants[12] = 2.0e-05
    constants[13] = 2.0e-06
    constants[14] = 0.0
    constants[15] = 0.25e-7
    constants[16] = 0.25e-7
    constants[18] = 400000.0
    constants[19] = 2.0e-05
    constants[20] = 2.0e-06
    constants[21] = 0.0
    constants[22] = 0.25e-7
    constants[23] = 0.25e-7
    constants[24] = 0.0
    constants[25] = 1050.0
    constants[26] = 0.004
    constants[27] = 9.81
    constants[28] = 0.2802
    constants[29] = -505.3
    constants[30] = 0.1324
    constants[31] = -11.14
    algebraic_variables[0] = 1.0
    algebraic_variables[1] = 1.0
    algebraic_variables[2] = 0
    algebraic_variables[5] = 0
    algebraic_variables[6] = 0


def compute_computed_constants(states, rates, constants, computed_constants, algebraic):
    computed_constants[0] = constants[2]*(constants[28]*exp(constants[29]*constants[2])+constants[30]*exp(constants[31]*constants[2]))
    computed_constants[1] = constants[25]*constants[1]/(3.14159265358979*pow(constants[2], 2.0))
    computed_constants[2] = 2.0*3.14159265358979*pow(constants[2], 3.0)*constants[1]/(constants[0]*computed_constants[0])
    computed_constants[3] = 8.0*constants[26]*constants[1]/(3.14159265358979*pow(constants[2], 4.0))
    computed_constants[4] = 0.01/computed_constants[2]
    computed_constants[5] = constants[13]*(constants[28]*exp(constants[29]*constants[13])+constants[30]*exp(constants[31]*constants[13]))
    computed_constants[6] = constants[25]*constants[12]/(3.14159265358979*pow(constants[13], 2.0))
    computed_constants[7] = 2.0*3.14159265358979*pow(constants[13], 3.0)*constants[12]/(constants[11]*computed_constants[5])
    computed_constants[8] = 8.0*constants[26]*constants[12]/(3.14159265358979*pow(constants[13], 4.0))
    computed_constants[9] = constants[15]+constants[16]
    computed_constants[10] = constants[20]*(constants[28]*exp(constants[29]*constants[20])+constants[30]*exp(constants[31]*constants[20]))
    computed_constants[11] = constants[25]*constants[19]/(3.14159265358979*pow(constants[20], 2.0))
    computed_constants[12] = 2.0*3.14159265358979*pow(constants[20], 3.0)*constants[19]/(constants[18]*computed_constants[10])
    computed_constants[13] = 8.0*constants[26]*constants[19]/(3.14159265358979*pow(constants[20], 4.0))
    computed_constants[14] = constants[22]+constants[23]


def compute_rates(voi, states, rates, constants, computed_constants, algebraic_variables):
    algebraic_variables[4] = states[1]/(computed_constants[2]/2.0)+constants[4]
    algebraic_variables[3] = algebraic_variables[4]+2.0*computed_constants[4]*(constants[5]-states[0])
    rates[0] = (algebraic_variables[3]-algebraic_variables[2]-computed_constants[3]*states[0]-constants[24]*constants[25]*constants[27]*constants[1]*cos(constants[3]*3.14159265358979/180.0))/computed_constants[1]
    rates[1] = constants[5]-states[0]
    rates[2] = states[0]-algebraic_variables[6]-algebraic_variables[5]
    rates[4] = algebraic_variables[6]-states[3]
    rates[6] = algebraic_variables[5]-states[5]
    algebraic_variables[8] = states[4]/constants[7]+constants[6]
    algebraic_variables[10] = states[7]/computed_constants[7]+constants[14]
    rates[3] = (algebraic_variables[8]-algebraic_variables[10]-computed_constants[8]*states[3])/computed_constants[6]
    rates[7] = states[3]-computed_constants[9]
    algebraic_variables[9] = states[6]/constants[9]+constants[8]
    algebraic_variables[11] = states[8]/computed_constants[12]+constants[21]
    rates[5] = (algebraic_variables[9]-algebraic_variables[11]-computed_constants[13]*states[5])/computed_constants[11]
    rates[8] = states[5]-computed_constants[14]


def compute_variables(voi, states, rates, constants, computed_constants, algebraic_variables):
    algebraic_variables[4] = states[1]/(computed_constants[2]/2.0)+constants[4]
    algebraic_variables[7] = states[2]/(computed_constants[2]/2.0)+constants[4]
    algebraic_variables[3] = algebraic_variables[4]+2.0*computed_constants[4]*(constants[5]-states[0])
    find_root_0(voi, states, rates, constants, computed_constants, algebraic_variables)
    algebraic_variables[8] = states[4]/constants[7]+constants[6]
    algebraic_variables[9] = states[6]/constants[9]+constants[8]
    algebraic_variables[10] = states[7]/computed_constants[7]+constants[14]
    algebraic_variables[11] = states[8]/computed_constants[12]+constants[21]
