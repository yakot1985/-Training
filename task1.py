a = [int(i) for i in input().split()]
if len(a) == 1:
    print(a[0])
else:
    for i in range(0,len(a)):
        if i == 0:
            s = (a[i+1]) + (a[len(a)-1])
            print(s,end=' ')
        elif i == len(a)-1:
            s = a[0] + a[len(a)-2]
            print(s,end=' ')
        else:
            s = (a[i-1]) + (a[i+1])
            print(s,end=' ')