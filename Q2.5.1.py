a = [2,4,10,6,8,4]
aMin = min(a)
aMax = max(a)
for i in range(len(a)):
  val = a[i]
  a[i] = (val-aMin) / (aMax-aMin)
  print (a[i])
