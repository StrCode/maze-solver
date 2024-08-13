from cell import Cell
from time import sleep

from graphics import Window


class Maze:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win: Window
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win

        self._create_cells()

    def _create_cells(self):
        self._cells = [
            [Cell(self._win) for _ in range(self._num_rows)]
            for _ in range(self._num_cols)
        ]
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

        # self._draw_cell(self.cell_size_x, self.cell_size_y)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

        # start_x = self.x1
        # start_y = self.y1
        # for cell_list in self._cells:
        #     for cell in cell_list:
        #         cell.draw(start_x, start_y, start_x + i, start_y + j)
        #         self._animate()
        #         start_x += i
        #     start_y += self.cell_size_y
        #     start_x = self.x1

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        sleep(0.05)
