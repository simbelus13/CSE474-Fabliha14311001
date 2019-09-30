'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

def Fact(n):
    if n==2:
        return 2
    if n==1:
        return 1
    if n==0:
        return 1
    return n*Fact(n-1)

def Power(b, p):
    b2=b
    if p==0:
        return 1
    else:
        for i in range(p-1):
            b*=b2        
        return b


x = int(input("Input number to find the exponential for that "))
sum=0
for i in range(1000):
    #print("Power is",Power(x,i))
    #print("factorial is", Fact(i))
    sum=sum+((Power(x,i))/(Fact(i)))
print("exp("+str(x)+") =",sum)
