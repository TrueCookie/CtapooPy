from graphics import *
import timeit

# funcs
# todo: init all cell (dead & alive)
# todo: cell.enable()
# todo: cell.disable()

DEAD = color_rgb(10, 10, 50)
ALIVE = color_rgb(230, 255, 230)


def is_alive(cell):
    return cell.config['fill'] == ALIVE


def init_grid(dim):
    grid = [[0 for cell in range(dim)] for line in range(dim)]
    for i in range(dim):
        for j in range(dim):
            grid[i][j] = set_cell(i, j)
    return grid


def draw_grid(grid, dim, window):
    for i in range(dim):
        for j in range(dim):
            grid[i][j].draw(window)


def set_cell(x, y):
    cell = Rectangle(Point(x, y), Point(x + 1, y + 1))
    cell.setFill(DEAD)
    return cell


def enable_cell(grid, x, y):
    grid[x][y].setFill(ALIVE)
    return grid


def disable_cell(grid, x, y):
    grid[x][y].setFill(DEAD)
    return grid


def around_coords(x, y):
    coords = list()
    coords.append(Point(x, y + 1))
    coords.append(Point(x + 1, y + 1))
    coords.append(Point(x + 1, y))
    coords.append(Point(x + 1, y - 1))
    coords.append(Point(x, y - 1))
    coords.append(Point(x - 1, y + 1))
    coords.append(Point(x - 1, y))
    coords.append(Point(x - 1, y - 1))
    return coords


def in_binding(point: Point, dim):
    return point.x in range(dim) and point.y in range(dim)


def update_grid(grid, dim):
    for i in range(dim):
        for j in range(dim):
            # check 8 cells around
            alive_count = 0
            for coord in around_coords(i, j):  # for each coord around
                if in_binding(coord, dim):
                    rcell = grid[coord.x.__int__()][coord.y.__int__()]
                    if is_alive(rcell):
                        alive_count = alive_count + 1
            # decide cell's fate
            if alive_count == 3:
                grid = enable_cell(grid, i, j)
            elif alive_count == 4:
                grid = disable_cell(grid, i, j)
    return grid


DIM = 32

win = GraphWin("grid", 600, 600)
win.setCoords(0, 0, DIM, DIM)

grid = init_grid(DIM)

# init
grid = enable_cell(grid, 10, 10)
grid = enable_cell(grid, 11, 12)
grid = enable_cell(grid, 12, 12)
grid = enable_cell(grid, 12, 13)

draw_grid(grid, DIM, win)

# update cycle
while True:
    grid = update_grid(grid, DIM)
