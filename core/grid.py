# grid.py
from pygame import Rect, Surface, SRCALPHA

def create_grid(window_width, window_height, cell_width=40*5, cell_height=13*5):
    """
    Створює сітку для розміщення блоків.
    Повертає:
      - список прямокутників (grid)
      - горизонтальні лінії (horizontal)
      - вертикальні лінії (vertical)
      - surface для малювання grid_screen
    """
    grid = []
    horizontal = [Rect(x, 0, 4, window_height) for x in range(0, 1000, cell_width + cell_width // 5)]
    vertical = [Rect(0, y, window_width, 4) for y in range(0, 1000, cell_height + cell_height // 5)]

    for y in range(0, 1000 + cell_height, cell_height):
        for x in range(0, 1600, cell_width):
            grid.append(Rect(x, y, cell_width, cell_height))

    grid_screen = Surface((window_width, window_height), SRCALPHA)
    return grid, horizontal, vertical, grid_screen
