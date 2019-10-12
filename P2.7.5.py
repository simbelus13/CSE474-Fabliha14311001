from mpmath import *
import math

def RangeAndHeight(a,v):
  R=((v**2)*(sin(2*a)))/9.81
  H=((v**2)*(sin(a)*sin(a)))/(2*9.81)
  value=[R,H]
  return value
  
rgANDht=RangeAndHeight(float(30*(pi/180)), float(10))
print ('Range of projectile is ', rgANDht[0])
print ('Maximum height attained by projectile is ' ,rgANDht[1])