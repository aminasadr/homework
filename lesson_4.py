from sys import argv
premium = int(100)
name, work_time, in_hour = argv
print(argv)
print("Количетво часов: ", work_time)
print("Зарплата в час: ", in_hour)
print("Зарплата: ", int(work_time)*int(in_hour) + premium)

my_list = [1, 3, 43, 4898, 37, 86, 11, 87, 74, 31, 29, 0, 3]
new_list = [el for el in my_list if el > my_list[my_list.index(el)-1]]
print(new_list)


my_num = (el for el in range(20, 240) if el%20==0 or el%21==0)
for el in my_num:
    print(el)

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [el for el in my_list if my_list.count(el) == 1]
print(new_list)

from functools import reduce
print(reduce(lambda x,y: x * y, [el for el in range(100, 1001) if el % 2 == 0]))

from itertools import cycle
from itertools import count
my_count = count(2)
my_cycle = cycle("FH36")
for el in range(4):
    print(next(my_cycle))
    print(next(my_count))


import math
from itertools import count
def gen():
    for el in count(1):
        yield math.factorial(el)

x = 0
for i in gen():
    if x == 4:
        break
    else:
        x += 1
        print(i)

