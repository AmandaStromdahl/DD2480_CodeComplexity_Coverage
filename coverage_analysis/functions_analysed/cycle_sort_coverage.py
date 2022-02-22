import sys
sys.path.append('../')
from data_structure.coverage_data_structure import CoverageData
# these imports are used for demonstration purpose
# from numpy import random
# from random import randint
# from data_structure.coverage_tool import Coverage_tool

# This algorithm is taken from the GitHub repository: https://github.com/TheAlgorithms/Python

def cycle_sort(array: list, coverage: CoverageData) -> list:
    coverage.log_branch("branch", 1)
    array_len = len(array)
    for cycle_start in range(0, array_len - 1):
        coverage.log_branch("branch", 2)
        item = array[cycle_start]
        pos = cycle_start
        for i in range(cycle_start + 1, array_len):
            coverage.log_branch("branch", 3)
            if array[i] < item:
                coverage.log_branch("branch", 4)
                pos += 1
            else:
                coverage.log_branch("branch", 5)
        if pos == cycle_start:
            coverage.log_branch("branch", 6)
            continue
        else:
            coverage.log_branch("branch", 7)
        while item == array[pos]:
            coverage.log_branch("branch", 8)
            pos += 1
        coverage.log_branch("branch", 9)
        array[pos], item = item, array[pos]
        while pos != cycle_start:
            coverage.log_branch("branch", 10)
            pos = cycle_start
            for i in range(cycle_start + 1, array_len):
                coverage.log_branch("branch", 11)
                if array[i] < item:
                    coverage.log_branch("branch", 12)
                    pos += 1
                else:
                    coverage.log_branch("branch", 13)
            while item == array[pos]:
                coverage.log_branch("branch", 14)
                pos += 1
            coverage.log_branch("branch", 15)
            array[pos], item = item, array[pos]
    coverage.log_branch("exit", 16)
    return array

# The code below is kept in comments in case a demonstration is needed

# if __name__ == "__main__":
#     # Example of unique run to get more detail on the access sequence
#     coverageData = CoverageData(16)
#     list = random.randint(100, size=(randint(1, 10))).tolist()
#     print(list)
#     cycle_sort(list, coverageData)
#     coverageData.print_results()