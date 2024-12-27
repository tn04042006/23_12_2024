def handle(f,x):
    return f(x)
#cách 1: thử ra lệnh cho lambda làm hàm kiểm tra số lẻ
ret1=handle(lambda x:x%2!=0,8)
print(ret1)

#cách 2: viết tường minh
def isOdd(n):
    return n%2 != 0
ret2=handle(lambda x:isOdd(x),7)
ret3=handle(isOdd,7)
print("ret2=",ret2)
print("ret3=",ret3)

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact=fact*i
    return fact
ret4=handle(lambda x:factorial(x),5)
print("5!=", ret4)

def handle2(f,x,y):
    return f(x,y)
ret5=handle2(lambda x,y:x+y,5,9)
print('ret5=', ret5)
