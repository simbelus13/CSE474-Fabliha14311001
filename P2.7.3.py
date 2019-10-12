def dotProd(x,y):
  return ((x[0]*y[0]) + (x[1]*y[1]) + (x[2]*y[2]))
def vectorProd(a,b):
  crossProd = [0,0,0]
  crossProd[0] = (a[1]*b[2])-(a[2]*b[1])
  crossProd[1] = (a[2]*b[0])-(a[0]*b[2])
  crossProd[2] = (a[0]*b[1])-(a[1]*b[0])
  return crossProd
def scalar3prod(x,y,z):
  return dotProd(x, vectorProd(y,z))
def vector3prod(x,y,z):
  return vectorProd(x, vectorProd(y,z))
  
#a = 2i + 3j - k
a=[2,3,-1]
#b = 4i -2j + 5k
b=[4,-2, 5]
#c = 23i+17j+21k
c=[23,17,21]

dotProduct = (dotProd(a,b))
print (dotProduct)
crossProduct = []
crossProduct = vectorProd(a,b)
print (crossProduct)
scalarTripleProduct = scalar3prod(a,b,c)
print (scalarTripleProduct)
vectorTripleProduct = []
vectorTripleProduct = vector3prod(a,b,c)
print (vectorTripleProduct)