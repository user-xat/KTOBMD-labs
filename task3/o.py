# O. Права доступа
def check_permission(perm: str, permissions: list[str]) -> None:
    if perm in permissions:
        print('OK')
    else:
        print("Access denied")


if __name__ == '__main__':
    FILENAME = '!access_rights.txt'
    files_dict = dict()

    with open(FILENAME) as fin:
        n = int(fin.readline().strip())
        for _ in range(n):
            file_and_rights = fin.readline().split()
            files_dict[file_and_rights[0]] = file_and_rights[1:]

        m = int(fin.readline().strip())
        for _ in range(m):
            operation, file = fin.readline().split()
            if operation == 'read':
                check_permission('R', files_dict[file])
            elif operation == 'write':
                check_permission('W', files_dict[file])
            elif operation == 'execute':
                check_permission('X', files_dict[file])
