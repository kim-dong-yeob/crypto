def euclidean(a,b):
    r1 = a
    r2 = b
 
    while 1:
        q = r1//r2
        r = r1%r2
        print(q,r1,r2,r)
 
        r1 = r2
        r2 = r
 
        if r2 == 0:
            print("gcd({})".format(r1))
            break
 
N1,N2 = map(int, input().split())
print("q  r1   r2   r")
euclidean(N1,N2)
