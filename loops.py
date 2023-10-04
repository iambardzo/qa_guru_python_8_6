#Циклы
import random

# While - цикл с предусловием
# пока пользователь не введет правильный номер,

#while True:
    #print("azaza")


required_number = 7
user_number = random.randint(0, 10)

while required_number != user_number:
    user_number = random.randint(0, 10)
    print(f"Введено число{user_number}")

iterations_count = 10
i = 0

while i < iterations_count:
    print(f"Текущая итерация: {i}")
    i += 1

    # For - Итерация списков и словарей

    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Marina", "age": 18},
    ]

from pprint import pprint


for user in users:
    pprint(user)

for user in users:
    pprint(f"Пользователю {user['name']} {user['age']} лет")


d = {
    "first": 1,
    "second": 2,
    "third": 3
}

for item in d:
    pprint(item)

for item in d.keys():
    pprint(item)

for item in d.values():
    pprint(item)

for item in d.items():
    pprint(item)

for (key, value) in d.items():
   print(f"Ключ: {key}, Значение: {value}")

   # for i in range - цикл с итератором

#print(list(range(5, 15, 2)))

iterations_count = 10

for i in range(3, iterations_count, 2):
    print(f"Текущая итерация: {i}")

# Breake/Continue/Else - Прерывание цикла

for i in range(iterations_count):
    if i % 2 == 0:
        continue
        print("Не выполняется")
    print(f"Точно нечетное число: {i}")


for i in range(iterations_count):
    if i % 2 == 0:
        continue
        print("Не выполняется")

    if i > 7:
        break
    print(f"Точно нечетное число: {i}")

for i in range(5):
    for j in range(5):
       print(i, j)
       if j == 3:
           continue

       if j == 4:
           break

    if i % 2 == 0:
        continue

# enumerate = ["Екатеринбург", "Москва", "Сочи"]

cities = ["Екатеринбург", "Москва", "Сочи"]

i = 1
for city in cities:
    print(f"{city} на {i} месте по загрязнению")
    i += 1

#i = 1
for i, city in enumerate(cities):
    print(f"{city} на {i} месте по загрязнению")
    #i += 1