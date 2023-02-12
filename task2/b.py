# B. Приглашения и конверты
a, b = int(input()), int(input())
c, d = int(input()), int(input())
if a <= c and b <= d or a <= d and b <= c:
    print('YES')
else:
    print('NO')
