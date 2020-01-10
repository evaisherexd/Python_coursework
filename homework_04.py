"""
Homework 4
Due on 6pm Nov 25

ID: 7815

"""




print("=================================Question 1==================================")    # do not alter

"""
1. Follow the prompts to complete the code in order to complete the list operation. The code is required to be as concise as possible, do not alter the existing code

 (10points)
"""

#(1)The initialization list t represents the electricity consumption of a household in a year and 12 months
t=[]    #do not alter

#Call the list method and add 271 electricity consumption in January to the list t

t.append(271)

print(t)  #do not alter

#(2)List tb contains the electricity consumption from 2 to 12 months, call the list method, expand the data of electricity consumption from 2 to 12 months to list t, and make the length of list t 12
tb=[151,78,92,83,134,357,421,210,88,92,135]   #do not alter

t.extend(tb)

print(t)    #do not alter

#(3)Find the month with the highest electricity consumption maxm

maxm=t.index(max(t)) +1

print(maxm)  #do not alter

#(4)Find the three months with the lowest electricity consumption m1, m2, m3
temp=[]
for i in t:
    temp.append(i)
temp.sort()
m1=t.index(temp[0])+1
m2=t.index(temp[1])+1
m3=t.index(temp[2])+1

print(m1,m2,m3)     #do not alter







print("=================================Question 2==================================")    # do not alter


"""
2. You will find two files in the folder, "name_score.txt" this file contains everyone's Chinese name and corresponding score;
 The "name_pinyin.txt" file contains each person's Chinese name and corresponding pinyin.

 Please write the program below, read these two files, and then generate a text file with a suffix of .txt. In the new text file, the first column is the pinyin corresponding to each person’s name, and the second column is the person’s score , And each person’s name and his corresponding grades are arranged from high to low.

 Note: The order of names in the two text files name_score.txt and name_pinyin.txt is different.

 Note:
 (1) If there is a newline character'\n' in the string, but the newline character'\n' in the string is not needed, you can use strip in the string method to remove the newline character, such as t=s.strip(' \n')
Remove the newline character in the string s and assign it to the string t
 (2) For sorting, refer to section 5.2.7 of the textbook
 (3) When doing this question, please put the text file to be read and your code file in the same file directory, otherwise it will cause trouble for us to mark (due to the file path)
 (4) This question is recommended to be solved by a dictionary (of course, it can be done without a dictionary)
 (20 points)
"""
f = open('name_score.txt')
p = open('name_pinyin.txt')
dicf={}
#dicfn=[]    #dicfn is a list of names in the name score table
#dicfs=[]    #dicfs is a list of scores in the name score table
for line in f.readlines():
    line=line.strip('\n') #Remove newline characters\n
    line=line.split(' ')
    print(line)
    dicf[line[0]]=int(line[1])
    #dicfn.append(line[:2])
    #dicfs.append(line[3:])
#print(dicfn)
#print(dicfs)
#c1=zip(dicfs,dicfn)
print(dicf)
#print(dict(c1))  #Create a dictionary c1 where the key is the score and the value is the name



#dicpn=[]    #dicpn is a list of names in the name pinyin table
#dicpp=[]    #
dicp={}
for lin in p.readlines():
    lin=lin.strip('\n') #Remove newline characters\n
    lin=lin.split(',')
    #dicpn.append(lin[:2])
    #dicpp.append(lin[3:])
#print(dicpn)
#print(dicpp)
#c2=zip(dicpn,dicpp)
#print(dict(c2))
    dicp[lin[1]]=lin[0]
print(dicp)

dictnew={}
for i in dicp:
    dictnew[i]=dicf[dicp[i]]
print(dictnew)

import operator
b=sorted(dictnew.items(),key=operator.itemgetter(1),reverse=True)
print(b)
for i in b:
    print(i[0]," ",i[1])

data = open("newfile.txt",'w',encoding="utf-8")
for i in b:
    print(i[0]," ",i[1],file=data)
data.close()

"""








print("=================================Question 3==================================")    # do not alter


"""
#3. Refer to the description of the third question in the homework instructions on the e-learning platform, and complete the code below

a1=open('transaction_record_A.txt')
a2=open('transaction_record_B.txt')
a3=open('transaction_record_C.txt')
b1=list(a1);b2=list(a2);b3=list(a3)

#Add the company of each element to the element, and merge the three companies into a list b11
b11=[];b21=[];b31=[]
for k in b1:
    k=k.strip('\n')
    k=k+",A"
    b11.append(k)
for k in b2:
    k=k.strip('\n')
    k=k+",B"
    b21.append(k)
for k in b3:
    k=k.strip('\n')
    k=k+",C"
    b31.append(k)
b11.extend(b21)
b11.extend(b31)
print(b11)

#Solve the millennium bug problem, output list b4
b4=[]
for i in b11:
    if i[0]=="9":
        i="19"+i
    else:
        i="20"+i
    b4.append(i)
print(b4)

#Change the notation of month and day to two digits, and output list b5
b5=[]
for j in b4:
    if j[6]=="-":
        c1=j[:5]
        c2=j[5:]
        c2="0"+c2
        j=c1+c2
    if j[9]==",":
        c3=j[:8]
        c4=j[8:]
        c4="0"+c4
        j=c3+c4
    b5.append(j)
print(b5)

#Sort by time, output list b6
b6=sorted(b5)
print(b6)

#Keep the amount after two decimal places and output list d1
d1=[]
for i in b6:
    j=i.split(",")
    print(j)
    j[1]=str(round(float(j[1]),2))
    i=",".join(j)
    print(i)
    d1.append(i)
print(d1)

#Calculate the total income and expenditure of each company
suma=0
sumb=0
sumc=0
for i in d1:
    if i[-1]=="A":
        suma+=float(i.split(",")[1])
    elif i[-1]=="B":
        sumb+=float(i.split(",")[1])
    else:
        sumc+=float(i.split(",")[1])

data = open("companyincome.txt",'w',encoding="utf-8")
for i in d1:
    print(i,file=data)
print("The total income of company A is",round(suma,2),"Yuan",file=data)
print("The total income of company B is",round(sumb,2),"Yuan",file=data)
print("The total income of company C is",round(sumc,2),"Yuan",file=data)
data.close()

#(30points)
"""


"""
