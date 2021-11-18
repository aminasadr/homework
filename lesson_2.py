list = [1, 2.5, "name", True, [1, 45], "winter"]
for i in range(len(list)):
    n = len(list)
    while n != 1:
        last = list[-1]
        print(type(last))
        list.pop(-1)
        print(list)
        n = n - 1
    if n == 0:
        print("End")
        break

list = [1, 2.5, 32, True, [1, 45], "winter"]
el = 0
n = len(list)
while el < n - 1:
   list[el], list[el + 1] = list[el + 1], list[el]
   el += 2
   print(list)
   if el >= n - 1:
       print("end")


months = ["Winter", "Spring", "Summer", "Autumn"]
num = [1, 2, 3, 4]
months_dict = dict(zip(num, months))
choice = int(input("Enter the number 1-12: "))
if choice == 1 or choice == 2 or choice == 12:
    print(months_dict.get(1))
elif choice == 3 or choice == 4 or choice == 5:
    print(months_dict.get(2))
elif choice == 6 or choice == 7 or choice == 8:
    print(months_dict.get(3))
elif choice == 9 or choice == 10 or choice == 11:
    print(months_dict.get(4))



text = input("enter your text: ")
words = text.split(" ")
for ind, el in enumerate(words):
    print(f"{ind}) {el[0:10]}")


my_list = [9, 7, 7, 3, 1, 1, 1]
value = int(input("enter: "))
while len(my_list) != 8:
    for i in range(len(my_list)):
        if my_list[i] == value:
            my_list.insert(i + 1, value)
            break
        elif my_list[0] < value:
            my_list.insert(0, value)
        elif my_list[-1] > value:
            my_list.append(value)
        elif my_list[i] > value and my_list[i + 1] < value:
            my_list.insert(i + 1, value)
            break
    print(my_list)
    break
























