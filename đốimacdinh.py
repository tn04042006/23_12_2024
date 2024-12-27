def isPrimenumber(x):
    count=0
    for i in range(1,x+1):
        if x%1==0:
            count=count+1
    return count==2
def handle(f,x):
    return f(x)
ret=handle(lambda x:isPrimenumber(x),6)
print(ret)
