# The content of this file was generated using the Python profile of libCellML 0.6.3.

from enum import Enum
from math import *


__version__ = "0.6.0"
LIBCELLML_VERSION = "0.6.3"

STATE_COUNT = 1
CONSTANT_COUNT = 2
COMPUTED_CONSTANT_COUNT = 0
ALGEBRAIC_VARIABLE_COUNT = 3

VOI_INFO = {"name": "time", "units": "second", "component": "environment"}

STATE_INFO = [
    {"name": "s", "units": "dimensionless", "component": "state"}
]

CONSTANT_INFO = [
    {"name": "period", "units": "second", "component": "parameters"},
    {"name": "amp", "units": "dimensionless", "component": "parameters"}
]

COMPUTED_CONSTANT_INFO = [
]

ALGEBRAIC_INFO = [
    {"name": "f", "units": "per_second", "component": "forcing"},
    {"name": "b", "units": "per_second", "component": "algebraic_loop"},
    {"name": "a", "units": "per_second", "component": "algebraic_loop"}
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

    algebraicVariables[1] = u[0]
    algebraicVariables[2] = u[1]

    f[0] = algebraicVariables[2]-(algebraicVariables[1]+algebraicVariables[0])
    f[1] = algebraicVariables[1]-(-algebraicVariables[2])


def find_root_0(voi, states, rates, constants, computed_constants, algebraic_variables):
    u = [nan]*2

    u[0] = algebraicVariables[1]
    u[1] = algebraicVariables[2]

    u = nla_solve(objective_function_0, u, 2, [voi, states, rates, constants, computed_constants, algebraic_variables])

    algebraicVariables[1] = u[0]
    algebraicVariables[2] = u[1]


def initialise_arrays(states, rates, constants, computed_constants, algebraic_variables):
    states[0] = 0.0
    constants[0] = 1.0
    constants[1] = 1.0
    algebraicVariables[1] = 0.0
    algebraicVariables[2] = 0.0


def compute_computed_constants(states, rates, constants, computed_constants, algebraic):
    pass


def compute_rates(voi, states, rates, constants, computed_constants, algebraic_variables):
    algebraicVariables[0] = constants[1]/constants[0]*sin(2.0*3.14159265358979*voi/constants[0])
    find_root_0(voi, states, rates, constants, computed_constants, algebraic_variables)
    rates[0] = algebraicVariables[2]


def compute_variables(voi, states, rates, constants, computed_constants, algebraic_variables):
    pass
