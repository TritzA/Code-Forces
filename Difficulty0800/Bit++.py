# https://codeforces.com/problemset/problem/282/A
n = int(input())

c = 0
for _ in range(n):
    s = input()
    if "+" in s:
        c += 1
    else:
        c -= 1

print(c)
