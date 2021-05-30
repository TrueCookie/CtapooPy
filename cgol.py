import msvcrt
import threading

from graphics import *
from time import sleep

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


def is_inside(point, cell):
    dl = cell.getP1()  # down left corner
    ur = cell.getP2()  # up right corner
    return dl.getX() < point.getX() < ur.getX() and dl.getY() < point.getY() < ur.getY()


def feel_click(grid, point, dim):
    for i in range(dim):
        for j in range(dim):
            if is_inside(point, grid[i][j]):
                enable_cell(grid, point.getX().__int__(), point.getY().__int__())
                return grid


def get_kbinput():
    global flag
    keystrk = input('Press a key \n')
    # key doesn't continue until key is pressed
    print("You just pressed: ", keystrk)
    flag = False
    print('flag: ', flag)

def get_clicks(grid):
    global flag
    while flag:
        click_point = win.getMouse()
        grid = feel_click(grid, click_point, DIM)


DIM = 32

win = GraphWin("grid", 600, 600)
win.setCoords(0, 0, DIM, DIM)

# default grid init
grid = init_grid(DIM)

grid = enable_cell(grid, 20, 20)
grid = enable_cell(grid, 21, 18)
grid = enable_cell(grid, 23, 18)
grid = enable_cell(grid, 22, 18)
grid = enable_cell(grid, 21, 20)

# draw
draw_grid(grid, DIM, win)

# live cells init todo: add enable cells by mouse clicking
# flag = True
# main_loop = threading.Thread(target=get_clicks, args=[grid])
# exit_loop = threading.Thread(target=get_kbinput)
#
# main_loop.start()
# exit_loop.start()

# update cycle
sleep(2)
while True:
    grid = update_grid(grid, DIM)
    sleep(0.25)
