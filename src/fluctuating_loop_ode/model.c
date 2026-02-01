/* The content of this file was generated using the C profile of libCellML 0.6.3. */

#include "model.h"

#include <math.h>
#include <stdlib.h>

const char VERSION[] = "0.7.0";
const char LIBCELLML_VERSION[] = "0.6.3";

const size_t STATE_COUNT = 1;
const size_t CONSTANT_COUNT = 2;
const size_t COMPUTED_CONSTANT_COUNT = 0;
const size_t ALGEBRAIC_VARIABLE_COUNT = 3;

const VariableInfo VOI_INFO = {"time", "second", "environment"};

const VariableInfo STATE_INFO[] = {
    {"s", "dimensionless", "state"}};

const VariableInfo CONSTANT_INFO[] = {
    {"period", "second", "parameters"},
    {"amp", "dimensionless", "parameters"}};

const VariableInfo COMPUTED_CONSTANT_INFO[1] = {{"IGNORE", "IGNORE", "IGNORE"}};

const VariableInfo ALGEBRAIC_INFO[] = {
    {"f", "per_second", "forcing"},
    {"b", "per_second", "algebraic_loop"},
    {"a", "per_second", "algebraic_loop"}};

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
    constants[0] = 1.0;
    constants[1] = 1.0;
}

void computeComputedConstants(double voi, double *states, double *rates, double *constants, double *computedConstants, double *algebraic)
{
}

void computeRates(double voi, double *states, double *rates, double *constants, double *computedConstants, double *algebraicVariables)
{
    algebraicVariables[2] = 1 / 2.0 * constants[1] * pow(constants[0], -1.0) * sin(2.0 * 3.14159265358979 * 500 * voi * pow(constants[0], -1.0));
    rates[0] = algebraicVariables[2];
}

void computeVariables(double voi, double *states, double *rates, double *constants, double *computedConstants, double *algebraicVariables)
{
    algebraicVariables[0] = constants[1] / constants[0] * sin(2.0 * 3.14159265358979 * 500 * voi / constants[0]);
    algebraicVariables[1] = algebraicVariables[2] - algebraicVariables[0];
}
