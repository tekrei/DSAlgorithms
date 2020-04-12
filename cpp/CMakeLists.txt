cmake_minimum_required(VERSION 3.0)

project(dsalgorithms-cpp)

# specify C++ standard
set(CMAKE_CXX_STANDARD 17)

set(INCLUDES ./includes)

# include directories
include_directories(${INCLUDES})

# find header files
file(GLOB_RECURSE HEADERS ${INCLUDES}/*.h)

# specify compiler flags
set(GCC_COVERAGE_COMPILE_FLAGS "-O3 -Wall -Wfloat-conversion")

add_definitions(${GCC_COVERAGE_COMPILE_FLAGS})

set(
    SOURCE_FILES
        main.cpp
        ${HEADERS}
)
add_executable(dsalgorithms-cpp ${SOURCE_FILES})
