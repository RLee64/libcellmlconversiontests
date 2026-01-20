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


def initialise_arrays(states, rates, constants, computed_constants, algebraic_variables):
    states[0] = 2.0
    computed_constants[0] = 5.0
    computed_constants[1] = 10.0
    computed_constants[2] = 10.0
    computed_constants[3] = 10.0
    computed_constants[4] = 10.0


def compute_computed_constants(states, rates, constants, computed_constants, algebraic):
    pass


def compute_rates(voi, states, rates, constants, computed_constants, algebraic_variables):
    algebraic_variables[1] = -pow(-computed_constants[2]*computed_constants[4]-computed_constants[4]*computed_constants[3], -1.0)*(computed_constants[4]*(computed_constants[1]+computed_constants[2]*computed_constants[0])-states[0])
    rates[0] = algebraic_variables[1]


def compute_variables(voi, states, rates, constants, computed_constants, algebraic_variables):
    algebraic_variables[1] = -pow(-computed_constants[2]*computed_constants[4]-computed_constants[4]*computed_constants[3], -1.0)*(computed_constants[4]*(computed_constants[1]+computed_constants[2]*computed_constants[0])-states[0])
    algebraic_variables[0] = computed_constants[0]-algebraic_variables[1]
    algebraic_variables[2] = algebraic_variables[0]*computed_constants[2]
    algebraic_variables[3] = computed_constants[1]+algebraic_variables[2]
    algebraic_variables[5] = algebraic_variables[1]*computed_constants[3]
    algebraic_variables[4] = states[0]/computed_constants[4]
