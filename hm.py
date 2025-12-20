list = ["Alex" , "Andriy" , "Vanya" , "Amy" , "Dan"]
age_list = ["18  Група: Молодь" , "9  Група: Дитина" , "48  Група:  Дорослий" , "21  Група: Молодь" , "4  Група: Дитина"]
try:
    index = int(input("Введіть число индексу: "))
    word = list[index]
    age = age_list[index]
    print("Імя: ",word , " Років: ",age)
except IndexError:
    print("Thats..not the guy")
except ValueError:
    print("I said number , NOT NAME!!")