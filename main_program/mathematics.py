""" imported math and Mathematics class """
import math
class Mathematics():
    """This class is made for making math calculations"""
    @classmethod
    def print_menu(cls):
        """Printing the menu"""
        print("1- Factorial\n2- Multiplication Table\n3- Fibonacci\n4- Sum up to given num")
        print("5- Decimal to others\n6- Advanced Calculator\n7- Divide remain")
        print("8- Greatest Common Divisor\n9- Logarithm")
        print("10- Power of the given number\n11- Square Root\n12- Radian to Degree")
        print("13- Degree to Radian\n14- Radian to Sinus\n15- Radian to Cosinus")
        print("16- Radian to Tangent\n17- Sinus to Radian")
        print("18- Cosinus to Radian\n19- Tangent to Radian\n99- EXIT to Main Menu ")

    @classmethod
    def factorial(cls):
        """Calculating factorial"""
        print("***** WELCOME TO FACTORIAL CALCULATOR *****")
        num = int(input(" Input number : "))
        fact = int(input(" Input Factorial : "))
        if num < 0:
            print("Sorry, factorial does not exist for negative numbers\n**********************")
        elif num == 0:
            print("The factorial of 0 is 1\n**********************")
        else:
            for i in range(1,num + 1):
                fact = fact * i
            print("The factorial of",num,"is",fact,"\n**********************")

    @classmethod
    def multiplication_table(cls):
        """Multiplication table up to given number"""
        print("***** WELCOME TO MULTIPLICATION TABLE CALCULATOR *****")
        num1 = int(input(" Input number :"))
        for i in range(1, num1+1):
            print(num1, 'x', i , '=' , i*num1,"\n************************")

    @classmethod
    def fibonacci(cls):
        """Simple fibonacci"""
        print("***** WELCOME TO FIBONACCI CALCULATOR *****")
        nterms = int(input("How many terms? "))
        first, second = 0, 1
        count = 0
        if nterms <= 0:
            print("Please enter a positive integer")
        elif nterms == 1:
            print("Fibonacci sequence upto",nterms,":")
            print(first)
        else:
            print("Fibonacci sequence:\n")
        while count < nterms:
            print(first)
            nth = first + second
            first = second
            second = nth
            count += 1
        print("\n ***********************")

    @classmethod
    def sum_up_to_num(cls):
        """Summary up to given number"""
        print("***** WELCOME TO SUM UP TO NUMBER CALCULATOR *****")
        num1 = int(input("Enter a positive number : "))
        if num1 < 0:
            print("Enter a postive number.")
        else:
            sum1 = 0
            while num1>0:
                sum1 += num1
                num1 -= 1
            print(f"The sum is : {sum1}" )

    @classmethod
    def dec_to_others(cls):
        """Converts decimal to binary,octal and hexadecimal"""
        print("***** WELCOME DECIMAL CALCULATOR *****")
        dec = int(input("Enter the decimal number : "))
        print("The decimal value of", dec, "is: ")
        print(bin(dec), "in binary.")
        print(oct(dec), "in octal.")
        print(hex(dec), "in hexadecimal.")

    @classmethod
    def advanced_calculator(cls):
        """Calculator"""
        print("***** WELCOME TO ADVANCED CALCULATOR *****")
        calc = input("Type calculation:\n")
        print("Answer: " + str(eval(calc)))

    @classmethod
    def fmod(cls):
        """Divide remain calculate"""
        print("***** WELCOME TO DIVIDE REMAIN CALCULATOR *****")
        div = float(input("Enter the number to divide : "))
        remain = float(input("Enter the division number : "))
        result = math.fmod(div,remain)
        print(f"Answer: {result}")

    @classmethod
    def gcd(cls):
        """Greatest common divisor calculation"""
        print("***** WELCOME TO GREATEST COMMON DIVISOR CALCULATOR *****")
        first = int(input("Enter the first number : "))
        second = int(input("Enter the second number : "))
        result = math.gcd(first,second)
        print(f"The result is : {result}")

    @classmethod
    def log(cls):
        """Logarithm"""
        print("***** WELCOME TO LOG OF FIRST VALUE OF SECOND CALCULATOR *****")
        first = int(input("Enter the first number : "))
        second = int(input("Enter the second number : "))
        result = math.log(first,second)
        print(f"The result is : {result}")

    @classmethod
    def power(cls):
        """Power"""
        print("***** WELCOME TO 1. NUMBERS POWER OF 2. NUMBER CALCULATOR *****")
        first = int(input("Enter the first number : "))
        second = int(input("Enter the second number : "))
        result = math.pow(first,second)
        print(f"The result is : {result}")

    @classmethod
    def sqrt(cls):
        """SQRT"""
        print("***** WELCOME TO SQUARE ROOT CALCULATOR *****")
        number = math.sqrt(int(input("Enter the number : ")))
        print(f"The result is : {number}")

    @classmethod
    def rad_deg(cls):
        """Radian to degree convert"""
        print("***** WELCOME TO RADIAN TO DEGREE CONVERTER *****")
        number = math.degrees(float(input("Enter the radian : ")))
        print(f"Entered radian is equal to {number} degrees.")

    @classmethod
    def deg_rad(cls):
        """Degrees to radian convert"""
        print("***** WELCOME TO DEGREE TO RADIAN CONVERTER *****")
        number = math.radians(float(input("Enter the degree : ")))
        print(f"Entered degree is equal to {number} radian.")

    @classmethod
    def sin(cls):
        """Radian to sinus """
        print("***** WELCOME TO RADIAN TO SINUS CONVERTER *****")
        number = math.sin(float(input("Enter the radian : ")))
        print(f"Entered radian is equal to sin {number} .")

    @classmethod
    def cos(cls):
        """Radian to cosinus"""
        print("***** WELCOME TO RADIAN TO COSINUS CONVERTER *****")
        number = math.cos(float(input("Enter the radian : ")))
        print(f"Entered radian is equal to cos {number} .")

    @classmethod
    def tan(cls):
        """Radian to tangent"""
        print("***** WELCOME TO RADIAN TO TANGENT CONVERTER *****")
        number = math.tan(float(input("Enter the radian : ")))
        print(f"Entered radian is equal to tan {number} .")

    @classmethod
    def sin_rad(cls):
        """Sinus to radian"""
        print("***** WELCOME TO SINUS TO RADIAN CONVERTER *****")
        number = math.asin(int(input("Enter the SIN : ")))
        print(f"Entered sin is equal to radian {number} .")

    @classmethod
    def cos_rad(cls):
        """Cosinus to radian"""
        print("***** WELCOME TO COSINUS TO RADIAN CONVERTER *****")
        number = math.acos(float(input("Enter the COS : ")))
        print(f"Entered cos is equal to radian {number} .")

    @classmethod
    def tan_rad(cls):
        """Tangent to radian"""
        print("***** WELCOME TO TANGENT TO RADIAN CONVERTER *****")
        number = math.atan(float(input("Enter the TAN : ")))
        print(f"Entered tan is equal to radian {number} .")

    def main(self):
        """This module is made as menu of this class"""
        work_on = True
        while work_on:
            self.print_menu()
            choice = input("Enter your choice : ")

            if choice == "1":
                self.factorial()
                self.continue_ask()

            elif choice == "2":
                self.multiplication_table()
                self.continue_ask()

            elif choice == "3":
                self.fibonacci()
                self.continue_ask()

            elif choice == "4":
                self.sum_up_to_num()
                self.continue_ask()

            elif choice == "5":
                self.dec_to_others()
                self.continue_ask()

            elif choice == "6":
                self.advanced_calculator()
                self.continue_ask()

            elif choice == "7":
                self.fmod()
                self.continue_ask()

            elif choice == "8":
                self.gcd()
                self.continue_ask()

            elif choice == "9":
                self.log()
                self.continue_ask()

            elif choice == "10":
                self.power()
                self.continue_ask()

            elif choice == "11":
                self.sqrt()
                self.continue_ask()

            elif choice == "12":
                self.rad_deg()
                self.continue_ask()

            elif choice == "13":
                self.deg_rad()
                self.continue_ask()

            elif choice == "14":
                self.sin()
                self.continue_ask()

            elif choice == "15":
                self.cos()
                self.continue_ask()

            elif choice == "16":
                self.tan()
                self.continue_ask()

            elif choice == "17":
                self.sin_rad()
                self.continue_ask()

            elif choice == "18":
                self.cos_rad()
                self.continue_ask()

            elif choice == "19":
                self.tan_rad()
                self.continue_ask()

            elif choice == "99":
                self.quit()

            else:
                print("INVALID INPUT! PLEASE CHOOSE BETWEEN 1-19 OR 99 TO EXIT")
                continue

    def continue_ask(self):
        """This module is made for asking continue the current menu or quit"""
        continue_on = True
        while continue_on:
            print("Do you want to continue Mathematic Calculators (Y/N) ? ")
            continue_ans = str(input().upper())
            if continue_ans == "Y":
                self.main()
            elif continue_ans == "N":
                self.quit()
            else:
                print("INVALID INPUT. PLEASE CHOOSE Y OR N ")
                continue

    @classmethod
    def quit(cls):
        """Quitting from program"""
        raise SystemExit
