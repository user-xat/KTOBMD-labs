# K. Номер появления слова
if __name__ == '__main__':
    FILENAME = '!input.txt'
    words_count_dict = dict()

    with open(FILENAME) as file:
        for line in file:
            for word in line.split():
                if word in words_count_dict:
                    words_count_dict[word] += 1
                else:
                    words_count_dict[word] = 0
                print(words_count_dict[word], end=" ")
        print()
