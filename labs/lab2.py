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
task1()



def task5():
    def get_digit_sum(n):
        # Функция для вычисления суммы цифр числа
        digit_sum = 0
        while n > 0:
            digit_sum += n % 10
            n //= 10
        return digit_sum

    def print_even_numbers_with_greater_sum(m, numbers):
        # Функция для вывода на экран чётных чисел с суммой цифр больше m
        for number in numbers:
            if number % 2 == 0 and get_digit_sum(number) > m:
                print(number)

    # Ввод трёх чисел
    numbers = []
    for i in range(3):
        number = float(input(f"Введите {i + 1} - е трёхзначное число: "))
        numbers.append(number)

    # Заданное значение для суммы цифр
    m = float(input("Введите значение m: "))

    # Вывод чётных чисел с суммой цифр больше m
    print_even_numbers_with_greater_sum(m, numbers)
task5()



def task3():
    def decimnal_in_new_system(number, base):
        if base < 2 or base > 36:
            print("!!! Ошибка: Основание должно быть в диапазоне от 2 до 36 !!!")

        integer_part = int(number)
        fractional_par = number - integer_part
        integer_result = ""

        while integer_part > 0:
            remainder = integer_part % base
            if remainder < 10:
                integer_result = str(remainder) + integer_result
            else:
                integer_result = chr(remainder + 55) + integer_result
            integer_part //= base

        fractional_result = ""
        precision = 4   # Количество знаков после запятой

        while precision > 0:
            fractional_par *= base
            int_part = int(fractional_par)
            if int_part < 10:
                fractional_result += str(int_part)
            else:
                fractional_result += chr(int_part + 55)
            fractional_par -= int_part
            precision -= 1

        if fractional_result:
            return f"{integer_result}.{fractional_result}"
        else:
            integer_result

    # Получение входных данных от пользователя
    user_number = float(input("Введите десятичную дробь для конвертации: "))
    user_base = int(input("Введите основание системы счисления (от 2 до 36): "))

    # Перевод жроби в заданную систему счисления и вывод результата
    result = decimnal_in_new_system(user_number, user_base)
    print(f"Результат перевода: {result} в систему с основанием " f"{user_base}")
task3()



def task6():
    def is_happy(number):
        number_str = str(number) # Преобразуем номер в строку для работы с цифрами

        if len(number_str) != 6: # Проверяем, что номер состоит ровно из 6 - ти цифр
            return print("Номер данного билета не существует")

        first_half = number_str[:3] # Разделим номер на первые и последние три цифры
        second_half = number_str[3:]

        first_sum = sum(int(digit) for digit in first_half) # Вычисляем сумму цифр первой и второй половины номера
        second_sum = sum(int(digit) for digit in second_half)

        return first_sum == second_sum # Сравниваем суммы и возвращаем результат

    number = int(input("Введите номер билета (от 000000 до 999999): "))

    if is_happy(number):
        print("Билет счастливый")
    else:
        print("Билет несчастливый")
task6()



def task8():
    def sum_of_series(epsilon):
        n = 2
        current_sum = 0

        while True:
            current_sum += 1 / n
            n += 1

            if (1 / n) < epsilon:
                print(current_sum)
                break
        return current_sum

    epsilon = float(input("Введите желаемую точность: "))
    result = sum_of_series(epsilon)
    print(f"Сумма ряда с точностью {epsilon} равна {result:0.4f}")
task8()
