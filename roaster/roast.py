import random

more = True
while more is True:
    random_lines = random.choice(open("text_files/roasts.txt", encoding="utf-8").readlines())
    print(random_lines)
    more = input("Want more roasts? y/n")
    if 'y' in more.lower():
        more = True
    else:
        more = False
    