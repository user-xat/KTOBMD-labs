# J. Забастовки
if __name__ == '__main__':
    n, k = map(int, input().split())
    strikes = set()

    for _ in range(k):
        a, b = map(int, input().split())
        d = a
        while d <= n:
            if not (d % 7 == 0 or (d+1) % 7 == 0):
                strikes.add(d)
            d += b

    print(len(strikes))
