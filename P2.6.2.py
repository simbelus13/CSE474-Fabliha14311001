strngg = "Write a program to read in a text file and censor any words in it that \n are on a list of banned words by replacing their letters with the same number of asterisks. Your program should store the banned words in \n lowercase but censor examples of these words in any case. Assume there is no punctuation."
#Same method as P2.6.1 may be implemented to read text, then break down text into separate letters, and then recombining letters to form words and finally store them as separate elements in the list
print (strngg)

print('....................................................')

aRR = []
#for line in range (len(strngg)):
aRR = strngg.split()
#print aRR

for i in range (len(aRR)):
  if (aRR[i]=='program') or (aRR[i]=='words') or (aRR[i]=='number'):
    size = len(aRR[i])
    aRR[i]='*'
    for j in range (size-1):
      aRR[i]=aRR[i]+'*'

print (aRR)