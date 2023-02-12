# N. Самое частое слово
if __name__ == '__main__':
    FILENAME = '!the_most_frequent_word.txt'
    words_count_dict = dict()

    with open(FILENAME) as file:
        for line in file:
            for word in line.split():
                words_count_dict[word] = words_count_dict.get(word, 0) + 1

    print(sorted(words_count_dict.items(),
          key=lambda x: (-x[1], x[0]))[0][0])
