name = input("enter your name: ")
age = input("enter your age: ")
print("Username is", name, ". He or she is", age, "years old")
time = int(input("time in sec: "))
hour = time // 3600
minute = (time - hour * 3600) // 60
sec = time - hour * 3600 - minute * 60
print(f"Time is {hour}:{minute}:{sec}")
# как добиться 01

n = str(input("enter number: "))
a = int(n)
b = int(n + n)
c = int(n + n + n)
result = a + b + c
print(result)
# предполагается, что мы вводим только положительные числа?

num = int(input("Enter number: "))
max_dig = num % 10
while num > 0:
    num = num // 10
    if num % 10 >= max_dig:
        max_dig = num % 10
    if num % 10 == 9:
        continue
else:
    print(f"maximal digit = {max_dig}")

earning = int(input("enter earning: "))
cost = int(input("enter cost: "))
if earning > cost:
    effect = (earning - cost) / earning
    n_person = int(input("number of employees: "))
    per_head = effect / n_person
    print(f"profit. Firm profitability is {effect}. Profit per employee: {per_head}")
if earning < cost:
    print("loss")

a = int(input("Distance in km: "))
b = int(input("A goal: "))
day = 1
while a < b:
    a = a + a / 10
    day += 1
    if a >= b:
        print(f"You will reach the goal in %.d days" % day)
