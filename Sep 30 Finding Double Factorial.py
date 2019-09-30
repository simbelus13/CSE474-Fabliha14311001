'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

#Finding double factorial
def dF(n):
    if n==2:
        return 2
    if n==1:
        return 1
    if n==0:
        return 1
    return n*dF(n-2)
print(dF(int(input("Enter number to get a double factorial result "))))
