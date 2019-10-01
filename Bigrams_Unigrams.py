#!/usr/bin/env python
# coding: utf-8

# In[76]:


import re
import sys

# In[77]:

inpFile = sys.argv[1]

rawData = open(inpFile).read()


# rawData[0:500]


# In[78]:


parsedData = rawData.split('\n')


# In[79]:



str = ''.join(rawData)
# str


# In[82]:



regex = "_[^\s]+"
newList = re.sub(regex,  '',    str)
#str.replace(re.findall(regex,str),'a')


# In[83]:


# newList
newList = newList.lower()
# newList


# In[84]:


parsedData = newList.split('\n')


# In[85]:


# parsedData


# In[86]:


unigrams ={}
f = open("Unigrams.txt", "a")



# In[87]:



wordcount = 0
for sentence in parsedData:
    words = sentence.split()
    for word in words:
        wordcount += 1
        if word in unigrams:
            unigrams[word] += 1
        else:
            unigrams[word] = 1
#f.write("Total Word count : {}\n\n".format(wordcount))

f.write("Unigrams\n\n")
for k, v in unigrams.items():
    f.write(k+" : {}\n".format(v))
    #f.write("%s : %s" % (k, v))
f.write("\n\n")
f.close()


# In[88]:




bigrams = dict()
# print(type(bigrams))
bicount = dict()


# In[92]:




for sentence in parsedData:
    words = re.split("\s",sentence)
    for i in range (0, len(words) - 1):
        nstr = words[i] + " " + words[i + 1]
        if nstr in bicount:
            bicount[nstr] += 1
        else:
            bicount[nstr] = 1

        

#BIGRAM FILE
#CORRECT ONE
#a = (1,5)
#print(type(a))
f = open("Bigrams.txt", "a")
f.write("Bigrams\n\n")

nstr = ()
bicount = {}
for sentence in parsedData:
    words = sentence.strip().split()
    for i in range (0, len(words) - 1):
        nstr = (words[i], words[i + 1])
        #print(nstr)
        #print(type(nstr))
        if nstr in bicount:
            bicount[nstr] += 1
        else:
            bicount[nstr] = 1

#biprob = dict()
for k,v in bicount.items():
    f.write(' '.join(k) + " : {}\n".format(v))
    # print(' '.join(k) + " : {}\n".format(v))
f.write("\n\n")
f.close()
#


# In[94]:


# bicount


# In[95]:


# for k,v in bicount.items():
#     print(v, unigrams[k[0]], v/unigrams[k[0]])


# In[96]:


f = open("No smoothing","a")
f.write("No smoothing\n\n\n")
f.write("Probabilities\n\n")
for k,v in bicount.items():
    prob = float(v) / float(unigrams[k[0]])
    f.write(' '.join(k) + " : {}\n".format(prob))
    # print(prob)
    #print(k.split()[0])
    #biprob = v/unigrams[k.split([0])]



# In[97]:


# inp = "The standard Turbo engine is hard to work"
# inp = inp.lower()
# inparr = inp.split()

# p0 = float(unigrams[inparr[0]])/float(len(unigrams))
# f.write("\n\nIndividual Probabilities\n\n")
# f.write("{}\n".format(p0))
# for i in range (0, (len(inparr) - 1)):
#     nstr = (inparr[i],inparr[i + 1])
#     #print(i, nstr)
#     if nstr in bicount:
#         abc = float(bicount[(inparr[i],inparr[i + 1])])/float(unigrams[inparr[i + 1]])
#         f.write("{}\n".format(abc))
#         p0 *= (float(bicount[(inparr[i],inparr[i + 1])])/float(unigrams[inparr[i + 1]]))
#     else:
#         f.write('0\n')
#         p0 *= 0
# f.write("\n\nOverall Probability:")
# #f.write(p0)
# f.write("{}".format(p0))
# f.close()


# In[98]:





biprob = dict()


# In[101]:



# for key in bicount:
#     #biprob[key] = bicount[key]/count[counts[key[0]]]
#     print(type(key))


# In[ ]:




f = open("add_one_smoothing.txt","a")
f.write("Add one smoothing\n\n\n")


f.write("\n\n")

f.write("Probabilities\n\n")
for k,v in bicount.items():
    #print(k, v, unigrams[k[0]])
    prob = float(v + 1) /float((unigrams[k[0]] + len(unigrams)))
    f.write(' '.join(k) + " : {}\n".format(prob))
 
    #print(k.split()[0])
    #biprob = v/unigrams[k.split([0])]


# In[105]:


# inp = "The standard Turbo engine is hard to work"
# inp = inp.lower()
# inparr = inp.split()

# p0 = float(unigrams[inparr[0]] + 1) / float(len(unigrams)) 
# f.write("\n\nIndividual Probabilities\n\n")
# f.write("{}\n".format(p0))
# # print(p0)
# for i in range (0, (len(inparr) - 1)):
#     nstr = (inparr[i],inparr[i + 1])
#     # print(i, nstr)
#     if nstr in bicount:
#         abc = float(bicount[(inparr[i],inparr[i + 1])] + 1)/float(unigrams[inparr[i + 1]] + len(unigrams))
#         #abc = float(unigrams[inparr[i + 1]] + len(unigrams))
#         # print("{}\n".format(abc))
#         f.write("{}\n".format(abc))
#         p0 *= (float(bicount[(inparr[i],inparr[i + 1])] + 1)/float(unigrams[inparr[i + 1]] + len(unigrams)))
#     else:
#         #print(inparr[i+1])
#         #print(unigrams[inparr[i + 1]])
#         abc = float(1) / float(unigrams[inparr[i + 1]] + len(unigrams))
#         # print(abc)
#         f.write("{}\n".format(abc))
#         #f.write('0\n')
#         p0 *= abc
# f.write("\n\nOverall Probability:")
# #f.write(p0)
# f.write("{}".format(p0))
# f.close()


# In[106]:


# print("Add one smoothing Probabilities\n\n")
for k,v in bicount.items():
    #print(v)
    prob = (v + 1) / (unigrams[k[0]] + len(unigrams))
    uni = (unigrams[k[0]] + len(unigrams))
    # print(v+1,uni,prob)
   # print(' '.join(k) + " : {}\n".format(prob))
f.close()   


freq_counts = {}
total_bigrams = len(bicount.items())

for k,v in bicount.items():
    if(v not in freq_counts):
        freq_counts.setdefault(v, [])
        freq_counts[v].append(k)
    else:
        freq_counts[v].append(k)
        
nc = {}

for k,v in freq_counts.items():
    nc[k] = len(v)
cstarr = float(nc[1])/float(total_bigrams)
nc [0] = cstarr

def good_turing(bigram):
    c1 = float(nc[1])/float(total_bigrams)
    
    if bigram not in bicount.keys():
        return float(c1)
    else:
        c = bicount[bigram]
    den= 0
    num = 0
    
    if((c+1) not in nc.keys()):
        num = 0
    else:
        num = nc[c+1]
    den = nc[c]
    
    
    c2 = float((c+1)*num)/float(den)
    return float(c2)/float(total_bigrams)

    

f = open("Good_turing.txt","a")
f.write("Good_turing\n\n\n")


f.write("\n\n")

f.write("Probabilities\n\n")

for k,v in bicount.items():
    prob = good_turing(k)
    f.write(' '.join(k) + " : {}\n".format(prob))
    
f.close()
# print("Good_turing done")


# In[ ]:





# inp = "the standard turbo engine is hard to work"
# inp = inp.lower()
# inparr = inp.split()

# p0 = float(unigrams[inparr[0]]) /float(len(unigrams)) 

# for i in range (0, (len(inparr) - 1)):
#     nstr = (inparr[i],inparr[i + 1])
#     # print(nstr)
#     abc = good_turing(nstr)
#     p0 *= abc
    # print(abc)
    
# print("\n\nOverall Probability:")

# print("{}".format(p0))


# In[207]:

    
# In[ ]:




