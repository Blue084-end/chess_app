# pieces/tot.py

from pieces.base import Piece

class Tot(Piece):
    def get_valid_moves(self, board):
        x, y = self.position
        moves = []

        # Đi thẳng
        dx = -1 if self.color == "black" else 1
        nx = x + dx
        if 0 <= nx < 10:
            target = board.grid[nx][y]
            if target is None or target.color != self.color:
                moves.append((nx, y))

        # Qua sông thì được đi ngang
        if (self.color == "red" and x < 5) or (self.color == "black" and x > 4):
            for dy in [-1, 1]:
                ny = y + dy
                if 0 <= ny < 9:
                    target = board.grid[x][ny]
                    if target is None or target.color != self.color:
                        moves.append((x, ny))

        return moves

