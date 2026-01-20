/* The content of this file was generated using the C profile of libCellML 0.6.3. */

#include "model.h"

#include <math.h>
#include <stdlib.h>

const char VERSION[] = "0.8.0";
const char LIBCELLML_VERSION[] = "0.6.3";

const size_t STATE_COUNT = 9;
const size_t CONSTANT_COUNT = 32;
const size_t COMPUTED_CONSTANT_COUNT = 15;
const size_t ALGEBRAIC_VARIABLE_COUNT = 12;

const VariableInfo VOI_INFO = {"time", "second", "environment"};

const VariableInfo STATE_INFO[] = {
    {"v", "m3_per_s", "input_vessel_module"},
    {"q_C", "m3", "input_vessel_module"},
    {"q_C_d", "m3", "input_vessel_module"},
    {"v", "m3_per_s", "capillary_0_module"},
    {"q_C", "m3", "pericyte_0_module"},
    {"v", "m3_per_s", "capillary_1_module"},
    {"q_C", "m3", "pericyte_1_module"},
    {"q_C", "m3", "capillary_0_module"},
    {"q_C", "m3", "capillary_1_module"}};

const VariableInfo CONSTANT_INFO[] = {
    {"E_input_vessel", "J_per_m3", "parameters"},
    {"l_input_vessel", "metre", "parameters"},
    {"r_input_vessel", "metre", "parameters"},
    {"theta_input_vessel", "dimensionless", "parameters"},
    {"u_ext_input_vessel", "J_per_m3", "parameters"},
    {"v_in_input_vessel", "m3_per_s", "parameters"},
    {"u_ext_pericyte_0", "J_per_m3", "parameters"},
    {"C_pericyte_0", "m6_per_J", "parameters"},
    {"u_ext_pericyte_1", "J_per_m3", "parameters"},
    {"C_pericyte_1", "m6_per_J", "parameters"},
    {"q_C_init_capillary_0", "m3", "parameters"},
    {"E_capillary_0", "J_per_m3", "parameters"},
    {"l_capillary_0", "metre", "parameters"},
    {"r_capillary_0", "metre", "parameters"},
    {"u_ext_capillary_0", "J_per_m3", "parameters"},
    {"v_out_1_capillary_0", "m3_per_s", "parameters"},
    {"v_out_2_capillary_0", "m3_per_s", "parameters"},
    {"q_C_init_capillary_1", "m3", "parameters"},
    {"E_capillary_1", "J_per_m3", "parameters"},
    {"l_capillary_1", "metre", "parameters"},
    {"r_capillary_1", "metre", "parameters"},
    {"u_ext_capillary_1", "J_per_m3", "parameters"},
    {"v_out_1_capillary_1", "m3_per_s", "parameters"},
    {"v_out_2_capillary_1", "m3_per_s", "parameters"},
    {"beta_g", "dimensionless", "parameters_global"},
    {"rho", "kg_per_m3", "parameters_global"},
    {"mu", "Js_per_m3", "parameters_global"},
    {"g", "m_per_s2", "parameters_global"},
    {"a_vessel", "dimensionless", "parameters_global"},
    {"b_vessel", "per_m", "parameters_global"},
    {"c_vessel", "dimensionless", "parameters_global"},
    {"d_vessel", "per_m", "parameters_global"}};

const VariableInfo COMPUTED_CONSTANT_INFO[] = {
    {"h", "metre", "input_vessel_module"},
    {"I", "Js2_per_m6", "input_vessel_module"},
    {"C", "m6_per_J", "input_vessel_module"},
    {"R", "Js_per_m6", "input_vessel_module"},
    {"R_v", "Js_per_m6", "input_vessel_module"},
    {"h", "metre", "capillary_0_module"},
    {"I", "Js2_per_m6", "capillary_0_module"},
    {"C", "m6_per_J", "capillary_0_module"},
    {"R", "Js_per_m6", "capillary_0_module"},
    {"v_out_total", "m3_per_s", "capillary_0_module"},
    {"h", "metre", "capillary_1_module"},
    {"I", "Js2_per_m6", "capillary_1_module"},
    {"C", "m6_per_J", "capillary_1_module"},
    {"R", "Js_per_m6", "capillary_1_module"},
    {"v_out_total", "m3_per_s", "capillary_1_module"}};

const VariableInfo ALGEBRAIC_INFO[] = {
    {"R", "Js_per_m6", "pericyte_0_module"},
    {"R", "Js_per_m6", "pericyte_1_module"},
    {"u_in", "J_per_m3", "pericyte_1_module"},
    {"u", "J_per_m3", "input_vessel_module"},
    {"u_C", "J_per_m3", "input_vessel_module"},
    {"v", "m3_per_s", "pericyte_1_module"},
    {"v", "m3_per_s", "pericyte_0_module"},
    {"u_C_d", "J_per_m3", "input_vessel_module"},
    {"u", "J_per_m3", "pericyte_0_module"},
    {"u", "J_per_m3", "pericyte_1_module"},
    {"u", "J_per_m3", "capillary_0_module"},
    {"u", "J_per_m3", "capillary_1_module"}};

double *createStatesArray()
{
    double *res = (double *)malloc(STATE_COUNT * sizeof(double));

    for (size_t i = 0; i < STATE_COUNT; ++i)
    {
        res[i] = NAN;
    }

    return res;
}

double *createConstantsArray()
{
    double *res = (double *)malloc(CONSTANT_COUNT * sizeof(double));

    for (size_t i = 0; i < CONSTANT_COUNT; ++i)
    {
        res[i] = NAN;
    }

    return res;
}

double *createComputedConstantsArray()
{
    double *res = (double *)malloc(COMPUTED_CONSTANT_COUNT * sizeof(double));

    for (size_t i = 0; i < COMPUTED_CONSTANT_COUNT; ++i)
    {
        res[i] = NAN;
    }

    return res;
}

double *createAlgebraicVariablesArray()
{
    double *res = (double *)malloc(ALGEBRAIC_VARIABLE_COUNT * sizeof(double));

    for (size_t i = 0; i < ALGEBRAIC_VARIABLE_COUNT; ++i)
    {
        res[i] = NAN;
    }

    return res;
}

void deleteArray(double *array)
{
    free(array);
}

typedef struct
{
    double voi;
    double *states;
    double *rates;
    double *constants;
    double *computedConstants;
    double *algebraicVariables;
} RootFindingInfo;

extern void nlaSolve(void (*objectiveFunction)(double *, double *, void *),
                     double *u, size_t n, void *data);

void objectiveFunction0(double *u, double *f, void *data)
{
    double voi = ((RootFindingInfo *)data)->voi;
    double *states = ((RootFindingInfo *)data)->states;
    double *rates = ((RootFindingInfo *)data)->rates;
    double *constants = ((RootFindingInfo *)data)->constants;
    double *computedConstants = ((RootFindingInfo *)data)->computedConstants;
    double *algebraicVariables = ((RootFindingInfo *)data)->algebraicVariables;

    algebraicVariables[5] = u[0];
    algebraicVariables[6] = u[1];
    algebraicVariables[2] = u[2];

    f[0] = algebraicVariables[2] - (algebraicVariables[7] + 2.0 * computedConstants[4] * (states[0] - algebraicVariables[6] - algebraicVariables[5]));
    f[1] = algebraicVariables[6] - (algebraicVariables[2] - algebraicVariables[8]) / algebraicVariables[0];
    f[2] = algebraicVariables[5] - (algebraicVariables[2] - algebraicVariables[9]) / algebraicVariables[1];
}

void findRoot0(double voi, double *states, double *rates, double *constants, double *computedConstants, double *algebraicVariables)
{
    RootFindingInfo rfi = {voi, states, rates, constants, computedConstants, algebraicVariables};
    double u[3];

    u[0] = algebraicVariables[5];
    u[1] = algebraicVariables[6];
    u[2] = algebraicVariables[2];

    nlaSolve(objectiveFunction0, u, 3, &rfi);

    algebraicVariables[5] = u[0];
    algebraicVariables[6] = u[1];
    algebraicVariables[2] = u[2];
}

void initialiseArrays(double *states, double *rates, double *constants, double *computedConstants, double *algebraicVariables)
{
    states[0] = 0.0;
    states[1] = 0.0;
    states[2] = 0.0;
    states[3] = 0.0;
    states[4] = 0.0;
    states[5] = 0.0;
    states[6] = 0.0;
    constants[10] = 1.0e-18;
    states[7] = constants[10];
    constants[17] = 1.0e-18;
    states[8] = constants[17];
    constants[0] = 400000.0;
    constants[1] = 2.0e-05;
    constants[2] = 4.0e-06;
    constants[3] = 0.0;
    constants[4] = 0.0;
    constants[5] = 1.0e-07;
    constants[6] = 0.0;
    constants[7] = 1.0;
    constants[8] = 0.0;
    constants[9] = 1.0;
    constants[11] = 400000.0;
    constants[12] = 2.0e-05;
    constants[13] = 2.0e-06;
    constants[14] = 0.0;
    constants[15] = 0.25e-7;
    constants[16] = 0.25e-7;
    constants[18] = 400000.0;
    constants[19] = 2.0e-05;
    constants[20] = 2.0e-06;
    constants[21] = 0.0;
    constants[22] = 0.25e-7;
    constants[23] = 0.25e-7;
    constants[24] = 0.0;
    constants[25] = 1050.0;
    constants[26] = 0.004;
    constants[27] = 9.81;
    constants[28] = 0.2802;
    constants[29] = -505.3;
    constants[30] = 0.1324;
    constants[31] = -11.14;
    algebraicVariables[0] = 1.0;
    algebraicVariables[1] = 1.0;
    algebraicVariables[2] = 0.0;
    algebraicVariables[5] = 0.0;
    algebraicVariables[6] = 0.0;
}

void computeComputedConstants(double voi, double *states, double *rates, double *constants, double *computedConstants, double *algebraicVariables)
{
    computedConstants[0] = constants[2] * (constants[28] * exp(constants[29] * constants[2]) + constants[30] * exp(constants[31] * constants[2]));
    computedConstants[1] = constants[25] * constants[1] / (3.14159265358979 * pow(constants[2], 2.0));
    computedConstants[2] = 2.0 * 3.14159265358979 * pow(constants[2], 3.0) * constants[1] / (constants[0] * computedConstants[0]);
    computedConstants[3] = 8.0 * constants[26] * constants[1] / (3.14159265358979 * pow(constants[2], 4.0));
    computedConstants[4] = 0.01 / computedConstants[2];
    computedConstants[5] = constants[13] * (constants[28] * exp(constants[29] * constants[13]) + constants[30] * exp(constants[31] * constants[13]));
    computedConstants[6] = constants[25] * constants[12] / (3.14159265358979 * pow(constants[13], 2.0));
    computedConstants[7] = 2.0 * 3.14159265358979 * pow(constants[13], 3.0) * constants[12] / (constants[11] * computedConstants[5]);
    computedConstants[8] = 8.0 * constants[26] * constants[12] / (3.14159265358979 * pow(constants[13], 4.0));
    computedConstants[9] = constants[15] + constants[16];
    computedConstants[10] = constants[20] * (constants[28] * exp(constants[29] * constants[20]) + constants[30] * exp(constants[31] * constants[20]));
    computedConstants[11] = constants[25] * constants[19] / (3.14159265358979 * pow(constants[20], 2.0));
    computedConstants[12] = 2.0 * 3.14159265358979 * pow(constants[20], 3.0) * constants[19] / (constants[18] * computedConstants[10]);
    computedConstants[13] = 8.0 * constants[26] * constants[19] / (3.14159265358979 * pow(constants[20], 4.0));
    computedConstants[14] = constants[22] + constants[23];
}

void computeRates(double voi, double *states, double *rates, double *constants, double *computedConstants, double *algebraicVariables)
{
    algebraicVariables[4] = states[1] / (computedConstants[2] / 2.0) + constants[4];
    algebraicVariables[3] = algebraicVariables[4] + 2.0 * computedConstants[4] * (constants[5] - states[0]);
    rates[0] = (algebraicVariables[3] - algebraicVariables[2] - computedConstants[3] * states[0] - constants[24] * constants[25] * constants[27] * constants[1] * cos(constants[3] * 3.14159265358979 / 180.0)) / computedConstants[1];
    rates[1] = constants[5] - states[0];
    algebraicVariables[7] = states[2] / (computedConstants[2] / 2.0) + constants[4];
    findRoot0(voi, states, rates, constants, computedConstants, algebraicVariables);
    rates[2] = states[0] - algebraicVariables[6] - algebraicVariables[5];
    rates[4] = algebraicVariables[6] - states[3];
    rates[6] = algebraicVariables[5] - states[5];
    algebraicVariables[8] = states[4] / constants[7] + constants[6];
    algebraicVariables[10] = states[7] / computedConstants[7] + constants[14];
    rates[3] = (algebraicVariables[8] - algebraicVariables[10] - computedConstants[8] * states[3]) / computedConstants[6];
    rates[7] = states[3] - computedConstants[9];
    algebraicVariables[9] = states[6] / constants[9] + constants[8];
    algebraicVariables[11] = states[8] / computedConstants[12] + constants[21];
    rates[5] = (algebraicVariables[9] - algebraicVariables[11] - computedConstants[13] * states[5]) / computedConstants[11];
    rates[8] = states[5] - computedConstants[14];
}

void computeVariables(double voi, double *states, double *rates, double *constants, double *computedConstants, double *algebraicVariables)
{
    algebraicVariables[4] = states[1] / (computedConstants[2] / 2.0) + constants[4];
    algebraicVariables[7] = states[2] / (computedConstants[2] / 2.0) + constants[4];
    algebraicVariables[3] = algebraicVariables[4] + 2.0 * computedConstants[4] * (constants[5] - states[0]);
    findRoot0(voi, states, rates, constants, computedConstants, algebraicVariables);
    algebraicVariables[8] = states[4] / constants[7] + constants[6];
    algebraicVariables[9] = states[6] / constants[9] + constants[8];
    algebraicVariables[10] = states[7] / computedConstants[7] + constants[14];
    algebraicVariables[11] = states[8] / computedConstants[12] + constants[21];
}
