class Calculator():
    def add(self, number1, number2):
        return number1 + number2
        
    def substract(self, number1, number2):
        return number1 - number2

    def multiply(self, number1, number2):
        return number1 - number2
        
    def divide(self, number1, number2):
        return number1 / number2

    def modulo(self, number1, number2):
        return number1 % number2 

    def power(self,number1, number2):
        return number1 ** number2

    def floor_division(self,number1, number2):
        return number1 // number2

    def main(self):

        while True:
            print("Please select an operation :\n 1 - Add\n 2 - Substract\n 3 - Multiply\n 4 - Divide")
            print(" 5 - Modulo\n 6 - Power of the given number\n 7 - Floor Division")
            select = float(input("Select operation : "))
                
            if select == 1:
                num1 = float(input("Enter number 1 : "))
                num2 = float(input("Enter number 2 : "))
                print(num1 , " + " , num2 , " = " , self.add(num1, num2))
                cont = input("Do you want to continue y/n ")
                if cont == "n":
                    break
                else:
                    continue
            elif select == 2:
                num1 = float(input("Enter number 1 : "))
                num2 = float(input("Enter number 2 : "))
                print(num1 , " - ", num2 , " = " , self.substract(num1, num2))
                cont = input("Do you want to continue y/n ")
                if cont == "n":
                    break
                else:
                    continue
            elif select == 3:
                num1 = float(input("Enter number 1 : "))
                num2 = float(input("Enter number 2 : "))
                print(num1 , " * ", num2 , " = " , self.multiply(num1, num2))
                cont = input("Do you want to continue y/n ")
                if cont == "n":
                    break
                else:
                    continue
            elif select == 4:
                num1 = float(input("Enter number 1 : "))
                num2 = float(input("Enter number 2 : "))
                print(num1 , " / ", num2 , " = " , self.divide(num1, num2))
                cont = input("Do you want to continue y/n ")
                if cont == "n":
                    break
                else:
                    continue
            elif select == 5:
                num1 = float(input("Enter number 1 : "))
                num2 = float(input("Enter number 2 : "))
                print(num1 , " % ", num2 , " = " , self.modulo(num1, num2))
                cont = input("Do you want to continue y/n ")
                if cont == "n":
                    break
                else:
                    continue
            elif select == 6:
                num1 = float(input("Enter number 1 : "))
                num2 = float(input("Enter number 2 : "))
                print(num1 , " ** ", num2 , " = " , self.power(num1, num2))
                cont = input("Do you want to continue y/n ")
                if cont == "n":
                    break
                else:
                    continue
            elif select == 7:
                num1 = float(input("Enter number 1 : "))
                num2 = float(input("Enter number 2 : "))
                print(num1 , " // ", num2 , " = " , self.floor_division(num1, num2))
                cont = input("Do you want to continue y/n ")
                if cont == "n":
                    break
                else:
                    continue
            else:
                print("Invalid output! Please select 1-2-3-4-5-6-7 ! \n ********************************************** \n ")
            continue