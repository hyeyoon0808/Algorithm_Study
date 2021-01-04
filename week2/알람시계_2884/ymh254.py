n, m = list(map(int, input().split()))

if m < 45:
    if n == 0:
        n = 23
        m = 60 - (45-m)
    else:
        n = n-1
        m = 60 - (45-m)
else:
    n = n
    m = m-45
print("{0}:{1}".format(n, m))
