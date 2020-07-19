# https://codeforces.com/problemset/problem/158/A
n, k = map(int, input().split())

partie = input().split()

min = int(partie[k - 1])
if min > 0:
    c = k
    for k in range(c, n):
        if int(partie[k]) == min:
            c += 1
        else:
            break
    print(c)
else:
    c = 0
    for i in partie:
        if int(i) > 0:
            c += 1
    print(c)
