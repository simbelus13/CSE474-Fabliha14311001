import urllib2
import numpy

data = urllib2.urlopen("https://scipython.com/static/media/problems/P2.6/redwood-data.txt").read()


#At first I created an array to store all the data
lS = []

#Each letter stored as a separate element in the list
for line in data:
    lS.append(line)

#Deleting unnecessary text in the beginning
popp=0
for n in range(len(lS)-1):
  if lS[n]=='A':
    popp=n
    break


lS = lS[popp : len(lS)]

#To check new list:
#print (lS)

#To print data line by line as shown in actual text:
#data = data.splitlines()
#for line in data:
  #print (line)


#Creating 4 separate lists to store the 4 different data
treeN = []
loc = []
diameter = []
height = []

#Finding out the number of lines in the text
limit = 0
for i in range(len(lS)):
  if lS[i]=='\n':
    limit=limit+1
#print limit

#Combining elements whenever I encounter a \t or \n which marks beginning of new type.
#Appending the new combined element into a separate list
#Deleting the combined element and running the whole process again
#lim==2 because numbers and strings have to be stored in separate arrays to avoid unidentifiable error

#For String type
Arr = []
def makePrpArr(lim,i):
  if lim==2:
    return
  if (lS[i]=='\t') or (lS[i]=='\n'):
    lS.pop(i)
    lS[0 : i] = [''.join(lS[0 : i])]
    Arr.append(lS[0])
    lS.pop(0)
    lim=lim+1
    makePrpArr(lim,i)
  else:
    makePrpArr(lim,i+1)

#For floating point type
Arr2 = []
def makePrpArr2(lim, i):
  if lim==2:
    return
  if (lS[i]=='\t') or (lS[i]=='\n'):
    lS.pop(i)
    lS[0 : i] = [''.join(lS[0 : i])]
    Arr2.append(lS[0])
    lS.pop(0)
    lim=lim+1
    makePrpArr2(lim,i)
  else:
    makePrpArr2(lim,i+1)

#Whole process runs as the same number of times as number of trees in text
for iter in range (limit):
  lim=0 
  makePrpArr(lim,0)
  lim=0
  makePrpArr2(lim,0)

#Now storing data into 4 separate lists
for iter in range (limit*2):
  if(iter%2==0):
    treeN.append(Arr[iter])
  else:
    loc.append(Arr[iter])

for iter in range (limit*2):
  if(iter%2==0):
    diameter.append(Arr2[iter])
  else:
    height.append(Arr2[iter])

#Finding max
tallestTree = max(height)
greatestDiameter = max(diameter)

for itr in range(limit):
  if height[itr]==tallestTree:
    print("Tallest tree is "+str(treeN[itr])+" located at "+str(loc[itr])+" of length "+str(tallestTree)+"m")
    break

for itr in range(limit):
  if diameter[itr]==greatestDiameter:
    print("Tree with greatest diameter is "+str(treeN[itr])+" located at "+str(loc[itr])+" of diameter "+str(greatestDiameter)+"m")
    break

