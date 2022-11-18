try:
    import sys
    import math
    import collections
    M = 10 ** 9 + 7
    def solve():
        n, m = map(int, input().split())
        arr = list(map(int, input().split()))
        temp = arr.copy()
        temp.sort()
        total = [0] * m
        d = collections.defaultdict(lambda: 0)
        for i in arr:
            d[i] += 1

        count = 0
        for i in range(m):
            for j in range(m):
                if (arr[i] == temp[j]):
                    index = j + (d[arr[i]] - 1)
                    total[index] = 1
                    d[arr[i]] -= 1
                    break
                else:
                    if (total[j] == 1):
                        count += 1

        return count

        n = int(input())
        A = input()
        B = input()
        A = A.replace("\r", "")
        B = B.replace("\r", "")
        i = 0
        cou = 0
        while (i < n):
            if ((A[i] == "0" and B[i] == "1") or (A[i] == "1" and B[i] == "0")):
                cou += 2
                i += 1
            elif (A[i] == "1" and B[i] == "1" and i < n - 1):
                if (A[i + 1] == "0" and B[i + 1] == "0"):
                    cou += 2
                    i += 2
                else:
                    cou += 0
                    i += 1
            elif (A[i] == "1" and B[i] == "1"):
                i += 1
            elif (A[i] == "0" and B[i] == "0" and i < n - 1):
                if (A[i + 1] == "1" and B[i + 1] == "1"):
                    cou += 2
                    i += 2
                else:
                    cou += 1
                    i += 1
            elif (A[i] == "0" and B[i] == "0"):
                cou += 1
                i += 1
            else:
                i += 1

        return cou
        for i in range(0, n):
            if (A[i] == "1" and B[i] == "1"):
                new_A += "1"
            elif ((A[i] == "0" and B[i] == "1") or (A[i] == "1" and B[i] == "0")):
                cou += 2
            else:
                new_A += "0"
        if (len(new_A) == 0):
            return cou
        new_B = "" + new_A[0]
        for i in range(1, len(new_A)):
            if (new_A[i] == "1" and new_A[i - 1] == "1"):
                pass
            else:
                new_B += new_A[i]
        count_one = new_B.count("1")
        count_zero = new_B.count("0")
        if (count_one > count_zero):
            cou += 2 * count_zero
        else:
            cou += 2 * count_one + (count_zero - count_one)
        return cou
        count_0 = new_string.count("0")
        if (count_0 == 0):
            return 0
        elif (count_0 == 1):
            return 1
        elif (count_0 > 1):
            return 2
        else:
            return 2

        if (n % 2):
            return (k // ((n // 2) + 1))
        else:
            return (k // ((n // 2) + 1))
        temp = modularExponentiation(2, n) - 1
        return modularExponentiation(temp, k)


    test = int(input())
    count1 = 1
    while count1 <= test:
        ans = solve()
        sys.stdout.write(str(ans) + "\n")
        count1 += 1
except EOFError:
    print("")