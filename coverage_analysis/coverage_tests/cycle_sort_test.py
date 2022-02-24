from numpy import random
from random import randint
import sys
sys.path.append('../')
from data_structure.coverage_tool import Coverage_tool
from data_structure.coverage_data_structure import CoverageData
from functions_analysed.cycle_sort_coverage import cycle_sort

'''
The cycle_sort() method should sort a specific list without
any problems. The reason this unique test list has been chosen since
it has the particularity that its execution on cycle_sort()
covers all the branches of the method
'''
def test_all_branches(coverage: CoverageData):
    test_list = [54, 50, 57, 33, 50, 50, 8, 31, 13, 2]
    assert cycle_sort(test_list, coverage) == sorted(test_list)

'''
The cycle_sort() method should sort any random list. This test
creates a list of random size and random values. The advantage
of random tests like this one is that it can sometimes raise
some problems or errors that no one thought about before
'''
def test_random_list(coverage: CoverageData):
    test_list = random.randint(100, size=(randint(1, 100))).tolist()
    assert cycle_sort(test_list, coverage) == sorted(test_list)

if __name__ == "__main__":
    tests = [test_all_branches, test_random_list]
    coverageTool = Coverage_tool(tests, 16)
    coverageTool.run()
    coverageTool.print_results()