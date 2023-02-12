# H. Вклад
n, k = map(int, input().split())
double = n * 2
years = 0
while n < double:
    n += n*k/100
    years += 1
print(years)
