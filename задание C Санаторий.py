con = list(map(int, input().split()))
k = 0
con.sort()
for i in range(2):
    if (con[2] - 1) > con[i]:
         k += ((con[2] - 1) - con[i])
print(k)