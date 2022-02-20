#RYAN LOI
#ITI1120 D
#ASSIGNMENT 2 PART 1

import math
import cmath
import random

        

def quadratic(a,b,c):
    '''(int,int,int)->str

    Takes the paramaters a,b,c and determines the roots of the quadratic equation.

    It will do this by calculating the discriminant and then return the roots
    according to the results of the discriminat.'''

    if a == 0:
        print("WARNING: If a equals 0, a divide by 0 error will occur!")
        print("Restarting program.")
    
    else:
        d = b**2 - 4*a*c #discriminant
        if d == 0:
            root = ((-b) + ((math.sqrt((b*b) - 4*a*c))))/(2*a)
            print('The quadratic equation ' + str(a) + ' x^2 +' + str(b) + 'x + ' + str(c))
            print('has one real root:')
            print(root)
        if d > 0:
            root1 = ((-b) + ((math.sqrt((b*b) - 4*a*c))))/(2*a)
            root2 = ((-b) - ((math.sqrt((b*b) - 4*a*c))))/(2*a)
            print('The quadratic equation ' + str(a) + 'x^2 ' + str(b) + 'x + ' + str(c))
            print('has two real roots:')
            print(root1,'and',root2)
        if d < 0:

            root1 = ((-b) + ((cmath.sqrt((b*b) - 4*a*c))))/(2*a)
            root2 = ((-b) - ((cmath.sqrt((b*b) - 4*a*c))))/(2*a)
            print('The quadratic equation ' + str(a) + 'x^2 + ' + str(b) + 'x + ' + str(c))
            print('has the following complex roots: ')
            print(root1,'and',root2)


# main



name=input("What is your name? ")

status=str(2)

if status=='2':
    def secondary_menu():
        '''(none) -> (None)
        Acts as the menu for quadratic equation solver. It will
        ask for the coefficients of a, b, and c and then will call the
        high_school_eqsolver(a,b,c) function to compute the results'''
        a = 0
        b = 0
        c = 0

        while type(a) != type(float):
            a = input('Input a coefficient for a: ')
            try:
                a = float(a)
                if a.is_integer() == True:
                    a = int(a)
                break
            except ValueError:
                print('Invalid input. Please input a number')

        while type(b) != type(float):
            b = input('Input a coefficient for b: ')
            try:
                b = float(b)
                if b.is_integer() == True:
                    b = int(b)
                break
            except ValueError:
                print('Invalid input. Please input a number')

        while type(c) != type(float):
            c = input('Input a coefficient for c: ')
            try:
                c = float(c)
                if c.is_integer() == True:
                    c = int(c)
                break
            except ValueError:
                print('Invalid input. Please input a number')


        quadratic(a,b,c)
        
        
    print("*"*46)
    print("*" + ' '*44 + "*")
    print("*__Welcome to the quadratic equation solver__*")
    print("*" + ' '*44 + "*")
    print("*"*46)
    #welcome msg
    
    flag=True
    while flag:
        question=input(name+", would you like a quadratic equation solved? ")

        question = question.lower()

        if question != "yes":
            flag=False
        else:
            print("Good choice!")
            secondary_menu()
                    
 
else:
    print("The program is not intended for you. The program will now terminate.")

print("Good bye "+name+"!")
