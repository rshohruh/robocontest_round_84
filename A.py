n, m = map(int, input().split())
if n < m or n > m*m:
    print(-1, -1)
else:
    print(max(0, n-m*4), (n-m)//4)