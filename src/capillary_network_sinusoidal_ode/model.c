/* The content of this file was generated using the C profile of libCellML 0.6.3. */

#include "model.h"

#include <math.h>
#include <stdlib.h>

const char VERSION[] = "0.7.0";
const char LIBCELLML_VERSION[] = "0.6.3";

const size_t STATE_COUNT = 9;
const size_t CONSTANT_COUNT = 34;
const size_t COMPUTED_CONSTANT_COUNT = 15;
const size_t ALGEBRAIC_VARIABLE_COUNT = 10;

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
    {"R_pericyte_0", "Js_per_m6", "parameters"},
    {"C_pericyte_0", "m6_per_J", "parameters"},
    {"u_ext_pericyte_1", "J_per_m3", "parameters"},
    {"R_pericyte_1", "Js_per_m6", "parameters"},
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
    {"u_d", "J_per_m3", "input_vessel_module"},
    {"u", "J_per_m3", "input_vessel_module"},
    {"u_C", "J_per_m3", "input_vessel_module"},
    {"v_out_2", "m3_per_s", "input_vessel_module"},
    {"v_out_1", "m3_per_s", "input_vessel_module"},
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

void initialiseArrays(double *states, double *rates, double *constants, double *computedConstants, double *algebraicVariables)
{
    states[0] = 0.0;
    states[1] = 0.0;
    states[2] = 0.0;
    states[3] = 0.0;
    states[4] = 0.0;
    states[5] = 0.0;
    states[6] = 0.0;
    constants[12] = 1.0e-18;
    states[7] = constants[12];
    constants[19] = 1.0e-18;
    states[8] = constants[19];
    constants[0] = 400000.0;
    constants[1] = 2.0e-05;
    constants[2] = 4.0e-06;
    constants[3] = 0.0;
    constants[4] = 0.0;
    constants[5] = 1.0e-07;
    constants[6] = 0.0;
    constants[7] = 1.0;
    constants[8] = 1.0;
    constants[9] = 0.0;
    constants[10] = 1.0;
    constants[11] = 1.0;
    constants[13] = 400000.0;
    constants[14] = 2.0e-05;
    constants[15] = 2.0e-06;
    constants[16] = 0.0;
    constants[17] = 0.25e-7;
    constants[18] = 0.25e-7;
    constants[20] = 400000.0;
    constants[21] = 2.0e-05;
    constants[22] = 2.0e-06;
    constants[23] = 0.0;
    constants[24] = 0.25e-7;
    constants[25] = 0.25e-7;
    constants[26] = 0.0;
    constants[27] = 1050.0;
    constants[28] = 0.004;
    constants[29] = 9.81;
    constants[30] = 0.2802;
    constants[31] = -505.3;
    constants[32] = 0.1324;
    constants[33] = -11.14;
}

void computeComputedConstants(double voi, double *states, double *rates, double *constants, double *computedConstants, double *algebraic)
{
    computedConstants[0] = constants[2] * (constants[30] * exp(constants[31] * constants[2]) + constants[32] * exp(constants[33] * constants[2]));
    computedConstants[1] = constants[27] * constants[1] / (3.14159265358979 * pow(constants[2], 2.0));
    computedConstants[2] = 2.0 * 3.14159265358979 * pow(constants[2], 3.0) * constants[1] / (constants[0] * computedConstants[0]);
    computedConstants[3] = 8.0 * constants[28] * constants[1] / (3.14159265358979 * pow(constants[2], 4.0));
    computedConstants[4] = 0.01 / computedConstants[2];
    computedConstants[5] = constants[15] * (constants[30] * exp(constants[31] * constants[15]) + constants[32] * exp(constants[33] * constants[15]));
    computedConstants[6] = constants[27] * constants[14] / (3.14159265358979 * pow(constants[15], 2.0));
    computedConstants[7] = 2.0 * 3.14159265358979 * pow(constants[15], 3.0) * constants[14] / (constants[13] * computedConstants[5]);
    computedConstants[8] = 8.0 * constants[28] * constants[14] / (3.14159265358979 * pow(constants[15], 4.0));
    computedConstants[9] = constants[17] + constants[18];
    computedConstants[10] = constants[22] * (constants[30] * exp(constants[31] * constants[22]) + constants[32] * exp(constants[33] * constants[22]));
    computedConstants[11] = constants[27] * constants[21] / (3.14159265358979 * pow(constants[22], 2.0));
    computedConstants[12] = 2.0 * 3.14159265358979 * pow(constants[22], 3.0) * constants[21] / (constants[20] * computedConstants[10]);
    computedConstants[13] = 8.0 * constants[28] * constants[21] / (3.14159265358979 * pow(constants[22], 4.0));
    computedConstants[14] = constants[24] + constants[25];
}

void computeRates(double voi, double *states, double *rates, double *constants, double *computedConstants, double *algebraicVariables)
{
    algebraicVariables[2] = states[1] / (computedConstants[2] / 2.0) + constants[4];
    algebraicVariables[1] = algebraicVariables[2] + 2.0 * computedConstants[4] * (constants[5] - states[0]);
    algebraicVariables[0] = pow(3.14159265358979 * constants[7] * constants[10] * pow(constants[2], 2.0) * constants[8] * constants[11] * constants[1] + -0.01 * (-sin(10000.0 * voi) * constants[10] * constants[8] * constants[11] - sin(10000.0 * voi) * constants[7] * constants[8] * constants[11]) * constants[0] * (pow(2.71828182845905, constants[2] * constants[31]) * constants[30] + pow(2.71828182845905, constants[2] * constants[33]) * constants[32]), -1.0) * (3.14159265358979 * constants[7] * constants[10] * pow(constants[2], 2.0) * constants[8] * constants[11] * constants[4] * constants[1] + 0.01 * constants[0] * (pow(2.71828182845905, constants[2] * constants[31]) * constants[30] + pow(2.71828182845905, constants[2] * constants[33]) * constants[32]) * (sin(10000.0 * voi) * constants[7] * constants[8] * (states[6] + constants[9] * constants[11]) + constants[10] * constants[11] * (sin(10000.0 * voi) * (states[4] + constants[6] * constants[8]) + states[0] * constants[7] * constants[8])) + states[2] * constants[0] * constants[7] * constants[10] * constants[8] * constants[11] * (pow(2.71828182845905, constants[2] * constants[31]) * constants[30] + pow(2.71828182845905, constants[2] * constants[33]) * constants[32]));
    rates[0] = (algebraicVariables[1] - algebraicVariables[0] - computedConstants[3] * states[0] - constants[26] * constants[27] * constants[29] * constants[1] * cos(constants[3] * 3.14159265358979 / 180.0)) / computedConstants[1];
    rates[1] = constants[5] - states[0];
    algebraicVariables[7] = states[6] / constants[11] + constants[9];
    algebraicVariables[3] = (algebraicVariables[0] - algebraicVariables[7]) / constants[10] * sin(10000.0 * voi);
    algebraicVariables[6] = states[4] / constants[8] + constants[6];
    algebraicVariables[4] = (algebraicVariables[0] - algebraicVariables[6]) / constants[7] * sin(10000.0 * voi);
    rates[2] = states[0] - algebraicVariables[4] - algebraicVariables[3];
    rates[4] = algebraicVariables[4] - states[3];
    rates[6] = algebraicVariables[3] - states[5];
    algebraicVariables[8] = states[7] / computedConstants[7] + constants[16];
    rates[3] = (algebraicVariables[6] - algebraicVariables[8] - computedConstants[8] * states[3]) / computedConstants[6];
    rates[7] = states[3] - computedConstants[9];
    algebraicVariables[9] = states[8] / computedConstants[12] + constants[23];
    rates[5] = (algebraicVariables[7] - algebraicVariables[9] - computedConstants[13] * states[5]) / computedConstants[11];
    rates[8] = states[5] - computedConstants[14];
}

void computeVariables(double voi, double *states, double *rates, double *constants, double *computedConstants, double *algebraicVariables)
{
    algebraicVariables[5] = states[2] / (computedConstants[2] / 2.0) + constants[4];
    algebraicVariables[0] = pow(3.14159265358979 * constants[7] * constants[10] * pow(constants[2], 2.0) * constants[8] * constants[11] * constants[1] + -0.01 * (-sin(10000.0 * voi) * constants[10] * constants[8] * constants[11] - sin(10000.0 * voi) * constants[7] * constants[8] * constants[11]) * constants[0] * (pow(2.71828182845905, constants[2] * constants[31]) * constants[30] + pow(2.71828182845905, constants[2] * constants[33]) * constants[32]), -1.0) * (3.14159265358979 * constants[7] * constants[10] * pow(constants[2], 2.0) * constants[8] * constants[11] * constants[4] * constants[1] + 0.01 * constants[0] * (pow(2.71828182845905, constants[2] * constants[31]) * constants[30] + pow(2.71828182845905, constants[2] * constants[33]) * constants[32]) * (sin(10000.0 * voi) * constants[7] * constants[8] * (states[6] + constants[9] * constants[11]) + constants[10] * constants[11] * (sin(10000.0 * voi) * (states[4] + constants[6] * constants[8]) + states[0] * constants[7] * constants[8])) + states[2] * constants[0] * constants[7] * constants[10] * constants[8] * constants[11] * (pow(2.71828182845905, constants[2] * constants[31]) * constants[30] + pow(2.71828182845905, constants[2] * constants[33]) * constants[32]));
    algebraicVariables[4] = (algebraicVariables[0] - algebraicVariables[6]) / constants[7] * sin(10000.0 * voi);
    algebraicVariables[3] = (algebraicVariables[0] - algebraicVariables[7]) / constants[10] * sin(10000.0 * voi);
}
