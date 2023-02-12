# I. Полиглоты
def print_result(user_set: set) -> None:
    print(len(user_set))
    [print(elem) for elem in user_set]


if __name__ == '__main__':
    n = int(input())
    everybody_knows = set()
    someone_knows = set()

    for _ in range(n):
        lang_count = int(input())
        lang = set()
        for _ in range(lang_count):
            lang.add(input())

        someone_knows.update(lang)
        if len(everybody_knows) == 0:
            everybody_knows.update(lang)
        else:
            everybody_knows.intersection_update(lang)

    print_result(everybody_knows)
    print_result(someone_knows)
