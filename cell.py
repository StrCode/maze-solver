from graphics import Line, Point, Window


class Cell:
    def __init__(self, win: Window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)

    def _get_center(self):
        if self._x1 is None or self._x2 is None or self._y1 is None or self._y2 is None:
            return None

        y_center = self._x1 + abs(self._x2 - self._x1) // 2
        x_center = self._y1 + abs(self._y2 - self._y1) // 2

        return Point(x_center, y_center)

    def draw_move(self, to_cell, undo=False):
        from_center = self._get_center()
        to_center = to_cell._get_center()

        if from_center is not None and to_center is not None:
            fill_color = "red"
            if undo:
                fill_color = "gray"

            line = Line(from_center, to_center)
            self._win.draw_line(line, fill_color)
