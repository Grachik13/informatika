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



def task3():
    def decimnal_in_new_system(number, base):
        if base < 2 or base > 36:
            return "Ошибка: Основание должно быть в диапазоне от 2 до 36"

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
