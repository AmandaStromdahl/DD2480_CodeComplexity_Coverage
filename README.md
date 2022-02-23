# DD2480_CodeComplexity_Coverage
A project repository for the third assignment for the course [DD2480 Software Engineering Fundamentals](https://www.kth.se/student/kurser/kurs/DD2480) at [KTH](https://www.kth.se/) (group 27, Spring semester 2022).

## Description

The purpose of this assignment was to analyse the code complexity and test coverage of an open source project. We chose to the repository [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) which is a collection of different implementations of algorithms from many different fields. The repository exists for educational purposes, that this is not a piece of production software used by other pieces of software. 

## The Content

This repos consist of a report and 3 subfolder with code pertaining to the complexity -and coverage analysis of [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python).

### The Report 

The main piece of interesting content in this repository can be found in the report which can be found [here](./report.md). In this document we thoroughly document the different findings related to the assignment. This is the recommended entry point for consuming this repo, as the report will link out to necessary files while providing more context.

### complex_functions

- This folder contains files from [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) which contains the functions we were interested in and related helper functions.
- The subfolder `tests` contains tests of some of the functions that is meant to be run with the coverage tool [Coverage.py](https://coverage.readthedocs.io/en/6.3.2/) and the testing framework [pytest](https://docs.pytest.org/en/7.0.x/). These tests exists to compare with our own ad-hoc coverage-tool (see [here](#coverage_analysis))
    - In order to see the test coverage run the commands,  
    ```bash
    $ covarge run -m pytest <test-file>.py
    $ covarge report 
    ```


### coverage_analysis

- This folder contain three subfolders `coverage_tests`, `data_structure`, `function_analysed`
   - `coverage_tests` contains tests of functions using our own ad-hoc coverage tool.
      - The coverage tool is embedded in the functions so the a test file is simply run using python,
      ```bash
      $ python <test-file>.py
      ```

   - `data_structure` contains the implementation of our ad-hoc coverage_tool
      - As previously described, this tool is implemented as a library that you have to call from the function that you are analyzing.

   - `analysed_functions` contains the functions from [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) to be analysed with our coverage tool.
      - The functions have been modified slightly to use our coverage tool 

### refactored_functions
  
This folder contains refactored versions of functions from [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python). The purpose of the refactoring was to reduce the code complexity and improve readability of the functions. 
