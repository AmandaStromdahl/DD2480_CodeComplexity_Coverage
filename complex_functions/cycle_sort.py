# This algorithm is taken from the GitHub repository: https://github.com/TheAlgorithms/Python

"""
Code contributed by Honey Sharma
Source: https://en.wikipedia.org/wiki/Cycle_sort
"""


def cycle_sort(array: list) -> list:
    array_len = len(array)
    # decision 1
    for cycle_start in range(0, array_len - 1):
        item = array[cycle_start]

        pos = cycle_start
        # decision 2
        for i in range(cycle_start + 1, array_len):
            # decision 3
            if array[i] < item:
                pos += 1

        # decision 4
        if pos == cycle_start:
            continue

        # decision 5
        while item == array[pos]:
            pos += 1

        array[pos], item = item, array[pos]
        # decision 6
        while pos != cycle_start:
            pos = cycle_start
            # decision 7
            for i in range(cycle_start + 1, array_len):
                # decision 8
                if array[i] < item:
                    pos += 1

            # decision 9
            while item == array[pos]:
                pos += 1

            array[pos], item = item, array[pos]

    # exit 1
    return array

"""
lizard CCN: 10
Manual CCN:
    9 decisions
    1 exit
    CNN = 9 - 1 + 2 = 10
"""