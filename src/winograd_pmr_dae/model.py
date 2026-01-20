# The content of this file was generated using the Python profile of libCellML 0.6.3.

from enum import Enum
from math import *


__version__ = "0.8.0"
LIBCELLML_VERSION = "0.6.3"

STATE_COUNT = 7
CONSTANT_COUNT = 38
COMPUTED_CONSTANT_COUNT = 0
ALGEBRAIC_VARIABLE_COUNT = 40

VOI_INFO = {"name": "time", "units": "dimensionless", "component": "environment"}

STATE_INFO = [
    {"name": "V", "units": "dimensionless", "component": "membrane"},
    {"name": "h", "units": "dimensionless", "component": "Na_h_gate"},
    {"name": "m", "units": "dimensionless", "component": "Na_m_gate"},
    {"name": "n", "units": "dimensionless", "component": "KD_n_gate"},
    {"name": "p", "units": "dimensionless", "component": "KM_p_gate"},
    {"name": "q", "units": "dimensionless", "component": "CaL_q_gate"},
    {"name": "Ca_i", "units": "dimensionless", "component": "dCa_i_dt"}
]

CONSTANT_INFO = [
    {"name": "C_m", "units": "dimensionless", "component": "membrane"},
    {"name": "V_T", "units": "dimensionless", "component": "membrane"},
    {"name": "V_S", "units": "dimensionless", "component": "membrane"},
    {"name": "F", "units": "dimensionless", "component": "membrane"},
    {"name": "R", "units": "dimensionless", "component": "membrane"},
    {"name": "T", "units": "dimensionless", "component": "membrane"},
    {"name": "period", "units": "dimensionless", "component": "stimulus_protocol"},
    {"name": "i_stimAmplitude", "units": "dimensionless", "component": "stimulus_protocol"},
    {"name": "i_stimEnd", "units": "dimensionless", "component": "stimulus_protocol"},
    {"name": "i_stimStart", "units": "dimensionless", "component": "stimulus_protocol"},
    {"name": "E_leak", "units": "dimensionless", "component": "I_leak"},
    {"name": "g_leak", "units": "dimensionless", "component": "I_leak"},
    {"name": "E_Na", "units": "dimensionless", "component": "I_Na"},
    {"name": "g_Na", "units": "dimensionless", "component": "I_Na"},
    {"name": "E_K", "units": "dimensionless", "component": "I_KD"},
    {"name": "g_KD", "units": "dimensionless", "component": "I_KD"},
    {"name": "g_KM", "units": "dimensionless", "component": "I_KM"},
    {"name": "tau_max", "units": "dimensionless", "component": "KM_p_gate"},
    {"name": "P_Ca", "units": "dimensionless", "component": "I_CaL"},
    {"name": "Z", "units": "dimensionless", "component": "G_nonlin"},
    {"name": "Ca_o", "units": "dimensionless", "component": "G_nonlin"},
    {"name": "d", "units": "dimensionless", "component": "dCa_i_dt"},
    {"name": "k", "units": "dimensionless", "component": "dCa_i_dt"},
    {"name": "tau_r", "units": "dimensionless", "component": "dCa_i_dt"},
    {"name": "Ca_inf", "units": "dimensionless", "component": "dCa_i_dt"},
    {"name": "g_inc", "units": "dimensionless", "component": "I_h"},
    {"name": "E_h", "units": "dimensionless", "component": "I_h"},
    {"name": "g_hbar", "units": "dimensionless", "component": "I_h"},
    {"name": "cac", "units": "dimensionless", "component": "I_h"},
    {"name": "V_S", "units": "dimensionless", "component": "I_h"},
    {"name": "k_2", "units": "dimensionless", "component": "rate_constants"},
    {"name": "k_4", "units": "dimensionless", "component": "rate_constants"},
    {"name": "tau_m", "units": "dimensionless", "component": "rate_constants"},
    {"name": "n_Ca", "units": "dimensionless", "component": "rate_constants"},
    {"name": "Ca_c", "units": "dimensionless", "component": "rate_constants"},
    {"name": "n_exp", "units": "dimensionless", "component": "rate_constants"},
    {"name": "p_C", "units": "dimensionless", "component": "rate_constants"},
    {"name": "P_c", "units": "dimensionless", "component": "rate_constants"}
]

COMPUTED_CONSTANT_INFO = [
]

ALGEBRAIC_INFO = [
    {"name": "I_h", "units": "dimensionless", "component": "I_h"},
    {"name": "I_CaL", "units": "dimensionless", "component": "I_CaL"},
    {"name": "I_KM", "units": "dimensionless", "component": "I_KM"},
    {"name": "I_KD", "units": "dimensionless", "component": "I_KD"},
    {"name": "I_Na", "units": "dimensionless", "component": "I_Na"},
    {"name": "I_leak", "units": "dimensionless", "component": "I_leak"},
    {"name": "I_app", "units": "dimensionless", "component": "stimulus_protocol"},
    {"name": "tau", "units": "dimensionless", "component": "stimulus_protocol"},
    {"name": "alpha", "units": "dimensionless", "component": "Na_m_gate"},
    {"name": "beta", "units": "dimensionless", "component": "Na_m_gate"},
    {"name": "tau_m", "units": "dimensionless", "component": "Na_m_gate"},
    {"name": "m_inf", "units": "dimensionless", "component": "Na_m_gate"},
    {"name": "alpha_h", "units": "dimensionless", "component": "Na_h_gate"},
    {"name": "beta_h", "units": "dimensionless", "component": "Na_h_gate"},
    {"name": "tau_h", "units": "dimensionless", "component": "Na_h_gate"},
    {"name": "h_inf", "units": "dimensionless", "component": "Na_h_gate"},
    {"name": "alpha_n", "units": "dimensionless", "component": "KD_n_gate"},
    {"name": "beta_n", "units": "dimensionless", "component": "KD_n_gate"},
    {"name": "tau_n", "units": "dimensionless", "component": "KD_n_gate"},
    {"name": "n_inf", "units": "dimensionless", "component": "KD_n_gate"},
    {"name": "p_inf", "units": "dimensionless", "component": "KM_p_gate"},
    {"name": "tau_p", "units": "dimensionless", "component": "KM_p_gate"},
    {"name": "G", "units": "dimensionless", "component": "G_nonlin"},
    {"name": "alpha_q", "units": "dimensionless", "component": "CaL_q_gate"},
    {"name": "beta_q", "units": "dimensionless", "component": "CaL_q_gate"},
    {"name": "tau_q", "units": "dimensionless", "component": "CaL_q_gate"},
    {"name": "q_inf", "units": "dimensionless", "component": "CaL_q_gate"},
    {"name": "drive_channel", "units": "dimensionless", "component": "dCa_i_dt"},
    {"name": "o_2", "units": "dimensionless", "component": "kinetic"},
    {"name": "o_1", "units": "dimensionless", "component": "kinetic"},
    {"name": "m", "units": "dimensionless", "component": "I_h"},
    {"name": "k_1Ca", "units": "dimensionless", "component": "rate_constants"},
    {"name": "p_1", "units": "dimensionless", "component": "kinetic"},
    {"name": "p_0", "units": "dimensionless", "component": "kinetic"},
    {"name": "alpha", "units": "dimensionless", "component": "rate_constants"},
    {"name": "beta", "units": "dimensionless", "component": "rate_constants"},
    {"name": "c_1", "units": "dimensionless", "component": "kinetic"},
    {"name": "k_3p", "units": "dimensionless", "component": "rate_constants"},
    {"name": "h_inf", "units": "dimensionless", "component": "rate_constants"},
    {"name": "tau_s", "units": "dimensionless", "component": "rate_constants"}
]


def lt_func(x, y):
    return 1.0 if x < y else 0.0


def leq_func(x, y):
    return 1.0 if x <= y else 0.0


def gt_func(x, y):
    return 1.0 if x > y else 0.0


def geq_func(x, y):
    return 1.0 if x >= y else 0.0


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


from nlasolver import nla_solve


def objective_function_0(u, f, data):
    voi = data[0]
    states = data[1]
    rates = data[2]
    constants = data[3]
    computed_constants = data[4]
    algebraic_variables = data[5]

    algebraic_variables[32] = u[0]

    f[0] = algebraic_variables[32]-(1.0-algebraic_variables[33])


def find_root_0(voi, states, rates, constants, computed_constants, algebraic_variables):
    u = [nan]*1

    u[0] = algebraic_variables[32]

    u = nla_solve(objective_function_0, u, 1, [voi, states, rates, constants, computed_constants, algebraic_variables])

    algebraic_variables[32] = u[0]


def objective_function_1(u, f, data):
    voi = data[0]
    states = data[1]
    rates = data[2]
    constants = data[3]
    computed_constants = data[4]
    algebraic_variables = data[5]

    algebraic_variables[28] = u[0]

    f[0] = algebraic_variables[28]-(1.0-algebraic_variables[36]-algebraic_variables[29])


def find_root_1(voi, states, rates, constants, computed_constants, algebraic_variables):
    u = [nan]*1

    u[0] = algebraic_variables[28]

    u = nla_solve(objective_function_1, u, 1, [voi, states, rates, constants, computed_constants, algebraic_variables])

    algebraic_variables[28] = u[0]


def initialise_arrays(states, rates, constants, computed_constants, algebraic_variables):
    states[0] = -70.0
    states[1] = 0.0
    states[2] = 0.0
    states[3] = 0.0
    states[4] = 0.0
    states[5] = 0.00247262
    states[6] = 100.0e-6
    constants[0] = 1.0e-3
    constants[1] = -55.0
    constants[2] = 0.0
    constants[3] = 96489.0
    constants[4] = 8.314
    constants[5] = 296.65
    constants[6] = 9.0
    constants[7] = -0.3
    constants[8] = 9.0
    constants[9] = 5.0
    constants[10] = -70.0
    constants[11] = 1.0
    constants[12] = 50.0
    constants[13] = 70.0
    constants[14] = -95.0
    constants[15] = 7.0
    constants[16] = 0.004
    constants[17] = 4.0
    constants[18] = 2.76e-4
    constants[19] = 2.0
    constants[20] = 2.0
    constants[21] = 1.0e-4
    constants[22] = 0.1
    constants[23] = 17.0e-3
    constants[24] = 100.0e-6
    constants[25] = 2.0
    constants[26] = -20.0
    constants[27] = 0.02
    constants[28] = 0.006
    constants[29] = 0.0
    constants[30] = 0.1
    constants[31] = 1.0
    constants[32] = 20.0e-3
    constants[33] = 4.0
    constants[34] = 0.006
    constants[35] = 1.0
    constants[36] = 0.01
    constants[37] = 0.01
    algebraic_variables[28] = 0.0
    algebraic_variables[32] = 0.0


def compute_computed_constants(states, rates, constants, computed_constants, algebraic_variables ):
    pass


def compute_rates(voi, states, rates, constants, computed_constants, algebraic_variables):
    algebraic_variables[2] = 1000.0*constants[16]*states[4]*(states[0]-constants[14])
    algebraic_variables[3] = 1000.0*constants[15]*pow(states[3], 4.0)*(states[0]-constants[14])
    algebraic_variables[4] = 1000.0*constants[13]*pow(states[2], 3.0)*states[1]*(states[0]-constants[12])
    algebraic_variables[5] = 1000.0*constants[11]*(states[0]-constants[10])
    algebraic_variables[7] = voi-constants[6]*floor(voi/constants[6])
    algebraic_variables[6] = constants[7] if and_func(geq_func(algebraic_variables[7], constants[9]), leq_func(algebraic_variables[7], constants[8])) else 0.0
    algebraic_variables[22] = pow(constants[19], 2.0)*pow(constants[3], 2.0)*1.0e-3*states[0]/(constants[4]*constants[5])*1.0e-6*(states[6]-constants[20]*exp(constants[19]*constants[3]*1.0e-3*states[0]/(constants[4]*constants[5])))/(1.0-exp(1.0e-3*constants[19]*constants[3]*states[0]/(constants[4]*constants[5])))
    algebraic_variables[1] = 1000.0*constants[18]*pow(states[5], 2.0)*algebraic_variables[22]
    algebraic_variables[31] = constants[30]*pow(states[6]/constants[34], constants[33])
    algebraic_variables[33] = algebraic_variables[32]*constants[30]/algebraic_variables[31]
    find_root_0(voi, states, rates, constants, computed_constants, algebraic_variables)
    algebraic_variables[37] = constants[31]*pow(algebraic_variables[32]/constants[36], constants[35])
    algebraic_variables[29] = constants[31]/algebraic_variables[37]*algebraic_variables[28]
    algebraic_variables[39] = constants[32]+1000.0/(exp((states[0]+71.55-constants[29])/14.2)+exp(-(states[0]+89.0-constants[29])/11.6))
    algebraic_variables[38] = 1.0/(1.0+exp((states[0]+75.0-constants[29])/5.5))
    algebraic_variables[34] = algebraic_variables[38]/algebraic_variables[39]
    algebraic_variables[35] = (1.0-algebraic_variables[38])/algebraic_variables[39]
    algebraic_variables[36] = algebraic_variables[35]/algebraic_variables[34]*algebraic_variables[29]
    find_root_1(voi, states, rates, constants, computed_constants, algebraic_variables)
    algebraic_variables[30] = algebraic_variables[29]+constants[25]+algebraic_variables[28]
    algebraic_variables[0] = 1000.0*constants[27]*algebraic_variables[30]*(states[0]-constants[26])
    rates[0] = 1.0e-3*(algebraic_variables[6]+-algebraic_variables[5]-algebraic_variables[4]-algebraic_variables[3]-algebraic_variables[2]-algebraic_variables[1]-algebraic_variables[0])/constants[0]
    algebraic_variables[9] = -0.28*5.0*(1.0-(-(states[0]-constants[1]-40.0)/(2.0*5.0))) if lt_func(fabs(-(states[0]-constants[1]-40.0)/5.0), 1.0e-6) else -0.28*(states[0]-constants[1]-40.0)/(exp(-(states[0]-constants[1]-40.0)/5.0)-1.0)
    algebraic_variables[8] = 0.32*4.0*(1.0-(13.0+constants[1]-states[0])/(2.0*4.0)) if lt_func(fabs((13.0+constants[1]-states[0])/4.0), 1.0e-6) else 0.32*(13.0+constants[1]-states[0])/(exp((13.0+constants[1]-states[0])/4.0)-1.0)
    algebraic_variables[10] = 1.0/(algebraic_variables[8]+algebraic_variables[9])
    algebraic_variables[11] = algebraic_variables[8]/(algebraic_variables[8]+algebraic_variables[9])
    rates[2] = (algebraic_variables[11]-states[2])/algebraic_variables[10]
    algebraic_variables[13] = 4.0/(1.0+exp((40.0+constants[2]+constants[1]-states[0])/5.0))
    algebraic_variables[12] = 0.128*exp((17.0+constants[1]+constants[2]-states[0])/18.0)
    algebraic_variables[14] = 1.0/(algebraic_variables[12]+algebraic_variables[13])
    algebraic_variables[15] = algebraic_variables[12]/(algebraic_variables[12]+algebraic_variables[13])
    rates[1] = (algebraic_variables[15]-states[1])/algebraic_variables[14]
    algebraic_variables[17] = 0.5*40.0*(1.0+(states[0]-constants[1]-10.0)/(2.0*40.0)) if lt_func(fabs(-(states[0]-constants[1]-10.0)/40.0), 1.0e-6) else 0.5*-(states[0]-constants[1]-10.0)/(exp(-(states[0]-constants[1]-10.0)/40.0)-1.0)
    algebraic_variables[16] = -0.032*5.0*(1.0-(states[0]-constants[1]-15.0)/(2.0*5.0)) if lt_func(fabs((states[0]-constants[1]-15.0)/5.0), 1.0e-6) else -0.032*(states[0]-constants[1]-15.0)/(exp((states[0]-constants[1]-15.0)/5.0)-1.0)
    algebraic_variables[18] = 1.0/(algebraic_variables[16]+algebraic_variables[17])
    algebraic_variables[19] = algebraic_variables[16]/(algebraic_variables[16]+algebraic_variables[17])
    rates[3] = (algebraic_variables[19]-states[3])/algebraic_variables[18]
    algebraic_variables[21] = constants[17]/(3.3*exp((states[0]+35.0)/20.0)+exp(-(states[0]+35.0)/20.0)) if and_func(lt_func((states[0]+35.0)/20.0, 25.0), gt_func((states[0]+35.0)/20.0, -25.0)) else 1.0
    algebraic_variables[20] = 1.0/(1.0+exp(-(states[0]+35.0)/10.0)) if and_func(lt_func(-(states[0]+35.0)/10.0, 25.0), gt_func(-(states[0]+35.0)/10.0, -25.0)) else 1.0
    rates[4] = (algebraic_variables[20]-states[4])/algebraic_variables[21]
    algebraic_variables[24] = 0.02*(5.36+(1.31-states[0])/2.0) if lt_func(fabs((1.31-states[0])/5.36), 1.0e-6) else 0.02*(1.31-states[0])/(1.0-exp((states[0]-1.31)/5.36))
    algebraic_variables[23] = 6.32/(1.0+exp(-(states[0]-5.0)/13.89))
    algebraic_variables[25] = 1.0/(algebraic_variables[23]+algebraic_variables[24])
    algebraic_variables[26] = 1.0/(1.0+exp((states[0]+10.0)/-10.0))
    rates[5] = (algebraic_variables[26]-states[5])/algebraic_variables[25]
    algebraic_variables[27] = constants[22]*algebraic_variables[1]/(2.0*constants[3]*constants[21])
    rates[6] = (constants[24]-states[6])/constants[23] if leq_func(algebraic_variables[27], 0.0) else algebraic_variables[27]+(constants[24]-states[6])/constants[23]


def compute_variables(voi, states, rates, constants, computed_constants, algebraic_variables):
    algebraic_variables[5] = 1000.0*constants[11]*(states[0]-constants[10])
    algebraic_variables[4] = 1000.0*constants[13]*pow(states[2], 3.0)*states[1]*(states[0]-constants[12])
    algebraic_variables[8] = 0.32*4.0*(1.0-(13.0+constants[1]-states[0])/(2.0*4.0)) if lt_func(fabs((13.0+constants[1]-states[0])/4.0), 1.0e-6) else 0.32*(13.0+constants[1]-states[0])/(exp((13.0+constants[1]-states[0])/4.0)-1.0)
    algebraic_variables[9] = -0.28*5.0*(1.0-(-(states[0]-constants[1]-40.0)/(2.0*5.0))) if lt_func(fabs(-(states[0]-constants[1]-40.0)/5.0), 1.0e-6) else -0.28*(states[0]-constants[1]-40.0)/(exp(-(states[0]-constants[1]-40.0)/5.0)-1.0)
    algebraic_variables[10] = 1.0/(algebraic_variables[8]+algebraic_variables[9])
    algebraic_variables[11] = algebraic_variables[8]/(algebraic_variables[8]+algebraic_variables[9])
    algebraic_variables[12] = 0.128*exp((17.0+constants[1]+constants[2]-states[0])/18.0)
    algebraic_variables[13] = 4.0/(1.0+exp((40.0+constants[2]+constants[1]-states[0])/5.0))
    algebraic_variables[14] = 1.0/(algebraic_variables[12]+algebraic_variables[13])
    algebraic_variables[15] = algebraic_variables[12]/(algebraic_variables[12]+algebraic_variables[13])
    algebraic_variables[3] = 1000.0*constants[15]*pow(states[3], 4.0)*(states[0]-constants[14])
    algebraic_variables[16] = -0.032*5.0*(1.0-(states[0]-constants[1]-15.0)/(2.0*5.0)) if lt_func(fabs((states[0]-constants[1]-15.0)/5.0), 1.0e-6) else -0.032*(states[0]-constants[1]-15.0)/(exp((states[0]-constants[1]-15.0)/5.0)-1.0)
    algebraic_variables[17] = 0.5*40.0*(1.0+(states[0]-constants[1]-10.0)/(2.0*40.0)) if lt_func(fabs(-(states[0]-constants[1]-10.0)/40.0), 1.0e-6) else 0.5*-(states[0]-constants[1]-10.0)/(exp(-(states[0]-constants[1]-10.0)/40.0)-1.0)
    algebraic_variables[18] = 1.0/(algebraic_variables[16]+algebraic_variables[17])
    algebraic_variables[19] = algebraic_variables[16]/(algebraic_variables[16]+algebraic_variables[17])
    algebraic_variables[2] = 1000.0*constants[16]*states[4]*(states[0]-constants[14])
    algebraic_variables[20] = 1.0/(1.0+exp(-(states[0]+35.0)/10.0)) if and_func(lt_func(-(states[0]+35.0)/10.0, 25.0), gt_func(-(states[0]+35.0)/10.0, -25.0)) else 1.0
    algebraic_variables[21] = constants[17]/(3.3*exp((states[0]+35.0)/20.0)+exp(-(states[0]+35.0)/20.0)) if and_func(lt_func((states[0]+35.0)/20.0, 25.0), gt_func((states[0]+35.0)/20.0, -25.0)) else 1.0
    algebraic_variables[22] = pow(constants[19], 2.0)*pow(constants[3], 2.0)*1.0e-3*states[0]/(constants[4]*constants[5])*1.0e-6*(states[6]-constants[20]*exp(constants[19]*constants[3]*1.0e-3*states[0]/(constants[4]*constants[5])))/(1.0-exp(1.0e-3*constants[19]*constants[3]*states[0]/(constants[4]*constants[5])))
    algebraic_variables[1] = 1000.0*constants[18]*pow(states[5], 2.0)*algebraic_variables[22]
    algebraic_variables[23] = 6.32/(1.0+exp(-(states[0]-5.0)/13.89))
    algebraic_variables[24] = 0.02*(5.36+(1.31-states[0])/2.0) if lt_func(fabs((1.31-states[0])/5.36), 1.0e-6) else 0.02*(1.31-states[0])/(1.0-exp((states[0]-1.31)/5.36))
    algebraic_variables[25] = 1.0/(algebraic_variables[23]+algebraic_variables[24])
    algebraic_variables[26] = 1.0/(1.0+exp((states[0]+10.0)/-10.0))
    algebraic_variables[27] = constants[22]*algebraic_variables[1]/(2.0*constants[3]*constants[21])
    algebraic_variables[31] = constants[30]*pow(states[6]/constants[34], constants[33])
    algebraic_variables[33] = algebraic_variables[32]*constants[30]/algebraic_variables[31]
    find_root_0(voi, states, rates, constants, computed_constants, algebraic_variables)
    algebraic_variables[37] = constants[31]*pow(algebraic_variables[32]/constants[36], constants[35])
    algebraic_variables[29] = constants[31]/algebraic_variables[37]*algebraic_variables[28]
    algebraic_variables[39] = constants[32]+1000.0/(exp((states[0]+71.55-constants[29])/14.2)+exp(-(states[0]+89.0-constants[29])/11.6))
    algebraic_variables[38] = 1.0/(1.0+exp((states[0]+75.0-constants[29])/5.5))
    algebraic_variables[34] = algebraic_variables[38]/algebraic_variables[39]
    algebraic_variables[35] = (1.0-algebraic_variables[38])/algebraic_variables[39]
    algebraic_variables[36] = algebraic_variables[35]/algebraic_variables[34]*algebraic_variables[29]
    find_root_1(voi, states, rates, constants, computed_constants, algebraic_variables)
    algebraic_variables[30] = algebraic_variables[29]+constants[25]+algebraic_variables[28]
    algebraic_variables[0] = 1000.0*constants[27]*algebraic_variables[30]*(states[0]-constants[26])
