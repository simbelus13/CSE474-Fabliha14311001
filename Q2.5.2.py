import math
tol = 1.e-14
an, bn = 1., math.sqrt(2)
while abs(an - bn) > tol:
  an, bn = (an + bn) / 2, math.sqrt(an * bn)
print('G = ',(1/an))