import random

apple = 5
list = [1, 2, 3, 4, 5, 7, 8, 9]
while apple in list:
    apple = random.randrange(10)
print(apple)
