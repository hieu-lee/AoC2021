def question1():
    c = 0
    check = {2, 4, 3, 7}
    with open("input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            _, v = line.split(" | ")
            v = [x.strip() for x in v.split()]
            for output in v:
                c += int(len(output) in check)
    return c


def question2():
    res = 0
    with open("input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            res += question2_helper(line)
    return res


def question2_helper(expression):
    u, v = expression.split(" | ")
    u = [x.strip() for x in u.split()]
    v = [x.strip() for x in v.split()]
    set_c_f = None
    set_b_d = None
    for signal in u:
        if len(signal) == 2:
            set_c_f = set(signal)
            break
    res = dict()
    for signal in u:
        if len(signal) == 3:
            for char in signal:
                if char not in set_c_f:
                    res["a"] = char
        if len(signal) == 4:
            set_b_d = set(signal).difference(set_c_f)
    for signal in u:
        if len(signal) == 6:
            tmp = set(signal)
            tmp = tmp.difference(set_c_f)
            tmp = tmp.difference(set_b_d)
            if len(tmp) == 2 and res["a"] in tmp:
                tmp.remove(res["a"])
                res["g"] = tmp.pop()
                break
    for signal in u:
        if len(signal) == 5:
            tmp = set(signal)
            if res["a"] in tmp and res["g"] in tmp:
                tmp.remove(res["a"])
                tmp.remove(res["g"])
                tmp = tmp.difference(set_b_d)
                if len(tmp) == 1:
                    res["f"] = tmp.pop()
                    for c in set_c_f:
                        if c != res["f"]:
                            res["c"] = c
                            break
    for signal in u:
        if len(signal) == 5:
            tmp = set(signal)
            if res["a"] in tmp and res["c"] in tmp and res["f"] in tmp and res["g"] in tmp:
                tmp.remove(res["a"])
                tmp.remove(res["c"])
                tmp.remove(res["f"])
                tmp.remove(res["g"])
                res["d"] = tmp.pop()
                for c in set_b_d:
                    if c != res["d"]:
                        res["b"] = c
                        break
    temp = set(res.values())
    temp = {"a", "b", "c", "d", "e", "f", "g"}.difference(temp)
    res["e"] = temp.pop()
    reverse_res = {res[k]: k for k in res}
    to_digit = {0: set("abcefg"), 1: set("cf"), 2: set("acdeg"), 3: set("acdfg"), 4: set(
        "bcdf"), 5: set("abdfg"), 6: set("abdfge"), 7: set("acf"), 8: set("abcdfge"), 9: set("abcdfg")}
    output = 0
    const = 1000
    for signal in v:
        tmp = set(signal)
        tmp = {reverse_res[x] for x in tmp}
        for d in to_digit:
            if tmp == to_digit[d]:
                output += const * d
                const //= 10
                break
    return output


print(question2())
