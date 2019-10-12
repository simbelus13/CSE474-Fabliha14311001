from mpmath import *
import math

def dF(x):
  if x==2:
    return 2
  if x==1:
    return 1
  if x==0:
    return 1
  return x*dF(x-2)
    
def sinm_cosn(m,n):
  if m<1 or n<1:
    return 'Invalid Inputs'
  elif m%2==0 and n%2==0:
    return (dF(m-1)*dF(n-1)*(pi/2))/dF(m+n)
  else:
    return (dF(m-1)*dF(n-1))/dF(m+n)

#Returns value of definite integral from question
print(sinm_cosn(int(input("Please enter value of m")), int(input("Please enter value of n"))))