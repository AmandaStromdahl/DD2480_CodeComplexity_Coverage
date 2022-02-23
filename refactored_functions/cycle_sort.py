# This algorithm is taken from the GitHub repository: https://github.com/TheAlgorithms/Python

'''
# Original version
def cycle_sort(array: list) -> list:
    array_len = len(array)
    for cycle_start in range(0, array_len - 1):
        item = array[cycle_start]

        pos = cycle_start
        for i in range(cycle_start + 1, array_len):
            if array[i] < item:
                pos += 1

        if pos == cycle_start:
            continue

        while item == array[pos]:
            pos += 1

        array[pos], item = item, array[pos]
        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start + 1, array_len):
                if array[i] < item:
                    pos += 1

            while item == array[pos]:
                pos += 1

            array[pos], item = item, array[pos]

    return array
'''

# ----------------------------------------------------------------
# REFACTORED: moved code from cycle_sort() into this helper function
# ----------------------------------------------------------------
def find_pos(array, cycle_start, item):
    pos = cycle_start
    for i in range(cycle_start + 1, len(array)):
        if array[i] < item:
            pos += 1
    return pos

# ----------------------------------------------------------------
# REFACTORED: moved code from cycle_sort() into this helper function
# ----------------------------------------------------------------
def place_item(array, pos, item):
    while item == array[pos]:
        pos += 1
    array[pos], item = item, array[pos]
    return item, pos

# ----------------------------------------------------------------
# REFACTORED: moved code from cycle_sort() into this helper function
# ----------------------------------------------------------------
def do_cycle(array, cycle_start, pos, item):
    while pos != cycle_start:
        pos = find_pos(array, cycle_start, item)
        item, pos = place_item(array, pos, item)
    return

# Refactored version
def cycle_sort(array: list) -> list:
    array_len = len(array)
    for cycle_start in range(0, array_len - 1):
        item = array[cycle_start]

        pos = find_pos(array, cycle_start, item)
        if pos == cycle_start:
            continue
        item, pos = place_item(array, pos, item)
        
        do_cycle(array, cycle_start, pos, item)

    return array

"""
Lizard CCN, original version of cycle_sort(): 10
Lizard CCN, refactored version of cycle_sort(): 3 => 70% cyclomatic complexity reduction
(Lizard CCN, find_pos(): 3)
(Lizard CCN, place_item(): 2)
(Lizard CCN, do_cycle(): 2)

Manual CCN, original version of cycle_sort(): 10
Manual CCN, refactored version of cycle_sort(): 3 (2 decisions - 1 exit + 2)
(Manual CCN, find_pos(): 3 (2 decisions - 1 exit + 2))
(Manual CCN, place_item(): 2 (1 decision - 1 exit + 2))
(Manual CCN, do_cycle(): 2 (1 decision - 1 exit + 2))
"""