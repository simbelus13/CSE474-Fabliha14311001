import matplotlib.pyplot as plt
import numpy as np

def f(x):
  return x**3-5*x**2+x
  
def FwdDiff(x,h):
  return (f(x+h)-f(x))/h
  
def CentralDiff(x,h):
  return (f(x+h)-f(x-h))/(2*h)
  
def ActualDerivative(x):
  return 3*x**2-10*x+1

FwdDiffH1 = []
CentralDiffH1 = []

print("Taking h = 1")
print()
h=1

for i in range(-2,7):
  FwdDiffH1.append(FwdDiff(i,h))
  CentralDiffH1.append(CentralDiff(i,h))
  
for i in range(9):
  print("When x = ", i-2)
  print("Fwd Differencing result= ", FwdDiffH1[i])
  print("Central Differencing result= ", CentralDiffH1[i])
  print("Actual Derivative result = ", ActualDerivative(i-2))
  print()

AbsErrFwdH1 = []
AbsErrCentralH1= []

for i in range(9):
  AbsErrFwdH1.append(abs(FwdDiffH1[i]-ActualDerivative(i-2)))
  AbsErrCentralH1.append(abs(CentralDiffH1[i]-ActualDerivative(i-2)))

plt.ylabel('Absolute Error')
plt.xlabel('x')

plt.plot(range(-2,7),AbsErrFwdH1,'k')
plt.plot(range(-2,7),AbsErrCentralH1,'r')

FwdDiffHhalf = []
CentralDiffHhalf = []
print("Taking h = 0.5")
print()
h=0.5

for i in range(17):
  FwdDiffHhalf.append(FwdDiff(-2+0.5*i,h))
  CentralDiffHhalf.append(CentralDiff(-2+0.5*i,h))

for i in range(17):
  print("When x = ", -2+i*0.5)
  print("Fwd Differencing result= ", FwdDiffHhalf[i])
  print("Central Differencing result= ", CentralDiffHhalf[i])
  print("Actual Derivative result= ", ActualDerivative(-2+i*0.5))
  print()

AbsErrFwdHhalf = []
AbsErrCentralHhalf = []

for i in range(17):
  AbsErrFwdHhalf.append(abs(FwdDiffHhalf[i]-ActualDerivative(-2+i*0.5)))
  AbsErrCentralHhalf.append(abs(CentralDiffHhalf[i]-ActualDerivative(-2+i*0.5)))

plt.plot(np.arange(-2,6.3,0.5),AbsErrFwdHhalf,'b')
plt.plot(np.arange(-2,6.3,0.5),AbsErrCentralHhalf,'g')

print("Color labels are as follows")
print("Black : Forward Differencing at h = 1")
print("Red : Absolute Error for Central Differencing at h = 1")
print("Blue : Absolute Error for Forward Differencing at h = 0.5")
print("Green : Absolute Error for Central Differencing at h = 0.5")
print()
plt.show()
