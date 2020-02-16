
def extendedEuclidean(x, y):
    r1 = x
    r2 = y
    s1 = 1
    s2 = 0
    t1 = 0
    t2 = 1

    while True:
        q = r1 // r2
        r = r1 - q * r2
        s = s1 - q * s2
        t = t1 - q * t2
        

        print(q, r1, r2, r, s1, s2, s, t1, t2, t)

        r1 = r2
        r2 = r
        s1 = s2
        s2 = s
        t1 = t2
        t2 = t

        if r2 == 0:
            print("r2 is 0")
            print("r1: %1d r2: %1d s1: %1d s2: %1d t1: %1d t2: %1d" % (r1,r2,s1,s2,t1,t2))
            break


if __name__=="__main__":
    x = int(input('x: '))
    y = int(input('y: '))
    extendedEuclidean(x, y)
