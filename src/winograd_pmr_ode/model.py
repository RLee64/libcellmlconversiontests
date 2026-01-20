# The content of this file was generated using the Python profile of libCellML 0.6.3.

from enum import Enum
from math import *


__version__ = "0.6.0"
LIBCELLML_VERSION = "0.6.3"

STATE_COUNT = 7
CONSTANT_COUNT = 38
COMPUTED_CONSTANT_COUNT = 0
ALGEBRAIC_VARIABLE_COUNT = 40

VOI_INFO = {"name": "time", "units": "second", "component": "environment"}

STATE_INFO = [
    {"name": "V", "units": "millivolt", "component": "membrane"},
    {"name": "h", "units": "dimensionless", "component": "Na_h_gate"},
    {"name": "m", "units": "dimensionless", "component": "Na_m_gate"},
    {"name": "n", "units": "dimensionless", "component": "KD_n_gate"},
    {"name": "p", "units": "dimensionless", "component": "KM_p_gate"},
    {"name": "q", "units": "dimensionless", "component": "CaL_q_gate"},
    {"name": "Ca_i", "units": "mM", "component": "dCa_i_dt"}
]

CONSTANT_INFO = [
    {"name": "C_m", "units": "mF_per_cm_squared", "component": "membrane"},
    {"name": "V_T", "units": "millivolt", "component": "membrane"},
    {"name": "V_S", "units": "millivolt", "component": "membrane"},
    {"name": "F", "units": "coulomb_per_mole", "component": "membrane"},
    {"name": "R", "units": "joule_per_mole_per_kelvin", "component": "membrane"},
    {"name": "T", "units": "kelvin", "component": "membrane"},
    {"name": "period", "units": "second", "component": "stimulus_protocol"},
    {"name": "i_stimAmplitude", "units": "milliampere_per_cm_squared", "component": "stimulus_protocol"},
    {"name": "i_stimEnd", "units": "second", "component": "stimulus_protocol"},
    {"name": "i_stimStart", "units": "second", "component": "stimulus_protocol"},
    {"name": "E_leak", "units": "millivolt", "component": "I_leak"},
    {"name": "g_leak", "units": "millisiemens_per_cm_squared", "component": "I_leak"},
    {"name": "E_Na", "units": "millivolt", "component": "I_Na"},
    {"name": "g_Na", "units": "millisiemens_per_cm_squared", "component": "I_Na"},
    {"name": "E_K", "units": "millivolt", "component": "I_KD"},
    {"name": "g_KD", "units": "millisiemens_per_cm_squared", "component": "I_KD"},
    {"name": "g_KM", "units": "millisiemens_per_cm_squared", "component": "I_KM"},
    {"name": "tau_max", "units": "second", "component": "KM_p_gate"},
    {"name": "P_Ca", "units": "cm_per_second", "component": "I_CaL"},
    {"name": "Z", "units": "dimensionless", "component": "G_nonlin"},
    {"name": "Ca_o", "units": "mM", "component": "G_nonlin"},
    {"name": "d", "units": "centimeter", "component": "dCa_i_dt"},
    {"name": "k", "units": "fixer", "component": "dCa_i_dt"},
    {"name": "tau_r", "units": "second", "component": "dCa_i_dt"},
    {"name": "Ca_inf", "units": "mM", "component": "dCa_i_dt"},
    {"name": "g_inc", "units": "dimensionless", "component": "I_h"},
    {"name": "E_h", "units": "millivolt", "component": "I_h"},
    {"name": "g_hbar", "units": "millisiemens_per_cm_squared", "component": "I_h"},
    {"name": "cac", "units": "mM", "component": "I_h"},
    {"name": "V_S", "units": "millivolt", "component": "I_h"},
    {"name": "k_2", "units": "per_second", "component": "rate_constants"},
    {"name": "k_4", "units": "per_second", "component": "rate_constants"},
    {"name": "tau_m", "units": "second", "component": "rate_constants"},
    {"name": "n_Ca", "units": "dimensionless", "component": "rate_constants"},
    {"name": "Ca_c", "units": "mM", "component": "rate_constants"},
    {"name": "n_exp", "units": "dimensionless", "component": "rate_constants"},
    {"name": "p_C", "units": "dimensionless", "component": "rate_constants"},
    {"name": "P_c", "units": "dimensionless", "component": "rate_constants"}
]

COMPUTED_CONSTANT_INFO = [
]

ALGEBRAIC_INFO = [
    {"name": "I_h", "units": "milliampere_per_cm_squared", "component": "membrane"},
    {"name": "I_CaL", "units": "milliampere_per_cm_squared", "component": "membrane"},
    {"name": "I_KM", "units": "milliampere_per_cm_squared", "component": "membrane"},
    {"name": "I_KD", "units": "milliampere_per_cm_squared", "component": "membrane"},
    {"name": "I_Na", "units": "milliampere_per_cm_squared", "component": "membrane"},
    {"name": "I_leak", "units": "milliampere_per_cm_squared", "component": "membrane"},
    {"name": "I_app", "units": "milliampere_per_cm_squared", "component": "membrane"},
    {"name": "tau", "units": "second", "component": "stimulus_protocol"},
    {"name": "alpha", "units": "per_second", "component": "Na_m_gate"},
    {"name": "beta", "units": "per_second", "component": "Na_m_gate"},
    {"name": "tau_m", "units": "second", "component": "Na_m_gate"},
    {"name": "m_inf", "units": "dimensionless", "component": "Na_m_gate"},
    {"name": "alpha_h", "units": "per_second", "component": "Na_h_gate"},
    {"name": "beta_h", "units": "per_second", "component": "Na_h_gate"},
    {"name": "tau_h", "units": "second", "component": "Na_h_gate"},
    {"name": "h_inf", "units": "dimensionless", "component": "Na_h_gate"},
    {"name": "alpha_n", "units": "per_second", "component": "KD_n_gate"},
    {"name": "beta_n", "units": "per_second", "component": "KD_n_gate"},
    {"name": "tau_n", "units": "second", "component": "KD_n_gate"},
    {"name": "n_inf", "units": "dimensionless", "component": "KD_n_gate"},
    {"name": "p_inf", "units": "dimensionless", "component": "KM_p_gate"},
    {"name": "tau_p", "units": "second", "component": "KM_p_gate"},
    {"name": "G", "units": "coulomb_per_cm_cubed", "component": "I_CaL"},
    {"name": "alpha_q", "units": "per_second", "component": "CaL_q_gate"},
    {"name": "beta_q", "units": "per_second", "component": "CaL_q_gate"},
    {"name": "tau_q", "units": "second", "component": "CaL_q_gate"},
    {"name": "q_inf", "units": "dimensionless", "component": "CaL_q_gate"},
    {"name": "drive_channel", "units": "mM_per_second", "component": "dCa_i_dt"},
    {"name": "o_2", "units": "dimensionless", "component": "I_h"},
    {"name": "o_1", "units": "dimensionless", "component": "I_h"},
    {"name": "m", "units": "dimensionless", "component": "I_h"},
    {"name": "k_1Ca", "units": "per_second", "component": "kinetic"},
    {"name": "p_1", "units": "dimensionless", "component": "kinetic"},
    {"name": "p_0", "units": "dimensionless", "component": "kinetic"},
    {"name": "alpha", "units": "dimensionless", "component": "kinetic"},
    {"name": "beta", "units": "dimensionless", "component": "kinetic"},
    {"name": "c_1", "units": "dimensionless", "component": "kinetic"},
    {"name": "k_3p", "units": "per_second", "component": "kinetic"},
    {"name": "h_inf", "units": "second", "component": "rate_constants"},
    {"name": "tau_s", "units": "second", "component": "rate_constants"}
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


def initialise_arrays(states, rates, constants, computed_constants, algebraic_variables):
    states[0] = -70.0
    states[1] = 0.0
    states[2] = 0.0
    states[3] = 0.0
    states[4] = 0.0
    states[5] = 0.00247262
    states[6] = 100.0e-6
    constants[0] = 0.001
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


def compute_computed_constants(states, rates, constants, computed_constants, algebraic):
    pass


def compute_rates(voi, states, rates, constants, computed_constants, algebraic_variables):
    algebraicVariables[7] = voi-constants[6]*floor(voi/constants[6])
    algebraicVariables[6] = constants[7] if and_func(geq_func(algebraicVariables[7], constants[9]), leq_func(algebraicVariables[7], constants[8])) else 0.0
    algebraicVariables[5] = 1000.0*constants[11]*(states[0]-constants[10])
    algebraicVariables[4] = 1000.0*constants[13]*pow(states[2], 3.0)*states[1]*(states[0]-constants[12])
    algebraicVariables[3] = 1000.0*constants[15]*pow(states[3], 4.0)*(states[0]-constants[14])
    algebraicVariables[2] = 1000.0*constants[16]*states[4]*(states[0]-constants[14])
    algebraicVariables[32] = pow(pow(states[6], constants[33])+pow(constants[34], constants[33]), -1.0)*pow(states[6], constants[33])
    algebraicVariables[29] = pow(constants[36], constants[35])*pow(pow(algebraicVariables[32], constants[35])-pow(constants[36], constants[35])*(-1.0-pow(2.71828182845905, 0.181818181818182*(75.0+states[0]-constants[29]))), -1.0)
    algebraicVariables[37] = constants[31]*pow(algebraicVariables[32]/constants[36], constants[35])
    algebraicVariables[28] = algebraicVariables[29]*pow(constants[31], -1.0)*algebraicVariables[37]
    algebraicVariables[30] = algebraicVariables[29]+constants[25]+algebraicVariables[28]
    algebraicVariables[0] = 1000.0*constants[27]*algebraicVariables[30]*(states[0]-constants[26])
    algebraicVariables[22] = pow(constants[19], 2.0)*pow(constants[3], 2.0)*0.001*states[0]/(constants[4]*constants[5])*0.000001*(states[6]-constants[20]*exp(constants[19]*constants[3]*0.001*states[0]/(constants[4]*constants[5])))/(1.0-exp(0.001*constants[19]*constants[3]*states[0]/(constants[4]*constants[5])))
    algebraicVariables[1] = 1000.0*constants[18]*pow(states[5], 2.0)*algebraicVariables[22]
    rates[0] = 0.001*(algebraicVariables[6]+-algebraicVariables[5]-algebraicVariables[4]-algebraicVariables[3]-algebraicVariables[2]-algebraicVariables[1]-algebraicVariables[0])/constants[0]
    algebraicVariables[8] = 0.32*4.0*(1.0-(13.0+constants[1]-states[0])/(2.0*4.0)) if lt_func(fabs((13.0+constants[1]-states[0])/4.0), 0.000001) else 0.32*(13.0+constants[1]-states[0])/(exp((13.0+constants[1]-states[0])/4.0)-1.0)
    algebraicVariables[9] = -0.28*5.0*(1.0-(-(states[0]-constants[1]-40.0)/(2.0*5.0))) if lt_func(fabs(-(states[0]-constants[1]-40.0)/5.0), 0.000001) else -0.28*(states[0]-constants[1]-40.0)/(exp(-(states[0]-constants[1]-40.0)/5.0)-1.0)
    algebraicVariables[10] = 1.0/(algebraicVariables[8]+algebraicVariables[9])
    algebraicVariables[11] = algebraicVariables[8]/(algebraicVariables[8]+algebraicVariables[9])
    rates[2] = (algebraicVariables[11]-states[2])/algebraicVariables[10]
    algebraicVariables[12] = 0.128*exp((17.0+constants[1]+constants[2]-states[0])/18.0)
    algebraicVariables[13] = 4.0/(1.0+exp((40.0+constants[2]+constants[1]-states[0])/5.0))
    algebraicVariables[14] = 1.0/(algebraicVariables[12]+algebraicVariables[13])
    algebraicVariables[15] = algebraicVariables[12]/(algebraicVariables[12]+algebraicVariables[13])
    rates[1] = (algebraicVariables[15]-states[1])/algebraicVariables[14]
    algebraicVariables[16] = -0.032*5.0*(1.0-(states[0]-constants[1]-15.0)/(2.0*5.0)) if lt_func(fabs((states[0]-constants[1]-15.0)/5.0), 0.000001) else -0.032*(states[0]-constants[1]-15.0)/(exp((states[0]-constants[1]-15.0)/5.0)-1.0)
    algebraicVariables[17] = 0.5*40.0*(1.0+(states[0]-constants[1]-10.0)/(2.0*40.0)) if lt_func(fabs(-(states[0]-constants[1]-10.0)/40.0), 0.000001) else 0.5*-(states[0]-constants[1]-10.0)/(exp(-(states[0]-constants[1]-10.0)/40.0)-1.0)
    algebraicVariables[18] = 1.0/(algebraicVariables[16]+algebraicVariables[17])
    algebraicVariables[19] = algebraicVariables[16]/(algebraicVariables[16]+algebraicVariables[17])
    rates[3] = (algebraicVariables[19]-states[3])/algebraicVariables[18]
    algebraicVariables[20] = 1.0/(1.0+exp(-(states[0]+35.0)/10.0)) if and_func(lt_func(-(states[0]+35.0)/10.0, 25.0), gt_func(-(states[0]+35.0)/10.0, -25.0)) else 1.0
    algebraicVariables[21] = constants[17]/(3.3*exp((states[0]+35.0)/20.0)+exp(-(states[0]+35.0)/20.0)) if and_func(lt_func((states[0]+35.0)/20.0, 25.0), gt_func((states[0]+35.0)/20.0, -25.0)) else 1.0
    rates[4] = (algebraicVariables[20]-states[4])/algebraicVariables[21]
    algebraicVariables[23] = 6.32/(1.0+exp(-(states[0]-5.0)/13.89))
    algebraicVariables[24] = 0.02*(5.36+(1.31-states[0])/2.0) if lt_func(fabs((1.31-states[0])/5.36), 0.000001) else 0.02*(1.31-states[0])/(1.0-exp((states[0]-1.31)/5.36))
    algebraicVariables[25] = 1.0/(algebraicVariables[23]+algebraicVariables[24])
    algebraicVariables[26] = 1.0/(1.0+exp((states[0]+10.0)/-10.0))
    rates[5] = (algebraicVariables[26]-states[5])/algebraicVariables[25]
    algebraicVariables[27] = constants[22]*algebraicVariables[1]/(2.0*constants[3]*constants[21])
    rates[6] = (constants[24]-states[6])/constants[23] if leq_func(algebraicVariables[27], 0.0) else algebraicVariables[27]+(constants[24]-states[6])/constants[23]


def compute_variables(voi, states, rates, constants, computed_constants, algebraic_variables):
    algebraicVariables[32] = pow(pow(states[6], constants[33])+pow(constants[34], constants[33]), -1.0)*pow(states[6], constants[33])
    algebraicVariables[29] = pow(constants[36], constants[35])*pow(pow(algebraicVariables[32], constants[35])-pow(constants[36], constants[35])*(-1.0-pow(2.71828182845905, 0.181818181818182*(75.0+states[0]-constants[29]))), -1.0)
    algebraicVariables[37] = constants[31]*pow(algebraicVariables[32]/constants[36], constants[35])
    algebraicVariables[28] = algebraicVariables[29]*pow(constants[31], -1.0)*algebraicVariables[37]
    algebraicVariables[30] = algebraicVariables[29]+constants[25]+algebraicVariables[28]
    algebraicVariables[0] = 1000.0*constants[27]*algebraicVariables[30]*(states[0]-constants[26])
    algebraicVariables[31] = constants[30]*pow(states[6]/constants[34], constants[33])
    algebraicVariables[33] = algebraicVariables[32]*constants[30]/algebraicVariables[31]
    algebraicVariables[38] = 1.0/(1.0+exp((states[0]+75.0-constants[29])/5.5))
    algebraicVariables[39] = constants[32]+1000.0/(exp((states[0]+71.55-constants[29])/14.2)+exp(-(states[0]+89.0-constants[29])/11.6))
    algebraicVariables[34] = algebraicVariables[38]/algebraicVariables[39]
    algebraicVariables[35] = (1.0-algebraicVariables[38])/algebraicVariables[39]
    algebraicVariables[36] = algebraicVariables[35]/algebraicVariables[34]*algebraicVariables[29]
