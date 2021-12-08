from collections import Counter


def question1():
    tracker = Counter()
    with open('input.txt') as f:
        lines = f.readlines()
        for line in lines:
            u, v = line.split(" -> ")
            u = [int(x) for x in u.split(",")]
            v = [int(x) for x in v.split(",")]
            if u[0] == v[0]:
                for i in range(min(u[1], v[1]), max(u[1], v[1]) + 1):
                    tracker[(u[0], i)] += 1
            elif u[1] == v[1]:
                for i in range(min(u[0], v[0]), max(u[0], v[0]) + 1):
                    tracker[(i, u[1])] += 1
    res = 0
    for point in tracker:
        if tracker[point] > 1:
            res += 1
    return res


def question2():
    tracker = Counter()
    with open('input.txt') as f:
        lines = f.readlines()
        for line in lines:
            u, v = line.split(" -> ")
            u = [int(x) for x in u.split(",")]
            v = [int(x) for x in v.split(",")]
            if u[0] == v[0]:
                for i in range(min(u[1], v[1]), max(u[1], v[1]) + 1):
                    tracker[(u[0], i)] += 1
            elif u[1] == v[1]:
                for i in range(min(u[0], v[0]), max(u[0], v[0]) + 1):
                    tracker[(i, u[1])] += 1
            elif abs(u[0] - v[0]) == abs(u[1] - v[1]):
                if u[0] > v[0] and u[1] > v[1]:
                    for i in range(0, u[0] - v[0] + 1):
                        tracker[(u[0] - i, u[1] - i)] += 1
                elif u[0] < v[0] and u[1] < v[1]:
                    for i in range(0, v[0] - u[0] + 1):
                        tracker[(u[0] + i, u[1] + i)] += 1
                elif u[0] > v[0] and u[1] < v[1]:
                    for i in range(0, u[0] - v[0] + 1):
                        tracker[(u[0] - i, u[1] + i)] += 1
                elif u[0] < v[0] and u[1] > v[1]:
                    for i in range(0, v[0] - u[0] + 1):
                        tracker[(u[0] + i, u[1] - i)] += 1
    res = 0
    for point in tracker:
        if tracker[point] > 1:
            res += 1
    return res


if __name__ == "__main__":
    print(question2())
