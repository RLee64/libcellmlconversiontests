# The content of this file was generated using the Python profile of libCellML 0.6.3.

from enum import Enum
from math import *


__version__ = "0.8.0"
LIBCELLML_VERSION = "0.6.3"

STATE_COUNT = 1
CONSTANT_COUNT = 0
COMPUTED_CONSTANT_COUNT = 0
ALGEBRAIC_VARIABLE_COUNT = 10

VOI_INFO = {"name": "t", "units": "dimensionless", "component": "algebraic_component"}

STATE_INFO = [
    {"name": "x", "units": "dimensionless", "component": "algebraic_component"}
]

CONSTANT_INFO = [
]

COMPUTED_CONSTANT_INFO = [
]

ALGEBRAIC_INFO = [
    {"name": "b", "units": "dimensionless", "component": "algebraic_component"},
    {"name": "a", "units": "dimensionless", "component": "algebraic_component"},
    {"name": "d", "units": "dimensionless", "component": "algebraic_component"},
    {"name": "c", "units": "dimensionless", "component": "algebraic_component"},
    {"name": "f", "units": "dimensionless", "component": "algebraic_component"},
    {"name": "e", "units": "dimensionless", "component": "algebraic_component"},
    {"name": "h", "units": "dimensionless", "component": "algebraic_component"},
    {"name": "g", "units": "dimensionless", "component": "algebraic_component"},
    {"name": "j", "units": "dimensionless", "component": "algebraic_component"},
    {"name": "i", "units": "dimensionless", "component": "algebraic_component"}
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

    algebraic_variables[0] = u[0]
    algebraic_variables[1] = u[1]

    f[0] = algebraic_variables[1]+2.0*algebraic_variables[0]+voi-0.0
    f[1] = algebraic_variables[1]+algebraic_variables[0]+-states[0]-0.0


def find_root_0(voi, states, rates, constants, computed_constants, algebraic_variables):
    u = [nan]*2

    u[0] = algebraic_variables[0]
    u[1] = algebraic_variables[1]

    u = nla_solve(objective_function_0, u, 2, [voi, states, rates, constants, computed_constants, algebraic_variables])

    algebraic_variables[0] = u[0]
    algebraic_variables[1] = u[1]


def objective_function_1(u, f, data):
    voi = data[0]
    states = data[1]
    rates = data[2]
    constants = data[3]
    computed_constants = data[4]
    algebraic_variables = data[5]

    algebraic_variables[2] = u[0]
    algebraic_variables[3] = u[1]

    f[0] = algebraic_variables[3]+2.0*algebraic_variables[2]+voi-0.0
    f[1] = algebraic_variables[3]+algebraic_variables[2]+-states[0]-0.0


def find_root_1(voi, states, rates, constants, computed_constants, algebraic_variables):
    u = [nan]*2

    u[0] = algebraic_variables[2]
    u[1] = algebraic_variables[3]

    u = nla_solve(objective_function_1, u, 2, [voi, states, rates, constants, computed_constants, algebraic_variables])

    algebraic_variables[2] = u[0]
    algebraic_variables[3] = u[1]


def objective_function_2(u, f, data):
    voi = data[0]
    states = data[1]
    rates = data[2]
    constants = data[3]
    computed_constants = data[4]
    algebraic_variables = data[5]

    algebraic_variables[4] = u[0]
    algebraic_variables[5] = u[1]

    f[0] = algebraic_variables[5]+2.0*algebraic_variables[4]+voi-0.0
    f[1] = algebraic_variables[5]+algebraic_variables[4]+-states[0]-0.0


def find_root_2(voi, states, rates, constants, computed_constants, algebraic_variables):
    u = [nan]*2

    u[0] = algebraic_variables[4]
    u[1] = algebraic_variables[5]

    u = nla_solve(objective_function_2, u, 2, [voi, states, rates, constants, computed_constants, algebraic_variables])

    algebraic_variables[4] = u[0]
    algebraic_variables[5] = u[1]


def objective_function_3(u, f, data):
    voi = data[0]
    states = data[1]
    rates = data[2]
    constants = data[3]
    computed_constants = data[4]
    algebraic_variables = data[5]

    algebraic_variables[6] = u[0]
    algebraic_variables[7] = u[1]

    f[0] = algebraic_variables[7]+2.0*algebraic_variables[6]+voi-0.0
    f[1] = algebraic_variables[7]+algebraic_variables[6]+-states[0]-0.0


def find_root_3(voi, states, rates, constants, computed_constants, algebraic_variables):
    u = [nan]*2

    u[0] = algebraic_variables[6]
    u[1] = algebraic_variables[7]

    u = nla_solve(objective_function_3, u, 2, [voi, states, rates, constants, computed_constants, algebraic_variables])

    algebraic_variables[6] = u[0]
    algebraic_variables[7] = u[1]


def objective_function_4(u, f, data):
    voi = data[0]
    states = data[1]
    rates = data[2]
    constants = data[3]
    computed_constants = data[4]
    algebraic_variables = data[5]

    algebraic_variables[8] = u[0]
    algebraic_variables[9] = u[1]

    f[0] = algebraic_variables[9]+2.0*algebraic_variables[8]+voi-0.0
    f[1] = algebraic_variables[9]+algebraic_variables[8]+-states[0]-0.0


def find_root_4(voi, states, rates, constants, computed_constants, algebraic_variables):
    u = [nan]*2

    u[0] = algebraic_variables[8]
    u[1] = algebraic_variables[9]

    u = nla_solve(objective_function_4, u, 2, [voi, states, rates, constants, computed_constants, algebraic_variables])

    algebraic_variables[8] = u[0]
    algebraic_variables[9] = u[1]


def initialise_arrays(states, rates, constants, computed_constants, algebraic_variables):
    states[0] = 0.0
    algebraic_variables[0] = 0.0
    algebraic_variables[1] = 0.0
    algebraic_variables[2] = 0.0
    algebraic_variables[3] = 0.0
    algebraic_variables[4] = 0.0
    algebraic_variables[5] = 0.0
    algebraic_variables[6] = 0.0
    algebraic_variables[7] = 0.0
    algebraic_variables[8] = 0.0
    algebraic_variables[9] = 0.0


def compute_computed_constants(states, rates, constants, computed_constants, algebraic_variables ):
    pass


def compute_rates(voi, states, rates, constants, computed_constants, algebraic_variables):
    find_root_0(voi, states, rates, constants, computed_constants, algebraic_variables)
    rates[0] = algebraic_variables[1]+3.0*algebraic_variables[0]


def compute_variables(voi, states, rates, constants, computed_constants, algebraic_variables):
    find_root_0(voi, states, rates, constants, computed_constants, algebraic_variables)
    find_root_1(voi, states, rates, constants, computed_constants, algebraic_variables)
    find_root_2(voi, states, rates, constants, computed_constants, algebraic_variables)
    find_root_3(voi, states, rates, constants, computed_constants, algebraic_variables)
    find_root_4(voi, states, rates, constants, computed_constants, algebraic_variables)
