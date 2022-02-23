# This algorithm is taken from the GitHub repository: https://github.com/TheAlgorithms/Python

class SearchProblem:
    """
    An interface to define search problems.
    The interface will be illustrated using the example of mathematical function.
    """

    def __init__(self, x: int, y: int, step_size: int, function_to_optimize):
        """
        The constructor of the search problem.

        x: the x coordinate of the current search state.
        y: the y coordinate of the current search state.
        step_size: size of the step to take when looking for neighbors.
        function_to_optimize: a function to optimize having the signature f(x, y).
        """
        self.x = x
        self.y = y
        self.step_size = step_size
        self.function = function_to_optimize

    def score(self) -> int:
        """
        Returns the output of the function called with current x and y coordinates.
        >>> def test_function(x, y):
        ...     return x + y
        >>> SearchProblem(0, 0, 1, test_function).score()  # 0 + 0 = 0
        0
        >>> SearchProblem(5, 7, 1, test_function).score()  # 5 + 7 = 12
        12
        """
        return self.function(self.x, self.y)

    def get_neighbors(self):
        """
        Returns a list of coordinates of neighbors adjacent to the current coordinates.

        Neighbors:
        | 0 | 1 | 2 |
        | 3 | _ | 4 |
        | 5 | 6 | 7 |
        """
        step_size = self.step_size
        return [
            SearchProblem(x, y, step_size, self.function)
            for x, y in (
                (self.x - step_size, self.y - step_size),
                (self.x - step_size, self.y),
                (self.x - step_size, self.y + step_size),
                (self.x, self.y - step_size),
                (self.x, self.y + step_size),
                (self.x + step_size, self.y - step_size),
                (self.x + step_size, self.y),
                (self.x + step_size, self.y + step_size),
            )
        ]

    def __hash__(self):
        """
        hash the string representation of the current search state.
        """
        return hash(str(self))

    def __eq__(self, obj):
        """
        Check if the 2 objects are equal.
        """
        if isinstance(obj, SearchProblem):
            return hash(str(self)) == hash(str(obj))
        return False

    def __str__(self):
        """
        string representation of the current search state.
        >>> str(SearchProblem(0, 0, 1, None))
        'x: 0 y: 0'
        >>> str(SearchProblem(2, 5, 1, None))
        'x: 2 y: 5'
        """
        return f"x: {self.x} y: {self.y}"