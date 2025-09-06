class Piece:
    def __init__(self, name, color, position):
        self.name = name      # "xe", "ma", "tuong"...
        self.color = color    # "red" hoặc "black"
        self.position = position  # (x, y)

    def get_valid_moves(self, board):
        # Trả về danh sách nước đi hợp lệ
        pass
# piece.py

class Piece:
    def __init__(self, name, color, position):
        self.name = name          # "xe", "ma", "tuong", "si", "phao", "tot"
        self.color = color        # "red" hoặc "black"
        self.position = position  # (x, y)

    def get_valid_moves(self, board):
        # Placeholder: mỗi quân sẽ có logic riêng
        return []

    def __repr__(self):
        return f"{self.color}_{self.name}@{self.position}"

