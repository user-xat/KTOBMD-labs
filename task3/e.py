# E. Кубики
def print_result(user_set: set) -> None:
    print(len(user_set))
    [print(x, end=" ") for x in sorted(user_set)]
    print()


if __name__ == '__main__':
    FILENAME = '!cubes.txt'
    anya_set = set()
    borya_set = set()
    with open(FILENAME) as file:
        n, m = map(int, file.readline().split())
        for _ in range(n):
            anya_set.add(int(file.readline().strip()))
        for _ in range(m):
            borya_set.add(int(file.readline().strip()))

    print_result(anya_set.intersection(borya_set))
    print_result(anya_set.difference(borya_set))
    print_result(borya_set.difference(anya_set))
