'''
Distance and Temprature Converters Class
'''
class DisTempConverters():
    """This class is made for converting values."""
    @classmethod
    def print_menu(cls):
        """This module is made for printing info menu"""
        print("\n***** Distance and Temprature Calculators *****")
        print("1- Km to Mile Converter\n2- Mile to Km Converter")
        print("3- Celcius to Fahrenheit Converter\n4- Fahrenheit to Celcius Converter")
        print("00- Exit to Main Menu\n99- EXIT")

    @classmethod
    def km_mile(cls):
        """This module is made for converting Kilometers to Miles"""
        print("***** WELCOME TO KM TO MILE CALCULATOR *****")
        kilometers = float(input(" Input KM : "))
        km_mile = ( kilometers * 0.621371 )
        print(f"{kilometers} KM is equal to {float(km_mile)} miles. \n**********************")

    @classmethod
    def mile_km(cls):
        """This module is made for converting Miles to Kilometers"""
        print("***** WELCOME TO MILE TO KM CALCULATOR *****")
        mile = float(input(" Input Mile : "))
        mile_km = ( mile / 0.62137119 )
        print(f"{mile} Mile is equal to {float(mile_km)} km's. \n**********************")

    @classmethod
    def cel_fah(cls):
        """This module is made for converting Celcius to Fahrenheit"""
        print("***** WELCOME TO CELCIUS TO FAHRENHEIT CALCULATOR *****")
        cel = float(input("Input Celcius : "))
        cel_fah = (cel * 1.8) + 32
        print(f"{cel} Celcius is equal to {cel_fah} Fahrenheit.\n**********************")

    @classmethod
    def fah_cel(cls):
        """This module is made for converting Celcius to Fahrenheit"""
        print("***** WELCOME TO FAHRENHEIT TO CELCIUS CALCULATOR *****")
        fah = float(input(" Input Fahrenheit : "))
        fah_cel = (fah - 32) / 1.8
        print(f"{fah} Fahrenheit is equal to {fah_cel} Celcius.\n********************** ")

    @classmethod
    def quit(cls):
        """This module is made for quit the whole program"""
        raise SystemExit

    def continue_ask(self):
        '''
        This module is made for asking continue the current menu or quit
        '''
        continue_on = True
        while continue_on:
            print("Do you want to continue Distance and Temprature Converters (Y/N) ? ")
            continue_ans = str(input().upper())
            if continue_ans == "Y":
                self.main()
            elif continue_ans == "N":
                self.quit()
            else:
                print("INVALID INPUT. PLEASE CHOOSE Y OR N ")
                continue

    def main(self):
        '''
        This module is made as menu of this class
        '''
        work_on = True
        while work_on:
            self.print_menu()
            choice = input("Enter your choice : ")

            if choice == "1":
                self.km_mile()
                self.continue_ask()

            elif choice == "2":
                self.mile_km()
                self.continue_ask()

            elif choice == "3":
                self.cel_fah()
                self.continue_ask()

            elif choice == "4":
                self.fah_cel()
                self.continue_ask()

            # elif choice == "00":
            #     mainprg = MainMenu()
            #     mainprg.Main()

            elif choice == "99":
                self.quit()

            else:
                print("INVALID INPUT! PLEASE CHOOSE BETWEEN 1-19 OR 99 TO EXIT")
                continue
