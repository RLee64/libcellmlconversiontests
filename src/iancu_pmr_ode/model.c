/* The content of this file was generated using the C profile of libCellML 0.6.3. */

#include "model.h"

#include <math.h>
#include <stdlib.h>

const char VERSION[] = "0.7.0";
const char LIBCELLML_VERSION[] = "0.6.3";

const size_t STATE_COUNT = 15;
const size_t CONSTANT_COUNT = 55;
const size_t COMPUTED_CONSTANT_COUNT = 4;
const size_t ALGEBRAIC_VARIABLE_COUNT = 34;

const VariableInfo VOI_INFO = {"time", "second", "environment"};

const VariableInfo STATE_INFO[] = {
    {"Gs_alpha_GTP", "uM", "caveolar_G_s_protein_activation_module"},
    {"Gs_beta_gamma", "uM", "caveolar_G_s_protein_activation_module"},
    {"Gs_alpha_GDP", "uM", "caveolar_G_s_protein_activation_module"},
    {"Gi_alpha_GTP", "uM", "caveolar_G_i_protein_activation_module"},
    {"Gi_beta_gamma", "uM", "caveolar_G_i_protein_activation_module"},
    {"Gi_alpha_GDP", "uM", "caveolar_G_i_protein_activation_module"},
    {"Gs_alpha_GTP", "uM", "extracaveolar_G_s_protein_activation_module"},
    {"Gs_beta_gamma", "uM", "extracaveolar_G_s_protein_activation_module"},
    {"Gs_alpha_GDP", "uM", "extracaveolar_G_s_protein_activation_module"},
    {"Gi_alpha_GTP", "uM", "extracaveolar_G_i_protein_activation_module"},
    {"Gi_beta_gamma", "uM", "extracaveolar_G_i_protein_activation_module"},
    {"Gi_alpha_GDP", "uM", "extracaveolar_G_i_protein_activation_module"},
    {"cAMP_cav", "uM", "cAMP_flux_module"},
    {"cAMP_ecav", "uM", "cAMP_flux_module"},
    {"cAMP_cyt", "uM", "cAMP_flux_module"}};

const VariableInfo CONSTANT_INFO[] = {
    {"K_H", "uM", "beta_1_adrenergic_parameters"},
    {"K_L", "uM", "beta_1_adrenergic_parameters"},
    {"K_C", "uM", "beta_1_adrenergic_parameters"},
    {"K_H", "uM", "muscarinic_parameters"},
    {"K_L", "uM", "muscarinic_parameters"},
    {"K_C", "uM", "muscarinic_parameters"},
    {"k_PDE2", "per_sec", "PDE_parameters"},
    {"Km_PDE2", "uM", "PDE_parameters"},
    {"k_PDE3", "per_sec", "PDE_parameters"},
    {"Km_PDE3", "uM", "PDE_parameters"},
    {"k_PDE4", "per_sec", "PDE_parameters"},
    {"Km_PDE4", "uM", "PDE_parameters"},
    {"k_act1", "per_sec", "G_s_parameters"},
    {"k_act2", "per_sec", "G_s_parameters"},
    {"k_hydr", "per_sec", "G_s_parameters"},
    {"k_reas", "per_uM_per_sec", "G_s_parameters"},
    {"k_act1", "per_sec", "G_i_parameters"},
    {"k_act2", "per_sec", "G_i_parameters"},
    {"k_hydr", "per_sec", "G_i_parameters"},
    {"k_reas", "per_uM_per_sec", "G_i_parameters"},
    {"R_Total", "uM", "caveolar_beta_1_adrenergic_receptor_module"},
    {"R_Total", "uM", "caveolar_muscarinic_receptor_module"},
    {"Gs_Total", "uM", "caveolar_G_s_protein_activation_module"},
    {"Gi_Total", "uM", "caveolar_G_i_protein_activation_module"},
    {"R_Total", "uM", "extracaveolar_beta_1_adrenergic_receptor_module"},
    {"R_Total", "uM", "extracaveolar_muscarinic_receptor_module"},
    {"Gs_Total", "uM", "extracaveolar_G_s_protein_activation_module"},
    {"Gi_Total", "uM", "extracaveolar_G_i_protein_activation_module"},
    {"MW_AC56", "kDa", "AC56_module"},
    {"ATP", "uM", "AC56_module"},
    {"Km_ATP", "uM", "AC56_module"},
    {"AF56", "dimensionless", "AC56_module"},
    {"AC_56", "uM", "AC56_module"},
    {"MW_AC47", "kDa", "AC47_ecav_module"},
    {"ATP", "uM", "AC47_ecav_module"},
    {"Km_ATP", "uM", "AC47_ecav_module"},
    {"AF47", "dimensionless", "AC47_ecav_module"},
    {"AC_47_ecav", "uM", "AC47_ecav_module"},
    {"ATP", "uM", "AC47_cyt_module"},
    {"Km_ATP", "uM", "AC47_cyt_module"},
    {"AF47", "dimensionless", "AC47_cyt_module"},
    {"AC_47_cyt", "uM", "AC47_cyt_module"},
    {"k_AC47_cyt", "per_sec", "AC47_cyt_module"},
    {"PDE2", "uM", "caveolar_PDE_module"},
    {"PDE3", "uM", "caveolar_PDE_module"},
    {"PDE4", "uM", "caveolar_PDE_module"},
    {"PDE2", "uM", "extracaveolar_PDE_module"},
    {"PDE4", "uM", "extracaveolar_PDE_module"},
    {"PDE2", "uM", "bulk_cytoplasmic_PDE_module"},
    {"PDE3", "uM", "bulk_cytoplasmic_PDE_module"},
    {"PDE4", "uM", "bulk_cytoplasmic_PDE_module"},
    {"V_cell", "litre", "cAMP_flux_module"},
    {"J_cav_cyt", "liters_per_second", "cAMP_flux_module"},
    {"J_cav_ecav", "liters_per_second", "cAMP_flux_module"},
    {"J_ecav_cyt", "liters_per_second", "cAMP_flux_module"}};

const VariableInfo COMPUTED_CONSTANT_INFO[] = {
    {"dcAMP_AC_47_cyt_dt", "uM_per_sec", "AC47_cyt_module"},
    {"V_cav", "litre", "cAMP_flux_module"},
    {"V_ecav", "litre", "cAMP_flux_module"},
    {"V_cyt", "litre", "cAMP_flux_module"}};

const VariableInfo ALGEBRAIC_INFO[] = {
    {"L_iso", "uM", "beta_1_adrenergic_parameters"},
    {"L_ach", "uM", "muscarinic_parameters"},
    {"RG", "uM", "caveolar_beta_1_adrenergic_receptor_module"},
    {"LRG", "uM", "caveolar_beta_1_adrenergic_receptor_module"},
    {"LR", "uM", "caveolar_beta_1_adrenergic_receptor_module"},
    {"R", "uM", "caveolar_beta_1_adrenergic_receptor_module"},
    {"G", "uM", "caveolar_beta_1_adrenergic_receptor_module"},
    {"RG", "uM", "caveolar_muscarinic_receptor_module"},
    {"LRG", "uM", "caveolar_muscarinic_receptor_module"},
    {"LR", "uM", "caveolar_muscarinic_receptor_module"},
    {"R", "uM", "caveolar_muscarinic_receptor_module"},
    {"G", "uM", "caveolar_muscarinic_receptor_module"},
    {"RG", "uM", "extracaveolar_beta_1_adrenergic_receptor_module"},
    {"LRG", "uM", "extracaveolar_beta_1_adrenergic_receptor_module"},
    {"LR", "uM", "extracaveolar_beta_1_adrenergic_receptor_module"},
    {"R", "uM", "extracaveolar_beta_1_adrenergic_receptor_module"},
    {"G", "uM", "extracaveolar_beta_1_adrenergic_receptor_module"},
    {"RG", "uM", "extracaveolar_muscarinic_receptor_module"},
    {"LRG", "uM", "extracaveolar_muscarinic_receptor_module"},
    {"LR", "uM", "extracaveolar_muscarinic_receptor_module"},
    {"R", "uM", "extracaveolar_muscarinic_receptor_module"},
    {"G", "uM", "extracaveolar_muscarinic_receptor_module"},
    {"k_AC56", "per_sec", "AC56_module"},
    {"dcAMP_AC_56_dt", "uM_per_sec", "AC56_module"},
    {"k_AC47_ecav", "per_sec", "AC47_ecav_module"},
    {"dcAMP_AC_47_ecav_dt", "uM_per_sec", "AC47_ecav_module"},
    {"dcAMP_cav_PDE2_dt", "uM_per_sec", "caveolar_PDE_module"},
    {"dcAMP_cav_PDE3_dt", "uM_per_sec", "caveolar_PDE_module"},
    {"dcAMP_cav_PDE4_dt", "uM_per_sec", "caveolar_PDE_module"},
    {"dcAMP_ecav_PDE2_dt", "uM_per_sec", "extracaveolar_PDE_module"},
    {"dcAMP_ecav_PDE4_dt", "uM_per_sec", "extracaveolar_PDE_module"},
    {"dcAMP_cyt_PDE2_dt", "uM_per_sec", "bulk_cytoplasmic_PDE_module"},
    {"dcAMP_cyt_PDE3_dt", "uM_per_sec", "bulk_cytoplasmic_PDE_module"},
    {"dcAMP_cyt_PDE4_dt", "uM_per_sec", "bulk_cytoplasmic_PDE_module"}};

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
    states[0] = 0.041983438;
    states[1] = 0.042634499;
    states[2] = 0.000651061;
    states[3] = 0.012644961;
    states[4] = 0.013274751;
    states[5] = 0.00062979;
    states[6] = 0.083866891;
    states[7] = 0.084522918;
    states[8] = 0.000656025;
    states[9] = 0.001018705;
    states[10] = 0.001475253;
    states[11] = 0.000456548;
    states[12] = 0.11750433;
    states[13] = 1.092200547;
    states[14] = 0.992583576;
    constants[0] = 0.035;
    constants[1] = 0.386;
    constants[2] = 8.809;
    constants[3] = 0.16;
    constants[4] = 11.0;
    constants[5] = 30.0;
    constants[6] = 20.0;
    constants[7] = 50.0;
    constants[8] = 1.25;
    constants[9] = 0.08;
    constants[10] = 2.5;
    constants[11] = 2.2;
    constants[12] = 5.0;
    constants[13] = 0.1;
    constants[14] = 0.8;
    constants[15] = 1.21e3;
    constants[16] = 2.5;
    constants[17] = 0.05;
    constants[18] = 0.8;
    constants[19] = 1.21e3;
    constants[20] = 0.633;
    constants[21] = 0.633;
    constants[22] = 10.0;
    constants[23] = 20.0;
    constants[24] = 0.633;
    constants[25] = 0.633;
    constants[26] = 10.0;
    constants[27] = 1.0;
    constants[28] = 130.0;
    constants[29] = 5000.0;
    constants[30] = 315.0;
    constants[31] = 500.0;
    constants[32] = 3.379;
    constants[33] = 130.0;
    constants[34] = 5000.0;
    constants[35] = 315.0;
    constants[36] = 130.0;
    constants[37] = 0.2;
    constants[38] = 5000.0;
    constants[39] = 315.0;
    constants[40] = 130.0;
    constants[41] = 0.136;
    constants[42] = 1.08e-3;
    constants[43] = 4.5;
    constants[44] = 5.6;
    constants[45] = 2.0;
    constants[46] = 0.02;
    constants[47] = 0.16;
    constants[48] = 5.0e-3;
    constants[49] = 7.5e-3;
    constants[50] = 5.0e-3;
    constants[51] = 38.0e-12;
    constants[52] = 7.5e-14;
    constants[53] = 7.5e-15;
    constants[54] = 1.5e-17;
}

void computeComputedConstants(double voi, double *states, double *rates, double *constants, double *computedConstants, double *algebraic)
{
    computedConstants[0] = constants[42] * constants[41] * constants[40] * constants[38] / (constants[39] + constants[38]);
    computedConstants[1] = 0.01 * constants[51];
    computedConstants[2] = 0.02 * constants[51];
    computedConstants[3] = 0.5 * constants[51];
}

void computeRates(double voi, double *states, double *rates, double *constants, double *computedConstants, double *algebraicVariables)
{
    algebraicVariables[0] = ((voi > 120.0) && (voi <= 720.0)) ? 1.0 : 1.0;
    algebraicVariables[6] = constants[22] - states[0] - states[2];
    algebraicVariables[5] = constants[1] * constants[0] * constants[2] * pow(constants[1] * constants[0] * constants[2] - (constants[0] * (-constants[2] * algebraicVariables[0] - constants[1] * (constants[22] + -states[0] - states[2])) - pow(constants[1], 2.0) * algebraicVariables[0] * (constants[22] + -states[0] - states[2])), -1.0) * constants[20];
    algebraicVariables[3] = algebraicVariables[0] * algebraicVariables[5] * algebraicVariables[6] / (constants[0] * constants[2] / constants[1]);
    algebraicVariables[2] = algebraicVariables[5] * algebraicVariables[6] / constants[2];
    rates[0] = algebraicVariables[2] * constants[13] + algebraicVariables[3] * constants[12] - states[0] * constants[14];
    rates[1] = algebraicVariables[2] * constants[13] + algebraicVariables[3] * constants[12] - states[2] * states[1] * constants[15];
    rates[2] = states[0] * constants[14] - states[2] * states[1] * constants[15];
    algebraicVariables[1] = ((voi > 240.0) && (voi <= 540.0)) ? 0.0 : 0.0;
    algebraicVariables[11] = constants[23] - states[3] - states[5];
    algebraicVariables[10] = constants[3] * constants[4] * constants[5] * pow(constants[3] * constants[4] * constants[5] - (constants[4] * (-constants[3] * (constants[23] + -states[3] - states[5]) - constants[4] * algebraicVariables[1] * (constants[23] + -states[3] - states[5])) - constants[3] * constants[5] * algebraicVariables[1]), -1.0) * constants[21];
    algebraicVariables[8] = algebraicVariables[1] * algebraicVariables[10] * algebraicVariables[11] / (constants[3] * constants[5] / constants[4]);
    algebraicVariables[7] = algebraicVariables[10] * algebraicVariables[11] / constants[5];
    rates[3] = algebraicVariables[7] * constants[17] + algebraicVariables[8] * constants[16] - states[3] * constants[18];
    rates[4] = algebraicVariables[7] * constants[17] + algebraicVariables[8] * constants[16] - states[5] * states[4] * constants[19];
    rates[5] = states[3] * constants[18] - states[5] * states[4] * constants[19];
    algebraicVariables[16] = constants[26] - states[6] - states[8];
    algebraicVariables[15] = constants[1] * constants[0] * constants[2] * pow(constants[1] * constants[0] * constants[2] - (constants[0] * (-constants[2] * algebraicVariables[0] - constants[1] * (constants[26] + -states[8] - states[6])) - pow(constants[1], 2.0) * algebraicVariables[0] * (constants[26] + -states[8] - states[6])), -1.0) * constants[24];
    algebraicVariables[13] = algebraicVariables[0] * algebraicVariables[15] * algebraicVariables[16] / (constants[0] * constants[2] / constants[1]);
    algebraicVariables[12] = algebraicVariables[15] * algebraicVariables[16] / constants[2];
    rates[6] = algebraicVariables[12] * constants[13] + algebraicVariables[13] * constants[12] - states[6] * constants[14];
    rates[7] = algebraicVariables[12] * constants[13] + algebraicVariables[13] * constants[12] - states[8] * states[7] * constants[15];
    rates[8] = states[6] * constants[14] - states[8] * states[7] * constants[15];
    algebraicVariables[21] = constants[27] - states[9] - states[11];
    algebraicVariables[20] = constants[3] * constants[4] * constants[5] * pow(constants[3] * constants[4] * constants[5] - (-constants[3] * constants[5] * algebraicVariables[1] + -pow(constants[4], 2.0) * algebraicVariables[1] * (-states[9] + constants[27] - states[11]) - constants[3] * constants[4] * (-states[9] + constants[27] - states[11])), -1.0) * constants[25];
    algebraicVariables[18] = algebraicVariables[1] * algebraicVariables[20] * algebraicVariables[21] / (constants[3] * constants[5] / constants[4]);
    algebraicVariables[17] = algebraicVariables[20] * algebraicVariables[21] / constants[5];
    rates[9] = algebraicVariables[17] * constants[17] + algebraicVariables[18] * constants[16] - states[9] * constants[18];
    rates[10] = algebraicVariables[17] * constants[17] + algebraicVariables[18] * constants[16] - states[11] * states[10] * constants[19];
    rates[11] = states[9] * constants[18] - states[11] * states[10] * constants[19];
    algebraicVariables[22] = (0.7 + 3.8234 * pow(states[0] / 1.0, 0.9787) / (0.1986 + pow(states[0] / 1.0, 0.9787))) * (1.0 + 1.0 / 1.4432 * -1.0061 * pow(states[3] / 1.0, 0.8356) / (0.1918 + pow(states[3] / 1.0, 0.8356))) * constants[28] / 60.0 * 0.001;
    algebraicVariables[23] = algebraicVariables[22] * constants[32] * constants[31] * constants[29] / (constants[30] + constants[29]);
    algebraicVariables[26] = constants[6] * constants[43] * states[12] / (constants[7] + states[12]);
    algebraicVariables[27] = constants[8] * constants[44] * states[12] / (constants[9] + states[12]);
    algebraicVariables[28] = constants[10] * constants[45] * states[12] / (constants[11] + states[12]);
    rates[12] = algebraicVariables[23] - (algebraicVariables[26] + algebraicVariables[27] + algebraicVariables[28]) - constants[53] * (states[12] - states[13]) / computedConstants[1] - constants[52] * (states[12] - states[14]) / computedConstants[1];
    algebraicVariables[24] = (0.063 + 2.01 * pow(states[6] * 1000.0, 1.0043) / (31.544 + pow(states[6] * 1000.0, 1.0043))) * (1.0 + 1.0 / 3.01 * 49.1 * pow(states[10] * 1000.0, 0.8921) / (25.44 + pow(states[10] * 1000.0, 0.8921))) * constants[33] / 60.0 * 0.001;
    algebraicVariables[25] = algebraicVariables[24] * constants[37] * constants[36] * constants[34] / (constants[35] + constants[34]);
    algebraicVariables[29] = constants[6] * constants[46] * states[13] / (constants[7] + states[13]);
    algebraicVariables[30] = constants[10] * constants[47] * states[13] / (constants[11] + states[13]);
    rates[13] = algebraicVariables[25] - (algebraicVariables[29] + algebraicVariables[30]) + constants[53] * (states[12] - states[13]) / computedConstants[2] - constants[54] * (states[13] - states[14]) / computedConstants[2];
    algebraicVariables[31] = constants[6] * constants[48] * states[14] / (constants[7] + states[14]);
    algebraicVariables[32] = constants[8] * constants[49] * states[14] / (constants[9] + states[14]);
    algebraicVariables[33] = constants[10] * constants[50] * states[14] / (constants[11] + states[14]);
    rates[14] = computedConstants[0] - (algebraicVariables[31] + algebraicVariables[32] + algebraicVariables[33]) + constants[52] * (states[12] - states[14]) / computedConstants[3] + constants[54] * (states[13] - states[14]) / computedConstants[3];
}

void computeVariables(double voi, double *states, double *rates, double *constants, double *computedConstants, double *algebraicVariables)
{
    algebraicVariables[5] = constants[1] * constants[0] * constants[2] * pow(constants[1] * constants[0] * constants[2] - (constants[0] * (-constants[2] * algebraicVariables[0] - constants[1] * (constants[22] + -states[0] - states[2])) - pow(constants[1], 2.0) * algebraicVariables[0] * (constants[22] + -states[0] - states[2])), -1.0) * constants[20];
    algebraicVariables[4] = algebraicVariables[0] * algebraicVariables[5] / constants[1];
    algebraicVariables[3] = algebraicVariables[0] * algebraicVariables[5] * algebraicVariables[6] / (constants[0] * constants[2] / constants[1]);
    algebraicVariables[2] = algebraicVariables[5] * algebraicVariables[6] / constants[2];
    algebraicVariables[10] = constants[3] * constants[4] * constants[5] * pow(constants[3] * constants[4] * constants[5] - (constants[4] * (-constants[3] * (constants[23] + -states[3] - states[5]) - constants[4] * algebraicVariables[1] * (constants[23] + -states[3] - states[5])) - constants[3] * constants[5] * algebraicVariables[1]), -1.0) * constants[21];
    algebraicVariables[9] = algebraicVariables[1] * algebraicVariables[10] / constants[4];
    algebraicVariables[8] = algebraicVariables[1] * algebraicVariables[10] * algebraicVariables[11] / (constants[3] * constants[5] / constants[4]);
    algebraicVariables[7] = algebraicVariables[10] * algebraicVariables[11] / constants[5];
    algebraicVariables[15] = constants[1] * constants[0] * constants[2] * pow(constants[1] * constants[0] * constants[2] - (constants[0] * (-constants[2] * algebraicVariables[0] - constants[1] * (constants[26] + -states[8] - states[6])) - pow(constants[1], 2.0) * algebraicVariables[0] * (constants[26] + -states[8] - states[6])), -1.0) * constants[24];
    algebraicVariables[14] = algebraicVariables[0] * algebraicVariables[15] / constants[1];
    algebraicVariables[13] = algebraicVariables[0] * algebraicVariables[15] * algebraicVariables[16] / (constants[0] * constants[2] / constants[1]);
    algebraicVariables[12] = algebraicVariables[15] * algebraicVariables[16] / constants[2];
    algebraicVariables[20] = constants[3] * constants[4] * constants[5] * pow(constants[3] * constants[4] * constants[5] - (-constants[3] * constants[5] * algebraicVariables[1] + -pow(constants[4], 2.0) * algebraicVariables[1] * (-states[9] + constants[27] - states[11]) - constants[3] * constants[4] * (-states[9] + constants[27] - states[11])), -1.0) * constants[25];
    algebraicVariables[19] = algebraicVariables[1] * algebraicVariables[20] / constants[4];
    algebraicVariables[18] = algebraicVariables[1] * algebraicVariables[20] * algebraicVariables[21] / (constants[3] * constants[5] / constants[4]);
    algebraicVariables[17] = algebraicVariables[20] * algebraicVariables[21] / constants[5];
}
