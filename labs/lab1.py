# task9

def convert_dollars_of_tenge(dollars):
    commission = 0.05
    tenge = dollars * 481
    total_amount = tenge - (tenge * commission)
    return round(total_amount, 3)

print(" ")

dollars_amount = float(input("Enter the amount of dollars: "))
result = convert_dollars_of_tenge(dollars_amount)

print(" ")

print("The equivalent amount in Kazakhstani tenge is: ", result, end = " ")
print("KZT")


# task_1

import math

x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))
z = float(input("Введите знфчение z: "))

a = (math.sqrt(abs(x - 1)) + math.tan(y)) / (1 + ((x ** 2) / 2) - math.log(1 + y))
b = math.sin(math.sqrt(abs(x - 1))) * math.cos(abs(z ** (1/3))) + x ** (1/3) + math.sqrt(y)

print("a = {0:.4f}, b = {1:.4f}".format(a, b))


# task_2

import math

x = float(input("Введите значение x: "))
a = 3
b = -2

f = a * ((x ** b + x) / 4) - x ** (b/3)

print("a = {0:.4f}".format(f))


# task_3

import math

x = float(input("Введите значение x: "))

# f = math.sqrt(math.log(math.cos(math.sqrt(x))))
f = math.sqrt(math.log(math.cos(1)))
print(f)
