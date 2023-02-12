# M. Выборы в США
if __name__ == '__main__':
    FILENAME = '!elections.txt'
    applicants = dict()

    with open(FILENAME) as file:
        for line in file:
            surname, votes = line.split()
            applicants[surname] = applicants.get(surname, 0) + int(votes)

    for surname in sorted(applicants.keys()):
        print(surname, applicants[surname])
