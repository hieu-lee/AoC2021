import math


def question1():
    arr = []
    with open("input.txt", "r") as f:
        lines = f.readlines()
        arr = [int(x) for x in lines[0].split(",")]
    m = int(median(arr))
    res = 0
    for a in arr:
        res += abs(a - m)
    return res


def median(arr):
    arr.sort()
    if len(arr) % 2 == 0:
        return (arr[len(arr)//2] + arr[len(arr)//2 - 1]) / 2
    else:
        return arr[len(arr)//2]


def question2_helper(arr):
    arr.sort()
    n = len(arr)
    S = [None] * n
    S[0] = arr[0]
    Sos = arr[0]**2
    for i in range(1, n):
        Sos += arr[i]**2
        S[i] = S[i - 1] + arr[i]
    res = math.inf
    for i in range(0, n-1):
        # x in [arr[i], arr[i+1]]
        t = n - 2 * (i+1)  # v - u
        k = (S[-1] + t/2) / n
        if arr[i] <= k <= arr[i+1]:
            x, y, z = int(math.floor(k + 0.5)), arr[i], arr[i+1]
            (tmp, tmp1, tmp2) = (
                Sos + n*x**2 - 2*x*S[-1] + (S[-1] - 2*S[i]) - t*x,
                Sos + n*y**2 - 2*y*S[-1] + (S[-1] - 2*S[i]) - t*y,
                Sos + n*z**2 - 2*z*S[-1] + (S[-1] - 2*S[i]) - t*z)
            tmp //= 2
            tmp1 //= 2
            tmp2 //= 2
            res = min(res, tmp)
            res = min(res, tmp1)
            res = min(res, tmp2)
        elif k < arr[i]:
            x = arr[i]
            tmp = Sos + n*x**2 - 2*x*S[-1] + (S[-1] - 2*S[i]) - t*x
            tmp //= 2
            res = min(res, tmp)
        else:
            x = arr[i+1]
            tmp = Sos + n*x**2 - 2*x*S[-1] + (S[-1] - 2*S[i]) - t*x
            tmp //= 2
            res = min(res, tmp)
    return res


def question2():
    arr = []
    with open("input.txt", "r") as f:
        lines = f.readlines()
        arr = [int(x) for x in lines[0].split(",")]
    return question2_helper(arr)


print(question2())
