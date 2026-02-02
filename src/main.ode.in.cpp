#include "common.h"
#include <vector>
#include <windows.h>

extern "C"
{
#include "model.h"
}

#include <cvode/cvode.h>
#include <nvector/nvector_serial.h>
#include <sunlinsol/sunlinsol_dense.h>

#include <fstream>
#include <iostream>

double freq = 0.0;
__int64 startTime = 0;

void startCounter()
{
    LARGE_INTEGER li;
    if (!QueryPerformanceFrequency(&li))
    {
        std::cout << "Error with QueryPerformanceFrequency" << std::endl;
    }
    freq = double(li.QuadPart) / 1000.0;

    QueryPerformanceCounter(&li);
    startTime = li.QuadPart;
}

double getCounter()
{
    LARGE_INTEGER li;
    QueryPerformanceCounter(&li);
    return double(li.QuadPart - startTime) / freq;
}

#define EXTERNALS @EXTERNALS@

#if (EXTERNALS == 1)
double externalVariable(double voi, double *states, double *rates, double *constants, double *computedConstants, double *algebraic, double *externals, size_t index)
{
    static const std::vector<std::vector<double>> externalValues =@EXTERNAL_VALUES@;

    for (size_t i = 0; i < externalValues.size() - 1; ++i)
    {
        double voi0 = externalValues[i][0];
        double voi1 = externalValues[i + 1][0];

        if ((voi >= voi0) && (voi < voi1))
        {
            double value0 = externalValues[i][index + 1];

            return value0 + (voi - voi0) / (voi1 - voi0) * (externalValues[i + 1][index + 1] - value0);
        }
    }

    return externalValues[externalValues.size() - 1][index + 1];
}
#endif

void printInformation()
{
    std::cout << "---------------------------------------[Information][BEGIN]" << std::endl;
    std::cout << "- Generator version: " << VERSION << std::endl;
    std::cout << "- libCellML version: " << LIBCELLML_VERSION << std::endl;
    std::cout << "---------------------------------------" << std::endl;
    std::cout << "- Variable of integration:" << std::endl;
    std::cout << "   - " << VOI_INFO.component << "." << VOI_INFO.name << " [" << VOI_INFO.units << "]" << std::endl;
    std::cout << "---------------------------------------" << std::endl;
    std::cout << "- Number of states: " << STATE_COUNT << std::endl;

    if (STATE_COUNT > 0)
    {
        for (size_t i = 0; i < STATE_COUNT; ++i)
        {
            std::cout << "   - " << STATE_INFO[i].name << " [" << STATE_INFO[i].units << "] [" << STATE_INFO[i].component << "]" << std::endl;
        }
    }

    std::cout << "---------------------------------------" << std::endl;
    std::cout << "- Number of constants: " << CONSTANT_COUNT << std::endl;

    if (CONSTANT_COUNT > 0)
    {
        for (size_t i = 0; i < CONSTANT_COUNT; ++i)
        {
            std::cout << "   - " << CONSTANT_INFO[i].name << " [" << CONSTANT_INFO[i].units << "] [" << CONSTANT_INFO[i].component << "]" << std::endl;
        }
    }

    std::cout << "---------------------------------------" << std::endl;
    std::cout << "- Number of computed constants: " << COMPUTED_CONSTANT_COUNT << std::endl;

    if (COMPUTED_CONSTANT_COUNT > 0)
    {
        for (size_t i = 0; i < COMPUTED_CONSTANT_COUNT; ++i)
        {
            std::cout << "   - " << COMPUTED_CONSTANT_INFO[i].name << " [" << COMPUTED_CONSTANT_INFO[i].units << "] [" << COMPUTED_CONSTANT_INFO[i].component << "]" << std::endl;
        }
    }

    std::cout << "---------------------------------------" << std::endl;
    std::cout << "- Number of algebraic variables: " << ALGEBRAIC_VARIABLE_COUNT << std::endl;

    if (ALGEBRAIC_VARIABLE_COUNT > 0)
    {
        for (size_t i = 0; i < ALGEBRAIC_VARIABLE_COUNT; ++i)
        {
            std::cout << "   - " << ALGEBRAIC_INFO[i].name << " [" << ALGEBRAIC_INFO[i].units << "] [" << ALGEBRAIC_INFO[i].component << "]" << std::endl;
        }
    }

#if (EXTERNALS == 1)
    std::cout << "---------------------------------------" << std::endl;
    std::cout << "- Number of external variables: " << EXTERNAL_COUNT << std::endl;

    if (EXTERNAL_COUNT > 0)
    {
        for (size_t i = 0; i < EXTERNAL_COUNT; ++i)
        {
            std::cout << "   - " << EXTERNAL_INFO[i].name << " [" << EXTERNAL_INFO[i].units << "] [" << EXTERNAL_INFO[i].component << "]" << std::endl;
        }
    }
#endif

    std::cout << "---------------------------------------[Information][END]" << std::endl;
}

void printHeaders(std::ofstream &file)
{
    file << "voi";

    for (size_t i = 0; i < STATE_COUNT; ++i)
    {
        file << "," << STATE_INFO[i].name;
    }

    for (size_t i = 0; i < CONSTANT_COUNT; ++i)
    {
        file << "," << CONSTANT_INFO[i].name;
    }

    for (size_t i = 0; i < COMPUTED_CONSTANT_COUNT; ++i)
    {
        file << "," << COMPUTED_CONSTANT_INFO[i].name;
    }

    for (size_t i = 0; i < ALGEBRAIC_VARIABLE_COUNT; ++i)
    {
        file << "," << ALGEBRAIC_INFO[i].name;
    }

#if (EXTERNALS == 1)
    for (size_t i = 0; i < EXTERNAL_COUNT; ++i)
    {
        file << "," << EXTERNAL_INFO[i].name;
    }
#endif

    file << std::endl;
}

#if (EXTERNALS == 1)
void collectValues(std::vector<double> &row, double voi, const double *states, const double *constants, const double *computedConstants, const double *algebraic, const double *externals)
#else
void collectValues(std::vector<double> &row, double voi, const double *states, const double *constants, const double *computedConstants, const double *algebraic)
#endif
{
    row.clear();
    row.push_back(voi);

    for (size_t i = 0; i < STATE_COUNT; ++i) row.push_back(states[i]);
    for (size_t i = 0; i < CONSTANT_COUNT; ++i) row.push_back(constants[i]);
    for (size_t i = 0; i < COMPUTED_CONSTANT_COUNT; ++i) row.push_back(computedConstants[i]);
    for (size_t i = 0; i < ALGEBRAIC_VARIABLE_COUNT; ++i) row.push_back(algebraic[i]);

#if (EXTERNALS == 1)
    for (size_t i = 0; i < EXTERNAL_COUNT; ++i) row.push_back(externals[i]);
#endif
}

typedef struct
{
#if (EXTERNALS == 1)
    void (*computeRates)(double, double *, double *, double *, double *, double *, double *, ExternalVariable);
#else
    void (*computeRates)(double, double *, double *, double *, double *, double *);
#endif

    double *constants;
    double *computedConstants;
    double *algebraic;
#if (EXTERNALS == 1)
    double *externals;

    ExternalVariable externalVariable;
#endif
} UserOdeData;

int func(double voi, N_Vector y, N_Vector yDot, void *userData)
{
    UserOdeData *realUserData = (UserOdeData *)userData;

#if (EXTERNALS == 1)
    realUserData->computeRates(voi, N_VGetArrayPointer_Serial(y), N_VGetArrayPointer_Serial(yDot), realUserData->constants, realUserData->computedConstants, realUserData->algebraic, realUserData->externals, realUserData->externalVariable);
#else
    realUserData->computeRates(voi, N_VGetArrayPointer_Serial(y), N_VGetArrayPointer_Serial(yDot), realUserData->constants, realUserData->computedConstants, realUserData->algebraic);
#endif

    return 0;
}

int main(int argc, char **argv)
{
    // Some information about the model.

    printInformation();

    // Start timer.
    startCounter();

    // Create our various arrays.

    double voi = 0.0;
    double *states = createStatesArray();
    double *rates = createStatesArray();
    double *constants = createConstantsArray();
    double *computedConstants = createComputedConstantsArray();
    double *algebraic = createAlgebraicVariablesArray();
#if (EXTERNALS == 1)
    double *externals = createExternalsArray();
#endif

    // Initialise our states, rates, constants, computed constants, and algebraic variables and output their initial
    // value/guess.

    initialiseArrays(states, rates, constants, computedConstants, algebraic);
    computeComputedConstants(voi, states, rates, constants, computedConstants, algebraic);

#if (EXTERNALS == 1)
    computeRates(voi, states, rates, constants, computedConstants, algebraic, externals, externalVariable);
    computeVariables(voi, states, rates, constants, computedConstants, algebraic, externals, externalVariable);
#else
    computeRates(voi, states, rates, constants, computedConstants, algebraic);
    computeVariables(voi, states, rates, constants, computedConstants, algebraic);
#endif

    std::vector<std::vector<double>> outputBuffer;

    if (!@SKIP_FIRST_OUTPUT_POINT@)
    {
        std::vector<double> row;
#if (EXTERNALS == 1)
        collectValues(row, voi, states, constants, computedConstants, algebraic, externals);
#else
        collectValues(row, voi, states, constants, computedConstants, algebraic);
#endif
        outputBuffer.push_back(std::move(row));
    }

    // Create our SUNDIALS context.

    SUNContext context;

    SUNContext_Create(0, &context);

    // Create our CVODE solver.

    void *solver = CVodeCreate(CV_BDF, context);

    // Initialise our CVODE solver.

    N_Vector y = N_VMake_Serial(STATE_COUNT, states, context);

    CVodeInit(solver, func, voi, y);

    // Set our user data.

#if (EXTERNALS == 1)
    UserOdeData userData = {computeRates, constants, computedConstants, algebraic, externals, externalVariable};
#else
    UserOdeData userData = {computeRates, constants, computedConstants, algebraic};
#endif

    CVodeSetUserData(solver, &userData);

    // Set our maximum number of steps.

    CVodeSetMaxNumSteps(solver, 99999);

    // Set our linear solver.

    SUNMatrix matrix = SUNDenseMatrix(STATE_COUNT, STATE_COUNT, context);
    SUNLinearSolver linearSolver = SUNLinSol_Dense(y, matrix, context);

    CVodeSetLinearSolver(solver, linearSolver, matrix);

    // Set our relative and absolute tolerances.

    CVodeSStolerances(solver,@RELATIVE_TOLERANCE@,@ABSOLUTE_TOLERANCE@);

    // Run our model.

    std::vector<double> outputPoints =@OUTPUT_POINTS@;

    if (!@USE_OUTPUT_POINTS@)
    {
        size_t i = 0;
        double voiMax =@ENDING_POINT@;
        double voiInterval =@POINT_INTERVAL@;

        do
        {
            voi = ++i * voiInterval;

            outputPoints.push_back(voi);
        } while (voi < voiMax);
    }

    for (const auto &outputPoint : outputPoints)
    {
        // Integrate our model.

        CVode(solver, outputPoint, y, &voi, CV_NORMAL);

        // Compute our variables.

#if (EXTERNALS == 1)
        computeVariables(voi, states, rates, constants, computedConstants, algebraic, externals, externalVariable);
#else
        computeVariables(voi, states, rates, constants, computedConstants, algebraic);
#endif

        std::vector<double> row;
#if (EXTERNALS == 1)
        collectValues(row, voi, states, constants, computedConstants, algebraic, externals);
#else
        collectValues(row, voi, states, constants, computedConstants, algebraic);
#endif
        outputBuffer.push_back(std::move(row));
    }

    // Output to csv

    // std::cout << "Pre output took: " << getCounter() / 1000 << " seconds" << std::endl;

    // std::ofstream file(std::string(argv[0]) + "___c.csv");
    // printHeaders(file);

    // for (const auto &row : outputBuffer)
    // {
    //     for (size_t i = 0; i < row.size(); ++i)
    //     {
    //         if (i > 0) file << ",";
    //         file << row[i];
    //     }
    //     file << "\n";
    // }

    // file.close();

    SUNLinSolFree(linearSolver);
    SUNMatDestroy(matrix);
    N_VDestroy_Serial(y);
    CVodeFree(&solver);
    SUNContext_Free(&context);

    deleteArray(states);
    deleteArray(rates);
    deleteArray(constants);
    deleteArray(computedConstants);
    deleteArray(algebraic);

    std::cout << "Program took: " << getCounter() / 1000 << " seconds" << std::endl;

    return 0;
}
