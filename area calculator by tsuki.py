
import math

# our objective is to get the area  of the shapes and make a calculator basically
#creator of this silly project : TsukiAiko

side = 0
lenght = 0
width = 0
height = 0
base = 0
radius = 0
area = 0
loop = True
#on top is just defining equations pieces that as it right now the following equations currently have 0


#rectangle = lenght * width

#triangle = (height * base)/2

#circle = math.pi * radius**2


#on top is the equations for the presented shapes we only have 4 :D -> now we have to write down the if stuff and user input
#i decided to write the equaions early as reference of what im supposed to do which each one of the shapes
#choice is the option to choose between 1 and 4 for the shapes
#i just figured out i can make a loop here and basically make it better
#my notes on this one are kinda messes up so my apologies <3 also i do have past experience with coding i know how to read it and
#understand it but i just did not know how to write it so making this by hand just me and nothing else honestly make me happy
print("""===============================
         AREA CALCULATOR :D
===============================""")

print(""" 
1) Square
2) rectangle
3) triangle
4) circle
5) Quit
""")
while loop == True:
    choice = int(input('Please choose your shape: '))

    if choice == 1:
        loop = False
        print('\nplease add the side of the square below')
        side = int(input(':'))
        square = side**2
        print(f'\nThe area is {square}\nthank you for using the calculator have a great day <3')

    elif choice == 2:
        loop = False
        print('\nplease add the lenght of the rectangle below')
        lenght = int(input(':'))
        print('\n please add the width of the rectangle below')
        width = int(input(':'))
        rectangle = lenght * width
        print(f'\nThe area is {rectangle}\nthank you for using the calculator have a great day <3')

    elif choice == 3:
        loop = False
        print('\nplease add the height of the triangle below')
        height = int(input(':'))
        print('\n please add the base of the triangle below')
        base = int(input(':'))
        triangle = (height * base)/2
        print(f'\nThe area is {triangle}\nthank you for using the calculator have a great day <3')

    elif choice == 4:
        loop = False
        print('\nplease add the radius of the circle below')
        radius = int(input(':'))
        circle = math.pi * radius**2
        print(f'\nThe area is {circle}\nthank you for using the calculator have a great day <3')
    elif choice == 5:
        loop = False
        print(f'\neven if theres no area \nthank you for using the calculator have a great day <3')
    else:
        print("invalid input please try again")


