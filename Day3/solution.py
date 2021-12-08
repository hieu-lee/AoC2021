numbers = []
with open('input.txt') as f:
    for line in f.readlines():
        numbers.append(line.strip())


def question1():
    n, m = len(numbers[0]), len(numbers)
    gamma = 0
    epsilon = 0
    for i in range(n):
        c = 0
        for j in range(m):
            c += int(numbers[j][i] == '1')
        bit = int(c >= (m >> 1))
        gamma <<= 1
        gamma |= bit
        epsilon <<= 1
        epsilon |= (1 - bit)

    return (gamma*epsilon)


def question2():
    n, m = len(numbers[0]), len(numbers)
    set_number = set(numbers)
    oxy_rating = "0b"
    carbon_rating = "0b"
    i = 0
    while len(set_number) > 1:
        c = 0
        for n in set_number:
            c += int(n[i] == "1")
        bit = int((c << 1) >= len(set_number))
        delete = []
        for n in set_number:
            if n[i] != str(bit):
                delete.append(n)
        for n in delete:
            set_number.remove(n)
        i += 1
    oxy_rating += set_number.pop()
    set_number = set(numbers)
    i = 0
    while len(set_number) > 1:
        c = 0
        for n in set_number:
            c += int(n[i] == "1")
        bit = 1 if ((c << 1) < len(set_number)) else 0
        delete = []
        for n in set_number:
            if n[i] != str(bit):
                delete.append(n)
        for n in delete:
            set_number.remove(n)
        i += 1
    carbon_rating += set_number.pop()
    return int(carbon_rating, 2) * int(oxy_rating, 2)


print(question2())
