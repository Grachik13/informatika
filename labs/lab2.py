# variant №9
def task1():
    def is_even(number):
        if number % 2 == 0:
            return True
        else:
            return False

    def is_divisible_by_three(number):
        if number % 3 == 0:
            return True
        else:
            return False

    while True:
        number = int(input("~~~ Введите число: "))
        if is_even(number):
            print(f"{number} - число оканчивается на чётную цифру")
        if is_divisible_by_three(number):
            print(f"{number} - число делится на 3 нацело")

