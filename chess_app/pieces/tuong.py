# pieces/tuong.py (bổ sung cho Tượng)

class Tuong(Piece):
    def get_valid_moves(self, board):
        x, y = self.position
        moves = []
        directions = [(-2, -2), (-2, 2), (2, -2), (2, 2)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            mx, my = x + dx // 2, y + dy // 2  # ô giữa
            if 0 <= nx < 10 and 0 <= ny < 9:
                # Không qua sông
                if self.color == "red" and nx < 5:
                    continue
                if self.color == "black" and nx > 4:
                    continue
                # Không bị cản
                if board.grid[mx][my] is None:
                    target = board.grid[nx][ny]
                    if target is None or target.color != self.color:
                        moves.append((nx, ny))
        return moves

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
