# pieces/base.py

class Piece:
    def __init__(self, name, color, position):
        self.name = name
        self.color = color
        self.position = position

    def get_valid_moves(self, board):
        return []

