# F. Количество слов в тексте
if __name__ == '__main__':
    FILENAME = '!words_count.txt'
    words_set = set()
    with open(FILENAME) as file:
        words_set.update(file.read().split())
    print(len(words_set))
