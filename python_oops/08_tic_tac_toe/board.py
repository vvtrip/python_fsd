class Board:
    
    EMPTY_CELL = 0
    
    def __init__(self):
        self.game_board = [[0, 0, 0],
                           [0, 0, 0],
                           [0, 0, 0]]
        
    def print_board(self):
        print("\nPositions:")
        self.print_board_with_positions()        

        print("Board:")
        for row in self.game_board:
            print("|", end="")
            for column in row:
                if column == Board.EMPTY_CELL:
                    print("   |", end="")
                else:
                    print(f" {column} |", end="")                
            print()
        print()

    def print_board_with_positions(self):
        print("| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |")

    def submit_move(self, player, move):
        row = move.get_row()
        col = move.get_column()
        value = self.game_board[row][col]
        if value == Board.EMPTY_CELL:
            self.game_board[row][col] = player.marker
        else:
            print("This position is already taken. Please take another one.")

    def is_game_over(self, player, last_move):
        return(self.check_row(player, last_move) or
               self.check_column(player, last_move) or
               self.check_diagonal(player) or
               self.check_antidiagonal(player))
    
    def check_row(self, player, last_move):
        row_index = last_move.get_row()
        return self.game_board[row_index].count(player.marker) == 3
    
    def check_column(self, player, last_move):
        counter = 0
        col_index = last_move.get_column()
        for i in range(3):
            if self.game_board[i][col_index] == player.marker:
                counter += 1

        return counter == 3
    
    def check_diagonal(self, player):
        counter = 0
        for i in range(3):
            if self.game_board[i][i] == player.marker:
                counter += 1

        return counter == 3

    def check_antidiagonal(self, player):
        counter = 0
        for i in range(3):
            if self.game_board[i][2-i] == player.marker:
                counter += 1
        return counter == 3
    
    def check_is_tie(self):

        counter = 0
        for row in self.game_board:
            counter += row.count(Board.EMPTY_CELL)
    
        return counter == 0
    
    def reset_board(self):
        self.game_board = [[0, 0, 0],
                           [0, 0, 0],
                           [0, 0, 0]]
