x=int(input("enter the value: "))
def fact(x):
    j=1
    for i in range(1,x+1):
        j=j*i
    return j

result=fact(x)
print(result)