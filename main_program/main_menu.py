'''
Welcome to my program. This is the main menu
'''
import calendar
from random import randint
import requests
from PIL import Image
from mathematics import Mathematics
from distance_temprature_converter import DisTempConverters
from games.tictactoe2 import TicTacToe
from games.tictactoe_advanced import TictactoeAdvanced
from games import games
from areas_perimeters import AreasPerimeters
from email_send import EmailApp
from tax_calculate import TaxCalculate
from exchange_office import ExchangeRates


class MainMenu():
    """ADD THE MENUS INFORMATION HERE     *************************"""

    @classmethod
    def print_menu(cls):
        """This is the printed menu"""
        print("\n\n***** Main Menu *****")
        print("1- Distance and Temprature Converters\n2- Mathematic Calculations")
        print("3- Area and Surface Calculators\n4- Show Annual Calendar")
        print("5- Browse/Add favorite website list\n6- Count Vowels")
        print("7- Download and open image\n8- Emails")
        print("9- Tax calculator\n10- Exchange Office")
        print("213- Basic Tic-Tac-Toe Game ! ")
        print("66- Games\n99- EXIT")

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

    def games_menu(self):
        """Games menu under Main Menu"""
        print("\n***** Games Menu *****")
        print("1- Guess the number\n2- Reverse it")
        print("3-\n4- TicTacToe Advanced")
        print("5- War Game Simulator")
        print("00- EXIT to Main Menu\n99- EXIT")
        work_on = True
        while work_on:
            choice = input("Enter your choice : ")
            if choice == "1":
                games.guess_the_number()
                self.games_menu()
            elif choice == "2":
                games.negative_index()
                self.games_menu()
            elif choice =="3":
                pass
            elif choice == "4":
                tictac2 = TictactoeAdvanced()
                tictac2.game_on()
                self.games_menu()
            elif choice == "5":
                import war_game
                self.games_menu()
            elif choice == "00":
                self.main()
            elif choice == "99":
                self.quit()
            else:
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
                self.main()

            elif choice == "2":
                mathematics = Mathematics()
                mathematics.main()
                self.main()

            elif choice == "3":
                area = AreasPerimeters()
                area.main()

            elif choice == "4":
                self.calendar()
                self.main()

            elif choice == "5":
                self.websites()
                self.continue_ask()

            elif choice == "66":
                self.games_menu()

            elif choice == "6":
                self.count_vowels()
                self.continue_ask()

            elif choice == "7":
                self.downloader()
                self.continue_ask()

            elif choice == "8":
                emails = EmailApp()
                emails.email()

            elif choice == "9":
                tax = TaxCalculate()
                tax.tax_rate()
                self.continue_ask()

            elif choice == "10":
                exchange = ExchangeRates()
                exchange.exchange_main() 

            elif choice == "31":
                tictac2 = TictactoeAdvanced()
                tictac2.game_on()

            elif choice == "11":
                self.count_vowels()
                self.continue_ask()

            elif choice == "32":
                tictac1 = TicTacToe()
                tictac1.game()

            elif choice == "99":
                self.quit()

            else:
                print("\nINVALID INPUT! PLEASE CHOOSE BETWEEN 1-19 OR 99 TO EXIT\n")
                continue

    @classmethod
    def calendar(cls):
        """Shows calendar"""
        work_on = True
        while work_on:
            print("\n\n***** Calendar *****")
            year = int(input("Enter Year : "))
            print(calendar.calendar(year))
            print("00- EXIT to Main Menu\n99- EXIT")
            ask = input("Enter choice :")
            if ask == "99":
                raise SystemExit
            elif ask == "00":
                break
            else:
                continue

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
        """Add and show websites. You should change directory !"""
        file1 = open("C:\\Users\\acer\\Desktop\\projects\\code_examples\\main_program\\web.txt","r")
        print(file1.read())
        addwebsite = input("Do you want to enter a new website ? (Y/N) : ").upper()
        if addwebsite == "Y":
            addwebsite1 = input("Enter the website you want to add the list : ")
            file1 = open("C:\\Users\\acer\\Desktop\\projects\\code_examples\\main_program\\web.txt","a")
            file1.write("\n" + addwebsite1)
            file1.close()
            file1 = open("C:\\Users\\acer\\Desktop\\projects\\code_examples\\main_program\\web.txt","r")
            print(file1.read())

    @classmethod
    def downloader(cls):
        """You can download any images from websites !Be aware of licences ! """
        print("\n\nYou can use this app to download images from any websites !")
        print("Your images will be downloaded at desktop with a random number name.")
        print("99- EXIT")
        image_name = randint(1,100000)
        img_url = input("Enter the full url starting with http:// : ")
        if img_url == "99":
            quit()
        downloaded_image = requests.get(f"{img_url}")
        file_name = open(f"C:\\Users\\acer\\Desktop\\{image_name}.jpg","wb")
        file_name.write(downloaded_image.content)
        file_name.close()
        program_working = True
        while program_working:

            print("Do you want to open downloaded file (Y/N) ? ")
            ask_open = str(input().upper())

            if ask_open == "Y":
                image_open = Image.open(f"C:\\Users\\acer\\Desktop\\{image_name}.jpg")
                image_open.show()

            elif ask_open == "N":
                break

            else:
                continue

if __name__ == "__main__":
    MainMenu().main()
