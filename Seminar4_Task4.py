# 4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо.
#  При расшифровке происходит обратная операция.
# К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию,
#  которая спрашивает ключ, считывает текст и дешифровывает его.


alphabet_ru = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"


def shift(text, symbols, n):
    index = symbols.find(text)
    if index + n < len(symbols):
        return symbols[index + n]
    else:
        return symbols[(index + n) % len(symbols)]

    

def back_shift(text, symbols, n):
    index = symbols.find(text)
    if index - n >= 0:
        return symbols[index - n]
    else:        
        return symbols[(index - n) % len(symbols)]

    

def encrypt(text, n = 2):
    res = ""
    for i in range(0, len(text)): 
        res += shift(text[i], alphabet_ru, n)
    return res


def decrypt (text, n = 2):
    res = ""
                   
    for i in range(0, len(text)):
        res += back_shift(text[i], alphabet_ru, n)
    return res

str = encrypt(input("Введите слово для кодирования: "))
print(f'Закодированный вариант: {str}')
decrypt_str = decrypt(str)
print(f'Раскодированный вариант: {decrypt_str}')