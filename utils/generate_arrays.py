import random

max_value = input('Max value: ')
count = input('Array size: ')
max_int = int(max_value)
count_int = int(count)+1
list_asc = []
list_dsc = []
for i in range(1, count_int):
    list_asc.append(random.randint(-max_int, max_int))
    list_dsc.append(random.randint(-max_int, max_int))

list_asc.sort()
list_dsc.sort(reverse=True)

print(f'asc_array = {list_asc}')
print(f'dsc_array = {list_dsc}')
