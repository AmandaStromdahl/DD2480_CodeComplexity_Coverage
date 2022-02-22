import numpy as np
import qiskit as q
import sys
sys.path.append('../')
from data_structure.coverage_data_structure import CoverageData

# This algorithm is taken from the GitHub repository: https://github.com/TheAlgorithms/Python

def dj_oracle(case: str, num_qubits: int, coverage: CoverageData) -> q.QuantumCircuit:
    """
    Returns a Quantum Circuit for the Oracle function.
    The circuit returned can represent balanced or constant function,
    according to the arguments passed
    """
    # This circuit has num_qubits+1 qubits: the size of the input,
    # plus one output qubit
    oracle_qc = q.QuantumCircuit(num_qubits + 1)

    # First, let's deal with the case in which oracle is balanced
    
    if case == "balanced":
        coverage.log_branch("branch", 1)
        # First generate a random number that tells us which CNOTs to
        # wrap in X-gates:
        b = np.random.randint(1, 2**num_qubits)
        # Next, format 'b' as a binary string of length 'n', padded with zeros:
        b_str = format(b, f"0{num_qubits}b")
        # Next, we place the first X-gates. Each digit in our binary string
        # correspopnds to a qubit, if the digit is 0, we do nothing, if it's 1
        # we apply an X-gate to that qubit:
        
        for index, bit in enumerate(b_str):  
            coverage.log_branch("branch", 2)          
            if bit == "1":
                coverage.log_branch("branch", 3)
                oracle_qc.x(index)
            else:
                coverage.log_branch("branch", 4)
        # Do the controlled-NOT gates for each qubit, using the output qubit
        # as the target:
        for index in range(num_qubits):
            coverage.log_branch("branch", 5)
            oracle_qc.cx(index, num_qubits)
            
        # Next, place the final X-gates        
        for index, bit in enumerate(b_str):
            coverage.log_branch("branch", 6)
            if bit == "1":
                coverage.log_branch("branch", 7)
                oracle_qc.x(index)
            else:
                coverage.log_branch("branch", 8)
    else:
        coverage.log_branch("branch", 9)
    # Case in which oracle is constant
    if case == "constant":
        coverage.log_branch("branch", 10)
        # First decide what the fixed output of the oracle will be
        # (either always 0 or always 1)
        output = np.random.randint(2)        
        if output == 1:
            coverage.log_branch("branch", 11)
            oracle_qc.x(num_qubits)
        else: 
            coverage.log_branch("branch", 12)
    else:
        coverage.log_branch("branch", 13)
    oracle_gate = oracle_qc.to_gate()
    oracle_gate.name = "Oracle"  # To show when we display the circuit
    coverage.log_branch("exit", 14)
    return oracle_gate