def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(True, 2, (1, 3, 5))
print_params(c=9)
print_params('строчка', b=9)
values_list = [1, False, 'String']
values_dict = {'a': 'String', 'b': 5.0, 'c': 7}
print_params(*values_list)
print_params(values_list)
print_params(values_dict)
print_params(*values_dict)
values_list_2 = [7, "sr"]
print_params(values_list_2)
print_params(*values_list_2, 42)
