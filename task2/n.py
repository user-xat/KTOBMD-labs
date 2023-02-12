# N. Выборы президента
n = int(input())
elements = input().split()
candidate, votes = 0, 0
for i in range(len(elements)):
    count = elements.count(elements[i])
    if count > votes:
        votes = count
        candidate = elements[i]
print(candidate)
