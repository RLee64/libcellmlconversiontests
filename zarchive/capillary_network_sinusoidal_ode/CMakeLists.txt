get_filename_component(DIR ${CMAKE_CURRENT_SOURCE_DIR} NAME)

build_executable(${DIR}
    ODE
    ENDING_POINT
        100
    POINT_INTERVAL
        0.0001
    RELATIVE_TOLERANCE
        1e-8
    ABSOLUTE_TOLERANCE
        1e-8
)
