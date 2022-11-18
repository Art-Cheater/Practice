test = int(input())

for test in range(test):
    n = int(input())
    s = input()

    out = []
    for x in s:
        if x == "U":
            out.append("D")
        elif x == "D":
            out.append("U")
        elif x == "L":
            out.append("L")
        elif x == "R":
            out.append("R")
    print(*out, sep="")
