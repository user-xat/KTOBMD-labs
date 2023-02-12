# S. Англо-латинский словарь
if __name__ == '__main__':
    latin_english_dict = dict()

    n = int(input().strip())
    for _ in range(n):
        english_word, latin_words = input().split(sep=" - ")
        latin_words = latin_words.split(sep=", ")
        for latin_word in latin_words:
            if latin_word in latin_english_dict:
                latin_english_dict[latin_word].append(english_word)
            else:
                latin_english_dict[latin_word] = [english_word]

    print(len(latin_english_dict))
    for word in sorted(latin_english_dict.keys()):
        latin_english_dict[word].sort()
        print("{} - {}".format(word,
              ", ".join(latin_english_dict[word])))
