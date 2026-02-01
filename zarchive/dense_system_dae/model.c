/* The content of this file was generated using the C profile of libCellML 0.6.3. */

#include "model.h"

#include <math.h>
#include <stdlib.h>

const char VERSION[] = "0.7.0";
const char LIBCELLML_VERSION[] = "0.6.3";

const size_t STATE_COUNT = 1;
const size_t CONSTANT_COUNT = 0;
const size_t COMPUTED_CONSTANT_COUNT = 0;
const size_t ALGEBRAIC_VARIABLE_COUNT = 5;

const VariableInfo VOI_INFO = {"t", "dimensionless", "algebraic_component"};

const VariableInfo STATE_INFO[] = {
    {"x", "dimensionless", "algebraic_component"}};

const VariableInfo CONSTANT_INFO[1] = {{"I", "IGNORE", "IGNORE"}};

const VariableInfo COMPUTED_CONSTANT_INFO[1] = {{"I", "IGNORE", "IGNORE"}};

const VariableInfo ALGEBRAIC_INFO[] = {
    {"e", "dimensionless", "algebraic_component"},
    {"d", "dimensionless", "algebraic_component"},
    {"c", "dimensionless", "algebraic_component"},
    {"b", "dimensionless", "algebraic_component"},
    {"a", "dimensionless", "algebraic_component"}};

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
    algebraicVariables[1] = u[1];
    algebraicVariables[2] = u[2];
    algebraicVariables[3] = u[3];
    algebraicVariables[4] = u[4];

    f[0] = algebraicVariables[4] + 2.0 * algebraicVariables[3] + 3.0 * algebraicVariables[2] + 4.0 * algebraicVariables[1] + 5.0 * algebraicVariables[0] + states[0] - 0.0;
    f[1] = algebraicVariables[4] + algebraicVariables[3] + algebraicVariables[2] + algebraicVariables[1] + algebraicVariables[0] + -states[0] - 0.0;
    f[2] = 4.0 * algebraicVariables[4] + -3.0 * algebraicVariables[3] + 2.0 * algebraicVariables[2] + -1.0 * algebraicVariables[1] + algebraicVariables[0] + voi - 0.0;
    f[3] = algebraicVariables[4] + 4.0 * algebraicVariables[3] + -2.0 * algebraicVariables[2] + 3.0 * algebraicVariables[1] + -1.0 * algebraicVariables[0] - 0.0;
    f[4] = -9.0 * algebraicVariables[4] + -2.0 * algebraicVariables[3] + 1.0 * algebraicVariables[2] + 1.0 * algebraicVariables[1] + 3.0 * algebraicVariables[0] - 0.0;
}

void findRoot0(double voi, double *states, double *rates, double *constants, double *computedConstants, double *algebraicVariables)
{
    RootFindingInfo rfi = {voi, states, rates, constants, computedConstants, algebraicVariables};
    double u[5];

    u[0] = algebraicVariables[0];
    u[1] = algebraicVariables[1];
    u[2] = algebraicVariables[2];
    u[3] = algebraicVariables[3];
    u[4] = algebraicVariables[4];

    nlaSolve(objectiveFunction0, u, 5, &rfi);

    algebraicVariables[0] = u[0];
    algebraicVariables[1] = u[1];
    algebraicVariables[2] = u[2];
    algebraicVariables[3] = u[3];
    algebraicVariables[4] = u[4];
}

void initialiseArrays(double *states, double *rates, double *constants, double *computedConstants, double *algebraicVariables)
{
    states[0] = 0.0;
    algebraicVariables[0] = 0.0;
    algebraicVariables[1] = 0.0;
    algebraicVariables[2] = 0.0;
    algebraicVariables[3] = 0.0;
    algebraicVariables[4] = 0.0;
}

void computeComputedConstants(double voi, double *states, double *rates, double *constants, double *computedConstants, double *algebraic)
{
}

void computeRates(double voi, double *states, double *rates, double *constants, double *computedConstants, double *algebraicVariables)
{
    findRoot0(voi, states, rates, constants, computedConstants, algebraicVariables);
    rates[0] = algebraicVariables[4] + 3.0 * algebraicVariables[3] + -algebraicVariables[2] + 2.0 * algebraicVariables[1] + -algebraicVariables[0];
}

void computeVariables(double voi, double *states, double *rates, double *constants, double *computedConstants, double *algebraicVariables)
{
    findRoot0(voi, states, rates, constants, computedConstants, algebraicVariables);
}
