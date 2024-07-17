from move import Move
from board import Board
from player import Player

class TicTacToeGame:

    def start(self):

        print("*******************************")
        print("  Welcome to Tic-Tac-Toe game  ")
        print("*******************************")

        human_player = Player()
        computer_player = Player(False)
        board = Board()

        while True:

            board.print_board()

            while True:

                player_move = human_player.get_move()
                board.submit_move(human_player, player_move)
                board.print_board()

                if board.check_is_tie():
                    print("It's a tie! ")
                    break
                elif board.is_game_over(human_player, player_move):
                    print("Awesome. You won the game")
                    break
                else:
                    computer_move = computer_player.get_move()
                    board.submit_move(computer_player, computer_move)
                    board.print_board()

                    if board.is_game_over(computer_player, computer_move):
                        print("Oops you lost")
                        break
            
            play_again = input("Would you like to play again? Enter X for YES or O for NO: ").upper()

            if play_again == "O":
                print("Bye! Come back soon 👋")
                break
            elif play_again == "X":
                self.start_new_round(board)
            else:
                print("Your input was not valid but I will assume that you want to play again. 💡")
                self.start_new_round(board)
 
    def start_new_round(self, board):
        print("*************")
        print("  New Round  ")
        print("*************")
        board.reset_board()
        board.print_board()
 
game = TicTacToeGame()
game.start()