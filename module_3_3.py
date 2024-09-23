# task 1
def print_params(a = 1, b = 'string', c = True):
    print(a, b, c)

print_params()
print_params(2)
print_params(2, False)
print_params(2, False, 100)
print_params(b = 25)
print_params(c = [1,2,3])

# task 2
values_list = ['Good', 99.9, [True, False]]
values_dict = {'a': 'first', 'b': 2, 'c': [3, 4, 5]}

print_params(*values_list)
print_params(**values_dict)

# task 3
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)