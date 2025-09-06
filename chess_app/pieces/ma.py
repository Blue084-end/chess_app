# pieces/ma.py

from pieces.base import Piece

class Ma(Piece):
    def get_valid_moves(self, board):
        x, y = self.position
        moves = []

        # Các hướng đi của mã
        directions = [
            ((-2, -1), (-1, 0)), ((-2, 1), (-1, 0)),
            ((2, -1), (1, 0)), ((2, 1), (1, 0)),
            ((-1, -2), (0, -1)), ((1, -2), (0, -1)),
            ((-1, 2), (0, 1)), ((1, 2), (0, 1))
        ]

        for (dx, dy), (block_x, block_y) in directions:
            bx, by = x + block_x, y + block_y
            tx, ty = x + dx, y + dy
            if 0 <= tx < 10 and 0 <= ty < 9:
                if board.grid[bx][by] is None:
                    target = board.grid[tx][ty]
                    if target is None or target.color != self.color:
                        moves.append((tx, ty))

        return moves

