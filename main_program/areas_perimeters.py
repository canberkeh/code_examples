'''
Areas, surfaces and perimeters
'''
class AreasPerimeters():
    """This class is made for calculating areas, perimeters and surfaces"""
    @classmethod
    def print_menu(cls):
        """This module is made for printing menu"""
        print("\n\n***** Area and Perimeter Calculators *****")
        print("1- Area of Trapezoid\n2- Area of Parallelogram\n3- Area and Surface of Cylinder")
        print("4- Area and Surface of Sphere\n5- Area of Sector\n00- EXIT to Main Menu\n99- EXIT")

    @classmethod
    def quit(cls):
        """This module is made for quitting the whole program"""
        raise SystemExit

    def continue_ask(self):
        """This module is made for asking continue the current menu or quit"""
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
        """This module is made as menu of this class"""
        work_on = True
        while work_on:
            self.print_menu()
            choice = input("Enter your choice : ")

            if choice == "1":
                self.trapezoid()
                self.continue_ask()

            elif choice == "2":
                self.parallelogram()
                self.continue_ask()

            elif choice == "3":
                self.cylinder()
                self.continue_ask()

            elif choice == "4":
                self.sphere()
                self.continue_ask()

            elif choice == "5":
                self.sector()
                self.continue_ask()

            elif choice == "00":
                break

            elif choice == "99":
                self.quit()

            else:
                print("INVALID INPUT! PLEASE CHOOSE BETWEEN 1-19 OR 99 TO EXIT")
                continue

    @classmethod
    def trapezoid(cls):
        """This module is for calculate the area of trapezoid"""
        print("***** Trapezoid Area *****")
        print("A trapezoid is a quadrilateral with two sides parallel.")
        print("An isosceles trapezoid is a trapezoid in which the base angles are equal so.")
        long = float(input("Long Base: "))
        short = float(input("Short Base: "))
        height = float(input("Height: "))
        area = ((long + short)/2)*height
        print(f"Area of Trapezoid is {area}")

    @classmethod
    def parallelogram(cls):
        """This module is for calculate the area of parallelogram"""
        print("***** Parallelogram Area *****")
        print("A parallelogram is a 4-sided shape formed by two pairs of parallel lines")
        base = float(input("Base: "))
        height = float(input("Height: "))
        area = base*height
        print(f"Area of Parallelogram is {area}")

    @classmethod
    def cylinder(cls, pi_number = 3.14):
        """This module is for calculate the area and surface of cylinder"""
        print("***** Cylinder Area and Surface *****")
        radius = float(input("Radius: "))
        height = float(input("Height: "))
        area = ((2*pi_number*(radius**2)) + (height*(2*pi_number*radius)))
        surface = (pi_number*height*(radius**2))
        print(f"Area of Cylinder is {area}\nSurface of Cylinder is {surface}")

    @classmethod
    def sphere(cls, pi_number = 3.14):
        """This module is for calculate the area and surface of sphere"""
        print("***** Sphere Area and Surface *****")
        radius = float(input("Radius: "))
        area = (4*pi_number*(radius**2))
        surface = ((4/3)*pi_number*(radius**3))
        print(f"Area of Sphere is {area}\nSurface of Sphere is {surface}")

    @classmethod
    def sector(cls, pi_number = 3.14):
        """This module is for calculate the area of sector"""
        print("***** Area of Sector *****")
        radius = float(input("Radius: "))
        area = (pi_number * (radius**2))
        print(f"Area of Sector is {area}")
