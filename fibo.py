r=int(input("enter the value: "))
def fibo(r):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(2,r+1):
         c=a+b
         a=b
         b=c
         print(c)
        


fibo(r)
