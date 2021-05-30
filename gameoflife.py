from graphics import *

win = GraphWin(width=200, height=200)
win.setCoords(0, 0, 10, 10)  # separate to 10 parts

square1 = Rectangle(Point(0, 0), Point(10, 10))  # (down_left, up_right) measured in 'parts'
square1.setFill(color=color_rgb(0, 255, 0))
square1.draw(win)
square2 = square1.clone()

win.getMouse()  # pause before closing
