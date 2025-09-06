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

