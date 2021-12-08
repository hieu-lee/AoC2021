measures = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        measures.append(int(line.strip()))


def question1():
    c = 0
    for i in range(1, len(measures)):
        if measures[i] > measures[i - 1]:
            c += 1
    return c


def question2():
    prev_index = 0
    prev_sum = measures[0] + measures[1] + measures[2]
    i = 1
    c = 0
    while i < len(measures) - 2:
        sum = prev_sum + measures[i + 2] - measures[prev_index]
        if sum > prev_sum:
            c += 1
        prev_sum = sum
        prev_index = i
        i += 1
    return c


print(question2())
