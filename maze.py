from cell import Cell
from time import sleep
import random


class Maze:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self.seed = seed

        if self.seed is not None:
            random.seed(self.seed)

        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        self._cells = [
            [Cell(self._win) for _ in range(self._num_rows)]
            for _ in range(self._num_cols)
        ]
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        lst_col = self._num_cols - 1
        lst_row = self._num_rows - 1
        self._cells[lst_col][lst_row].has_bottom_wall = False
        self._draw_cell(lst_col, lst_row)

    def _break_walls_r(self, i: int, j: int):
        first_cell = self._cells[i][j]
        first_cell.visited = True
        while True:
            to_visit = []
            adjacent_left = self._cells[i - 1][j]
            adjacent_right = self._cells[i + 1][j]
            adjacent_bottom = self._cells[i][j + 1]
            adjacent_top = self._cells[i][j - 1]

            if adjacent_left and adjacent_left.visited is False:
                to_visit.append(adjacent_left)

            if adjacent_right and adjacent_right.visited is False:
                to_visit.append(adjacent_right)

            if adjacent_bottom and adjacent_bottom.visited is False:
                to_visit.append(adjacent_bottom)

            if adjacent_top and adjacent_top.visited is False:
                to_visit.append(adjacent_top)

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return
            else:
                rand_num = random.randrange(0, len(to_visit))
                selected_cell = to_visit[rand_num]

                # TODO: create a function that knocks down walls between current and selected cell

                print(selected_cell)

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        sleep(0.05)
