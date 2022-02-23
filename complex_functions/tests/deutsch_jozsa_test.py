import sys
sys.path.append('../')
from deutsch_jozsa import dj_oracle

# This test checks the generation of a constant Quantum Circuit. 
# The test asserts that the Quantum Circuit has the correct number of qubits and the 
# correct name.
def test_constant():
    num_qubits = 10
    q = dj_oracle("constant", num_qubits)
    assert q.num_qubits == num_qubits + 1
    assert q.name == "Oracle"
    
# This test checks the generation of a balanced Quantum Circuit. 
# The test asserts that the Quantum Circuit has the correct number of qubits and the 
# correct name.
    num_qubits = 10
    q = dj_oracle("balanced", num_qubits)
    assert q.num_qubits == num_qubits + 1
    assert q.name == "Oracle"