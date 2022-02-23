import sys

sys.path.append("../")

from data_structure.coverage_tool import Coverage_tool
from data_structure.coverage_data_structure import CoverageData
from functions_analysed.insertion_sort_coverage import insertion_sort


def single_element_collection_test(coverage: CoverageData):
    input = [1]
    assert insertion_sort(input, coverage) == [1]


def sorted_collection_test(coverage: CoverageData):
    input = [1, 2, 3, 4, 5, 6]
    assert insertion_sort(input, coverage) == [1, 2, 3, 4, 5, 6]


def reversed_collection_test(coverage: CoverageData):
    input = [6, 5, 4, 3, 2, 1]
    assert insertion_sort(input, coverage) == [1, 2, 3, 4, 5, 6]


def shuffled_collection_test(coverage: CoverageData):
    input = [6, 1, 7, 9, 3, 8, 2, 5, 4, 0]
    assert insertion_sort(input, coverage) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


if __name__ == "__main__":
    # run test using the coverage tool
    tests = [
        single_element_collection_test,
        sorted_collection_test,
        reversed_collection_test,
        shuffled_collection_test,
    ]
    coverageTool = Coverage_tool(tests, 4)
    coverageTool.run()
    coverageTool.print_results()
