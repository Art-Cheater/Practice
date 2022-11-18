tests = int(input())

for test in range(tests):
    n = int(input())
    s_original = list(input())
    s_sorted = sorted(s_original)
    k = 0
    i = 0
    while i < n:
        if s_original[i] != s_sorted[i]:
            k += 1

        i += 1
    print(k)
