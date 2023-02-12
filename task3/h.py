# H. Угадай число - 2
if __name__ == '__main__':
    n = int(input())
    supposed_numbers = set()
    waste_numbers = set()

    while True:
        question = input()
        if question == 'HELP':
            break
        numbers = set(map(int, question.split()))

        if len(numbers) <= n // 2:
            waste_numbers.update(numbers)
            print('NO')
        else:
            supposed_numbers.update(numbers)
            print('YES')
        n -= len(numbers)

    [print(x, end=" ")
     for x in sorted(supposed_numbers.difference(waste_numbers))]
    print()
