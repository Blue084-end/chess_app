
# pieces/tuong.py

from pieces.base import Piece

class Tuong(Piece):
    def get_valid_moves(self, board):
        x, y = self.position
        moves = []
        palace_x = range(0, 3) if self.color == "black" else range(7, 10)
        palace_y = range(3, 6)

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx in palace_x and ny in palace_y:
                target = board.grid[nx][ny]
                if target is None or target.color != self.color:
                    moves.append((nx, ny))
        return moves
