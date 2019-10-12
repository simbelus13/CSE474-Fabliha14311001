#run in python 2.7
import urllib2
import numpy

data = urllib2.urlopen("https://scipython.com/static/media/problems/P2.6/ex2-6-g-esi-data.txt").read()

#To print data line by line as shown in actual text:
data = data.splitlines()
for line in data:
  print (line)

#concatanating where name of astronomical object has been split into separate columns
def con(x):
  if x[0]=='Earth' or x[0]=='Jupiter':
    return x
  else:
    c=0
    for i in range (len(x)):
      ind=list(x[1])
      chk2=0
      for w in range (len(ind)):
        if (ind[w]) == '.':
          chk2=chk2+1
      if chk2!=0:
        return x
      elif c==2:
        return x
      elif c==1:
        i=i-1
        if type(x[i+1])==str:
          x[i] = x[i]+x[i+1]
          x.pop(i+1)
          c=c+1
          return x
        elif type(x[i+1])==int:
          x[i] = x[i]+x[i+1]
          x.pop(i+1)
          c=c+1
          return x
      if c==0:
        if type(x[i+1])==str:
          x[i] = x[i]+x[i+1]
          x.pop(i+1)
          c=c+1
        elif type(x[i+1])==int:
          x[i] = x[i]+x[i+1]
          x.pop(i+1)
          c=c+1
    


#To arrange data in proper order i.e. concatanating where name of astronomical object has been split into separate columns
print
for r in range (3, len(data)):
  data[r]=data[r].split()
  letters=list(data[r][1])
  chkk=0
  for w in range (len(letters)):
    if (letters[w]) == '.':
      chkk=chkk+1
  if chkk==0:
    data[r]=con(data[r])
  print data[r]

#w_i = parameter value of mars: parameter value of earth
#range of r varies from Earth i.e. data[3] to WASP-26b
#range of s iterates through the parameters for individual astronomical bodies. s=n in original formula
print
ESI=[0,0,0,1,1,1,1,1,1,1,1,1,1,1,1]
for r in range (3,15):
  for s in range (1,8):
    numerator = float(data[r][s])-float(data[3][s])
    denominator = float(data[r][s])+float(data[3][s])
    exp=(float(data[r][s])/float(data[3][s]))/(s)
    ESI[r]=ESI[r]*((1-abs(numerator/denominator))**exp)

for c in range (3,15):
  print"ESI of", data[c][0], "=", ESI[c]
