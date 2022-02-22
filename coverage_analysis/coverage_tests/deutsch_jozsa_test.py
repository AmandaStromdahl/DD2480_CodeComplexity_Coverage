from numpy import random
from numpy import array
from random import randint
import sys
sys.path.append('../')
from data_structure.coverage_tool import Coverage_tool
from data_structure.coverage_data_structure import CoverageData
from functions_analysed.deutsch_jozsa_coverage import dj_oracle

# test for generating a constant oracle
def test_constant(coverage: CoverageData):
    num_qubits = 10
    q = dj_oracle("constant", num_qubits, coverage)
    assert q.num_qubits == num_qubits + 1
    assert q.name == "Oracle"
    
# test for generating balanced oracle
def test_balanced(coverage: CoverageData):
    num_qubits = 10
    q = dj_oracle("balanced", num_qubits, coverage)
    assert q.num_qubits == num_qubits + 1
    assert q.name == "Oracle"

if __name__ == "__main__":
    tests = [test_constant, test_balanced]
    coverageTool = Coverage_tool(tests, 14)
    coverageTool.run()
    coverageTool.print_results()