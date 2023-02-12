# R. Банковские счета
FILENAME = '!bank_accounts.txt'
clients_info = dict()


def deposit(name: str, sum: int) -> None:
    clients_info[name] = clients_info.get(name, 0) + sum


def withdraw(name: str, sum: int) -> None:
    clients_info[name] = clients_info.get(name, 0) - sum


def transfer(name1: str, name2: str, sum: int) -> None:
    clients_info[name1] = clients_info.get(name1, 0) - sum
    clients_info[name2] = clients_info.get(name2, 0) + sum


def balance(name: str) -> None:
    if name in clients_info:
        print(clients_info[name])
    else:
        print('ERROR')


def income(p: int) -> None:
    for name in clients_info.keys():
        if clients_info[name] > 0:
            clients_info[name] = int(
                clients_info[name]*p/100) + clients_info[name]


if __name__ == '__main__':
    with open(FILENAME) as fin:
        for line in fin:
            operation_data = line.split()
            operation = operation_data[0]
            if operation == 'DEPOSIT':
                deposit(operation_data[1], int(operation_data[2]))
            elif operation == 'WITHDRAW':
                withdraw(operation_data[1], int(operation_data[2]))
            elif operation == 'TRANSFER':
                transfer(operation_data[1],
                         operation_data[2], int(operation_data[3]))
            elif operation == 'BALANCE':
                balance(operation_data[1])
            elif operation == 'INCOME':
                income(int(operation_data[1]))
