# game.py

from board import Board
import copy

def clone_grid(grid):
    return [[copy.deepcopy(cell) for cell in row] for row in grid]


def make_move(self, from_pos, to_pos):
    fx, fy = from_pos
    tx, ty = to_pos
    piece = self.board.get_piece(fx, fy)

    if not piece or piece.color != self.turn:
        return False

    valid_moves = piece.get_valid_moves(self.board)
    if (tx, ty) not in valid_moves:
        return False

    # Lưu trạng thái trước khi đi
    self.history.append({
        "grid": clone_grid(self.board.grid),
        "turn": self.turn
    })
    self.redo_stack.clear()

    self.board.move_piece(from_pos, to_pos)
    self.switch_turn()
    return True


def undo(self):
    if not self.history:
        return False
    last_state = self.history.pop()
    self.redo_stack.append({
        "grid": clone_grid(self.board.grid),
        "turn": self.turn
    })
    self.board.grid = clone_grid(last_state["grid"])
    self.turn = last_state["turn"]
    return True

def redo(self):
    if not self.redo_stack:
        return False
    next_state = self.redo_stack.pop()
    self.history.append({
        "grid": clone_grid(self.board.grid),
        "turn": self.turn
    })
    self.board.grid = clone_grid(next_state["grid"])
    self.turn = next_state["turn"]
    return True



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
