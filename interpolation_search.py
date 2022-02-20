# This algorithm is taken from the GitHub repository: https://github.com/TheAlgorithms/Python

def interpolation_search(sorted_collection, item):
    """Pure implementation of interpolation search algorithm in Python
    Be careful collection must be ascending sorted, otherwise result will be
    unpredictable
    :param sorted_collection: some ascending sorted collection with comparable items
    :param item: item value to search
    :return: index of found item or None if item is not found
    """
    left = 0
    right = len(sorted_collection) - 1
    # decision 1
    while left <= right:
        # avoid divided by 0 during interpolation
        # decision 2
        if sorted_collection[left] == sorted_collection[right]:
            # decision 3
            if sorted_collection[left] == item:
                # exit 1
                return left
            else:
                # exit 2
                return None
        point = left + ((item - sorted_collection[left]) * (right - left)) // (
            sorted_collection[right] - sorted_collection[left]
        )
        # out of range check
        # decision 4
        if point < 0 or point >= len(sorted_collection):
            # exit 3
            return None
        current_item = sorted_collection[point]
        # decision 5
        if current_item == item:
            # exit 4
            return point
        else:
            # decision 6
            if point < left:
                right = left
                left = point
            # decision 7
            elif point > right:
                left = right
                right = point
            # decision 8
            else:
                # decision 9
                if item < current_item:
                    right = point - 1
                else:
                    left = point + 1
    # exit 5
    return None

"""
lizard CCN: 10
Manual CCN:
    9 decisions
    5 exits
    CNN = 9 - 5 + 2 = 6
"""