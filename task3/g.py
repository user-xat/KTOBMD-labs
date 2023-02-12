# G. Угадай число
if __name__ == '__main__':
    n = int(input())
    supposed_numbers = set()
    waste_numbers = set()

    while True:
        question = input()
        if question == 'HELP':
            break
        numbers = list(map(int, question.split()))

        answer = input()
        if answer == 'YES':
            supposed_numbers.update(numbers)
        else:
            waste_numbers.update(numbers)

    [print(x, end=" ")
     for x in sorted(supposed_numbers.difference(waste_numbers))]
    print()
