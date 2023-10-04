import random

# строковые константы
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

chars = ''

# переменные запрашиваемой информации
pw_cnt = int(input('Количество паролей для генерации: '))
pw_len = int(input('Длину одного пароля: '))
pw_digit_on = input('Включать ли цифры 0-9? ')
pw_upp_on = input('Включать ли прописные буквы A-Z? ')
pw_low_on = input('Включать ли строчные буквы a-z? ')
pw_symbols_on = input('Включать ли символы !#$%&*+-=?@^_? ')
pw_exceptions = input('Исключать ли неоднозначные символы "il1Lo0O"? ')

if pw_digit_on in ['Да', 'да', 'д', '+', 'yes', 'YES', 'Yes', 'y', 'Y', 'ДА']:
    chars += digits
if pw_upp_on in ['Да', 'да', 'д', '+', 'yes', 'YES', 'Yes', 'y', 'Y', 'ДА']:
    chars += uppercase_letters
if pw_low_on in ['Да', 'да', 'д', '+', 'yes', 'YES', 'Yes', 'y', 'Y', 'ДА']:
    chars += lowercase_letters
if pw_symbols_on in ['Да', 'да', 'д', '+', 'yes', 'YES', 'Yes', 'y', 'Y', 'ДА']:
    chars += punctuation
if pw_exceptions in ['Да', 'да', 'д', '+', 'yes', 'YES', 'Yes', 'y', 'Y', 'ДА']:
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')


# функция генерации паролей
def generate_password(pw_len, chars):
    password = ''
    for j in range(pw_len):
        password += random.choice(chars)
    return password


for _ in range(pw_cnt):
    print(generate_password(pw_len, chars))
