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

# NOTE: CNN labels: decision <number> , exit <number>


def new_generation(cells: list[list[int]]) -> list[list[int]]:
    """
    Generates the next generation for a given state of Conway's Game of Life.
    >>> new_generation(BLINKER)
    [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
    """
    next_generation = []
    # decision 1
    for i in range(len(cells)):
        next_generation_row = []
        # decision 2
        for j in range(len(cells[i])):
            # Get the number of live neighbours
            neighbour_count = 0

            # decision 3,4
            if i > 0 and j > 0:
                neighbour_count += cells[i - 1][j - 1]
            # decision 5
            if i > 0:
                neighbour_count += cells[i - 1][j]
            # decision 6, 7
            if i > 0 and j < len(cells[i]) - 1:
                neighbour_count += cells[i - 1][j + 1]
            # decision 8
            if j > 0:
                neighbour_count += cells[i][j - 1]
            # decision 9
            if j < len(cells[i]) - 1:
                neighbour_count += cells[i][j + 1]
            # decision 10, 11
            if i < len(cells) - 1 and j > 0:
                neighbour_count += cells[i + 1][j - 1]
            # decision 12
            if i < len(cells) - 1:
                neighbour_count += cells[i + 1][j]
            # decision 13, 14
            if i < len(cells) - 1 and j < len(cells[i]) - 1:
                neighbour_count += cells[i + 1][j + 1]

            # Rules of the game of life (excerpt from Wikipedia):
            # 1. Any live cell with two or three live neighbours survives.
            # 2. Any dead cell with three live neighbours becomes a live cell.
            # 3. All other live cells die in the next generation.
            #    Similarly, all other dead cells stay dead.
            alive = cells[i][j] == 1
            # decision 15,16,17,18
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


# NOTE: CNN = 18 - 1 + 2 = 19


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
