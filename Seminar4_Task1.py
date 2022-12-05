# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]


import math 
# Функция вывода всех простых множителей заданного числа 
def prime_factors(num): 
    # Используем цикл для вывода четных множителей 
    while num % 2 == 0: 
        num = num / 2  
        print(2,)
 
    for i in range(3, int(math.sqrt(num)) + 1, 2): 
 
        # Используем цикл для вывода нечетных множителей  
        while num % i == 0: 
            num = num / i 
            print(i) 
    if num > 2: 
        print(num) 

 
num = 20
prime_factors(num) 
