# game.py

from board import Board

class Game:
    def __init__(self):
        self.board = Board()
        self.turn = "red"
        self.history = []

    def make_move(self, from_pos, to_pos):
        fx, fy = from_pos
        tx, ty = to_pos
        piece = self.board.get_piece(fx, fy)

        # Kiểm tra có quân ở vị trí xuất phát
        if not piece:
            return False

        # Kiểm tra đúng lượt
        if piece.color != self.turn:
            return False

        # Lấy danh sách nước đi hợp lệ
        valid_moves = piece.get_valid_moves(self.board)

        # Kiểm tra nước đi có hợp lệ không
        if (tx, ty) not in valid_moves:
            return False

        # Thực hiện di chuyển
        self.board.move_piece(from_pos, to_pos)
        self.history.append((from_pos, to_pos))
        self.switch_turn()
        return True

    def switch_turn(self):
        self.turn = "black" if self.turn == "red" else "red"

    def restart(self):
        self.board = Board()
        self.turn = "red"
        self.history.clear()



class Game:
    def __init__(self):
        self.board = Board()
        self.turn = "red"
        self.history = []

    def make_move(self, from_pos, to_pos):
        # Kiểm tra hợp lệ, cập nhật bàn cờ
        pass

    def restart(self):
        self.board.setup_initial_position()
        self.turn = "red"
        self.history.clear()

# game.py

from board import Board

class Game:
    def __init__(self):
        self.board = Board()
        self.turn = "red"
        self.history = []

    def make_move(self, from_pos, to_pos):
        fx, fy = from_pos
        piece = self.board.get_piece(fx, fy)
        if piece and piece.color == self.turn:
            moved = self.board.move_piece(from_pos, to_pos)
            if moved:
                self.history.append((from_pos, to_pos))
                self.switch_turn()
                return True
        return False

    def switch_turn(self):
        self.turn = "black" if self.turn == "red" else "red"

    def restart(self):
        self.board = Board()
        self.turn = "red"
        self.history.clear()
