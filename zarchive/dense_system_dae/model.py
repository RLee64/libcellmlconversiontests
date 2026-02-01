# The content of this file was generated using the Python profile of libCellML 0.6.3.

from enum import Enum
from math import *


__version__ = "0.6.0"
LIBCELLML_VERSION = "0.6.3"

STATE_COUNT = 1
CONSTANT_COUNT = 0
COMPUTED_CONSTANT_COUNT = 0
ALGEBRAIC_VARIABLE_COUNT = 5

VOI_INFO = {"name": "t", "units": "dimensionless", "component": "algebraic_component"}

STATE_INFO = [
    {"name": "x", "units": "dimensionless", "component": "algebraic_component"}
]

CONSTANT_INFO = [
]

COMPUTED_CONSTANT_INFO = [
]

ALGEBRAIC_INFO = [
    {"name": "e", "units": "dimensionless", "component": "algebraic_component"},
    {"name": "d", "units": "dimensionless", "component": "algebraic_component"},
    {"name": "c", "units": "dimensionless", "component": "algebraic_component"},
    {"name": "b", "units": "dimensionless", "component": "algebraic_component"},
    {"name": "a", "units": "dimensionless", "component": "algebraic_component"}
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

    algebraicVariables[0] = u[0]
    algebraicVariables[1] = u[1]
    algebraicVariables[2] = u[2]
    algebraicVariables[3] = u[3]
    algebraicVariables[4] = u[4]

    f[0] = algebraicVariables[4]+2.0*algebraicVariables[3]+3.0*algebraicVariables[2]+4.0*algebraicVariables[1]+5.0*algebraicVariables[0]+states[0]-0.0
    f[1] = algebraicVariables[4]+algebraicVariables[3]+algebraicVariables[2]+algebraicVariables[1]+algebraicVariables[0]+-states[0]-0.0
    f[2] = 4.0*algebraicVariables[4]+-3.0*algebraicVariables[3]+2.0*algebraicVariables[2]+-1.0*algebraicVariables[1]+algebraicVariables[0]+voi-0.0
    f[3] = algebraicVariables[4]+4.0*algebraicVariables[3]+-2.0*algebraicVariables[2]+3.0*algebraicVariables[1]+-1.0*algebraicVariables[0]-0.0
    f[4] = -9.0*algebraicVariables[4]+-2.0*algebraicVariables[3]+1.0*algebraicVariables[2]+1.0*algebraicVariables[1]+3.0*algebraicVariables[0]-0.0


def find_root_0(voi, states, rates, constants, computed_constants, algebraic_variables):
    u = [nan]*5

    u[0] = algebraicVariables[0]
    u[1] = algebraicVariables[1]
    u[2] = algebraicVariables[2]
    u[3] = algebraicVariables[3]
    u[4] = algebraicVariables[4]

    u = nla_solve(objective_function_0, u, 5, [voi, states, rates, constants, computed_constants, algebraic_variables])

    algebraicVariables[0] = u[0]
    algebraicVariables[1] = u[1]
    algebraicVariables[2] = u[2]
    algebraicVariables[3] = u[3]
    algebraicVariables[4] = u[4]


def initialise_arrays(states, rates, constants, computed_constants, algebraic_variables):
    states[0] = 0.0
    algebraicVariables[0] = 0.0
    algebraicVariables[1] = 0.0
    algebraicVariables[2] = 0.0
    algebraicVariables[3] = 0.0
    algebraicVariables[4] = 0.0


def compute_computed_constants(states, rates, constants, computed_constants, algebraic):
    pass


def compute_rates(voi, states, rates, constants, computed_constants, algebraic_variables):
    find_root_0(voi, states, rates, constants, computed_constants, algebraic_variables)
    rates[0] = algebraicVariables[4]+3.0*algebraicVariables[3]+-algebraicVariables[2]+2.0*algebraicVariables[1]+-algebraicVariables[0]


def compute_variables(voi, states, rates, constants, computed_constants, algebraic_variables):
    find_root_0(voi, states, rates, constants, computed_constants, algebraic_variables)
