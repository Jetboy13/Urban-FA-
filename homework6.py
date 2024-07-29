my_dict = {'Alex': 1985, 'Sasha': 1986, 'Valentin': 1987}
print(my_dict)
my_dict ['Max'] = 1988
print(my_dict)
my_dict.update({'Artem': 1989, 'Lev': 1984})
print(my_dict)
my_dict ['Sasha'] = 1986
a = my_dict.pop('Sasha')
print(a)
print(my_dict)

my_set = {1, 2, 3, 2, 2, 1, 4, 7, 4, 5, 6, 7}
print(set(my_set))
my_set.update ({8, 9})
print(my_set)
my_set.remove(2)
print(my_set)