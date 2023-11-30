class Connect4:
   def __init__(self):
       self.board = [[0 for _ in range(7)] for _ in range(6)]
       self.current_player = 1

   def drop_piece(self, column):
       for row in range(5, -1, -1):
           if self.board[row][column] == 0:
               self.board[row][column] = self.current_player
               break

   def check_win(self):
       # Check horizontally
       for row in range(6):
           for col in range(4):
               if self.board[row][col] == self.board[row][col + 1] == self.board[row][col + 2] == self.board[row][col + 3] != 0:
                   return True

       # Check vertically
       for col in range(7):
           for row in range(3):
               if self.board[row][col] == self.board[row + 1][col] == self.board[row + 2][col] == self.board[row + 3][col] != 0:
                   return True

       # Check diagonally (/)
       for row in range(3):
           for col in range(4):
               if self.board[row][col] == self.board[row + 1][col + 1] == self.board[row + 2][col + 2] == self.board[row + 3][col + 3] != 0:
                   return True

       # Check diagonally (\)
       for row in range(3, 6):
           for col in range(4):
               if self.board[row][col] == self.board[row - 1][col + 1] == self.board[row - 2][col + 2] == self.board[row - 3][col + 3] != 0:
                   return True

       return False

   def print_board(self):
       for row in self.board:
           print(' '.join(str(cell) for cell in row))


def play_game():
   game = Connect4()

   while True:
       game.print_board()
       col = int(input("Player " + str(game.current_player) + ", choose a column to drop your piece: "))
       game.drop_piece(col)

       if game.check_win():
           game.print_board()
           print("Player " + str(game.current_player) + " wins!")
           break

       game.current_player = 2 if game.current_player == 1 else 1


play_game()