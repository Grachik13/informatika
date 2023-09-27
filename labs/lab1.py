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
