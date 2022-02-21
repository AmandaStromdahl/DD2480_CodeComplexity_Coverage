import pytest
from .coverage_data_structure import CoverageData
import random

# the constructor should raise an error when the number of branches in <= 0
def test_0_branch():
    with pytest.raises(ValueError):
        CoverageData(0)

# the access sequence and data should be "empty" when no log is done
def test_no_log():
    coverage = CoverageData(1)
    assert coverage.get_access_sequence() == []
    assert coverage.get_data() == {}

# the log_branch method should raise an error when the id is bigger than the number of branches
def test_wrong_id():
    coverage = CoverageData(1)
    with pytest.raises(IndexError):
        coverage.log_branch("branch", 2)

# the log_branch method should raise an error when the type is invalid
def test_wrong_type():
    coverage = CoverageData(1)
    with pytest.raises(NameError):
        coverage.log_branch("invalid_type", 1)

# test that the first log of a branch is correctly initialized and correctly log
def test_first_log():
    coverage = CoverageData(1)
    coverage.log_branch("branch", 1)
    assert coverage.get_access_sequence() == [1]
    assert coverage.get_data() == {1: {"type" : "branch", "total": 1}}

# test that random multiple logs works
def test_multiple_logs():
    nb = random.randint(1, 10)
    coverage = CoverageData(nb)
    access_sequence = []
    data = {}
    nb_logs = random.randint(1, 100)
    for i in range(nb_logs):
        id = random.randint(1, nb)
        access_sequence.append(id)
        if not id in data:
            if random.randint(0, 1) == 0:
                type = "branch"
            else:
                type = "exit"
            data[id] = {"type": type, "total": 1}
        else:
            data[id]["total"] = data[id]["total"] + 1
        coverage.log_branch(data[id]["type"], id)
    result_sequence = coverage.get_access_sequence()
    assert len(result_sequence) == len(access_sequence)
    result_data = coverage.get_data()
    assert len(result_data) == len(data)
    for i in range(nb_logs):
        assert access_sequence[i] == result_sequence[i]
    for id in range(1, nb + 1):
        if not id in data:
            assert not id in result_data
        else:
            assert result_data[id] == data[id]
    