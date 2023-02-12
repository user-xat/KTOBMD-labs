################## Задача 2. Сравнение предложений ######################
import numpy as np
import re
from scipy.spatial.distance import cosine


# Читает текст из переданного файла
def get_text(filename: str) -> str:
    text = ""
    with open(filename) as fin:
        text = fin.read()
    return text


# Возвращает список уникальных слов в тексте
def get_words(text: str) -> set[str]:
    return set(filter(lambda x: x != "", re.split(r"[^A-z]", text.lower())))


# Назначает каждому слову уникальный индекс
def get_tokens(words: set[str]) -> dict[str, int]:
    tokens = dict()
    i = 0
    for word in words:
        tokens[word] = i
        i += 1
    return tokens


# Возвращает матрицу n*d, где n - количество предложений, а d - количество уникальных слов в тексте
def get_matrix(text: str, sentence_count: int, tokens: dict[str, int]) -> np.ndarray:
    matrix = np.zeros((sentence_count, len(tokens)))
    i = 0

    for sentence in text.split('\n'):
        words = get_words(sentence)
        for word in words:
            matrix[i, tokens[word]] += 1
        i += 1

    return matrix


# Возвращает номера двух ближайщих предложений к первому
def find_closest_sentence(matrix) -> tuple[int, int]:
    max_first = 0
    sentence_first, sentence_second = 0, 0

    for i in range(1, len(matrix)):
        similarity = cosine(matrix[0], matrix[i])
        if similarity >= max_first:
            max_first = similarity
            sentence_first, sentence_second = i, sentence_first

    return (sentence_first, sentence_second)


if __name__ == '__main__':
    FILENAME = 'sentences.txt'
    n = 22  # количество предложений

    text = get_text(FILENAME)
    words = get_words(text)
    tokens = get_tokens(words)
    matrix = get_matrix(text, n, tokens)

    first, second = find_closest_sentence(matrix)

    with open('submission-1.txt', 'w') as fout:
        fout.write("{:d} {:d}".format(first, second))
