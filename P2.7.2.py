def dF(n):
    if n==2:
        return 2
    if n==1:
        return 1
    if n==0:
        return 1
    return n*dF(n-1)
j=1
while j>0:
  result = dF(j)
  print ('for ', j)
  print(result, ' is factorial')
  digits = list(str(result))
  for i in range (len(digits)):
    digits[i]=int(digits[i])
  sum=0
  for i in range (len(digits)):
    sum=sum+digits[i]
  print (sum, ' is sum of factorial digits')
  #print(result%sum)
  if (result%sum)!=0:
    print(j, 'is answer because its factorial is not divisible by sum of its digits.')
    j=0
  else:
    j=j+1
    print()
