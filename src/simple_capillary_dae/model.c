/* The content of this file was generated using the C profile of libCellML 0.6.3. */

#include "model.h"

#include <math.h>
#include <stdlib.h>

const char VERSION[] = "0.8.0";
const char LIBCELLML_VERSION[] = "0.6.3";

const size_t STATE_COUNT = 1;
const size_t CONSTANT_COUNT = 0;
const size_t COMPUTED_CONSTANT_COUNT = 5;
const size_t ALGEBRAIC_VARIABLE_COUNT = 6;

const VariableInfo VOI_INFO = {"t", "dimensionless", "Capillary"};

const VariableInfo STATE_INFO[] = {
    {"q", "dimensionless", "Capillary"}};

const VariableInfo CONSTANT_INFO[1] = {{"IGNORE", "IGNORE", "IGNORE"}};

const VariableInfo COMPUTED_CONSTANT_INFO[] = {
    {"v_in", "dimensionless", "Capillary"},
    {"P_out", "dimensionless", "Capillary"},
    {"R", "dimensionless", "Capillary"},
    {"R_v", "dimensionless", "Capillary"},
    {"C", "dimensionless", "Capillary"}};

const VariableInfo ALGEBRAIC_INFO[] = {
    {"v_y", "dimensionless", "Capillary"},
    {"P_C", "dimensionless", "Capillary"},
    {"P_x", "dimensionless", "Capillary"},
    {"P_R_v", "dimensionless", "Capillary"},
    {"P_R", "dimensionless", "Capillary"},
    {"v_z", "dimensionless", "Capillary"}};

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

    algebraicVariables[0] = u[0];
    algebraicVariables[2] = u[1];
    algebraicVariables[3] = u[2];
    algebraicVariables[4] = u[3];
    algebraicVariables[5] = u[4];

    f[0] = computedConstants[0] - (algebraicVariables[0] + algebraicVariables[5]);
    f[1] = algebraicVariables[2] - (algebraicVariables[3] + algebraicVariables[1]);
    f[2] = algebraicVariables[2] - (computedConstants[1] + algebraicVariables[4]);
    f[3] = algebraicVariables[4] - algebraicVariables[5] * computedConstants[2];
    f[4] = algebraicVariables[3] - algebraicVariables[0] * computedConstants[3];
}

void findRoot0(double voi, double *states, double *rates, double *constants, double *computedConstants, double *algebraicVariables)
{
    RootFindingInfo rfi = {voi, states, rates, constants, computedConstants, algebraicVariables};
    double u[5];

    u[0] = algebraicVariables[0];
    u[1] = algebraicVariables[2];
    u[2] = algebraicVariables[3];
    u[3] = algebraicVariables[4];
    u[4] = algebraicVariables[5];

    nlaSolve(objectiveFunction0, u, 5, &rfi);

    algebraicVariables[0] = u[0];
    algebraicVariables[2] = u[1];
    algebraicVariables[3] = u[2];
    algebraicVariables[4] = u[3];
    algebraicVariables[5] = u[4];
}

void initialiseArrays(double *states, double *rates, double *constants, double *computedConstants, double *algebraicVariables)
{
    states[0] = 2.0;
    computedConstants[0] = 5.0;
    computedConstants[1] = 10.0;
    computedConstants[2] = 10.0;
    computedConstants[3] = 10.0;
    computedConstants[4] = 10.0;
    algebraicVariables[0] = 0.0;
    algebraicVariables[2] = 0.0;
    algebraicVariables[3] = 0.0;
    algebraicVariables[4] = 0.0;
    algebraicVariables[5] = 0.0;
}

void computeComputedConstants(double voi, double *states, double *rates, double *constants, double *computedConstants, double *algebraicVariables)
{
}

void computeRates(double voi, double *states, double *rates, double *constants, double *computedConstants, double *algebraicVariables)
{
    algebraicVariables[1] = states[0] / computedConstants[4];
    findRoot0(voi, states, rates, constants, computedConstants, algebraicVariables);
    rates[0] = algebraicVariables[0];
}

void computeVariables(double voi, double *states, double *rates, double *constants, double *computedConstants, double *algebraicVariables)
{
    algebraicVariables[1] = states[0] / computedConstants[4];
    findRoot0(voi, states, rates, constants, computedConstants, algebraicVariables);
}
