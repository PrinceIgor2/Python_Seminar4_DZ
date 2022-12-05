# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]

# Функция определения простых множителей заданного числа
def get_prime_factors(user_number):
    prime_factors_list = []
    for i in range(2, user_number):
        while user_number % i == 0:
            user_number /= i
            prime_factors_list.append(i)
    return prime_factors_list

given_number = int(input("Введите натуральное число: "))
prime_factors_list = get_prime_factors(given_number)
print(f'Список простых множителей числа {given_number} :{prime_factors_list}')