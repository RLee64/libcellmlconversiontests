/* The content of this file was generated using the C profile of libCellML 0.6.3. */

#include "model.h"

#include <math.h>
#include <stdlib.h>

const char VERSION[] = "0.7.0";
const char LIBCELLML_VERSION[] = "0.6.3";

const size_t STATE_COUNT = 1;
const size_t CONSTANT_COUNT = 0;
const size_t COMPUTED_CONSTANT_COUNT = 0;
const size_t ALGEBRAIC_VARIABLE_COUNT = 6;

const VariableInfo VOI_INFO = {"t", "dimensionless", "algebraic_component"};

const VariableInfo STATE_INFO[] = {
    {"x", "dimensionless", "algebraic_component"}};

const VariableInfo CONSTANT_INFO[] = {"I", "IGNORE", "IGNORE"};

const VariableInfo COMPUTED_CONSTANT_INFO[] = {"I", "IGNORE", "IGNORE"};

const VariableInfo ALGEBRAIC_INFO[] = {
    {"f", "dimensionless", "algebraic_component"},
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

void initialiseArrays(double *states, double *rates, double *constants, double *computedConstants, double *algebraicVariables)
{
    states[0] = 0.0;
}

void computeComputedConstants(double voi, double *states, double *rates, double *constants, double *computedConstants, double *algebraic)
{
}

void computeRates(double voi, double *states, double *rates, double *constants, double *computedConstants, double *algebraicVariables)
{
    algebraicVariables[0] = 1 / 1073.0 * (-1240.0 * states[0] + 478.0 * voi);
    algebraicVariables[1] = 1 / 23.0 * (-239.0 * algebraicVariables[0] + 89.0 * voi + -238.0 * states[0]);
    algebraicVariables[2] = -1 / 20.0 * (19.0 * algebraicVariables[1] + 27.0 * algebraicVariables[0] + 3.0 * voi + 34.0 * states[0]);
    algebraicVariables[3] = -1 / 12.0 * (29.0 * algebraicVariables[0] + voi + 16.0 * algebraicVariables[2] + 25.0 * algebraicVariables[1] + 18.0 * states[0]);
    algebraicVariables[4] = -5.0 * algebraicVariables[0] + -2.0 * states[0] + -4.0 * algebraicVariables[1] + -3.0 * algebraicVariables[2] + -2.0 * algebraicVariables[3];
    algebraicVariables[5] = -(6.0 * algebraicVariables[0] + states[0] + 5.0 * algebraicVariables[1] + 4.0 * algebraicVariables[2] + 3.0 * algebraicVariables[3] + 2.0 * algebraicVariables[4]);
    rates[0] = algebraicVariables[5] + 3.0 * algebraicVariables[4] + -algebraicVariables[3] + 2.0 * algebraicVariables[2] + -algebraicVariables[1] + 4.0 * algebraicVariables[0];
}

void computeVariables(double voi, double *states, double *rates, double *constants, double *computedConstants, double *algebraicVariables)
{
    algebraicVariables[0] = 1 / 1073.0 * (-1240.0 * states[0] + 478.0 * voi);
    algebraicVariables[1] = 1 / 23.0 * (-239.0 * algebraicVariables[0] + 89.0 * voi + -238.0 * states[0]);
    algebraicVariables[2] = -1 / 20.0 * (19.0 * algebraicVariables[1] + 27.0 * algebraicVariables[0] + 3.0 * voi + 34.0 * states[0]);
    algebraicVariables[3] = -1 / 12.0 * (29.0 * algebraicVariables[0] + voi + 16.0 * algebraicVariables[2] + 25.0 * algebraicVariables[1] + 18.0 * states[0]);
    algebraicVariables[4] = -5.0 * algebraicVariables[0] + -2.0 * states[0] + -4.0 * algebraicVariables[1] + -3.0 * algebraicVariables[2] + -2.0 * algebraicVariables[3];
    algebraicVariables[5] = -(6.0 * algebraicVariables[0] + states[0] + 5.0 * algebraicVariables[1] + 4.0 * algebraicVariables[2] + 3.0 * algebraicVariables[3] + 2.0 * algebraicVariables[4]);
}
