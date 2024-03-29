
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
    def calculate_series_sum(epsilon):
        sum = 0
        n = 1

        while True:
            term = 1 / n
            sum += term

            if abs(term) < epsilon:
                break

            n += 1

        return sum

    epsilon = float(input("Введите точность е: "))
    result = calculate_series_sum(epsilon)
    print(f"Сумма членов ряда с точностью {epsilon} равна: {result}")
task8()



def task2():

    import numpy as np
    import matplotlib.pyplot as plt

    # Опеределение функции для x <= 0:
    def f1(x):
        return np.cos(pi * x)

    # Определение функции для x > 0:
    def f2(x):
        return x ** 2 + 1

    # Задание диапазона значений x:
    a, b = map(float, input("Введите диапазон значений x: "))
    x = linspace(a, b, 100)

    # Вычислить значения функции f1(x) и f2(x) для всех значений x
    y1 = np.where(x <= 0, f1(x), np.nan)
    y2 = np.where(x > 0, f2(x), np.nan)

    # Построение графика
    plt.plot(x, y1, label = 'f(x) = cos(pi * x), x <= 0')
    plt.plot(x, y2, label = 'f(x) = x ** 2 + 1, x > 0')

    # Настройка осей и заголовка графика
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.zlabel('График функций f(x) = cos(pi * x) и f(x) = x ** 2 + 1')

    # Добавление легенды
    plt.legend()

    # Отображение графика
    plt.show()

task2()
