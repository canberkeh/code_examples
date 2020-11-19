class TicTacToeAdvanced():
       
    def display_board(self, board):
        print("\n" *6)
        print(board[7] + " | " + board[8] + " | " + board[9])
        print("--+---+--")
        print(board[4] + " | " + board[5] + " | " + board[6])
        print("--+---+--")
        print(board[1] + " | " + board[2] + " | " + board[3])



    def player_input(self):
        marker = ' '
        while marker != "X" and marker != "O":
            marker = input("Player 1 choose X or O : ").upper()
        if marker == "X":
            return ("X","O")
        else:
            return ("O","X")


    def place_marker(self, board, marker, position):
        board[position] = marker


    def win_check(self, board, mark):


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



    def choose_first(self):
        import random
        flip = random.randint(0,1)

        if flip == 0:
            return "Player 1"
        else:
            return "Player 2"

    def space_check(self, board, position):

        return board[position] == " "


    def full_board_check(self, board):

        for i in range(1,10):
            if self.space_check(board, i):
                return False
        return True


    def player_choice(self, board, turn):

        position = 0 

        while position not in [1,2,3,4,5,6,7,8,9] or not self.space_check(board,position):
            position = int(input(turn + " Choose position : (1-9) "))
        return position

    def replay(self):

        choice = input("Do you want to play again ? Y/N ")

        return choice == "y".upper()


    def GameOn(self):
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

#print('\n'*100)    BOTH CLEARS

# def display_game(game_list):
#     print("Here is the current list")

#     for i in game_list:
#         print(i)
# display_game(game_list)

# def position_choice():
#     #This original choice value can be anything that is not an integer
#     choice = "wrong"

#     #While the choice is not a digit, keep asking.
#     while choice not in ["1", "2", "3","4","5","6","7","8","9"]:

#         #we should not convert here, otherwise we get an error on a wrong input
#         choice = input("Pick a position to replace (1,2,3,4,5,6,7,8,9): ")

#         if choice not in ["1", "2", "3","4","5","6","7","8","9"]:
#             #This clears the current output below the cell
#             #clear_output()

#             print ("Sorry, invalid choice ! ")

#         #Optionally you can clear everything after running the function
#         #clear_output()

#     #We can convert once the while loop above has confirmed we have a digit.    
#     return int(choice)


# def replacement_choice(game_list,position):

#     user_replacement = input("Type a string to place at position: ")
#     game_list[position] = user_replacement
 
#     return game_list

# def gameon_choice():

#     #This original choice value can be anything that is not a Y or N
#     choice = "wrong"

#     #While the choice is not a digit, keep asking
#     while choice not in ["Y","y","n","N"]:
        
#         #We should not conver here, otherwise we get an error on a wrong input
#         choice = input("Keep playing? (Y / N): ")

#         if choice not in ["Y", "N","y","n"]:
#             #This clears the current output below the cell
#             #clear_output()

#             print ("Sorry, invalid choice. Please choose Y or N  ")

#     if choice == "y" or choice == "Y":
#         #game is still on
#         return True
#     else:
#         #game is over
#         return False

# #variable to keep game playing
# gameon_choice()

# #first game list
# game_on = True
# game_list = [[1,2,3],[4,5,6],[7,8,9]]

# while game_on:
#     #clear any historical output and show the game list
#     #clear_output()
#     display_game(game_list)

#     #have player choose position
#     position = position_choice()

#     #Rewrite that position and update game list
#     game_list = replacement_choice(game_list,position)

#     #Clear screen and show the updated game list
#     #clear_output()
#     display_game(game_list)

#     #ask if you want to keep playing
#     game_on = gameon_choice()

# # #def tic_tac_toe():
# #     list1 = ["X", "O", "X"]
# #     list2 = ["O", "X", "O"]
# #     list3 = [" ", " ", "X"]
# #     print("***** Welcome to Tic-Tac-Toe Game ! *****")
# #     print("          ",list1)
# #     print("          ",list2)
# #     print("          ",list3)
    
# #     #Variables
    
# #     #Initial 
# #     choice = "WRONG"
# #     acceptable_range = range(0,10)
# #     within_range = False
# #     #Two conditions to check
# #     #Digit or Withing_Range == False

# #     while choice.isdigit() == False or within_range == False: #to check if the input is number and between the given range
        

# #         # Digit check
# #         choice = input("Please enter a number : ")
# #         if choice.isdigit() == False: # if its not a digit then show a warning
# #             print("Sorry, that is not a digit !")
        
# #         #Range check
# #         if choice.isdigit() == True:
# #             if int(choice) in acceptable_range:
# #                 within_range = True
# #             else:
# #                 print("Sorry, you are not in range between 1-10")
# #                 within_range = False

# #     return int(choice)


# # tic_tac_toe()