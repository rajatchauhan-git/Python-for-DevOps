#command like argument

import sys #we need to import the sys module

def add(num1, num2):
    add = num1 + num2
    return add

def sub(num1, num2):
    sub = num1 - num2
    return sub

def mul(num1, num2):
    multi = num1 * num2
    return multi

def div(num1, num2):
    div = num1 / num2
    return div

num1 = float(sys.argv[1]) #to read command line argument of num1
operation = sys.argv[2]
num2 = float(sys.argv[3]) #to read command line argument of num2

if operation == "add":
    output = add(num1, num2)
    print(output)

if operation == "mul":
    output = mul(num1,num2)
    print(output)

if operation == "sub":
    output = sub(num1,num2)
    print(output)

if operation == "div":
    output = div(num1,num2)
    print(output)

# we need to run the program with name and num1 add num2