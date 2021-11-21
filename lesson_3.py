#def divide(x, y):
    #try:
        #result = int(x) / int(y)
    #except ZeroDivisionError as err_1:
        #return err_1
    #except ValueError as err_2:
        #return err_2
    #return result
#print(divide(input("enter x: "), input("enter y: ")))



#def information(name, surname, birth_date, city, email, phone_number):
    #print(f"surname - {surname}; name - {name}; email - {email}; phone_number - {phone_number}; birth_date - {birth_date}; city - {city}")
#information(name = input("enter your name: "), surname = input("enter your surname: "), birth_date = input("enter your birth_date: "),
            #city = input("enter your city: "), email = input("enter your email: "), phone_number = input("enter your phone_number: "))



#def divide(x, y, z):
    #sum = x + y + z
    #little = min(x, y, z)
    #result = sum - little
    #return result
#print(divide(int(input("enter x: ")), int(input("enter y: ")), int(input("enter z: "))))


#def my_func(x, y):
    #n = 1
    #while n <= abs(y):
        #x_res = pow(x, n)
        #n += 1
    #else:
        #result = 1 / x_res
    #return result
#print(my_func(2, -4))


def my_sum():
    sum_res = 0
    while True:
        chars = input("num or q: ").split()
        for num in chars:
            if num == "q":
                return sum_res
            else:
                try:
                    sum_res += int(num)
                except ValueError:
                    print("Input error")
        print(f'Your final sum is {sum_res}')
print(my_sum())




def int_func():
    words = input("words: ")
    for word in words:
        letters = 0
        for let in word:
            if 97 <= ord(let) <= 122:
                letters += 1
                if len(word) == letters:
                    print(words.title())
            else:
                print(f'Only small latin letters')
        break
int_func()














