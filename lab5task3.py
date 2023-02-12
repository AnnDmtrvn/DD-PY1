from random import randint
 
 
def get_unique_list_numbers(lst_length=15, start=-10, stop=10):
    lst = list()
    n = 0
    while n < lst_length:
        num = randint(start, stop)
        if num not in lst:
            lst.append(num)
            n += 1
    return lst
 
 
list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
