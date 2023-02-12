# B. Количество совпадающих
if __name__ == '__main__':
    first_set = set(input().split())
    second_set = set(input().split())
    print(len(first_set.intersection(second_set)))
