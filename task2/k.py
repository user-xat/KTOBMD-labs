# K. Самое длинное слово
print(len(sorted(input().split(), key=lambda x: len(x), reverse=True)[0]))
