import random
name = random.randint(1, 5)
print('Привет, попробуй угадать число, которое я загадал)')
what = input('Число от 1 до 5: ')
print(name)
if int(what) == int(name):
    print("А ты хорош, угадал!")
else:
    print("Не правильно!\nНе расстаривайся, я просто везучий")