print("Considering the recurrence relation x0 = 1, x1 = (1/3), and x^(N+1) = (13/3)xN - (4/3)x^(N-1), leads to:" )
x=1.0
y=(1/3)
for i in range(14):
    z=(13/3)*y-(4/3)*x
    x=y
    y=z
    print("x"+str(i+2) ,"=", z)
print()
err=(1/3)**15
print("However, x"+str(15) ,"in accordance to the closed form expression is",(1/3)**15)
abserr = (z-err)
relerr=(z-err)/z
print()
print("Therefore, at x15 Relative error is ", str(relerr) +", and, Absolute error is", abserr)