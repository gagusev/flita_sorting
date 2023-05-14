cmake_minimum_required(VERSION 3.22)
project(SORTING)

set(CMAKE_CXX_STANDARD 17)

add_executable(SORTING main.c 
                       merge_sort.h
                       selection_sort.h)