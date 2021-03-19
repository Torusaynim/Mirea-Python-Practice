import random

endOfSurname=["ов", "ин", "ский", "ли", "ян", "як", "ич", "ев", "о", "ий", "ын", "их", "ых", "цкий", "ла"]
mass1 = ["а", "е", "и", "о", "у", "э", "ю", "я"]
mass4 = ["А", "Е", "И", "О", "У", "Э", "Ю", "Я"]
mass2 = ["ц", "к", "н", "г", "ш", "щ", "з", "х", "ф", "в", "п", "р", "л", "д", "ж", "ч", "с", "м", "т", "б"]
mass3 = ["Ц", "К", "Н", "Г", "Ш", "Щ", "З", "Х", "Ф", "В", "П", "Р", "Л", "Д", "Ж", "Ч", "С", "М", "Т", "Б"]

if random.randint(0, 1) == 0:
    str = mass4[random.randint(0, 7)]
    for i in range(2, 4):
        str += mass2[random.randint(0, 19)]
        str += mass1[random.randint(0, 7)]
else:
    str = mass3[random.randint(0, 19)]
    for i in range(2, 4):
        str += mass1[random.randint(0, 7)]
        str += mass2[random.randint(0, 19)]

str += endOfSurname[random.randint(0, 14)]

print(str)
