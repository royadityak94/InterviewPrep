cmake_minimum_required(VERSION 3.15)
project(Algorithms_C)

set(CMAKE_CXX_STANDARD 14)
include_directories(include)
add_executable(Algorithms_C src/main/lowest_integer_array.cpp src/main/lowest_integer_array.h src/main/catch.hpp src/main/longest_subarray_with_k_characters.cpp src/main/longest_subarray_with_k_characters.h)