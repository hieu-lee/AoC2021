class Board:
    def __init__(self, rows, columns, position):
        self.rows = rows
        self.columns = columns
        self.unmarked = {i for i in position}
        self.position = position

    def mark(self, number) -> bool:
        if number in self.unmarked:
            self.unmarked.remove(number)
            i, j = self.position[number]
            self.rows[i].remove(number)
            self.columns[j].remove(number)
            return (not self.rows[i] or not self.columns[j])


numbers = []
boards = []

with open("testinput.txt") as f:
    lines = f.readlines()
    numbers = [int(x) for x in lines[0].strip().split(",")]
    for i in range(2, len(lines), 6):
        rows = [[int(x) for x in lines[j].split()] for j in range(i, i + 5)]
        columns = [[rows[j][i] for j in range(5)] for i in range(5)]
        position = dict()
        for i in range(5):
            for j in range(5):
                position[rows[i][j]] = (i, j)
        rows = [set(x) for x in rows]
        columns = [set(x) for x in columns]
        boards.append(Board(rows, columns, position))


def question1():
    for n in numbers:
        for b in boards:
            if b.mark(n):
                return n*sum(b.unmarked)


def question2():
    res = 0
    count = 0
    for b in boards:
        c = 0
        for n in numbers:
            c += 1
            if b.mark(n):
                if c > count:
                    count = c
                    res = n*sum(b.unmarked)
                break
    return res


print(question2())
