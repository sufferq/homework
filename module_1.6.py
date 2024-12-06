my_dict = {'Dima': 2005, 'Alisa': 2007}
print(my_dict)
print(my_dict['Dima'])
print(my_dict.get('Stepa'))
my_dict.update({'Artem': 2007,'Sergei': 2006})
a = my_dict.pop('Alisa')
print(a)
print(my_dict)

#Множество
my_set = {1,1,2,'Яблоко',3,3}
print(my_set)
my_set.add(123.4)
my_set.add(5)
my_set.discard(2)
print(my_set)
