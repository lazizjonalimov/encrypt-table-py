def solution(table):
    n = len(table[0])

    t = [[0] * 2*n for i in range(2*n)]

    i = 0
    for i in range(2*n):
        j = 0
        while j < n:
            t[2 * n - i//2 - j - 1][2 * n - 3 - i % 2 - i//2 + j] = table[i][j]

            j += 1

    encrypted_t = [[0] *n for i in range(2*n)]
    i = 0
    for i in range(2*n):
        j = 0
        while j < n:
            encrypted_t[i][j] = t[2 * n - i // 2 - j - 1][2 * n - 4 + i % 2 + i // 2 - j]
            j += 1

    print('[', end='')
    for i in encrypted_t:
        if encrypted_t[-1] == i:
            print(f'{i}]')
            break
        print(f'{i},')

table = [['a', 'b', 'c'],
         ['d', 'e', 'f'],
         ['g', 'h', 'i'],
         ['j', 'k', 'l'],
         ['m', 'n', 'o'],
         ['p', 'q', 'r']]



print(solution(table))
