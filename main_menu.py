'''
Welcome to my program. This is the main menu
'''
import calendar
from main_program.mathematics import Mathematics
from main_program.distance_temprature_converter import DisTempConverters
from main_program.Calculator import Calculator
from main_program.Games.tictactoe2 import TicTacToe
from main_program.Games.TicTacToeAdvanced import TicTacToeAdvanced
from main_program.Games import Games
from main_program.areas_perimeters import AreasPerimeters

class MainMenu():
    """This is the whole programs first look"""

    @classmethod
    def print_menu(cls):
        """This is the printed menu"""
        print("1- Distance and Temprature Converters\n2- Mathematic Calculations")
        print("3 - Basic Calculator\n4 - Show Annual Calendar ")
        print("5 - Guess the number\n6 - Reverse it !\n7 - Show me the Websites !")
        print("8 - Basic Tic-Tac-Toe Game !\n9 - Advanced Tic Tac Toe ! ")
        print("10 - Area and Surface Calculators\n11 - Count Vowels\n99 - EXIT")

    @classmethod
    def quit(cls):
        """This is the quitting function"""
        raise SystemExit

    def continue_ask(self):
        """This is the continue check"""
        continue_on = True
        while continue_on:
            print("Do you want to continue Main Menu (Y/N) ? ")
            continue_ans = str(input().upper())
            if continue_ans == "Y":
                self.main()
            elif continue_ans == "N":
                self.quit()
            else:
                print("INVALID INPUT. PLEASE CHOOSE Y OR N ")
                continue

    def main(self):
        """Main menu"""
        work_on = True
        while work_on:
            self.print_menu()
            choice = input("Enter your choice : ")
            if choice == "1":
                distemcon = DisTempConverters()
                distemcon.main()

            elif choice == "2":
                mathematics = Mathematics()
                mathematics.main()

            elif choice == "3":
                calc = Calculator()
                calc.main()

            elif choice == "4":
                self.calendar()
                self.continue_ask()

            elif choice == "5":
                Games.guess_the_number()

            elif choice == "6":
                Games.negative_index()

            elif choice == "7":
                self.websites()
                self.continue_ask()

            elif choice == "8":
                tictac1 = TicTacToe()
                tictac1.game()

            elif choice == "9":
                tictac2 = TicTacToeAdvanced()
                tictac2.GameOn()

            elif choice == "10":
                area = AreasPerimeters()
                area.main()

            elif choice == "11":
                self.count_vowels()
                self.continue_ask()

            elif choice == "99":
                self.quit()

            else:
                print("\nINVALID INPUT! PLEASE CHOOSE BETWEEN 1-19 OR 99 TO EXIT\n")
                continue

    @classmethod
    def calendar(cls):
        """Shows calendar"""
        year = int(input("Enter Year : "))
        print(calendar.calendar(year))

    @classmethod
    def count_vowels(cls, vowels = 'aeıioöuü'):
        """Vowel counter"""
        sentence = input("Enter your words to find out how many vowels in there : ").casefold()
        count = {}.fromkeys(vowels,0)
        for i in sentence:
            if i in count:
                count[i] += 1
        print(count)

    @classmethod
    def websites(cls):
        """Add and show websites"""
        file1 = open("web.txt","r")
        print(file1.read())
        addwebsite = input("Do you want to enter a new website ? ( Y / N ) : ").upper()
        if addwebsite == "Y":
            addwebsite1 = input("Enter the website you want to add the list : ")
            file1 = open("web.txt","a")
            file1.write("\n" + addwebsite1)
            file1.close()
            file1 = open("web.txt","r")
            print(file1.read())

if __name__ == "__main__":
    MainMenu().main()
