# board.py

from pieces.xe import Xe
from pieces.ma import Ma
from pieces.tuong import Tuong
from pieces.si import Si
from pieces.phao import Phao
from pieces.tot import Tot


def setup_initial_position(self):
    # Quân đen (black)
    self.grid[0] = [
        Xe("xe", "black", (0, 0)),
        Ma("ma", "black", (0, 1)),
        Tuong("tuong", "black", (0, 2)),
        Si("si", "black", (0, 3)),
        Tuong("tuong", "black", (0, 4)),
        Si("si", "black", (0, 5)),
        Tuong("tuong", "black", (0, 6)),
        Ma("ma", "black", (0, 7)),
        Xe("xe", "black", (0, 8))
    ]
    self.grid[2][1] = Phao("phao", "black", (2, 1))
    self.grid[2][7] = Phao("phao", "black", (2, 7))
    for i in range(0, 9, 2):
        self.grid[3][i] = Tot("tot", "black", (3, i))

    # Quân đỏ (red)
    self.grid[9] = [
        Xe("xe", "red", (9, 0)),
        Ma("ma", "red", (9, 1)),
        Tuong("tuong", "red", (9, 2)),
        Si("si", "red", (9, 3)),
        Tuong("tuong", "red", (9, 4)),
        Si("si", "red", (9, 5)),
        Tuong("tuong", "red", (9, 6)),
        Ma("ma", "red", (9, 7)),
        Xe("xe", "red", (9, 8))
    ]
    self.grid[7][1] = Phao("phao", "red", (7, 1))
    self.grid[7][7] = Phao("phao", "red", (7, 7))
    for i in range(0, 9, 2):
        self.grid[6][i] = Tot("tot", "red", (6, i))


class Board:
    def __init__(self):
        self.grid = [[None for _ in range(9)] for _ in range(10)]
        self.setup_initial_position()

    def setup_initial_position(self):
        # Đặt quân vào vị trí khai cuộc
        pass

    def move_piece(self, from_pos, to_pos):
        # Di chuyển quân, kiểm tra hợp lệ
        pass
# board.py

from piece import Piece

class Board:
    def __init__(self):
        self.grid = [[None for _ in range(9)] for _ in range(10)]
        self.setup_initial_position()

    def setup_initial_position(self):
        # Đặt quân khai cuộc cho cả hai bên
        self.grid[0] = [
            Piece("xe", "black", (0, 0)),
            Piece("ma", "black", (0, 1)),
            Piece("tuong", "black", (0, 2)),
            Piece("si", "black", (0, 3)),
            Piece("tuong", "black", (0, 4)),
            Piece("si", "black", (0, 5)),
            Piece("tuong", "black", (0, 6)),
            Piece("ma", "black", (0, 7)),
            Piece("xe", "black", (0, 8))
        ]
        self.grid[2][1] = Piece("phao", "black", (2, 1))
        self.grid[2][7] = Piece("phao", "black", (2, 7))
        for i in range(0, 9, 2):
            self.grid[3][i] = Piece("tot", "black", (3, i))

        self.grid[9] = [
            Piece("xe", "red", (9, 0)),
            Piece("ma", "red", (9, 1)),
            Piece("tuong", "red", (9, 2)),
            Piece("si", "red", (9, 3)),
            Piece("tuong", "red", (9, 4)),
            Piece("si", "red", (9, 5)),
            Piece("tuong", "red", (9, 6)),
            Piece("ma", "red", (9, 7)),
            Piece("xe", "red", (9, 8))
        ]
        self.grid[7][1] = Piece("phao", "red", (7, 1))
        self.grid[7][7] = Piece("phao", "red", (7, 7))
        for i in range(0, 9, 2):
            self.grid[6][i] = Piece("tot", "red", (6, i))

    def move_piece(self, from_pos, to_pos):
        fx, fy = from_pos
        tx, ty = to_pos
        piece = self.grid[fx][fy]
        if piece:
            piece.position = (tx, ty)
            self.grid[tx][ty] = piece
            self.grid[fx][fy] = None
            return True
        return False

    def get_piece(self, x, y):
        return self.grid[x][y]

