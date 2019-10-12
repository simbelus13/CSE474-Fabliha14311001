from mpmath import *
import math

def pyramid_AV(n,s,h):
  a=0.5*s*cot(pi/n)
  A=0.5*n*s*a
  l = sqrt(h**2 + a**2)
  V=(1/3)*A*h
  S=A+(1/2)*n*s*l
  val=[V,S]
  return val
  
  
n=float(input('Enter no. of sides of regular polygon'))
s=float(input('Enter length of side'))
h=float(input('Enter height of pyramid'))
ans = pyramid_AV(n,s,h)
print('Volume = ',ans[0])
print('Total Surface Area = ',ans[1])