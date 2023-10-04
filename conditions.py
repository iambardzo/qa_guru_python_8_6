#Условия

# Boolean - 3 состояния

b = bool

t = True
f = False
n = None

# is/elif/else

if True:
    print("Успешно")

if False:
    print("Провал")

code = 200

if 200 <= code < 400:
    print("Проверка пройдена")
elif 400 <= code < 600:
    print("Провал")
else:
    print("Непонятка")

# Пустые объекты

user_list = []

if user_list == []:
    pass

if user_list:
    pass

items_count = 0

if items_count == 0:
    pass

if items_count:
    pass


if "abc" == "":
    pass

if "abc":
    pass



print(bool(100))
print(bool(-100))
print(bool(0))


print(bool("abc"))
print(bool(""))


print(bool([]))
print(bool([1, 2, 3]))
print(bool([False]))