from graphics import Window
from maze import Maze


def main():
    win = Window(800, 600)
    num_cols = 5
    num_rows = 5
    m1 = Maze(10, 10, num_rows, num_cols, 10, 10, win, 5)
    win.wait_for_close()


main()
