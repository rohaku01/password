import random
import string



lower = string.ascii_lowercase
upper = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

all = lower + upper + numbers + symbols

pass_lenght = int(input('Введите длину пароля: '))

temp = random.sample(all, pass_lenght)

password = ''.join(temp)

print('Ваш пароль:', password)

