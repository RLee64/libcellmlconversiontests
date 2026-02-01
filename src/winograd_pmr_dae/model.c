/* The content of this file was generated using the C profile of libCellML 0.6.3. */

#include "model.h"

#include <math.h>
#include <stdlib.h>

const char VERSION[] = "0.8.0";
const char LIBCELLML_VERSION[] = "0.6.3";

const size_t STATE_COUNT = 7;
const size_t CONSTANT_COUNT = 38;
const size_t COMPUTED_CONSTANT_COUNT = 0;
const size_t ALGEBRAIC_VARIABLE_COUNT = 40;

const VariableInfo VOI_INFO = {"time", "dimensionless", "environment"};

const VariableInfo STATE_INFO[] = {
    {"V", "dimensionless", "membrane"},
    {"h", "dimensionless", "Na_h_gate"},
    {"m", "dimensionless", "Na_m_gate"},
    {"n", "dimensionless", "KD_n_gate"},
    {"p", "dimensionless", "KM_p_gate"},
    {"q", "dimensionless", "CaL_q_gate"},
    {"Ca_i", "dimensionless", "dCa_i_dt"}};

const VariableInfo CONSTANT_INFO[] = {
    {"C_m", "dimensionless", "membrane"},
    {"V_T", "dimensionless", "membrane"},
    {"V_S", "dimensionless", "membrane"},
    {"F", "dimensionless", "membrane"},
    {"R", "dimensionless", "membrane"},
    {"T", "dimensionless", "membrane"},
    {"period", "dimensionless", "stimulus_protocol"},
    {"i_stimAmplitude", "dimensionless", "stimulus_protocol"},
    {"i_stimEnd", "dimensionless", "stimulus_protocol"},
    {"i_stimStart", "dimensionless", "stimulus_protocol"},
    {"E_leak", "dimensionless", "I_leak"},
    {"g_leak", "dimensionless", "I_leak"},
    {"E_Na", "dimensionless", "I_Na"},
    {"g_Na", "dimensionless", "I_Na"},
    {"E_K", "dimensionless", "I_KD"},
    {"g_KD", "dimensionless", "I_KD"},
    {"g_KM", "dimensionless", "I_KM"},
    {"tau_max", "dimensionless", "KM_p_gate"},
    {"P_Ca", "dimensionless", "I_CaL"},
    {"Z", "dimensionless", "G_nonlin"},
    {"Ca_o", "dimensionless", "G_nonlin"},
    {"d", "dimensionless", "dCa_i_dt"},
    {"k", "dimensionless", "dCa_i_dt"},
    {"tau_r", "dimensionless", "dCa_i_dt"},
    {"Ca_inf", "dimensionless", "dCa_i_dt"},
    {"g_inc", "dimensionless", "I_h"},
    {"E_h", "dimensionless", "I_h"},
    {"g_hbar", "dimensionless", "I_h"},
    {"cac", "dimensionless", "I_h"},
    {"V_S", "dimensionless", "I_h"},
    {"k_2", "dimensionless", "rate_constants"},
    {"k_4", "dimensionless", "rate_constants"},
    {"tau_m", "dimensionless", "rate_constants"},
    {"n_Ca", "dimensionless", "rate_constants"},
    {"Ca_c", "dimensionless", "rate_constants"},
    {"n_exp", "dimensionless", "rate_constants"},
    {"p_C", "dimensionless", "rate_constants"},
    {"P_c", "dimensionless", "rate_constants"}};

const VariableInfo COMPUTED_CONSTANT_INFO[1] = {{"IGNORE", "IGNORE", "IGNORE"}};

const VariableInfo ALGEBRAIC_INFO[] = {
    {"I_h", "dimensionless", "I_h"},                 // 0
    {"I_CaL", "dimensionless", "I_CaL"},             // 1
    {"I_KM", "dimensionless", "I_KM"},               // 2
    {"I_KD", "dimensionless", "I_KD"},               // 3
    {"I_Na", "dimensionless", "I_Na"},               // 4
    {"I_leak", "dimensionless", "I_leak"},           // 5
    {"I_app", "dimensionless", "stimulus_protocol"}, // 6
    {"tau", "dimensionless", "stimulus_protocol"},   // 7
    {"alpha", "dimensionless", "Na_m_gate"},         // 8
    {"beta", "dimensionless", "Na_m_gate"},          // 9
    {"tau_m", "dimensionless", "Na_m_gate"},         // 10
    {"m_inf", "dimensionless", "Na_m_gate"},         // 11
    {"alpha_h", "dimensionless", "Na_h_gate"},       // 12
    {"beta_h", "dimensionless", "Na_h_gate"},        // 13
    {"tau_h", "dimensionless", "Na_h_gate"},         // 14
    {"h_inf", "dimensionless", "Na_h_gate"},         // 15
    {"alpha_n", "dimensionless", "KD_n_gate"},       // 16
    {"beta_n", "dimensionless", "KD_n_gate"},        // 17
    {"tau_n", "dimensionless", "KD_n_gate"},         // 18
    {"n_inf", "dimensionless", "KD_n_gate"},         // 19
    {"p_inf", "dimensionless", "KM_p_gate"},         // 20
    {"tau_p", "dimensionless", "KM_p_gate"},         // 21
    {"G", "dimensionless", "G_nonlin"},              // 22
    {"alpha_q", "dimensionless", "CaL_q_gate"},      // 23
    {"beta_q", "dimensionless", "CaL_q_gate"},       // 24
    {"tau_q", "dimensionless", "CaL_q_gate"},        // 25
    {"q_inf", "dimensionless", "CaL_q_gate"},        // 26
    {"drive_channel", "dimensionless", "dCa_i_dt"},  // 27
    {"o_2", "dimensionless", "kinetic"},             // 28
    {"o_1", "dimensionless", "kinetic"},             // 29
    {"m", "dimensionless", "I_h"},                   // 30
    {"k_1Ca", "dimensionless", "rate_constants"},
    {"p_1", "dimensionless", "kinetic"},
    {"p_0", "dimensionless", "kinetic"},
    {"alpha", "dimensionless", "rate_constants"},
    {"beta", "dimensionless", "rate_constants"},
    {"c_1", "dimensionless", "kinetic"},
    {"k_3p", "dimensionless", "rate_constants"},
    {"h_inf", "dimensionless", "rate_constants"},
    {"tau_s", "dimensionless", "rate_constants"}};

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

    algebraicVariables[32] = u[0];
    algebraicVariables[33] = u[1];

    f[0] = algebraicVariables[32] - (1.0 - algebraicVariables[33]);
    f[1] = algebraicVariables[33] - (algebraicVariables[32] * constants[30] / algebraicVariables[31]);
}

void findRoot0(double voi, double *states, double *rates, double *constants, double *computedConstants, double *algebraicVariables)
{
    RootFindingInfo rfi = {voi, states, rates, constants, computedConstants, algebraicVariables};
    double u[2];

    u[0] = algebraicVariables[32];
    u[1] = algebraicVariables[33];

    nlaSolve(objectiveFunction0, u, 2, &rfi);

    algebraicVariables[32] = u[0];
    algebraicVariables[33] = u[0];
}

void objectiveFunction1(double *u, double *f, void *data)
{
    double voi = ((RootFindingInfo *)data)->voi;
    double *states = ((RootFindingInfo *)data)->states;
    double *rates = ((RootFindingInfo *)data)->rates;
    double *constants = ((RootFindingInfo *)data)->constants;
    double *computedConstants = ((RootFindingInfo *)data)->computedConstants;
    double *algebraicVariables = ((RootFindingInfo *)data)->algebraicVariables;

    algebraicVariables[28] = u[0];
    algebraicVariables[29] = u[1];
    algebraicVariables[36] = u[2];

    f[0] = algebraicVariables[28] - (1.0 - algebraicVariables[36] - algebraicVariables[29]);
    f[1] = algebraicVariables[29] - (constants[31] / algebraicVariables[37] * algebraicVariables[28]);
    f[2] = algebraicVariables[36] - (algebraicVariables[35] / algebraicVariables[34] * algebraicVariables[29]);
}

void findRoot1(double voi, double *states, double *rates, double *constants, double *computedConstants, double *algebraicVariables)
{
    RootFindingInfo rfi = {voi, states, rates, constants, computedConstants, algebraicVariables};
    double u[3];

    u[0] = algebraicVariables[28];
    u[1] = algebraicVariables[29];
    u[2] = algebraicVariables[36];

    nlaSolve(objectiveFunction1, u, 3, &rfi);

    algebraicVariables[28] = u[0];
    algebraicVariables[29] = u[1];
    algebraicVariables[36] = u[2];
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
    constants[0] = 1.0e-3;
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
    algebraicVariables[28] = 0.0;
    algebraicVariables[32] = 0.0;
}

void computeComputedConstants(double voi, double *states, double *rates, double *constants, double *computedConstants, double *algebraicVariables)
{
}

void computeRates(double voi, double *states, double *rates, double *constants, double *computedConstants, double *algebraicVariables)
{
    algebraicVariables[2] = 1000.0 * constants[16] * states[4] * (states[0] - constants[14]);
    algebraicVariables[3] = 1000.0 * constants[15] * pow(states[3], 4.0) * (states[0] - constants[14]);
    algebraicVariables[4] = 1000.0 * constants[13] * pow(states[2], 3.0) * states[1] * (states[0] - constants[12]);
    algebraicVariables[5] = 1000.0 * constants[11] * (states[0] - constants[10]);
    algebraicVariables[7] = voi - constants[6] * floor(voi / constants[6]);
    algebraicVariables[6] = ((algebraicVariables[7] >= constants[9]) && (algebraicVariables[7] <= constants[8])) ? constants[7] : 0.0;
    algebraicVariables[22] = pow(constants[19], 2.0) * pow(constants[3], 2.0) * 1.0e-3 * states[0] / (constants[4] * constants[5]) * 1.0e-6 * (states[6] - constants[20] * exp(constants[19] * constants[3] * 1.0e-3 * states[0] / (constants[4] * constants[5]))) / (1.0 - exp(1.0e-3 * constants[19] * constants[3] * states[0] / (constants[4] * constants[5])));
    algebraicVariables[1] = 1000.0 * constants[18] * pow(states[5], 2.0) * algebraicVariables[22];
    algebraicVariables[31] = constants[30] * pow(states[6] / constants[34], constants[33]);
    findRoot0(voi, states, rates, constants, computedConstants, algebraicVariables);
    algebraicVariables[37] = constants[31] * pow(algebraicVariables[32] / constants[36], constants[35]);
    algebraicVariables[39] = constants[32] + 1000.0 / (exp((states[0] + 71.55 - constants[29]) / 14.2) + exp(-(states[0] + 89.0 - constants[29]) / 11.6));
    algebraicVariables[38] = 1.0 / (1.0 + exp((states[0] + 75.0 - constants[29]) / 5.5));
    algebraicVariables[34] = algebraicVariables[38] / algebraicVariables[39];
    algebraicVariables[35] = (1.0 - algebraicVariables[38]) / algebraicVariables[39];
    findRoot1(voi, states, rates, constants, computedConstants, algebraicVariables);
    algebraicVariables[30] = algebraicVariables[29] + constants[25] + algebraicVariables[28];
    algebraicVariables[0] = 1000.0 * constants[27] * algebraicVariables[30] * (states[0] - constants[26]);
    rates[0] = 1.0e-3 * (algebraicVariables[6] + -algebraicVariables[5] - algebraicVariables[4] - algebraicVariables[3] - algebraicVariables[2] - algebraicVariables[1] - algebraicVariables[0]) / constants[0];
    algebraicVariables[9] = (fabs(-(states[0] - constants[1] - 40.0) / 5.0) < 1.0e-6) ? -0.28 * 5.0 * (1.0 - (-(states[0] - constants[1] - 40.0) / (2.0 * 5.0))) : -0.28 * (states[0] - constants[1] - 40.0) / (exp(-(states[0] - constants[1] - 40.0) / 5.0) - 1.0);
    algebraicVariables[8] = (fabs((13.0 + constants[1] - states[0]) / 4.0) < 1.0e-6) ? 0.32 * 4.0 * (1.0 - (13.0 + constants[1] - states[0]) / (2.0 * 4.0)) : 0.32 * (13.0 + constants[1] - states[0]) / (exp((13.0 + constants[1] - states[0]) / 4.0) - 1.0);
    algebraicVariables[10] = 1.0 / (algebraicVariables[8] + algebraicVariables[9]);
    algebraicVariables[11] = algebraicVariables[8] / (algebraicVariables[8] + algebraicVariables[9]);
    rates[2] = (algebraicVariables[11] - states[2]) / algebraicVariables[10];
    algebraicVariables[13] = 4.0 / (1.0 + exp((40.0 + constants[2] + constants[1] - states[0]) / 5.0));
    algebraicVariables[12] = 0.128 * exp((17.0 + constants[1] + constants[2] - states[0]) / 18.0);
    algebraicVariables[14] = 1.0 / (algebraicVariables[12] + algebraicVariables[13]);
    algebraicVariables[15] = algebraicVariables[12] / (algebraicVariables[12] + algebraicVariables[13]);
    rates[1] = (algebraicVariables[15] - states[1]) / algebraicVariables[14];
    algebraicVariables[17] = (fabs(-(states[0] - constants[1] - 10.0) / 40.0) < 1.0e-6) ? 0.5 * 40.0 * (1.0 + (states[0] - constants[1] - 10.0) / (2.0 * 40.0)) : 0.5 * -(states[0] - constants[1] - 10.0) / (exp(-(states[0] - constants[1] - 10.0) / 40.0) - 1.0);
    algebraicVariables[16] = (fabs((states[0] - constants[1] - 15.0) / 5.0) < 1.0e-6) ? -0.032 * 5.0 * (1.0 - (states[0] - constants[1] - 15.0) / (2.0 * 5.0)) : -0.032 * (states[0] - constants[1] - 15.0) / (exp((states[0] - constants[1] - 15.0) / 5.0) - 1.0);
    algebraicVariables[18] = 1.0 / (algebraicVariables[16] + algebraicVariables[17]);
    algebraicVariables[19] = algebraicVariables[16] / (algebraicVariables[16] + algebraicVariables[17]);
    rates[3] = (algebraicVariables[19] - states[3]) / algebraicVariables[18];
    algebraicVariables[21] = (((states[0] + 35.0) / 20.0 < 25.0) && ((states[0] + 35.0) / 20.0 > -25.0)) ? constants[17] / (3.3 * exp((states[0] + 35.0) / 20.0) + exp(-(states[0] + 35.0) / 20.0)) : 1.0;
    algebraicVariables[20] = ((-(states[0] + 35.0) / 10.0 < 25.0) && (-(states[0] + 35.0) / 10.0 > -25.0)) ? 1.0 / (1.0 + exp(-(states[0] + 35.0) / 10.0)) : 1.0;
    rates[4] = (algebraicVariables[20] - states[4]) / algebraicVariables[21];
    algebraicVariables[24] = (fabs((1.31 - states[0]) / 5.36) < 1.0e-6) ? 0.02 * (5.36 + (1.31 - states[0]) / 2.0) : 0.02 * (1.31 - states[0]) / (1.0 - exp((states[0] - 1.31) / 5.36));
    algebraicVariables[23] = 6.32 / (1.0 + exp(-(states[0] - 5.0) / 13.89));
    algebraicVariables[25] = 1.0 / (algebraicVariables[23] + algebraicVariables[24]);
    algebraicVariables[26] = 1.0 / (1.0 + exp((states[0] + 10.0) / -10.0));
    rates[5] = (algebraicVariables[26] - states[5]) / algebraicVariables[25];
    algebraicVariables[27] = constants[22] * algebraicVariables[1] / (2.0 * constants[3] * constants[21]);
    rates[6] = (algebraicVariables[27] <= 0.0) ? (constants[24] - states[6]) / constants[23] : algebraicVariables[27] + (constants[24] - states[6]) / constants[23];
}

void computeVariables(double voi, double *states, double *rates, double *constants, double *computedConstants, double *algebraicVariables)
{
    algebraicVariables[5] = 1000.0 * constants[11] * (states[0] - constants[10]);
    algebraicVariables[4] = 1000.0 * constants[13] * pow(states[2], 3.0) * states[1] * (states[0] - constants[12]);
    algebraicVariables[8] = (fabs((13.0 + constants[1] - states[0]) / 4.0) < 1.0e-6) ? 0.32 * 4.0 * (1.0 - (13.0 + constants[1] - states[0]) / (2.0 * 4.0)) : 0.32 * (13.0 + constants[1] - states[0]) / (exp((13.0 + constants[1] - states[0]) / 4.0) - 1.0);
    algebraicVariables[9] = (fabs(-(states[0] - constants[1] - 40.0) / 5.0) < 1.0e-6) ? -0.28 * 5.0 * (1.0 - (-(states[0] - constants[1] - 40.0) / (2.0 * 5.0))) : -0.28 * (states[0] - constants[1] - 40.0) / (exp(-(states[0] - constants[1] - 40.0) / 5.0) - 1.0);
    algebraicVariables[10] = 1.0 / (algebraicVariables[8] + algebraicVariables[9]);
    algebraicVariables[11] = algebraicVariables[8] / (algebraicVariables[8] + algebraicVariables[9]);
    algebraicVariables[12] = 0.128 * exp((17.0 + constants[1] + constants[2] - states[0]) / 18.0);
    algebraicVariables[13] = 4.0 / (1.0 + exp((40.0 + constants[2] + constants[1] - states[0]) / 5.0));
    algebraicVariables[14] = 1.0 / (algebraicVariables[12] + algebraicVariables[13]);
    algebraicVariables[15] = algebraicVariables[12] / (algebraicVariables[12] + algebraicVariables[13]);
    algebraicVariables[3] = 1000.0 * constants[15] * pow(states[3], 4.0) * (states[0] - constants[14]);
    algebraicVariables[16] = (fabs((states[0] - constants[1] - 15.0) / 5.0) < 1.0e-6) ? -0.032 * 5.0 * (1.0 - (states[0] - constants[1] - 15.0) / (2.0 * 5.0)) : -0.032 * (states[0] - constants[1] - 15.0) / (exp((states[0] - constants[1] - 15.0) / 5.0) - 1.0);
    algebraicVariables[17] = (fabs(-(states[0] - constants[1] - 10.0) / 40.0) < 1.0e-6) ? 0.5 * 40.0 * (1.0 + (states[0] - constants[1] - 10.0) / (2.0 * 40.0)) : 0.5 * -(states[0] - constants[1] - 10.0) / (exp(-(states[0] - constants[1] - 10.0) / 40.0) - 1.0);
    algebraicVariables[18] = 1.0 / (algebraicVariables[16] + algebraicVariables[17]);
    algebraicVariables[19] = algebraicVariables[16] / (algebraicVariables[16] + algebraicVariables[17]);
    algebraicVariables[2] = 1000.0 * constants[16] * states[4] * (states[0] - constants[14]);
    algebraicVariables[20] = ((-(states[0] + 35.0) / 10.0 < 25.0) && (-(states[0] + 35.0) / 10.0 > -25.0)) ? 1.0 / (1.0 + exp(-(states[0] + 35.0) / 10.0)) : 1.0;
    algebraicVariables[21] = (((states[0] + 35.0) / 20.0 < 25.0) && ((states[0] + 35.0) / 20.0 > -25.0)) ? constants[17] / (3.3 * exp((states[0] + 35.0) / 20.0) + exp(-(states[0] + 35.0) / 20.0)) : 1.0;
    algebraicVariables[22] = pow(constants[19], 2.0) * pow(constants[3], 2.0) * 1.0e-3 * states[0] / (constants[4] * constants[5]) * 1.0e-6 * (states[6] - constants[20] * exp(constants[19] * constants[3] * 1.0e-3 * states[0] / (constants[4] * constants[5]))) / (1.0 - exp(1.0e-3 * constants[19] * constants[3] * states[0] / (constants[4] * constants[5])));
    algebraicVariables[1] = 1000.0 * constants[18] * pow(states[5], 2.0) * algebraicVariables[22];
    algebraicVariables[23] = 6.32 / (1.0 + exp(-(states[0] - 5.0) / 13.89));
    algebraicVariables[24] = (fabs((1.31 - states[0]) / 5.36) < 1.0e-6) ? 0.02 * (5.36 + (1.31 - states[0]) / 2.0) : 0.02 * (1.31 - states[0]) / (1.0 - exp((states[0] - 1.31) / 5.36));
    algebraicVariables[25] = 1.0 / (algebraicVariables[23] + algebraicVariables[24]);
    algebraicVariables[26] = 1.0 / (1.0 + exp((states[0] + 10.0) / -10.0));
    algebraicVariables[27] = constants[22] * algebraicVariables[1] / (2.0 * constants[3] * constants[21]);
    algebraicVariables[31] = constants[30] * pow(states[6] / constants[34], constants[33]);
    algebraicVariables[33] = algebraicVariables[32] * constants[30] / algebraicVariables[31];
    findRoot0(voi, states, rates, constants, computedConstants, algebraicVariables);
    algebraicVariables[37] = constants[31] * pow(algebraicVariables[32] / constants[36], constants[35]);
    algebraicVariables[29] = constants[31] / algebraicVariables[37] * algebraicVariables[28];
    algebraicVariables[39] = constants[32] + 1000.0 / (exp((states[0] + 71.55 - constants[29]) / 14.2) + exp(-(states[0] + 89.0 - constants[29]) / 11.6));
    algebraicVariables[38] = 1.0 / (1.0 + exp((states[0] + 75.0 - constants[29]) / 5.5));
    algebraicVariables[34] = algebraicVariables[38] / algebraicVariables[39];
    algebraicVariables[35] = (1.0 - algebraicVariables[38]) / algebraicVariables[39];
    algebraicVariables[36] = algebraicVariables[35] / algebraicVariables[34] * algebraicVariables[29];
    findRoot1(voi, states, rates, constants, computedConstants, algebraicVariables);
    algebraicVariables[30] = algebraicVariables[29] + constants[25] + algebraicVariables[28];
    algebraicVariables[0] = 1000.0 * constants[27] * algebraicVariables[30] * (states[0] - constants[26]);
}
