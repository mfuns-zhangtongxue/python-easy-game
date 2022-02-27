import random

number = random.randint(1,100)
print(input('数字'))
if (input() > number):
    print('大了')
elif (input() < number):
    print('小了')
else (input() = number):
    print('你猜对了')