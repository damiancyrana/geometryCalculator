from enum import IntEnum
import calculations_functions


Figures_Menu = IntEnum('Figures_menu', 'Rectangle Square Triangle Trapezoid Circle')

while True:
    choice = int(input("""Select a geometric figure to calculate:
        1 - Rectangle  
        2 - Square  
        3 - Triangle  
        4 - Trapezoid  
        5 - Circle
        6 - End
    Chose: """))

    # rectangle
    if choice == Figures_Menu.Rectangle:
        a = float(input("Side a = "))
        b = float(input("Side b = "))
        print("Rectangle Area  =", calculations.rectangle(a, b))

    # square
    elif choice == Figures_Menu.Square:
        a = float(input("Side a = "))
        print("Square Area  =", calculations.square(a))

    # triangle
    elif choice == Figures_Menu.Triangle:
        a = float(input("Base a = "))
        h = float(input("Height h = "))
        print("Triangle Area =", calculations.triangle(a, h))

    # trapezoid
    elif choice == Figures_Menu.Trapezoid:
        a = float(input("Base a = "))
        b = float(input("Base b = "))
        h = float(input("Height h = "))
        print("Triangle Area =", calculations.trapezoid(a, b, h))

    # circle
    elif choice == Figures_Menu.Circle:
        r = float(input("Radius r = "))
        print("Circle Area  =", calculations.circle(r))

    # Instruction ending the program
    elif choice == 6:
        finish = input("Do you want to finish the program ? [y/n] ")
        if finish == "y":
            break
        else:
            continue
    else:
        print("You didn't choose a function from the range !")
