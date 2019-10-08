def function(x):
    return x * (x + 2) - 1

xn1 = float(input("Enter beginning of interval: "))
xn = float(input("Enter end of interval: "))
precision = float(input("Enter precision of method: "))

x = xn1

if(function(xn1) * function(xn) < 0):
  while(abs(function(x)) > precision):
    print("X: ", x, " f(x): ", function(x))

    x = xn - ((function(xn) * (xn - xn1)) / (function(xn) - function(xn1)))
    xn1 = xn
    xn = x