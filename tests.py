from maze import Maze


class Tests:
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, None)
        assert len(m1._cells) == num_cols
        assert len(m1._cells[0]) == num_rows

    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 13, 15, None)
        assert len(m1._cells) == num_cols
        assert len(m1._cells[0]) == num_rows

    def test_maze_check_entrance_break(self):
        num_cols = 5
        num_rows = 6
        m1 = Maze(0, 0, num_rows, num_cols, 12, 12, None)
        m1._break_entrance_and_exit()
        entrance_cell = m1._cells[0][0]
        assert entrance_cell.has_top_wall is False

    def test_maze_check_exit_break(self):
        num_cols = 5
        num_rows = 6
        m1 = Maze(0, 0, num_rows, num_cols, 12, 12, None)
        m1._break_entrance_and_exit()
        exit_cell = m1._cells[num_cols - 1][num_rows - 1]
        assert exit_cell.has_bottom_wall is False

    def test_reset_visited_cells(self):
        num_cols = 5
        num_rows = 6
        m1 = Maze(0, 0, num_rows, num_cols, 12, 12, None)
        m1._break_entrance_and_exit()
        for col in m1._cells:
            for cell in col:
                assert cell.visited is False
