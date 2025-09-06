# game.py

from board import Board
import copy





import json

def save_game(self, filename="saved_game.json"):
    data = {
        "board": [[piece.name if piece else None for piece in row] for row in self.board],
        "turn": self.turn,
        "move_history": self.move_history,
        "red_time": st.session_state.red_time,
        "black_time": st.session_state.black_time,
        "player_color": st.session_state.player_color,
    }
    with open(filename, "w") as f:
        json.dump(data, f)

def load_game(self, filename="saved_game.json"):
    import os
    if not os.path.exists(filename):
        st.warning("Không tìm thấy file lưu ván chơi.")
        return

    with open(filename, "r") as f:
        data = json.load(f)

    # Khôi phục bàn cờ
    for i in range(10):
        for j in range(9):
            name = data["board"][i][j]
            self.board[i][j] = self.create_piece(name, (i, j)) if name else None

    self.turn = data["turn"]
    self.move_history = data["move_history"]
    st.session_state.red_time = data["red_time"]
    st.session_state.black_time = data["black_time"]
    st.session_state.player_color = data["player_color"]
    st.session_state.turn_start_time = datetime.datetime.now()




def update_stats(self):
    # Tăng số trận đã chơi cho cả hai bên
    st.session_state.player_stats["Az"]["played"] += 1
    st.session_state.player_stats["Bot"]["played"] += 1

    # Cập nhật số trận thắng
    if self.winner == "Az":
        st.session_state.player_stats["Az"]["won"] += 1
    elif self.winner == "Bot":
        st.session_state.player_stats["Bot"]["won"] += 1



self.move_history = []  # Khởi tạo danh sách lịch sử nước đi

self.move_history.append((from_pos, to_pos, piece.name))



def update_time(self):
    import datetime
    now = datetime.datetime.now()
    elapsed = (now - st.session_state.turn_start_time).total_seconds()
    if self.turn == "red":
        st.session_state.red_time -= elapsed
    else:
        st.session_state.black_time -= elapsed
    st.session_state.turn_start_time = now



def evaluate_board(self):
    values = {
        "tot": 1,
        "phao": 3,
        "ma": 3,
        "xe": 5,
        "si": 2,
        "tuong": 100
    }
    score = 0
    for row in self.board.grid:
        for piece in row:
            if piece:
                val = values.get(piece.name, 0)
                if piece.color == "do":
                    score += val
                else:
                    score -= val
    return score



def get_best_move(self):
    best_score = float("inf")
    best_move = None
    for row in self.board.grid:
        for piece in row:
            if piece and piece.color == self.turn:
                moves = piece.get_valid_moves(self.board)
                for move in moves:
                    backup = self.board.clone()
                    self.move_piece(piece.position, move)
                    score = self.evaluate_board()
                    self.board = backup
                    if score < best_score:
                        best_score = score
                        best_move = (piece.position, move)
    return best_move







import random

def get_ai_move(self):
    all_moves = []
    for row in self.board.grid:
        for piece in row:
            if piece and piece.color == self.turn:
                moves = piece.get_valid_moves(self.board)
                for move in moves:
                    all_moves.append((piece.position, move))
    if all_moves:
        return random.choice(all_moves)
    return None


def make_ai_move(self):
    move = self.get_ai_move()
    if move:
        from_pos, to_pos = move
        self.move_piece(from_pos, to_pos)




def serialize(self):
    data = {
        "turn": self.turn,
        "grid": [
            [
                {
                    "name": piece.name,
                    "color": piece.color,
                    "position": piece.position
                } if piece else None
                for piece in row
            ]
            for row in self.board.grid
        ]
    }
    return data

def load_from_data(self, data):
    from pieces.xe import Xe
    from pieces.ma import Ma
    from pieces.tuong import Tuong
    from pieces.si import Si
    from pieces.phao import Phao
    from pieces.tot import Tot

    name_map = {
        "xe": Xe,
        "ma": Ma,
        "tuong": Tuong,
        "si": Si,
        "phao": Phao,
        "tot": Tot
    }

    self.turn = data["turn"]
    self.board.grid = []
    for row in data["grid"]:
        new_row = []
        for cell in row:
            if cell:
                cls = name_map[cell["name"]]
                new_row.append(cls(cell["name"], cell["color"], tuple(cell["position"])))
            else:
                new_row.append(None)
        self.board.grid.append(new_row)



class Game:
    def __init__(self):
        self.board = Board()
        self.turn = "red"
        self.history = []
        self.redo_stack = []
        self.winner = None

    def check_game_over(self):
        # Kiểm tra xem Tướng còn tồn tại không
        red_alive = False
        black_alive = False
        for row in self.board.grid:
            for piece in row:
                if piece and piece.name == "tuong":
                    if piece.color == "red":
                        red_alive = True
                    elif piece.color == "black":
                        black_alive = True

        if not red_alive:
            self.winner = "black"
        elif not black_alive:
            self.winner = "red"


def make_move(self, from_pos, to_pos):
    fx, fy = from_pos
    tx, ty = to_pos
    piece = self.board.get_piece(fx, fy)

    if not piece or piece.color != self.turn:
        return False

    valid_moves = piece.get_valid_moves(self.board)
    if (tx, ty) not in valid_moves:
        return False

    self.history.append({
        "grid": clone_grid(self.board.grid),
        "turn": self.turn
    })
    self.redo_stack.clear()

    self.board.move_piece(from_pos, to_pos)
    self.check_game_over()
    if not self.winner:
        self.switch_turn()
    return True






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
