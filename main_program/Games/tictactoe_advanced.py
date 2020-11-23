'''
Tictactoe game. Allows to choose marker X or O at the beginning.
'''
import random
class TictactoeAdvanced():
    """game class"""
    @classmethod
    def display_board(cls, board):
        """Displaying board at beginning and every turn."""
        print("\n" *6)
        print(board[7] + " | " + board[8] + " | " + board[9])
        print("--+---+--")
        print(board[4] + " | " + board[5] + " | " + board[6])
        print("--+---+--")
        print(board[1] + " | " + board[2] + " | " + board[3])

    @classmethod
    def player_input(cls):
        """Marker choice"""
        marker = ' '
        while marker != "X" and marker != "O":
            marker = input("Player 1 choose X or O : ").upper()
        if marker == "X":
            return ("X","O")
        else:
            return ("O","X")

    @classmethod
    def place_marker(cls, board, marker, position):
        """Places marker to the wanted position on board"""
        board[position] = marker

    @classmethod
    def win_check(cls, board, mark):
        """Win check for OOO or xxx or Tie on board"""
        if board[1] == mark and board[2] == mark and board[3] == mark:
            print("Congratz "+ mark + "you won the game! ")
            return True
        elif board[4] == mark and board[5] == mark and board[6] == mark:
            print("Congratz "+ mark + "you won the game! ")
            return True
        elif board[7] == mark and board[8] == mark and board[9] == mark:
            print("Congratz "+ mark + "you won the game! ")
            return True
        elif board[1] == mark and board[4] == mark and board[7] == mark:
            print("Congratz "+ mark + "you won the game! ")
            return True
        elif board[2] == mark and board[5] == mark and board[8] == mark:
            print("Congratz "+ mark + "you won the game! ")
            return True
        elif board[1] == mark and board[5] == mark and board[9] == mark:
            print("Congratz "+ mark + "you won the game! ")
            return True
        elif board[3] == mark and board[5] == mark and board[7] == mark:
            print("Congratz "+ mark + "you won the game! ")
            return True

        return False

    @classmethod
    def choose_first(cls):
        """Player turn changes after one played"""
        flip = random.randint(0,1)

        if flip == 0:
            return "Player 1"
        else:
            return "Player 2"

    @classmethod
    def space_check(cls, board, position):
        """if wanted place on board is full then play again until its empty"""
        return board[position] == " "

    def full_board_check(self, board):
        """if the board is full then stop the game"""
        for i in range(1,10):
            if self.space_check(board, i):
                return False
        return True

    def player_choice(self, board, turn):
        """puts marker on the wanted position on board"""
        position = 0

        while position not in [1,2,3,4,5,6,7,8,9] or not self.space_check(board,position):
            position = int(input(turn + " Choose position : (1-9) "))
        return position

    @classmethod
    def replay(cls):
        """Asks to play again after game ended or tied"""
        choice = input("Do you want to play again ? Y/N ")

        return choice == "y".upper()

    def game_on(self):
        """Main program"""
        print("Welcome to Tic TAC TOE ")

        while True:
            the_board = [" "]*10
            player1_marker,player2_marker = self.player_input()

            turn = self.choose_first()
            print(turn + " will go first")

            play_game = input("Ready to play ? Y/N").upper()

            if play_game == "Y":
                game_on = True
            else:
                game_on = False

            while game_on:
                if turn == "Player 1":
                    self.display_board(the_board)
                    position = self.player_choice(the_board, turn)

                    self.place_marker(the_board, player1_marker,position)

                    if self.win_check(the_board, player1_marker):
                        self.display_board(the_board)
                        print("Player 1 has Won !")
                        game_on = False
                    else:
                        if self.full_board_check(the_board):
                            self.display_board(the_board)
                            print("Its a TIE ")
                            game_on = False
                        else:
                            turn = "Player 2"
                else:
                    self.display_board(the_board)
                    position = self.player_choice(the_board, turn)

                    self.place_marker(the_board, player2_marker,position)

                    if self.win_check(the_board, player2_marker):
                        self.display_board(the_board)
                        print("Player 2 has Won !")
                        game_on = False
                    else:
                        if self.full_board_check(the_board):
                            self.display_board(the_board)
                            print("Its a TIE ")
                            game_on = False
                        else:
                            turn = "Player 1"

            if not self.replay():
                break
