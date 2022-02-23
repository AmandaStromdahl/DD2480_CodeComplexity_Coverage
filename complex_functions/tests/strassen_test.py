import sys
sys.path.append('../')
from strassen import strassen

# This test asserts that strassen() raises an exception when the dimensions
# of the matrices don't match.
def test_exception():
    test_matrix1 = [[1], [1]]
    test_matrix2 = [[1], [1]]        
    try:
        strassen(test_matrix1, test_matrix2)
        assert False
    except Exception:
        assert True
    
# This test checks the multiplication of two nxn-matrices.
# In this case n = 2. 
def test_equal_dimensions():
    test_matrix1 = [[2, 2], [2, 2]]
    test_matrix2 = [[1, 1], [1, 1]]  
    assert strassen(test_matrix1, test_matrix2) == [test_matrix1, test_matrix2]

# This test checks the multiplication of two non-quadratic matrices that have compatible 
# dimensions.
def test_no_error():
    test_matrix1 = [[1,2], [1,2], [1,2]]
    test_matrix2 = [[1,2,3], [1,2,3]]
    assert strassen(test_matrix1, test_matrix2) == [[3,6,9], [3,6,9], [3,6,9]]
