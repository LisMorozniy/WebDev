def foo(a, b, c, d):
    if (a <= b and a <= c and a <= d):
        print(a)
    elif (b <= a and b <= c and b <= d):
        print (b)
    elif (c <= a and c <= b and c <= d):
        print (c)
    elif (d <= a and d <= b and d <= c):
        print (d)

a = list(map(int,input().split()))

foo(a[0], a[1], a[2], a[3])
