# The content of this file was generated using the Python profile of libCellML 0.6.3.

from enum import Enum
from math import *


__version__ = "0.6.0"
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


def initialise_arrays(states, rates, constants, computed_constants, algebraic_variables):
    states[0] = 0.0


def compute_computed_constants(states, rates, constants, computed_constants, algebraic):
    pass


def compute_rates(voi, states, rates, constants, computed_constants, algebraic_variables):
    algebraicVariables[0] = -states[0]-voi
    algebraicVariables[1] = -(2.0*algebraicVariables[0]+voi)
    rates[0] = algebraicVariables[1]+3.0*algebraicVariables[0]


def compute_variables(voi, states, rates, constants, computed_constants, algebraic_variables):
    algebraicVariables[0] = -states[0]-voi
    algebraicVariables[1] = -(2.0*algebraicVariables[0]+voi)
    algebraicVariables[2] = -voi-states[0]
    algebraicVariables[3] = -(voi+2.0*algebraicVariables[2])
    algebraicVariables[4] = -states[0]-voi
    algebraicVariables[5] = -(2.0*algebraicVariables[4]+voi)
    algebraicVariables[6] = -states[0]-voi
    algebraicVariables[7] = -(2.0*algebraicVariables[6]+voi)
    algebraicVariables[8] = -states[0]-voi
    algebraicVariables[9] = -(2.0*algebraicVariables[8]+voi)
