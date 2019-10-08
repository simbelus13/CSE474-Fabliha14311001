#!/usr/bin/env python
# coding: utf-8

# In[45]:


#Text file read from pc, stored as separate words into array aRR.
aRR = []
with open(r'C:\Users\Asus\Desktop\CSE474.txt','r') as c:
    for line in c:
        print (line)
with open(r'C:\Users\Asus\Desktop\CSE474.txt','r') as f:
    for line in f:
        for word in line.split():
           aRR.append(word) 


# In[46]:


#print (aRR)


# In[47]:


#Sensored word is replaced with same number of asterisks
censoredWord = ['binary','line','after']
for i in range (len(aRR)):
   for j in range (len(censoredWord)): 
      if (aRR[i].lower()==censoredWord[j]): 
        size = len(aRR[i])
        aRR[i]='*'
        for k in range (size-1):
          aRR[i]=aRR[i]+'*'

#print (aRR)


# In[48]:


#Array aRR printed as one whole string
sent_str = ""
for i in aRR:
    sent_str += str(i) + " "
sent_str = sent_str[:-1]
print(sent_str)


# In[ ]:




