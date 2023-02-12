# P. Частотный анализ
if __name__ == '__main__':
    FILENAME = '!frequency_analysis.txt'
    words_frequency = dict()

    with open(FILENAME) as fin:
        for line in fin:
            for word in line.split():
                words_frequency[word] = words_frequency.get(word, 0) + 1

    [print(word[0]) for word in sorted(
        words_frequency.items(), key=lambda x: (-x[1], x[0]))]
