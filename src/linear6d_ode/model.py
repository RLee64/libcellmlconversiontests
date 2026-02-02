# The content of this file was generated using the Python profile of libCellML 0.6.3.

from enum import Enum
from math import *


__version__ = "0.6.0"
LIBCELLML_VERSION = "0.6.3"

STATE_COUNT = 1
CONSTANT_COUNT = 0
COMPUTED_CONSTANT_COUNT = 0
ALGEBRAIC_VARIABLE_COUNT = 6

VOI_INFO = {"name": "t", "units": "dimensionless", "component": "algebraic_component"}

STATE_INFO = [
    {"name": "x", "units": "dimensionless", "component": "algebraic_component"}
]

CONSTANT_INFO = [
]

COMPUTED_CONSTANT_INFO = [
]

ALGEBRAIC_INFO = [
    {"name": "f", "units": "dimensionless", "component": "algebraic_component"},
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


def initialise_arrays(states, rates, constants, computed_constants, algebraic_variables):
    states[0] = 0.0


def compute_computed_constants(states, rates, constants, computed_constants, algebraic):
    pass


def compute_rates(voi, states, rates, constants, computed_constants, algebraic_variables):
    algebraicVariables[0] = 1/1073.0*(-1240.0*states[0]+478.0*voi)
    algebraicVariables[1] = 1/23.0*(-239.0*algebraicVariables[0]+89.0*voi+-238.0*states[0])
    algebraicVariables[2] = -1/20.0*(19.0*algebraicVariables[1]+27.0*algebraicVariables[0]+3.0*voi+34.0*states[0])
    algebraicVariables[3] = -1/12.0*(29.0*algebraicVariables[0]+voi+16.0*algebraicVariables[2]+25.0*algebraicVariables[1]+18.0*states[0])
    algebraicVariables[4] = -5.0*algebraicVariables[0]+-2.0*states[0]+-4.0*algebraicVariables[1]+-3.0*algebraicVariables[2]+-2.0*algebraicVariables[3]
    algebraicVariables[5] = -(6.0*algebraicVariables[0]+states[0]+5.0*algebraicVariables[1]+4.0*algebraicVariables[2]+3.0*algebraicVariables[3]+2.0*algebraicVariables[4])
    rates[0] = algebraicVariables[5]+3.0*algebraicVariables[4]+-algebraicVariables[3]+2.0*algebraicVariables[2]+-algebraicVariables[1]+4.0*algebraicVariables[0]


def compute_variables(voi, states, rates, constants, computed_constants, algebraic_variables):
    algebraicVariables[0] = 1/1073.0*(-1240.0*states[0]+478.0*voi)
    algebraicVariables[1] = 1/23.0*(-239.0*algebraicVariables[0]+89.0*voi+-238.0*states[0])
    algebraicVariables[2] = -1/20.0*(19.0*algebraicVariables[1]+27.0*algebraicVariables[0]+3.0*voi+34.0*states[0])
    algebraicVariables[3] = -1/12.0*(29.0*algebraicVariables[0]+voi+16.0*algebraicVariables[2]+25.0*algebraicVariables[1]+18.0*states[0])
    algebraicVariables[4] = -5.0*algebraicVariables[0]+-2.0*states[0]+-4.0*algebraicVariables[1]+-3.0*algebraicVariables[2]+-2.0*algebraicVariables[3]
    algebraicVariables[5] = -(6.0*algebraicVariables[0]+states[0]+5.0*algebraicVariables[1]+4.0*algebraicVariables[2]+3.0*algebraicVariables[3]+2.0*algebraicVariables[4])
