# https://codeforces.com/problemset/problem/263/A
mat = [input().split(), input().split(), input().split(), input().split(), input().split()]

m = 2
for x, a in enumerate(mat):
    if "1" in a:
        for y, b in enumerate(a):
            if b == "1":
                print(abs(x - m) + abs(y - m))
