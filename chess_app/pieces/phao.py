# pieces/phao.py

from pieces.base import Piece

class Phao(Piece):
    def get_valid_moves(self, board):
        x, y = self.position
        moves = []

        def linear_moves(dx, dy):
            i, j = x + dx, y + dy
            jumped = False
            while 0 <= i < 10 and 0 <= j < 9:
                target = board.grid[i][j]
                if not jumped:
                    if target is None:
                        moves.append((i, j))
                    else:
                        jumped = True
                else:
                    if target:
                        if target.color != self.color:
                            moves.append((i, j))
                        break
                i += dx
                j += dy

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            linear_moves(dx, dy)

        return moves

