# G. Миллионер
k = int(input())
res = '1'
i = 1
while i < k:
    i += len(res)
    res += '0'
if i == k:
    print('1')
else:
    print('0')
