# written for CS 6320 S19 - Homework 2
# Written by Vishal Chandar Ramachandran
# Email : VXR180002@utdallas.edu

# To execute script: python homework1.py corpus.txt "sentence one here." "sentence two goes here"
# input: corpus.txt - this file contains the input corpus for training
# output: 8 tables, 4 probabilities

import sys
token=[]
tokens1=[]
tokens2=[]

corpus= sys.argv[1]
S1=sys.argv[2]
S2=sys.argv[3]
sys.stdout.write("\nSentence 1 : "+S1)
sys.stdout.write("\nSentence 2 : "+S2)
sys.stdout.write("\n\nScenario 1 = without smoothing")
sys.stdout.write("\nScenario 2 = with add-one smoothing\n\n")

S1=S1.replace('.','')
S1=S1.replace(',','')
S2=S2.replace('.','')
S2=S2.replace(',','')
with open(corpus,'r') as f:
    for line in f:
        for word in line.split():
            if(word==',' or word=='.'):
                continue
            else:
                token.append(word.lower())
for i in range(0,len(token)-1):
    if(token[i+1]=="'s"):
        token[i]=token[i]+"'s"
x=[]
for word in token:
    if(word!="'s"):
        x.append(word)
token=x
x=[]
for word in S1.split():
    tokens1.append(word.lower())
s1=tokens1
for word in set(tokens1):
    x.append(word)
tokens1=x
x=[]
for word in S2.split():
    tokens2.append(word.lower())
s2=tokens2
for word in set(tokens2):
    x.append(word)
tokens2=x

print("##########    QUESTION A - Bigram counts    ##########")
print("\nTable 1 - SCENARIO 1 SENTENCE 1 BI-GRAM TABLE")
print("__________________________________________________\n")
###############SCENARIO 1 BI-GRAM TABLE SENTENCE 1###############
n1=[]
sys.stdout.write('\t')
for word in tokens1:
    sys.stdout.write(word)
    sys.stdout.write('\t')
print()
for k in range(0,len(tokens1)):
    sys.stdout.write(tokens1[k])
    sys.stdout.write('\t')
    for j in range(0,len(tokens1)):
        l=0
        for i in range(0,len(token)):
            if(token[i]==tokens1[k] and token[i+1]==tokens1[j]):
                l=l+1
        n1.append(l)
        m=str(l)
        sys.stdout.write(m)
        sys.stdout.write('\t')
    print()
cou1=[]
for i in set(n1):
    cou1.append([i,n1.count(i)])
print('\n\n\n')
print("Table 2 - SCENARIO 1 SENTENCE 2 BI-GRAM TABLE")
print("__________________________________________________\n")
###############SCENARIO 1 BI-GRAM TABLE SENTENCE 2###############
n2=[]
sys.stdout.write('\t')
for word in tokens2:
    sys.stdout.write(word)
    sys.stdout.write('\t')
print()
for k in range(0,len(tokens2)):
    sys.stdout.write(tokens2[k])
    sys.stdout.write('\t')
    for j in range(0,len(tokens2)):
        l=0
        for i in range(0,len(token)):
            if(token[i]==tokens2[k] and token[i+1]==tokens2[j]):
                l=l+1
        n2.append(l)
        m=str(l)
        sys.stdout.write(m)
        sys.stdout.write('\t')
    print()
cou2=[]
for i in set(n2):
    cou2.append([i,n2.count(i)])
print('\n\n\n')
print("Table 3 - SCENARIO 2 SENTENCE 1 BI-GRAM TABLE")
print("__________________________________________________\n")
###############SCENARIO 2 BI-GRAM TABLE SENTENCE 1###############
sys.stdout.write('\t')
for word in tokens1:
    sys.stdout.write(word)
    sys.stdout.write('\t')
print()
for k in range(0,len(tokens1)):
    sys.stdout.write(tokens1[k])
    sys.stdout.write('\t')
    for j in range(0,len(tokens1)):
        l=1
        for i in range(0,len(token)):
            if(token[i]==tokens1[k] and token[i+1]==tokens1[j]):
                l=l+1
        m=str(l)
        sys.stdout.write(m)
        sys.stdout.write('\t')
    print()
print('\n\n\n')
print("Table 4 - SCENARIO 2 SENTENCE 2 BI-GRAM TABLE")
print("__________________________________________________\n")
###############SCENARIO 2 BI-GRAM TABLE SENTENCE 2###############
sys.stdout.write('\t')
for word in tokens2:
    sys.stdout.write(word)
    sys.stdout.write('\t')
print()
for k in range(0,len(tokens2)):
    sys.stdout.write(tokens2[k])
    sys.stdout.write('\t')
    for j in range(0,len(tokens2)):
        l=1
        for i in range(0,len(token)):
            if(token[i]==tokens2[k] and token[i+1]==tokens2[j]):
                l=l+1
        m=str(l)
        sys.stdout.write(m)
        sys.stdout.write('\t')
    print()
print('\n\n\n')

print("##########    QUESTION B - Bigram Probabilities    ##########")
print("\nTable 5 - SCENARIO 1 SENTENCE 1 PROBABILITY TABLE")
print("__________________________________________________\n")
###############SCENARIO 1 PROBABILITY TABLE SENTENCE 1###############
prob11=[]
sys.stdout.write('\t')
for word in tokens1:
    sys.stdout.write(word)
    sys.stdout.write('\t')
print()
for k in range(0,len(tokens1)):
    sys.stdout.write(tokens1[k])
    c=0
    for word in token:
        if(word==tokens1[k]):
            c=c+1
    sys.stdout.write('\t')
    for j in range(0,len(tokens1)):
        l=0
        for i in range(0,len(token)):
            if(token[i]==tokens1[k] and token[i+1]==tokens1[j]):
                l=l+1
        l=l/c
        prob11.append([tokens1[k],tokens1[j],l])
        m=str(round(l,4))
        sys.stdout.write(m)
        sys.stdout.write('\t')
    print()
print('\n\n\n')
print("Table 6 - SCENARIO 1 SENTENCE 2 PROBABILITY TABLE")
print("__________________________________________________\n")
###############SCENARIO 1 PROBABILITY TABLE SENTENCE 2###############

prob12=[]
sys.stdout.write('\t')
for word in tokens2:
    sys.stdout.write(word)
    sys.stdout.write('\t')
print()
for k in range(0,len(tokens2)):
    sys.stdout.write(tokens2[k])
    c=0
    for word in token:
        if(word==tokens2[k]):
            c=c+1
    sys.stdout.write('\t')
    for j in range(0,len(tokens2)):
        l=0
        for i in range(0,len(token)):
            if(token[i]==tokens2[k] and token[i+1]==tokens2[j]):
                l=l+1
        l=l/c
        prob12.append([tokens2[k],tokens2[j],l])
        m=str(round(l,4))
        sys.stdout.write(m)
        sys.stdout.write('\t')
    print()
print('\n\n\n')
print("Table 7 - SCENARIO 2 SENTENCE 1 PROBABILITY TABLE")
print("__________________________________________________\n")
###############SCENARIO 2 PROBABILITY TABLE SENTENCE 1###############
prob21=[]
sys.stdout.write('\t')
for word in tokens1:
    sys.stdout.write(word)
    sys.stdout.write('\t')
print()
for k in range(0,len(tokens1)):
    sys.stdout.write(tokens1[k])
    c=len(set(token))
    for word in token:
        if(word==tokens1[k]):
            c=c+1
    sys.stdout.write('\t')
    for j in range(0,len(tokens1)):
        l=1
        for i in range(0,len(token)):
            if(token[i]==tokens1[k] and token[i+1]==tokens1[j]):
                l=l+1
        l=l/c
        prob21.append([tokens1[k],tokens1[j],l])
        m=str(round(l,4))
        sys.stdout.write(m)
        sys.stdout.write('\t')
    print()
print('\n\n\n')
print("Table 8 - SCENARIO 2 SENTENCE 2 PROBABILITY TABLE")
print("__________________________________________________\n")
###############SCENARIO 2 PROBABILITY TABLE SENTENCE 2###############

prob22=[]
sys.stdout.write('\t')
for word in tokens2:
    sys.stdout.write(word)
    sys.stdout.write('\t')
print()
for k in range(0,len(tokens2)):
    sys.stdout.write(tokens2[k])
    c=len(set(token))
    for word in token:
        if(word==tokens2[k]):
            c=c+1
    sys.stdout.write('\t')
    for j in range(0,len(tokens2)):
        l=1
        for i in range(0,len(token)):
            if(token[i]==tokens2[k] and token[i+1]==tokens2[j]):
                l=l+1
        l=l/c
        prob22.append([tokens2[k],tokens2[j],l])
        m=str(round(l,4))
        sys.stdout.write(m)
        sys.stdout.write('\t')
    print()
print("\n\n\n")



print("##########   QUESTION C  ##########")
print("\n4 probabilities are : \n")
print("SCENARIO 1 PROBABILITY\n")
p=1
for i in range(0,len(s1)-1):
    for word in prob11:
        if(s1[i]==word[0] and s1[i+1]==word[1]):
            p=p*word[2]
print("1. Sentence 1 = "+str(p))

p=1
for i in range(0,len(s2)-1):
    for word in prob12:
        if(s2[i]==word[0] and s2[i+1]==word[1]):
            p=p*word[2]
print("2. Sentence 2  = "+str(p))
p=1
print("\n")
print("SCENARIO 2 PROBABILITY\n")
for i in range(0,len(s1)-1):
    for word in prob21:
        if(s1[i]==word[0] and s1[i+1]==word[1]):
            p=p*word[2]
print("3. Sentence 1 = "+str(p))
p=1
for i in range(0,len(s2)-1):
    for word in prob22:
        if(s2[i]==word[0] and s2[i+1]==word[1]):
            p=p*word[2]
print("4. Sentence 2 = "+str(p))
p=1
print("\n\n<-------------------------End of Script output-------------------------->")