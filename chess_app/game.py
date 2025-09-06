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
