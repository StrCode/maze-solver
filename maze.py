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
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

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
        self._cells[i][j].visited = True
        while True:
            direction_list = []

            # determine which cell(s) to visit next
            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                direction_list.append((i - 1, j))

            # right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                direction_list.append((i + 1, j))

            # bottom
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                direction_list.append((i, j + 1))

            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                direction_list.append((i, j - 1))

            # if there is nowhere to go from here
            # just break out
            if len(direction_list) == 0:
                self._draw_cell(i, j)
                return

            # randomly choose the next direction to go
            direction_index = random.randrange(len(direction_list))
            direction = direction_list[direction_index]

            # knock out walls between this cell and the next cell(s)
            # right
            if direction[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # left
            if direction[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # down
            if direction[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            # up
            if direction[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            # recursively visit the next cell
            self._break_walls_r(direction[0], direction[1])

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i: int, j: int):
        self._animate()

        self._cells[i][j].visited = True

        lst_col = self._num_cols - 1
        lst_row = self._num_rows - 1
        if i == lst_col and j == lst_row:
            return True
        direction_list = []

        # determine which cell(s) to visit next
        # left
        if i > 0:
            direction_list.append((i - 1, j))

        # right
        if i < self._num_cols - 1:
            direction_list.append((i + 1, j))

        # bottom
        if j < self._num_rows - 1:
            direction_list.append((i, j + 1))

        # up
        if j > 0:
            direction_list.append((i, j - 1))

        for direction in sorted(direction_list):
            current_cell: Cell = self._cells[i][j]
            next_cell: Cell = self._cells[direction[0]][direction[1]]
            has_wall = True

            # right
            if direction[0] == i + 1:
                if not self._cells[i + 1][j].has_left_wall:
                    has_wall = False

            # left
            if direction[0] == i - 1:
                if not self._cells[i - 1][j].has_right_wall:
                    has_wall = False

            # down
            if direction[1] == j + 1:
                if not self._cells[i][j + 1].has_top_wall:
                    has_wall = False

            # up
            if direction[1] == j - 1:
                if not self._cells[i][j - 1].has_bottom_wall:
                    has_wall = False

            if next_cell and has_wall is False and next_cell.visited is False:
                current_cell.draw_move(next_cell, False)
                result = self._solve_r(direction[0], direction[1])
                if result:
                    return True
                current_cell.draw_move(self._cells[direction[0]][direction[1]], True)

        return False

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        sleep(0.05)
