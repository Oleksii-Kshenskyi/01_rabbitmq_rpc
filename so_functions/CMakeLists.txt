cmake_minimum_required(VERSION 3.20.0)

project(sofuncs)

set(LIB_SRC lib.cxx)
set(TEST_SRC test.cxx)

add_library(sofuncs SHARED ${LIB_SRC})

add_executable(sotest ${TEST_SRC})
set_target_properties(sotest sofuncs
                      PROPERTIES 
                      CXX_STANDARD 20 
                      CXX_STANDARD_REQUIRED ON)
target_link_libraries(sotest sofuncs)
