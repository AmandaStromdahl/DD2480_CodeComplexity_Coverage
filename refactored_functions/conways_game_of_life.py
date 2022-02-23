# This algorithm is taken from the GitHub repository: https://github.com/TheAlgorithms/Python

"""
Conway's Game of Life implemented in Python.
https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
"""
from __future__ import annotations

from PIL import Image

# Define glider example
GLIDER = [
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

# Define blinker example
BLINKER = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]


'''
ORIGINAL VERSION:
def new_generation(cells: list[list[int]]) -> list[list[int]]:
    """
    Generates the next generation for a given state of Conway's Game of Life.
    >>> new_generation(BLINKER)
    [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
    """
    next_generation = []
    for i in range(len(cells)):
        next_generation_row = []
        for j in range(len(cells[i])):
            # Get the number of live neighbours
            neighbour_count = 0

            if i > 0 and j > 0:
                neighbour_count += cells[i - 1][j - 1]
            if i > 0:
                neighbour_count += cells[i - 1][j]
            if i > 0 and j < len(cells[i]) - 1:
                neighbour_count += cells[i - 1][j + 1]
            if j > 0:
                neighbour_count += cells[i][j - 1]
            if j < len(cells[i]) - 1:
                neighbour_count += cells[i][j + 1]
            if i < len(cells) - 1 and j > 0:
                neighbour_count += cells[i + 1][j - 1]
            if i < len(cells) - 1:
                neighbour_count += cells[i + 1][j]
            if i < len(cells) - 1 and j < len(cells[i]) - 1:
                neighbour_count += cells[i + 1][j + 1]

            # Rules of the game of life (excerpt from Wikipedia):
            # 1. Any live cell with two or three live neighbours survives.
            # 2. Any dead cell with three live neighbours becomes a live cell.
            # 3. All other live cells die in the next generation.
            #    Similarly, all other dead cells stay dead.
            alive = cells[i][j] == 1
            if (
                (alive and 2 <= neighbour_count <= 3)
                or not alive
                and neighbour_count == 3
            ):
                next_generation_row.append(1)
            else:
                next_generation_row.append(0)

        next_generation.append(next_generation_row)
    # exit 1
    return next_generation

'''


def active_neighbours(cells, x, y):
    """
    Counts how many of the surrounding cells are on.
    """
    neighbour_count = 0

    for (dx, dy) in [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, -1),
    ]:
        if x + dx < 0 or x + dx > len(cells[x]) - 1:
            continue
        if y + dy < 0 or y + dy > len(cells) - 1:
            continue
        neighbour_count += cells[y + dy][x + dx]
    return neighbour_count


def cell_should_be_on(alive, neighbour_count):
    """
    Checks if a cell should be on in accordance to the rules of game of life.
    ----
    Rules of the game of life (excerpt from Wikipedia):
    1. Any live cell with two or three live neighbours survives.
    2. Any dead cell with three live neighbours becomes a live cell.
    3. All other live cells die in the next generation.
       Similarly, all other dead cells stay dead.
    """
    return (alive and 2 <= neighbour_count <= 3) or not alive and neighbour_count == 3


def new_generation(cells: list[list[int]]) -> list[list[int]]:
    """
    Generates the next generation for a given state of Conway's Game of Life.
    >>> new_generation(BLINKER)
    [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
    """
    next_generation = []
    for y in range(len(cells)):
        next_generation_row = []
        for x in range(len(cells[y])):
            # Get the number of live neighbours
            neighbour_count = active_neighbours(cells, x, y)

            alive = cells[y][x] == 1
            if cell_should_be_on(alive, neighbour_count):
                next_generation_row.append(1)
            else:
                next_generation_row.append(0)

        next_generation.append(next_generation_row)
    # exit 1
    return next_generation


def generate_images(cells: list[list[int]], frames: int) -> list[Image.Image]:
    """
    Generates a list of images of subsequent Game of Life states.
    """
    images = []
    for _ in range(frames):
        # Create output image
        img = Image.new("RGB", (len(cells[0]), len(cells)))
        pixels = img.load()

        # Save cells to image
        for x in range(len(cells)):
            for y in range(len(cells[0])):
                colour = 255 - cells[y][x] * 255
                pixels[x, y] = (colour, colour, colour)

        # Save image
        images.append(img)
        cells = new_generation(cells)
    return images


if __name__ == "__main__":
    images = generate_images(GLIDER, 16)
    images[0].save("out.gif", save_all=True, append_images=images[1:])
