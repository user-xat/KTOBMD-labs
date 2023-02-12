# C. Пересечение множеств
if __name__ == '__main__':
    first_set = set(map(int, input().split()))
    second_set = set(map(int, input().split()))
    intersect = sorted(first_set.intersection(second_set))
    [print(x, end=" ") for x in intersect]
    print()
