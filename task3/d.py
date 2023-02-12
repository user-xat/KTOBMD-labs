# D. Встречалось ли число раньше
if __name__ == '__main__':
    numbers = input().split()
    already_seen = set()
    for x in numbers:
        if x in already_seen:
            print("YES")
        else:
            already_seen.add(x)
            print("NO")
