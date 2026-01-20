/* The content of this file was generated using the C profile of libCellML 0.6.3. */

#include "model.h"

#include <math.h>
#include <stdlib.h>

const char VERSION[] = "0.7.0";
const char LIBCELLML_VERSION[] = "0.6.3";

const size_t STATE_COUNT = 7;
const size_t CONSTANT_COUNT = 38;
const size_t COMPUTED_CONSTANT_COUNT = 0;
const size_t ALGEBRAIC_VARIABLE_COUNT = 40;

const VariableInfo VOI_INFO = {"time", "second", "environment"};

const VariableInfo STATE_INFO[] = {
    {"V", "millivolt", "membrane"},
    {"h", "dimensionless", "Na_h_gate"},
    {"m", "dimensionless", "Na_m_gate"},
    {"n", "dimensionless", "KD_n_gate"},
    {"p", "dimensionless", "KM_p_gate"},
    {"q", "dimensionless", "CaL_q_gate"},
    {"Ca_i", "mM", "dCa_i_dt"}};

const VariableInfo CONSTANT_INFO[] = {
    {"C_m", "mF_per_cm_squared", "membrane"},
    {"V_T", "millivolt", "membrane"},
    {"V_S", "millivolt", "membrane"},
    {"F", "coulomb_per_mole", "membrane"},
    {"R", "joule_per_mole_per_kelvin", "membrane"},
    {"T", "kelvin", "membrane"},
    {"period", "second", "stimulus_protocol"},
    {"i_stimAmplitude", "milliampere_per_cm_squared", "stimulus_protocol"},
    {"i_stimEnd", "second", "stimulus_protocol"},
    {"i_stimStart", "second", "stimulus_protocol"},
    {"E_leak", "millivolt", "I_leak"},
    {"g_leak", "millisiemens_per_cm_squared", "I_leak"},
    {"E_Na", "millivolt", "I_Na"},
    {"g_Na", "millisiemens_per_cm_squared", "I_Na"},
    {"E_K", "millivolt", "I_KD"},
    {"g_KD", "millisiemens_per_cm_squared", "I_KD"},
    {"g_KM", "millisiemens_per_cm_squared", "I_KM"},
    {"tau_max", "second", "KM_p_gate"},
    {"P_Ca", "cm_per_second", "I_CaL"},
    {"Z", "dimensionless", "G_nonlin"},
    {"Ca_o", "mM", "G_nonlin"},
    {"d", "centimeter", "dCa_i_dt"},
    {"k", "fixer", "dCa_i_dt"},
    {"tau_r", "second", "dCa_i_dt"},
    {"Ca_inf", "mM", "dCa_i_dt"},
    {"g_inc", "dimensionless", "I_h"},
    {"E_h", "millivolt", "I_h"},
    {"g_hbar", "millisiemens_per_cm_squared", "I_h"},
    {"cac", "mM", "I_h"},
    {"V_S", "millivolt", "I_h"},
    {"k_2", "per_second", "rate_constants"},
    {"k_4", "per_second", "rate_constants"},
    {"tau_m", "second", "rate_constants"},
    {"n_Ca", "dimensionless", "rate_constants"},
    {"Ca_c", "mM", "rate_constants"},
    {"n_exp", "dimensionless", "rate_constants"},
    {"p_C", "dimensionless", "rate_constants"},
    {"P_c", "dimensionless", "rate_constants"}};

const VariableInfo COMPUTED_CONSTANT_INFO[1] = {{"IGNORE", "IGNORE", "IGNORE"}};

const VariableInfo ALGEBRAIC_INFO[] = {
    {"I_h", "milliampere_per_cm_squared", "membrane"},
    {"I_CaL", "milliampere_per_cm_squared", "membrane"},
    {"I_KM", "milliampere_per_cm_squared", "membrane"},
    {"I_KD", "milliampere_per_cm_squared", "membrane"},
    {"I_Na", "milliampere_per_cm_squared", "membrane"},
    {"I_leak", "milliampere_per_cm_squared", "membrane"},
    {"I_app", "milliampere_per_cm_squared", "membrane"},
    {"tau", "second", "stimulus_protocol"},
    {"alpha", "per_second", "Na_m_gate"},
    {"beta", "per_second", "Na_m_gate"},
    {"tau_m", "second", "Na_m_gate"},
    {"m_inf", "dimensionless", "Na_m_gate"},
    {"alpha_h", "per_second", "Na_h_gate"},
    {"beta_h", "per_second", "Na_h_gate"},
    {"tau_h", "second", "Na_h_gate"},
    {"h_inf", "dimensionless", "Na_h_gate"},
    {"alpha_n", "per_second", "KD_n_gate"},
    {"beta_n", "per_second", "KD_n_gate"},
    {"tau_n", "second", "KD_n_gate"},
    {"n_inf", "dimensionless", "KD_n_gate"},
    {"p_inf", "dimensionless", "KM_p_gate"},
    {"tau_p", "second", "KM_p_gate"},
    {"G", "coulomb_per_cm_cubed", "I_CaL"},
    {"alpha_q", "per_second", "CaL_q_gate"},
    {"beta_q", "per_second", "CaL_q_gate"},
    {"tau_q", "second", "CaL_q_gate"},
    {"q_inf", "dimensionless", "CaL_q_gate"},
    {"drive_channel", "mM_per_second", "dCa_i_dt"},
    {"o_2", "dimensionless", "I_h"},
    {"o_1", "dimensionless", "I_h"},
    {"m", "dimensionless", "I_h"},
    {"k_1Ca", "per_second", "kinetic"},
    {"p_1", "dimensionless", "kinetic"},
    {"p_0", "dimensionless", "kinetic"},
    {"alpha", "dimensionless", "kinetic"},
    {"beta", "dimensionless", "kinetic"},
    {"c_1", "dimensionless", "kinetic"},
    {"k_3p", "per_second", "kinetic"},
    {"h_inf", "second", "rate_constants"},
    {"tau_s", "second", "rate_constants"}};

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
    states[0] = -70.0;
    states[1] = 0.0;
    states[2] = 0.0;
    states[3] = 0.0;
    states[4] = 0.0;
    states[5] = 0.00247262;
    states[6] = 100.0e-6;
    constants[0] = 0.001;
    constants[1] = -55.0;
    constants[2] = 0.0;
    constants[3] = 96489.0;
    constants[4] = 8.314;
    constants[5] = 296.65;
    constants[6] = 9.0;
    constants[7] = -0.3;
    constants[8] = 9.0;
    constants[9] = 5.0;
    constants[10] = -70.0;
    constants[11] = 1.0;
    constants[12] = 50.0;
    constants[13] = 70.0;
    constants[14] = -95.0;
    constants[15] = 7.0;
    constants[16] = 0.004;
    constants[17] = 4.0;
    constants[18] = 2.76e-4;
    constants[19] = 2.0;
    constants[20] = 2.0;
    constants[21] = 1.0e-4;
    constants[22] = 0.1;
    constants[23] = 17.0e-3;
    constants[24] = 100.0e-6;
    constants[25] = 2.0;
    constants[26] = -20.0;
    constants[27] = 0.02;
    constants[28] = 0.006;
    constants[29] = 0.0;
    constants[30] = 0.1;
    constants[31] = 1.0;
    constants[32] = 20.0e-3;
    constants[33] = 4.0;
    constants[34] = 0.006;
    constants[35] = 1.0;
    constants[36] = 0.01;
    constants[37] = 0.01;
}

void computeComputedConstants(double voi, double *states, double *rates, double *constants, double *computedConstants, double *algebraic)
{
}

void computeRates(double voi, double *states, double *rates, double *constants, double *computedConstants, double *algebraicVariables)
{
    algebraicVariables[7] = voi - constants[6] * floor(voi / constants[6]);
    algebraicVariables[6] = ((algebraicVariables[7] >= constants[9]) && (algebraicVariables[7] <= constants[8])) ? constants[7] : 0.0;
    algebraicVariables[5] = 1000.0 * constants[11] * (states[0] - constants[10]);
    algebraicVariables[4] = 1000.0 * constants[13] * pow(states[2], 3.0) * states[1] * (states[0] - constants[12]);
    algebraicVariables[3] = 1000.0 * constants[15] * pow(states[3], 4.0) * (states[0] - constants[14]);
    algebraicVariables[2] = 1000.0 * constants[16] * states[4] * (states[0] - constants[14]);
    algebraicVariables[32] = pow(pow(states[6], constants[33]) + pow(constants[34], constants[33]), -1.0) * pow(states[6], constants[33]);
    algebraicVariables[29] = pow(constants[36], constants[35]) * pow(pow(algebraicVariables[32], constants[35]) - pow(constants[36], constants[35]) * (-1.0 - pow(2.71828182845905, 0.181818181818182 * (75.0 + states[0] - constants[29]))), -1.0);
    algebraicVariables[37] = constants[31] * pow(algebraicVariables[32] / constants[36], constants[35]);
    algebraicVariables[28] = algebraicVariables[29] * pow(constants[31], -1.0) * algebraicVariables[37];
    algebraicVariables[30] = algebraicVariables[29] + constants[25] + algebraicVariables[28];
    algebraicVariables[0] = 1000.0 * constants[27] * algebraicVariables[30] * (states[0] - constants[26]);
    algebraicVariables[22] = pow(constants[19], 2.0) * pow(constants[3], 2.0) * 0.001 * states[0] / (constants[4] * constants[5]) * 0.000001 * (states[6] - constants[20] * exp(constants[19] * constants[3] * 0.001 * states[0] / (constants[4] * constants[5]))) / (1.0 - exp(0.001 * constants[19] * constants[3] * states[0] / (constants[4] * constants[5])));
    algebraicVariables[1] = 1000.0 * constants[18] * pow(states[5], 2.0) * algebraicVariables[22];
    rates[0] = 0.001 * (algebraicVariables[6] + -algebraicVariables[5] - algebraicVariables[4] - algebraicVariables[3] - algebraicVariables[2] - algebraicVariables[1] - algebraicVariables[0]) / constants[0];
    algebraicVariables[8] = (fabs((13.0 + constants[1] - states[0]) / 4.0) < 0.000001) ? 0.32 * 4.0 * (1.0 - (13.0 + constants[1] - states[0]) / (2.0 * 4.0)) : 0.32 * (13.0 + constants[1] - states[0]) / (exp((13.0 + constants[1] - states[0]) / 4.0) - 1.0);
    algebraicVariables[9] = (fabs(-(states[0] - constants[1] - 40.0) / 5.0) < 0.000001) ? -0.28 * 5.0 * (1.0 - (-(states[0] - constants[1] - 40.0) / (2.0 * 5.0))) : -0.28 * (states[0] - constants[1] - 40.0) / (exp(-(states[0] - constants[1] - 40.0) / 5.0) - 1.0);
    algebraicVariables[10] = 1.0 / (algebraicVariables[8] + algebraicVariables[9]);
    algebraicVariables[11] = algebraicVariables[8] / (algebraicVariables[8] + algebraicVariables[9]);
    rates[2] = (algebraicVariables[11] - states[2]) / algebraicVariables[10];
    algebraicVariables[12] = 0.128 * exp((17.0 + constants[1] + constants[2] - states[0]) / 18.0);
    algebraicVariables[13] = 4.0 / (1.0 + exp((40.0 + constants[2] + constants[1] - states[0]) / 5.0));
    algebraicVariables[14] = 1.0 / (algebraicVariables[12] + algebraicVariables[13]);
    algebraicVariables[15] = algebraicVariables[12] / (algebraicVariables[12] + algebraicVariables[13]);
    rates[1] = (algebraicVariables[15] - states[1]) / algebraicVariables[14];
    algebraicVariables[16] = (fabs((states[0] - constants[1] - 15.0) / 5.0) < 0.000001) ? -0.032 * 5.0 * (1.0 - (states[0] - constants[1] - 15.0) / (2.0 * 5.0)) : -0.032 * (states[0] - constants[1] - 15.0) / (exp((states[0] - constants[1] - 15.0) / 5.0) - 1.0);
    algebraicVariables[17] = (fabs(-(states[0] - constants[1] - 10.0) / 40.0) < 0.000001) ? 0.5 * 40.0 * (1.0 + (states[0] - constants[1] - 10.0) / (2.0 * 40.0)) : 0.5 * -(states[0] - constants[1] - 10.0) / (exp(-(states[0] - constants[1] - 10.0) / 40.0) - 1.0);
    algebraicVariables[18] = 1.0 / (algebraicVariables[16] + algebraicVariables[17]);
    algebraicVariables[19] = algebraicVariables[16] / (algebraicVariables[16] + algebraicVariables[17]);
    rates[3] = (algebraicVariables[19] - states[3]) / algebraicVariables[18];
    algebraicVariables[20] = ((-(states[0] + 35.0) / 10.0 < 25.0) && (-(states[0] + 35.0) / 10.0 > -25.0)) ? 1.0 / (1.0 + exp(-(states[0] + 35.0) / 10.0)) : 1.0;
    algebraicVariables[21] = (((states[0] + 35.0) / 20.0 < 25.0) && ((states[0] + 35.0) / 20.0 > -25.0)) ? constants[17] / (3.3 * exp((states[0] + 35.0) / 20.0) + exp(-(states[0] + 35.0) / 20.0)) : 1.0;
    rates[4] = (algebraicVariables[20] - states[4]) / algebraicVariables[21];
    algebraicVariables[23] = 6.32 / (1.0 + exp(-(states[0] - 5.0) / 13.89));
    algebraicVariables[24] = (fabs((1.31 - states[0]) / 5.36) < 0.000001) ? 0.02 * (5.36 + (1.31 - states[0]) / 2.0) : 0.02 * (1.31 - states[0]) / (1.0 - exp((states[0] - 1.31) / 5.36));
    algebraicVariables[25] = 1.0 / (algebraicVariables[23] + algebraicVariables[24]);
    algebraicVariables[26] = 1.0 / (1.0 + exp((states[0] + 10.0) / -10.0));
    rates[5] = (algebraicVariables[26] - states[5]) / algebraicVariables[25];
    algebraicVariables[27] = constants[22] * algebraicVariables[1] / (2.0 * constants[3] * constants[21]);
    rates[6] = (algebraicVariables[27] <= 0.0) ? (constants[24] - states[6]) / constants[23] : algebraicVariables[27] + (constants[24] - states[6]) / constants[23];
}

void computeVariables(double voi, double *states, double *rates, double *constants, double *computedConstants, double *algebraicVariables)
{
    algebraicVariables[32] = pow(pow(states[6], constants[33]) + pow(constants[34], constants[33]), -1.0) * pow(states[6], constants[33]);
    algebraicVariables[29] = pow(constants[36], constants[35]) * pow(pow(algebraicVariables[32], constants[35]) - pow(constants[36], constants[35]) * (-1.0 - pow(2.71828182845905, 0.181818181818182 * (75.0 + states[0] - constants[29]))), -1.0);
    algebraicVariables[37] = constants[31] * pow(algebraicVariables[32] / constants[36], constants[35]);
    algebraicVariables[28] = algebraicVariables[29] * pow(constants[31], -1.0) * algebraicVariables[37];
    algebraicVariables[30] = algebraicVariables[29] + constants[25] + algebraicVariables[28];
    algebraicVariables[0] = 1000.0 * constants[27] * algebraicVariables[30] * (states[0] - constants[26]);
    algebraicVariables[31] = constants[30] * pow(states[6] / constants[34], constants[33]);
    algebraicVariables[33] = algebraicVariables[32] * constants[30] / algebraicVariables[31];
    algebraicVariables[38] = 1.0 / (1.0 + exp((states[0] + 75.0 - constants[29]) / 5.5));
    algebraicVariables[39] = constants[32] + 1000.0 / (exp((states[0] + 71.55 - constants[29]) / 14.2) + exp(-(states[0] + 89.0 - constants[29]) / 11.6));
    algebraicVariables[34] = algebraicVariables[38] / algebraicVariables[39];
    algebraicVariables[35] = (1.0 - algebraicVariables[38]) / algebraicVariables[39];
    algebraicVariables[36] = algebraicVariables[35] / algebraicVariables[34] * algebraicVariables[29];
}
