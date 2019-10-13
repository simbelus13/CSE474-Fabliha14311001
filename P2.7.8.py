def exp(x,n):
  t=0
  if (n==0):
    t=1
  else:
    if (n%2==0):
      t=(exp(x,n/2)*exp(x,n/2))
    else:
      t= x*exp(x,n-1)
  return t

def tetration(x,n):
  if (n == 0):
    return 1
  else:
    return exp(x, tetration(x, n-1))
    

x=2
n=4
print(tetration(x,n))


