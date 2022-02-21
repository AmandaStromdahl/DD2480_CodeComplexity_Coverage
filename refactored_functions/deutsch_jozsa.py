import numpy as np
import qiskit as q

# This algorithm is taken from the GitHub repository: https://github.com/TheAlgorithms/Python

"""
# Original version
def dj_oracle(case: str, num_qubits: int) -> q.QuantumCircuit:

    # Returns a Quantum Circuit for the Oracle function.
    # The circuit returned can represent balanced or constant function,
    # according to the arguments passed
    
    # This circuit has num_qubits+1 qubits: the size of the input,
    # plus one output qubit
    oracle_qc = q.QuantumCircuit(num_qubits + 1)

    # First, let's deal with the case in which oracle is balanced
    
    if case == "balanced":
        # First generate a random number that tells us which CNOTs to
        # wrap in X-gates:
        b = np.random.randint(1, 2**num_qubits)
        # Next, format 'b' as a binary string of length 'n', padded with zeros:
        b_str = format(b, f"0{num_qubits}b")
        # Next, we place the first X-gates. Each digit in our binary string
        # correspopnds to a qubit, if the digit is 0, we do nothing, if it's 1
        # we apply an X-gate to that qubit:
        
        for index, bit in enumerate(b_str):
            if bit == "1":
                oracle_qc.x(index)
        # Do the controlled-NOT gates for each qubit, using the output qubit
        # as the target:
        
        for index in range(num_qubits):
            oracle_qc.cx(index, num_qubits)
        # Next, place the final X-gates        
        for index, bit in enumerate(b_str):
            if bit == "1":
                oracle_qc.x(index)

    # Case in which oracle is constant
    
    if case == "constant":
        # First decide what the fixed output of the oracle will be
        # (either always 0 or always 1)
        output = np.random.randint(2)
        
        if output == 1:
            oracle_qc.x(num_qubits)

    oracle_gate = oracle_qc.to_gate()
    oracle_gate.name = "Oracle"  # To show when we display the circuit
    
    return oracle_gate
"""

# Refactored version
def dj_oracle(case: str, num_qubits: int) -> q.QuantumCircuit:
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
        
        # ----------------------------------------------------------------
        # REFACTORED: moved balanced oracle generation to helper function
        # ----------------------------------------------------------------
        oracle_qc = getBalancedOracle(oracle_qc, num_qubits)
        # ----------------------------------------------------------------
        
    # Case in which oracle is constant
    
    if case == "constant":
        # First decide what the fixed output of the oracle will be
        # (either always 0 or always 1)
        output = np.random.randint(2)
        
        if output == 1:
            oracle_qc.x(num_qubits)

    oracle_gate = oracle_qc.to_gate()
    oracle_gate.name = "Oracle"  # To show when we display the circuit
    
    return oracle_gate

# ----------------------------------------------------------------
# REFACTORED: moved code from strassen() into this helper function
# ----------------------------------------------------------------
def getBalancedOracle(oracle_qc: q.QuantumCircuit, num_qubits: int) -> q.QuantumCircuit:
    # First generate a random number that tells us which CNOTs to
    # wrap in X-gates:
    b = np.random.randint(1, 2**num_qubits)
    # Next, format 'b' as a binary string of length 'n', padded with zeros:
    b_str = format(b, f"0{num_qubits}b")
    # Next, we place the first X-gates. Each digit in our binary string
    # correspopnds to a qubit, if the digit is 0, we do nothing, if it's 1
    # we apply an X-gate to that qubit:
    
    for index, bit in enumerate(b_str):
        if bit == "1":
            oracle_qc.x(index)
    # Do the controlled-NOT gates for each qubit, using the output qubit
    # as the target:
    
    for index in range(num_qubits):
        oracle_qc.cx(index, num_qubits)
    # Next, place the final X-gates        
    for index, bit in enumerate(b_str):
        if bit == "1":
            oracle_qc.x(index)
    
    return oracle_qc
# ----------------------------------------------------------------

    """
    Lizard CCN, original version of dj_oracle(): 9
    Lizard CCN, refactored version dj_oracle(): 4  => approx. 56% cyclomatic complexity reduction
    
    (Lizard CCN, getBalancedOracle(): 6)
    """

