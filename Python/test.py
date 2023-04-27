###TEST ONLY! WILL BE FINAL VERSION SOME TIME SOON###
import math
import time
from fractions import Fraction as f
from time import sleep as s
################################################
time.strftime("%I:%M %p  ")
time.strftime("%m/%d/%Y")
if time.strftime('%p') == 'AM':
    print("Good Morning")
    print("The Time is:",time.strftime('%I:%M %p '))
    print("The Date is:",time.strftime("%m/%d/%Y"))
elif time.strftime('%p') == 'PM':
    print("Good Afternoon")
    print("The Time is:",time.strftime('%I:%M %p'))
    print("The Date is:",time.strftime('%m/%d/%Y'))

needs = input("What would you like? ")
if needs == 'Pythagorean Theorem':
    a = int(input("What is the length of side A? "))
    b = int(input("What is the length of side B? "))
    c = math.sqrt(a**2 + b**2)
    print("Side C's length is ", c)

if needs == 'decimal to fraction':
    decimal = input("What is the Decimal? ")
    fraction_to_decimal = f(decimal)
    print("Your Fraction is ", fraction_to_decimal)

if needs == 'fraction to decimal':
    numerator = int(input("What is the Numerator? "))
    denominator = int(input("What is the Denominator? "))
    decimal_to_fraction = (numerator / denominator)
    print(decimal_to_fraction)

if needs == 'slope':
    y2 = int(input("What is y2? "))
    y1 = int(input("What is y1? "))
    x2 = int(input("What is x2? "))
    x1 = int(input("What is x1? "))
    slope = (y2 - y1) / (x2 - x1)
    print("Your slope is ", slope)

if needs == 'Calculator':
    operation = input("What Operation")
    if operation == 'multiply':
        num1 = int(input("Enter the 1st Number: "))
        num2 = int(input("Enter the 2nd Number: "))
        num3 = num1 * num2
        print(num3)
    if operation == 'divide':
        num1 = int(input("Enter the 1st Number: "))
        num2 = int(input("Enter the 2nd Number: "))
        num3 = num1 / num2
        print(num3)
    if operation == 'add':
        num1 = int(input("Enter the 1st Number: "))
        num2 = int(input("Enter the 2nd Number: "))
        num3 = num1 + num2
        print(num3)
    if operation == 'subtract':
        num1 = int(input("Enter the 1st Number: "))
        num2 = int(input("Enter the 2nd Number: "))
        num3 = num1 - num2
        print(num3)

if needs == 'square root':
    sqrt = int(input("What is the number? "))
    num1 = math.sqrt(sqrt)
    print("The Square root of", sqrt,"is", num1)

if needs == 'find b':
    y2 = int(input("What is y2? "))
    y1 = int(input("What is y1? "))
    x2 = int(input("What is x2? "))
    x1 = int(input("What is x1? "))
    slope = f(y2 - y1) / f(x2 - x1)
    print("Your slope is ", slope)
    s(3)
    print("y =", y2, "m =", slope, "x =", x2)
    s(3)
    print("So we are going to take the slope", slope, "and", x2, "and multiply them together")
    s(3)
    x3 = slope * x2
    print("When we multiply we get:", x3)
    s(3)
    print("So the equation is now", y2,"=", x3,"+ b")
    s(3)
    if x3 > 0:
        print("Now we are going to subtract", x3,"from", y2)
        y3 = y2 - x3
        s(3)
        print("And when we do that we get b =", y3)
        s(3)
        print("So the equation is now:")
        if y3 > 0:
            s(3)
            print("y =", slope,"x +", y3)
        elif y3 < 0:
            s(3)
            print("y =", slope,"x",y3)
    elif x3 < 0:
        print("now we are going to add", x3,"to", y2)
        y3 = y2 + x3
        s(3)
        print("And when we do that we get b =", y3)
        s(3)
        print("So the equation is now:")
        if y3 > 0:
            s(3)
            print("y =", slope,"x +", y3)
        elif y3 < 0:
            s(3)
            print("y =", slope,"x", y3)

if needs == 'Simplified or not':
    how = int(input("How many numbers are there? "))
    if how == 2:
        is_var = input("are there variables? ")
        if is_var == 'yes':
            how_vars = int(input("How many variables are there? "))
            if how_vars == 1:
                var_vars = input("What is the variables? ")
                num1 = int(input("What is the first number(Don't ENTER the VARIABLE!) "))
                num2 = int(input("What is the second number?(Don't ENTER the VARIABLE!) "))
                what_var = input("Which number has the variable?(num1, num2 or both?) ")
                if what_var == 'num1':
                    if num2 < 0:
                        print("So the equation is ", num1,var_vars,num2, sep='')
                        if what_var == 'num1' != 'num2':
                           s(3)
                           print("Thinking...")
                           s(3)
                           print("The equation is simplified")
                    if num2 > 0:
                        print("So the equation is ", num1,var_vars,"+",num2, sep='')
                        if what_var == 'num1' != 'num2':
                           s(3)
                           print("Thinking...")
                           print("The equation is simplified")                        
                if what_var == 'num2':
                    if num2 < 0:
                        print("So the equation is ",num1,num2,var_vars, sep='')
                        if what_var == 'num2':
                           s(3)
                           print("Thinking...")
                           s(3)
                           print("The equation is simplified")
                if what_var == 'both':
                    if num2 < 0:
                        print("So the equation is ",num1,var_vars,num2, sep='')
                        if what_var == 'both':
                           s(3)
                           print("Thinking...")
                           s(3)
                           print("The equation is simplified")