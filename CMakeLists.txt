cmake_minimum_required(VERSION 3.20)
project(algorithms_and_structures CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

include(FetchContent)

FetchContent_Declare(
    Catch2
    GIT_REPOSITORY https://github.com/catchorg/Catch2.git
    GIT_TAG        v3.8.1
)

FetchContent_MakeAvailable(Catch2)
list(APPEND CMAKE_MODULE_PATH ${catch2_SOURCE_DIR}/extras)

enable_testing()
include(CTest)
include(Catch)

file(GLOB_RECURSE TEST_SOURCES CONFIGURE_DEPENDS
    "${CMAKE_SOURCE_DIR}/solutions/*/*/cpp/test_*.cpp"
    "${CMAKE_SOURCE_DIR}/structures/cpp/test_*.cpp"
)

foreach(TEST_SRC ${TEST_SOURCES})
    get_filename_component(TEST_NAME "${TEST_SRC}" NAME_WE)
    get_filename_component(TEST_DIR "${TEST_SRC}" DIRECTORY)
    file(RELATIVE_PATH REL_DIR "${CMAKE_SOURCE_DIR}" "${TEST_DIR}")
    string(REPLACE "/" "_" TARGET_ID "${REL_DIR}")
    set(TARGET_NAME "${TARGET_ID}_${TEST_NAME}")

    add_executable(${TARGET_NAME} ${TEST_SRC})
    target_link_libraries(${TARGET_NAME} PRIVATE Catch2::Catch2WithMain)
    target_include_directories(${TARGET_NAME} PRIVATE "${CMAKE_SOURCE_DIR}/structures/cpp")

    catch_discover_tests(${TARGET_NAME})
endforeach()
