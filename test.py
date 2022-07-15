# asd = {
# 	"type": "phone",
# 	"vendor": "me",
# 	"model": "Meizu m6s",
# 	"price": 100
# }

# asd["audio_jack"] = True
# asd["price"] = 70
# print(asd)

# print(asd.get("price"))
# print("discount" in asd) 
# for key, value in asd.items():
# 	print("{}: {}".format(key, value))


#02 Редактор Sublime

#Задание.jpg
# dict = {
# 	"Pasha": {
# 		"city": "Kharkiv",
# 		"temperature": "30",
# 		"wind": "15km/h",
# 	    },
# 	"Sasha": {
# 		"city": "Kiyv",
# 		"temperature": "25",
# 		"wind": "5km/h"
# 	    },
# 	"Alex": {
# 		"city": "Dnepr",
# 		"temperature": "34",
# 		"wind": "10km/h"
# 	    },
# 	}
# name = input("Enter one of the following names : Pasha, Sasha, Alex: ")

# try:
# 	if name == "Pasha":
# 		print(dict.get("Pasha"))
# 	elif name == "Sasha":
# 		print(dict.get("Sasha"))
# 	elif name == "Alex":
# 		print(dict.get("Alex"))
# 	else:
# 		print("please, try again and enter the name correct")
# except Exception as ex:
# 	print("blyat'")


#06 Сложные типы данных

#Задание 1.jpg
# mylist = [2, 3, 4, 5, 6, 7,]
# mylist.append("Python")

# print(mylist[0:7:6])
# print(mylist[1:4])
# print(len(mylist))
# print(mylist.index(6))
# del mylist[6]
# print(mylist)

#Задание 2.jpg
# weather = {
# 	"city": "Kiyv",
# 	"temperature": 15,
# 	"wind": "east"
# }
# print(weather.get("city"))
# weather["temperature"] = 13
# print(weather.get("temperature"))
# print(len(weather))
# print(weather.get("country"))
# weather["date"] = "27.05.2017"
# print(weather)

# mylist = []

# mylist.append({"weather": 'solne4no', "date": '13.01.2033'})
# mylist.append({"weather": 'pasmurno', "date": '24.12.2022'})
# mylist.append({"weather": 'dojdb', "date": '27.06.2077'})

# for asd in mylist:
# 	print(asd)


#08 Функции


#Задание 1.jpg
# def get_summ(one, two, delimeter=' '):
# 	asd = str(one) + str(delimeter) + str(two)
# 	print(asd.upper())
# 	return asd

# get_summ("Hello", 'world!', delimeter='&')
# get_summ('Hello', 'world!', ' + ')
# get_summ('Hello', 'world!',)

# #OR LIKE THAT
# def get_summ(word):
# 	asd = print(word.upper())
# 	return asd

# get_summ(input("enter something: "))

#Задание 2.jpg