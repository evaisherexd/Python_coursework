# -*- coding: utf-8 -*-

"""
Homework 6

Due on Dec 30 at 6 pm

Please carefully read this homework instructions and the requirements of each question

Instructions for this assignment:
(1) If a question prohibits you from using the built-in sorting algorithm of the Python language (such as the sorted function, the sort method of the list),
Please choose a sorting algorithm that you think is more efficient and write it into your homework code (you can directly copy the sorting algorithm code in the course code)
(2) If you are prohibited from using the built-in search algorithm of Python language (such as if x in alist) in a question, please write a search algorithm by yourself
(3) Since text files are not like Word documents, numbers can be subscripted and subscripted. When you describe the time complexity of the algorithm in your homework, please write as follows

O(1): Constant
O(N): Linear
O(N^2): Quadratic
O(log_2 N): logarithmic
O(Nlog_2 N): Linear logarithmic
O(2^N): Exponential

Where "_" means subscript, "^" means superscript

(4) The algorithm time complexity required to be estimated in this assignment is the worst-case time complexity
"""

print("=================================Question 1==================================")    # do not alter

"""
1. Find duplicate numbers in the list

It is known that some numbers in list a are repeated once, but I don't know which numbers are repeated. Please design the algorithm that you think has the lowest time complexity, and then write a program to find the repeated numbers in the list a and print them out.

After completing the program, please use # or triple quotation marks to analyze the time complexity of your algorithm: You should write the asymptotic relationship between the time complexity of your algorithm and the length of the list N, and briefly explain the reason.

note:
1. This question prohibits the use of Python's built-in sorting algorithm (such as the sorted function, the sort method of the list)
2. You can use Python's built-in search algorithm for this question, but when analyzing the time complexity of your algorithm, you need to know the time complexity of the search algorithm you use.


(15 points)

"""
a=[31,56,235,967,718,3655,21,56,1121,939,501,98,100,8,23,21,12,10,899,9992]

#Please complete your algorithm below

def merge(left, right):    #Merge two lists
    merged = []
    i, j = 0, 0         #i and j are used as the subscripts of left and right respectively
    left_len, right_len = len(left), len(right)  #Get the length of the left and right sublists separately
    while i < left_len and j < right_len:      #Loop to merge left and right sublist elements
        if left[i] <= right[j]:
            merged.append(left[i])        #Merge left sublist elements
            i += 1
        else:
            merged.append(right[j])       #Merge right sublist elements
            j += 1
    merged.extend(left[i:])                #Merge the remaining elements in the left sublist
    merged.extend(right[j:])               #Merge the remaining elements in the right sublist
    return merged                       #Return to the merged list
def mergeSort(a):            #Merge sort
    if len(a) <= 1:           #Empty or only 1 element, return the list directly
        return a
    mid = len(a) // 2         #Middle of the list
    left = mergeSort(a[:mid])  #Merge sort left sublist
    right = mergeSort(a[mid:]) #Merge sort right sublist
    return merge(left, right)   #Merge the left and right sublists in sorted order

rept=[]
i=0
a1=mergeSort(a)
while i < len(a1)-1:
    if a1[i]==a1[i+1]:
        rept.append(a1[i])
    i+=1
print(rept)

#The time complexity of the algorithm is O(Nlog_2 N), the time complexity of the union sorting is O(Nlog_2 N), and the time complexity of the search program is O(n)
#Adding toghther to get the time complexity as O(Nlog_2 N)

print("=================================Question 2==================================")    # do not alter


"""
3. Divisible 01 knapsack problem

Given a backpack, the maximum weight it can bear is Maxweight=150, list weight
Represents the weight of each item, and the list value represents the value of each item.

Please write a program to stuff items into the backpack to maximize the value of the backpack as long as the backpack is not overweight.
Your algorithm should meet the following requirements

(1) Backpacks cannot be overweight
(2) There is only one piece of each item, and it can be divided.
In other words, item A can be stuffed into a backpack, or 0.5 pieces, or not into the backpack, but it is impossible to stuff more than one

Every time you stuff an item into your backpack, please use the print function to output the following information
a) The value of the item
b) The weight of the stuffed item
c) The current total weight of the backpack
d) The total value of items in the current backpack
When the backpack is full, use the print function to output the total value of the items in the backpack

After completing the program, please analyze the time complexity of your algorithm in the form of # sign or triple quotes and comments: you should write
The asymptotic relationship between the time complexity of your algorithm and the type of item N, and briefly explain the reason.

note:
1. This question prohibits the use of Python's built-in sorting algorithm (such as the sorted function, the sort method of the list)
2. This question prohibits the use of Python's built-in search algorithm (for example, using the in keyword to determine whether the element is in the list, min function, max function)

Tip: Greedy algorithm can be used for this question.
The core idea of greedy algorithm is: When solving the problem, each step always makes the best choice currently.

(20 points)

"""

Maxweight=150    # the maximum weight the backpack can withstand
weight = [35,30,60,50,40,10,25]
value = [10,40,30,50,35,40,30]

#Please complete your algorithm below

i=1
avg=[]   #A list of the value-to-quality ratio of each item
weightsum=0
valuesum=0
while i < len(weight)+1:  #Count with i, traverse all objects of weight
    avg.append(round(value[i-1]/weight[i-1],1))   #Add the unit value of each item to the avg list
    i+=1
print(avg)
def maxnum(list1):  #Define a function maxnum to find the maximum parameter in the list
    maxn=list1[0]  #initial value
    maxind=0
    j=0
    while j<len(list1):
        if list1[j]>maxn:   #Find the maximum value maxn and the maximum value parameter maxind by searching in order
            maxn=list1[j]
            maxind=j
        j+=1
    return(maxind)
k=0
while weightsum<150 and k<=len(weight):  #Introduce the number of loops to count k, when all the items are put into the backpack and the weight is less than 150, the loop stops
    k+=1
    j=maxnum(avg)  #j is the maximum parameter in the avg list
    print(avg)
    print(j)
    if weightsum+weight[j]<=150:   #When the current weightsum plus the current weight of j is less than or equal to 150,
        weightsum+=weight[j]       #Add the weight of j to weightsum
        valuesum+=value[j]         #Add value of j to valuesum
        print("The value of this item is:",value[j])
        print("The weight of the item is:",weight[j])
        print("The total weight is:",weightsum)
        print("The total value is:",valuesum)
    else:
        valuesum+=((150-weightsum)/weight[j])*value[j]
        print("The value of this item is:",((150-weightsum)/weight[j])*value[j])
        print("The weight of the item is:",150-weightsum)
        print("The total weight is:",150)
        print("The total value is:",valuesum)
        weightsum=150
    avg[j]=0    #At the end of each loop, change the current maximum value to 0 so that the next loop can find the second largest value

#The time complexity is O(N^2). The time complexity is determined by the loop of while weightsum<150. In the worst case, the time complexity is n, that is, put every item in it
# The time complexity of embedded a maxnum(avg) is n
#The total time complexity is multiplication of two n


print("=================================Question 3==================================")    # do not alter

"""
3.Please use code to implement a class that represents complex numbers

Define a class called complex_number to describe the complex number a+bi (in order to avoid conflicts with Python's built-in complex type, the form of a+bi is used instead of a+bj). This class should include the following instance methods (functions) and properties

1) Constructor, used to initialize the real and imaginary parts of complex numbers
2) The real and imag attributes are used to obtain the real and imaginary parts of complex numbers, respectively
3) Overloaded str() function, which returns a string output in the form of a+bi
4) Overloaded "+" operator, used to calculate the sum of two complex numbers a+bi and c+di, or the sum of a complex number (a+bi) and a real number
5) Overloaded "-" operator, used to calculate the difference between two complex numbers a+bi and c+di, or the difference between a complex number (a+bi) and a real number
6) The conjugate method, which returns the conjugate complex number of the complex number
7) Overloaded abs() function, used to calculate the modulus of the complex number
8) Overloaded "*" operator, used to calculate the product of two complex numbers a+bi and c+di, or the product of a complex number (a+bi) and a real number
9) Overloaded "/" operator, used to calculate the quotient of two complex numbers a+bi and c+di, or the quotient of a complex number (a+bi) and a real number

The output demonstration effect of the test code for this question is shown in the homework description document. Your code output effect should be similar to the demonstration effect

(30 points)


"""

#Please complete the code of your definition class below

class complex_number:
    def __init__(self,a,b):
        self.real=a
        self.imag=b
    def __str__(self):
        if self.imag>0:
            return str(self.real)+"+"+str(self.imag)+"i"
        else:
            return str(self.real)+str(self.imag)+"i"
    def __add__(self,other):
        return complex_number(self.real+other.real,self.imag+other.imag)
    def __sub__(self,other):
       return complex_number(self.real-other.real,self.imag-other.imag)
    def conjugate(self):
        return complex_number(self.real,-self.imag)
    def __abs__(self):
        return (self.real**2+self.imag**2)**0.5
    def __mul__(self,other):
        return complex_number(self.real*other.real-self.imag*other.imag,self.imag*other.real+\
                              self.real*other.imag)
    def __truediv__(self, other):
        return complex_number((self.real*other.real+self.imag*other.imag)/\
                              (other.imag**2+other.real**2),\
                              (self.imag*other.real-self.real*other.imag)/\
                              (other.imag**2+other.real**2))


#The following is the test code, do not alter
c1=complex_number(1,2)
c2=complex_number(3,-4)
print("c1 =",c1)
print("c2 =",c2)
print("c1.real=",c1.real)
print("c1.imag=",c1.imag)
print("abs(c1)=",abs(c1))
print("c1+c2 =",c1+c2)
print("c1+25=",c1+25)
print("c1-c2=",c1-c2)
print("c1-12=",c1-12)
print("c1.conjugate()=",c1.conjugate())
print("c1*c2=",c1*c2)
print("c1*5=",c1*5)
print("c1/c2=",c1/c2)
print("c1/5=",c1/5)


print("=================================Question 4==================================")    # do not alter

"""
4.Class inheritance

The code of the class account is given below to describe the bank account. The class account has two instance attributes: accnum (account) and balance (account balance).

Class account has several instance methods at the same time
GetBalance: used to output account balance
__str__: used for print objects
deposit: Used to deposit the amount (the deposit amount cannot be a negative number), and output the account balance after depositing the amount

Please write two classes SavingsAccount and CreditCard, which represent savings account and credit card account respectively, both of which inherit from the base class account.

Please decide by yourself the instance attributes and instance methods that need to be added in the two derived classes SavingsAccount and CreditCard.
The derived class you define should have at least the following functions:

Derived class SavingsAccount
(1) Add an instance method withdraw to spend a certain amount of money. Since the savings account cannot be overdrawn (that is, the amount cannot be a negative number),
if the amount spent is greater than the account balance, the transaction is cancelled and the current account balance is notified.


Derived class CreditCard
(1) Add the instance attribute overdraftlimit, which is used to describe the credit card overdraft limit
(2) Add an instance method withdraw to spend a certain amount of money. If the amount spent exceeds the account balance + overdraft limit, the transaction will be cancelled and the current account available limit will be notified
(3) When using the print function to print objects of the derived CreditCard, in addition to outputting the account number and account balance, it also outputs the current available limit (that is, the sum of the account balance and the overdraft limit)

The output demonstration effect of the test code for this question is shown in the homework description document. The output effect of your code should be similar to the demonstration effect

(25 points)


"""

class account:
    def __init__(self,accnum,balance=0.0):
        self.accnum=accnum  #account number
        self.balance=balance  #Initial account balance

    def GetBalance(self):
        print("The account balance is: ", self.balance, " Yuan")
        return self.balance

    def __str__(self):
       return "Account: "+str(self.accnum)+" Balance: "+str(self.balance)+"Yuan"

    def deposit(self,dep):
        if dep>0:
           self.balance+=dep
           print("Deposit ",dep," Yuan")
           self.GetBalance()
        else:
           print("The deposit amount cannot be negative")


#Please complete your code to define the derived class below

class SavingsAccount(account):
    def __init__(self,accnum,balance):
        account.__init__(self,accnum,balance)
    def withdraw(self,wit):
        if wit<self.balance:
            self.balance-=wit
            print("Expenditure",wit,"Yuan")
            self.GetBalance()
        else:
            print("Account cannot be overdrawn")
            self.GetBalance()

class CreditCard(account):
    def __init__(self,accnum,overdraftlimit,balance=0.0):
        account.__init__(self,accnum,balance)
        self.overdraftlimit=overdraftlimit
    def __str__(self):
       return "Account: "+str(self.accnum)+" Balance: "+str(self.balance)+"Yuan" +"Available:"+str(self.overdraftlimit+self.balance)
    def withdraw(self,wit):
        if wit<self.balance+self.overdraftlimit:
            self.balance-=wit
            print("Expenditure",wit,"Yuan")
            self.GetBalance()
        else:
            print("Exceed the overdraft limit"+",Current available:"+str(self.overdraftlimit+self.balance)+"Yuan")




#The following is the test code, do not alter
print("**************Savings Account test code****************")
acc1=SavingsAccount(20191001,10000) #account 20191001, initial 10000元
print(acc1)
acc1.deposit(1000)
acc1.withdraw(5000)
acc1.withdraw(8000)

print("**************CreditCard test code****************")
acc2=CreditCard(20192001,20000) #account 20191001,initial 0 yuan, overdraft limit 20000yuan
print(acc2)
acc2.withdraw(2000)
acc2.withdraw(30000)
acc2.deposit(3000)
