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