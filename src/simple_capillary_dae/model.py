# The content of this file was generated using the Python profile of libCellML 0.6.3.

from enum import Enum
from math import *


__version__ = "0.8.0"
LIBCELLML_VERSION = "0.6.3"

STATE_COUNT = 1
CONSTANT_COUNT = 0
COMPUTED_CONSTANT_COUNT = 6
ALGEBRAIC_VARIABLE_COUNT = 5

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
    {"name": "C", "units": "dimensionless", "component": "Capillary"},
    {"name": "v_z", "units": "dimensionless", "component": "Capillary"}
]

ALGEBRAIC_INFO = [
    {"name": "v_y", "units": "dimensionless", "component": "Capillary"},
    {"name": "P_C", "units": "dimensionless", "component": "Capillary"},
    {"name": "P_x", "units": "dimensionless", "component": "Capillary"},
    {"name": "P_R_v", "units": "dimensionless", "component": "Capillary"},
    {"name": "P_R", "units": "dimensionless", "component": "Capillary"}
]


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

    algebraic_variables[3] = u[0]

    f[0] = algebraic_variables[3]-(algebraic_variables[2]+algebraic_variables[1])


def find_root_0(voi, states, rates, constants, computed_constants, algebraic_variables):
    u = [nan]*1

    u[0] = algebraic_variables[3]

    u = nla_solve(objective_function_0, u, 1, [voi, states, rates, constants, computed_constants, algebraic_variables])

    algebraic_variables[3] = u[0]


def objective_function_1(u, f, data):
    voi = data[0]
    states = data[1]
    rates = data[2]
    constants = data[3]
    computed_constants = data[4]
    algebraic_variables = data[5]

    algebraic_variables[4] = u[0]

    f[0] = algebraic_variables[4]-computed_constants[5]*computed_constants[2]


def find_root_1(voi, states, rates, constants, computed_constants, algebraic_variables):
    u = [nan]*1

    u[0] = algebraic_variables[4]

    u = nla_solve(objective_function_1, u, 1, [voi, states, rates, constants, computed_constants, algebraic_variables])

    algebraic_variables[4] = u[0]


def initialise_arrays(states, rates, constants, computed_constants, algebraic_variables):
    states[0] = 2.0
    computed_constants[0] = 10.0
    computed_constants[1] = 10.0
    computed_constants[2] = 10.0
    computed_constants[3] = 10.0
    computed_constants[4] = 10.0
    algebraic_variables[3] = 2.0
    algebraic_variables[4] = 2.0


def compute_computed_constants(states, rates, constants, computed_constants, algebraic_variables ):
    algebraic_variables[1] = states[0]/computed_constants[4]
    find_root_1(voi, states, rates, constants, computed_constants, algebraic_variables)
    algebraic_variables[2] = computed_constants[1]+algebraic_variables[4]
    find_root_0(voi, states, rates, constants, computed_constants, algebraic_variables)
    algebraic_variables[0] = algebraic_variables[3]/computed_constants[3]
    computed_constants[5] = computed_constants[0]+algebraic_variables[0]


def compute_rates(voi, states, rates, constants, computed_constants, algebraic_variables):
    rates[0] = algebraic_variables[0]


def compute_variables(voi, states, rates, constants, computed_constants, algebraic_variables):
    algebraic_variables[1] = states[0]/computed_constants[4]
    find_root_1(voi, states, rates, constants, computed_constants, algebraic_variables)
    algebraic_variables[2] = computed_constants[1]+algebraic_variables[4]
    find_root_0(voi, states, rates, constants, computed_constants, algebraic_variables)
    algebraic_variables[0] = algebraic_variables[3]/computed_constants[3]
