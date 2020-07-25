# https://codeforces.com/problemset/problem/546/A
k, n, w = map(int, input().split())

prix = ((w * (w + 1)) // 2) * k

if prix - n < 0:
    print(0)
else:
    print(prix - n)
