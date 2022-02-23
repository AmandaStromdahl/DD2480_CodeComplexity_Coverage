import sys

sys.path.append("../")
from rgb_hsv_conversion import hsv_to_rgb


# Tests that the converter gives a correct value for mixed input.
def test_mixed_values():
    hue = 5.0
    sat = 0.2
    val = 0.6
    assert hsv_to_rgb(hue,sat,val) == [153,125,122]

# Tests that the converter raises an exception when improper values are supplied.
def test_improper_values():
    hue = 5.0
    sat = 1.0
    val = -0.2
    try:
        hsv_to_rgb(hue,sat,val)
        assert False
    except Exception:
        assert True

# Tests that the converter still works when all values are on the edge.
def test_edge_values():
    hue = 359.99
    sat = 0.9999
    val = 0.0001
    assert hsv_to_rgb(hue,sat,val) == [0,0,0]

# Tests that the converter still works when all values are at zero.
def test_zeroed_values():
    hue = 0.0
    sat = 0.0
    val = 0.0
    assert hsv_to_rgb(hue,sat,val) == [0,0,0]