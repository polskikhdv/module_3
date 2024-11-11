calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    res_tuple = len(string), string.upper(), string.lower()
    count_calls()
    print(res_tuple)


def is_contains(string, list_to_search):
    string = string.lower()
    list_to_search = [i.lower() for i in list_to_search]
    count_calls()
    result = list_to_search.count(string)
    return print(bool(result))


string_info('Capybara')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['recycling', 'cyclic'])
print(calls)
