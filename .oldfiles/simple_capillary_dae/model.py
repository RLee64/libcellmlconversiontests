# The content of this file was generated using the Python profile of libCellML 0.6.3.

from enum import Enum
from math import *


__version__ = "0.6.0"
LIBCELLML_VERSION = "0.6.3"

STATE_COUNT = 1
CONSTANT_COUNT = 0
COMPUTED_CONSTANT_COUNT = 5
ALGEBRAIC_VARIABLE_COUNT = 6

VOI_INFO = {"name": "t", "units": "dimensionless", "component": "Capillary"}

STATE_INFO = [
    {"name": "q", "units": "dimensionless", "component": "Capillary"}
]

CONSTANT_INFO = [
]

COMPUTED_CONSTANT_INFO = [
    {"name": "v_in", "units": "dimensionless", "component": "Capillary"},
    {"name": "P_out", "units": "dimensionless", "component": "Capillary"},
    {"name": "R", "units": "dimensionless", "component": "Capillary"},
    {"name": "R_v", "units": "dimensionless", "component": "Capillary"},
    {"name": "C", "units": "dimensionless", "component": "Capillary"}
]

ALGEBRAIC_INFO = [
    {"name": "v_z", "units": "dimensionless", "component": "Capillary"},
    {"name": "v_y", "units": "dimensionless", "component": "Capillary"},
    {"name": "P_R", "units": "dimensionless", "component": "Capillary"},
    {"name": "P_x", "units": "dimensionless", "component": "Capillary"},
    {"name": "P_C", "units": "dimensionless", "component": "Capillary"},
    {"name": "P_R_v", "units": "dimensionless", "component": "Capillary"}
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

    algebraic_variables[0] = u[0]
    algebraic_variables[1] = u[1]
    algebraic_variables[2] = u[2]
    algebraic_variables[3] = u[3]
    algebraic_variables[5] = u[4]

    f[0] = computed_constants[0]-(algebraic_variables[1]+algebraic_variables[0])
    f[1] = algebraic_variables[3]-(computed_constants[1]+algebraic_variables[2])
    f[2] = algebraic_variables[3]-(algebraic_variables[5]+algebraic_variables[4])
    f[3] = algebraic_variables[2]-(algebraic_variables[0]*computed_constants[2])
    f[4] = algebraic_variables[5]-(algebraic_variables[1]*computed_constants[3])
    
    
def find_root_0(voi, states, rates, constants, computed_constants, algebraic_variables):
    u = [nan]*5

    u[0] = algebraic_variables[0]
    u[1] = algebraic_variables[1]
    u[2] = algebraic_variables[2]
    u[3] = algebraic_variables[3]
    u[4] = algebraic_variables[5]

    u = nla_solve(objective_function_0, u, 5, [voi, states, rates, constants, computed_constants, algebraic_variables])

    algebraic_variables[0] = u[0]
    algebraic_variables[1] = u[1]
    algebraic_variables[2] = u[2]
    algebraic_variables[3] = u[3]
    algebraic_variables[5] = u[4]


def initialise_arrays(states, rates, constants, computed_constants, algebraic_variables):
    states[0] = 2.0
    computed_constants[0] = 5.0
    computed_constants[1] = 10.0
    computed_constants[2] = 10.0
    computed_constants[3] = 10.0
    computed_constants[4] = 10.0
    algebraic_variables[0] = 1.0
    algebraic_variables[1] = 1.0
    algebraic_variables[2] = 1.0
    algebraic_variables[3] = 1.0
    algebraic_variables[5] = 1.0


def compute_computed_constants(states, rates, constants, computed_constants, algebraic):
    pass


def compute_rates(voi, states, rates, constants, computed_constants, algebraic_variables):
    rates[0] = algebraic_variables[1]


def compute_variables(voi, states, rates, constants, computed_constants, algebraic_variables):
    algebraic_variables[4] = states[0]/computed_constants[4]
    find_root_0(voi, states, rates, constants, computed_constants, algebraic_variables)

