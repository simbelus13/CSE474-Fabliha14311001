import numpy
import matplotlib.pyplot
def f(x):
  return x**5+2*(x**2)+3*(x**3)+x+1
def derivf(x):
  return 5*(x**4)+4*x+9*(x**2)+1
  
NewtonMethodIteration = []

def NewtonMethod(xOld):
  xNew = xOld - f(xOld)/derivf(xOld)
  return xNew

xOld = 2.134
#input("Please enter value for x")
xNew = 0.0
for i in range(int(input("Please input number of iterations for x"))):
  xNew = NewtonMethod(xOld)
  #xNew = NewtonMethodIteration.append(NewtonMethod(xOld))
  print (xNew)
  xOld = xNew
  
  
