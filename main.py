def fibo(x):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(2,x):
        c=a+b
        a=b
        b=c
        print(c)
        
fibo(6)
