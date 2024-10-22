from typing import Tuple
from xmlrpc.client import boolean

calls = 0

def count_calls():
    global calls
    calls += 1
    return calls

def string_info(row):
    rows: tuple = ()
    row_1 = [len(row), row.upper(), row.lower()]
    rows = tuple (row_1)
    count_calls()
    return rows

def is_contains(string, list_to_search):
    for i in range (len(list_to_search)):
        stringer = list_to_search [i]
        list_to_search [i] = stringer.lower()
    string = string.lower()
    boolin = string in list_to_search
    count_calls()
    return boolin


print(string_info('Capybara'))

print(string_info('Armageddon'))

print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN

print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches

print(calls)
