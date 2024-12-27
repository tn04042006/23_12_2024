def H10toH2(n):
    if n>0:
        sd=n%2
        n=n//2
        H10toH2(n)
        print(sd, end=' ')
n=587
H10toH2(n)