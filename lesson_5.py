with open ("lesson5_1.txt", "w", encoding = "utf-8") as my_text:
    print(input("Enter your text: "), file = my_text)

from itertools import count
with open ("lesson5_2.txt", "r", encoding = "utf-8") as my_text:
    content = my_text.read()
    lines = content.count('\n')
    line_num = 0
    while line_num < lines:
        l_cont = my_text.readline()
        line_num += 1
    for i, value in enumerate(l_cont, 1):
        words = len(l_cont.split())
        print(f"line_num is {i}, words num in line us {words}")


with open ("lesson5_3", "r", encoding = "utf-8") as my_text:
    workers_dict = {line.split()[0]: float(line.split()[1]) for line in my_text}
    av_salary = (sum(workers_dict.values())/len(workers_dict))
    print(av_salary)
    for el in workers_dict.items():
        if el[1] < 20000.0:
            print(el[0])

from googletrans import Translator
with open ("lesson5_4_translated", "w", encoding = "utf-8") as my_translation:
    with open ("lesson5_4", "r", encoding = "utf-8" ):
        my_text = lesson5_4.read()
        translator = Translator()
        translations = translator.translate(my_text, dest= 'ru')
        print(lesson5_4_translated)


from random import randint
with open ("lesson5_5", "w+", encoding = "utf-8") as my_text:
    my_text.write(" ".join([str(randint(1, 20)) for el in range(100)]))
    my_text.seek(0)
    summ = sum(map(int, my_text.readline().split()))
    print(summ)


dic = {}
numbers = " 1234567890"
with open ("lesson5_6", "r", encoding = "utf-8") as my_text:
    for line in my_text:
        lessons, hours = line.split(":")
        dic[lessons] = sum(map(int, "".join([num for num in hours if num in numbers]).split()))
print(dic)








