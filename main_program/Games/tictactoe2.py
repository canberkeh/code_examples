class TicTacToe():

    theBoard = { "7" : " ","8" : " ","9" : " ",
                "4" : " ","5" : " ","6" : " ",
                "1" : " ","2" : " ","3" : " " }
    
    useable_characters = [1,2,3,4,5,6,7,8,9]

    board_keys = []

    example_board = { "7" : "7" , "8" : "8" , "9" : "9",
                "4" : "4" , "5" : "5" , "6" : "6", 
                "1" : "1" , "2" : "2" , "3" : "3" }

    

    def printBoard(self, theBoard):

        for key in theBoard:
            self.board_keys.append(key)
        print("*****************  INFORMATION  *****************")
        print("*****     Welcome to Tic Tac Toe game !     *****")
        print("*****You can use your numpad like down below*****")
        print("******************* "+self.example_board["7"] + " | " + self.example_board["8"] + " | " + self.example_board["9"]+" *******************")
        print("********************--+---+--********************")
        print("******************* "+self.example_board["4"] + " | " + self.example_board["5"] + " | " + self.example_board["6"]+" *******************")
        print("********************--+---+--********************")
        print("******************* "+self.example_board["1"] + " | " + self.example_board["2"] + " | " + self.example_board["3"]+" *******************")
        print("*************************************************")
        print("*************************************************")
        print("\n")
        print(self.theBoard["7"] + " | " + self.theBoard["8"] + " | " + self.theBoard["9"])
        print("--+---+--")
        print(self.theBoard["4"] + " | " + self.theBoard["5"] + " | " + self.theBoard["6"])
        print("--+---+--")
        print(self.theBoard["1"] + " | " + self.theBoard["2"] + " | " + self.theBoard["3"])
        

    
    #starts game
    def game(self):
        turn = 'X'
        count = 0

        do_start = input("Press enter to start ")
        if do_start == "@":
            pass
        else:
            self.printBoard(self.theBoard)

        # Iteration till the 9. turn. Renewing the board everytime and changes players.
        for i in range(10):

                        
            self.printBoard(self.theBoard)
            print("It's your turn," + turn + ".Move to which place?")
            
            move = input()
            
            # If the place is filled
            if self.theBoard[move] == ' ' :
                self.theBoard[move] = turn
                count += 1
            
            else:
                print("That place is already filled.\nMove to which place?")
                continue

            # Now we will check if player X or O has won,for every move after 5 moves. 
            if count >= 5:
                if ((self.theBoard['7'] == self.theBoard['8'] == self.theBoard['9'] != ' ')or
                (self.theBoard['4'] == self.theBoard['5'] == self.theBoard['6'] != ' ')or
                (self.theBoard['1'] == self.theBoard['2'] == self.theBoard['3'] != ' ') or 
                (self.theBoard['1'] == self.theBoard['4'] == self.theBoard['7'] != ' ') or
                (self.theBoard['2'] == self.theBoard['5'] == self.theBoard['8'] != ' ') or
                (self.theBoard['3'] == self.theBoard['6'] == self.theBoard['9'] != ' ') or
                (self.theBoard['7'] == self.theBoard['5'] == self.theBoard['3'] != ' ') or
                (self.theBoard['1'] == self.theBoard['5'] == self.theBoard['9'] != ' ')):
                    self.wincheck(turn)               
                    break
        
            
            # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
            if count == 9:
                print("\nGame Over.\n")                
                print("It's a Tie!!")
            else:
                # Now we have to change the player after every move.
                if turn =='X':
                    turn = 'O'
                else:
                    turn = 'X'
        self.restart()

    def restart(self):
        # Now we will ask if player wants to restart the game or not.
        restart = input("Do want to play Again?(y/n)")
        if restart == "y" or restart == "Y":  
            for key in self.board_keys:
                self.theBoard[key] = " "

            self.game()
    #Wincheck starts after => 5. turn
    def wincheck(self, turn):
        self.printBoard(self.theBoard)
        print("\nGame Over.\n")                
        print(" **** " +turn + " won. ****")