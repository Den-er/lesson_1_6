my_dict = {"Daniil": 2011, 'Egor': 1989, "Elena": 2000 }
print (my_dict)
print ("Год рождения Егора:", my_dict.get ('Egor'))
print(my_dict.get('d'), "Ключа нет")
my_dict.update({'Den': 2000,
                'Nimona': 2016})
print (my_dict)
del my_dict ["Daniil"]
print (my_dict)


my_set = {2,4,6, 2,7,7,7, True, True, False, True, 'set','list',(1,3,4,5),(1,3,4,5),(1,3,4,5)}
print('Множество:', my_set)
my_set.add('low')
my_set.add('jet')
my_set.discard(2)
print('Изменённое множество:', my_set)


