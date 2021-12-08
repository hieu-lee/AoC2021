commands = []
with open('testinput.txt') as f:
    for line in f.readlines():
        tmp = line.strip().split()
        tmp[1] = int(tmp[1])
        commands.append(tmp)


def question1():
    horizontal_pos = 0
    depth = 0
    for command in commands:
        if command[0] == "forward":
            horizontal_pos += command[1]
        elif command[0] == "up":
            depth -= command[1]
        elif command[0] == "down":
            depth += command[1]
    return horizontal_pos*depth


def question2():
    horizontal_pos = 0
    depth = 0
    aim = 0
    for command in commands:
        if command[0] == "up":
            aim -= command[1]
        elif command[0] == "down":
            aim += command[1]
        elif command[0] == "forward":
            horizontal_pos += command[1]
            depth += aim*command[1]
    return horizontal_pos*depth


print(question2())
