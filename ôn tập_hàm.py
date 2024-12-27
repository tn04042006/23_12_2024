def giaithua(n):
    gt=1
    for i in range (1,n+1):
        gt=gt*i
    return gt
def A(n,k):
    return giaithua(n)/giaithua(n-k)
def C(n,k):
    return giaithua(n)/(giaithua(n-k)*giaithua(k))
gt_5=giaithua(5)
print("5!=", gt_5)
print("A(5,3)=", A(5,3))
print("C(5,3)=",C(5,3))


