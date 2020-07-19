# https://codeforces.com/problemset/problem/231/A
n = int(input())

cmpt = 0
for _ in range(n):
    if len(input().replace("0", "")) > 3:
        cmpt += 1

print(cmpt)
