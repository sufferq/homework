def print_params(a = 1, b = "строка", c = True):
    print (a,b,c)

#1.Функция с параметрами по умолчанию:
print()
print_params(2, 3, 4)
print_params(b = 25)
print_params(c = [1, 2, 3])

#2.Распаковка параметров
print()
values_list = [90, "Coconut", True]
print_params(*values_list)
values_dict = {"a": 5, "b": "globus", "c": True}
print_params(**values_dict)

#3.Распаковка + отдельные параметры:
print()
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)






