# https://codeforces.com/problemset/problem/266/A
n, s = int(input()), input()

c = 0
for i in range(1, n):
    p = s[i - 1]
    if p == s[i]:
        c += 1

print(c)
