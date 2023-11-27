#program for add, sub , multi, and divide without function.
# num1 = 2
# num2 = 10

# addition = num1 + num2
# print("Value of addition is ", str(addition))

# sub = num1 - num2
# print(sub)

# multi = num1 * num2
# print(multi)


#same program with defining functions
# num1 = 10
# num2 = 5

# def addition():
#     add = num1 + num2
#     print(add)

# def substration():
#     sub = num1 - num2
#     print(sub)

# def multiplication():
#     multi = num1 * num2
#     print(multi)

# def division():
#     div = num1 / num2
#     print(div)

# addition()
# substration()
# multiplication()
# division()

#make your program more modular by calling the values in functions

def addition(num1, num2):
    add = num1 + num2
    return add

def subtraction(num1, num2):
    sub = num1 - num2
    return sub

def multiplication(num1, num2):
    multi = num1 * num2
    return multi

def division(num1, num2):
    div = num1 / num2
    return div

print("sum of values is: ", str(addition(5, 10)))
print(subtraction(5, 10))
print(multiplication(5, 10))
print(division(5, 10)) 