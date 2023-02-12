# J. Сколько коротких слов?
with open('input.txt') as fin:
    print(len(list(filter(lambda x: len(x) <= 3, fin.read().split()))))
