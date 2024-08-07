from graphics import Window, Line, Point


def main():
    win = Window(800, 600)
    line = Line(Point(30, 30), Point(90, 30))
    win.draw_line(line, "red")
    win.wait_for_close()


main()
