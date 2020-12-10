#!/usr/bin/env python3


i="y"
while i != "n":
    a = int(input("Enter number a: "))
    o = input("Operator: ")
    b = int(input("Enter number b: "))

    if o == '+':
        print("{a} + {b} = {s}".format(a=a, b=b, s=a+b))
    elif o == '-':
        print("{a} - {b} = {s}".format(a=a, b=b, s=a-b))
    elif o == '*':
        print("{a} * {b} = {s}".format(a=a, b=b, s=a*b))
    elif o == '/':
        print("{a} / {b} = {s}".format(a=a, b=b, s=a/b))
    elif o == '//':
        print("{a} // {b} = {s}".format(a=a, b=b, s=a//b))
    elif o == '%':
        print("{a} % {b} = {s}".format(a=a, b=b, s=a % b))
    elif o == '**':
        print("{a} // {b} = {s}".format(a=a, b=b, s=a**b))
    else:
        print("Error")
    i=input("Next? y/n")
