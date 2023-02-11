Copyright 2023 Timothy Borunov

This repository features two files: mat_mult.py and mat_mult_tester.py

mat_mult.py contains a single function implemented in python with no additional libraries
which performs matrix multiplication between to input matrices. The matrices must be of the type
list of list of integers in order for the function to work. Error checking is implemented to make
sure the function will run and otherwise outputs a corresponding error message.

mat_mult_tester.py contains unit tests which assess whether mat_mult function works as intended
using pytest

In order to streamline everything, a separate run_tests.py file exists which runs mat_mult_tester.py with additional 
methods to test memory allocation and CPU profiling. This is a script that is used by github actions
