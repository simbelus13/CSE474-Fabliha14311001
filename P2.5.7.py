print("Generating Hailstone Sequence starting at 27")
n = 27
while(n>0):
  if (n==1):
    print(1)
    break
  elif (n%2==0):
    print(int(n))
    n=n/2
  else:
    print(int(n))
    n=int((3*n)+1)
print()
n = int(input("Input number to generate stopping time of Hailstone Sequence"))
a = []
if n>0:
  while(n>0):
    if (n==1):
      a.append(1)
      break
    elif (n%2==0):
      a.append(int(n))
      n=n/2
    else:
      a.append(int(n))
      n=int((3*n)+1)
  print(len(a))