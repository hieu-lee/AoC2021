def question1(x):
    state = []
    with open("testinput.txt", "r") as f:
        lines = f.readlines()
        state = [int(x) for x in lines[0].split(",")]
    for _ in range(x):
        n = len(state)
        j = 0
        while j < n:
            if state[j] == 0:
                state[j] = 6
                state.append(8)
            else:
                state[j] -= 1
            j += 1
    return len(state)


def question2(x):
    state = []
    with open("input.txt", "r") as f:
        lines = f.readlines()
        state = [int(x) for x in lines[0].split(",")]
    res = 0
    for fish in state:
        res += question2_helper(fish, x)
    return res


def question2_helper(m, n):
    if n < 7:
        return 1 if m >= n else 2
    F = [[0 for _ in range(n+1)] for _ in range(9)]
    for i in range(9):
        for j in range(7):
            if i >= j:
                F[i][j] = 1
            else:
                F[i][j] = 2
    for j in range(7, n+1):
        for i in range(9):
            if i - 7 < 0:
                F[i][j] = F[i][j-7] + F[2+i][j-7]
            else:
                F[i][j] = F[i-7][j-7]
    return F[m][n]


print(question2(256))
