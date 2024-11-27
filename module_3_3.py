def print_params(a=1, b='string', c=True):
    print(a, b, c)
print_params()
print_params('a', 'b', 'c')
print_params(1, 2)
print_params('a', 'b')
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [5, 'song', False]
print(values_list)

values_dict = {'a': 3, 'b': 'link', 'c': False}
print(values_dict)

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['text', 16]
print_params(*values_list_2, c=False)
