# pieces/xe.py

from pieces.base import Piece

class Xe(Piece):
    def get_valid_moves(self, board):
        x, y = self.position
        moves = []

        # Đi lên
        for i in range(x - 1, -1, -1):
            if board.grid[i][y] is None:
                moves.append((i, y))
            elif board.grid[i][y].color != self.color:
                moves.append((i, y))
                break
            else:
                break

        # Đi xuống
        for i in range(x + 1, 10):
            if board.grid[i][y] is None:
                moves.append((i, y))
            elif board.grid[i][y].color != self.color:
                moves.append((i, y))
                break
            else:
                break

        # Đi trái
        for j in range(y - 1, -1, -1):
            if board.grid[x][j] is None:
                moves.append((x, j))
            elif board.grid[x][j].color != self.color:
                moves.append((x, j))
                break
            else:
                break

        # Đi phải
        for j in range(y + 1, 9):
            if board.grid[x][j] is None:
                moves.append((x, j))
            elif board.grid[x][j].color != self.color:
                moves.append((x, j))
                break
            else:
                break

        return moves

