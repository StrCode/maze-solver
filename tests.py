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
