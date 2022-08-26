# a = 2
# b = 4.5
# print(a + b)

# v = int(input("Введите число от 1 до 10: "))
# if v > 10:
# 	print("Error. please, enter number from 1 to 10 ")
# else:
# 	print(v * 10)


# name = input("Enter your name: ")
# print("Hello, " + name + " how are you doing?")


#Неделя 2. Условный оператор If.


#Задание1.jpg. Возраст.
# age = input("enter your age: ")
#
# try:
# 	age_input = int(age)
#
# 	if age_input >= 4 and age_input <= 7:
# 		print("You have to go to a kindergarten")
# 	elif age_input > 7 and age_input < 17:
# 		print("You have to go to a school")
# 	elif age_input >= 17 and age_input < 22:
# 		print("You have to go to a university")
# 	elif age_input >= 22 and age_input <= 59:
# 		print("You have to work")
# 	elif age_input >= 60:
# 		print("You have to retire")
#
# except Exception as ex:
# 	print("use only numbers")

#Задание2.jpg. Сравнение строк.
def my_func(str1, str2):

    if str1 == str2:
        return 1
    elif len(str1) >= len(str2) and not str2 == "learn":
        return 2
    elif str2 == "learn" and len(str1) != len(str2) or len(str1) == len(str2):
        return 3
    else:
        print("conditions arent met")

str1 = input()
str2 = input()

r = my_func(str1, str2)
print(r)

#Цикл for

#Задание 3.jpg. Оценки.
school_score = [
    {"school_class": "1a", "scores": [5, 5, 5, 5, 2]},
    {"school_class": "1b", "scores": [4, 4, 4, 2, 3]},
    {"school_class": "1c", "scores": [1, 2, 3, 4, 5]},
    {"school_class": "1d", "scores": [4, 3, 3, 3, 5]},
]
for score in school_score:
    counter = score.get("scores")
    every_class = 0
    for i in counter:
        every_class += i

    score.update({'total_class_score': every_class / len(counter)})
    print(f'{score.get("school_class")} {score.get("total_class_score")}')

# total_school_score = 0
for a in school_score:
    total_school_score = 0
    asd = a.get("scores")
    jopa = len(asd)
    # print(jopa)
    for i in asd:
        total_school_score += i
        idk = total_school_score / jopa

print("total school score:",idk)


#Цикл while 


#Задание.jpg (1)
spisok = ["Валера","Вася", "Маша", "Петя", "Саша", "Даша"]
count = 0
while True:
    count+=1
    search=spisok.pop()
    if search == "Валера":
        print("Валера нашелся на попытке №", count,".......")
        break
    else:
        print("ахх.. где же валера... Попытка найти №", count)

#(2 v2 but the problem isnt fixed =))
spisok = ["Валера","Вася", "Маша", "Петя", "Саша", "Даша"]

def find_person(input):
    name = input("enter the name: ")
    if name in spisok:
        print("gz man, the name {}".format(name), "exists")
    elif name != spisok:
        print("cant find entered name. try again")
        return name
while True:
    if find_person(input) == "quit":
        print("quiting=)...")
        break

#(3)
def ask_user():
    aboba = input("how is it going?: ")
    return aboba

while True:
    if ask_user() == "im good":
        print("cya")
        break

#(4)
while True:
    aboba = input("how is it going?: ")
    def ask_user(aboba):
        asd = aboba
        return asd
    if ask_user(aboba) == "im good":
        print("cya =)")
        break
    elif ask_user(aboba) == "goodbye":
        print("cya =)")
        break


    def get_answer():
        a = aboba.endswith("?")
        return a
    if get_answer():
        print("ананас")
        continue
    else:
        print("дурак?")
        continue
