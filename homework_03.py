"""
Homework 3
Due on Monday, October 28 at 6pm
"""

import random     #Import random module, do not modify this
import math       #Import math module, do not modify this



print("=================================Question 1==================================")    # do not alter

"""
 1. Write a program to find the number of common divisors of two numbers a and b
  Requirements: Use enumeration or other algorithms to implement. The algorithm represented by your code should have a certain universality, which means that it is not only applicable to these two numbers,
  It also applies to any other positive integers (10 points)



"""
#Two positive integers a and b are given below, do not alter
a=9240
b=56858

# Please complete the code below to find the number of common divisors of a and b, and finally save this number in the variable ng.
list1=[]
list2=[]
list3=[]

#When a is divisible by i, i is a divisor of a. Add the divisor i of each a to the set of list1
for i in range(1,a+1):
   if a%i==0:
     list1.append(i)
print(list1)

#When b is divisible by k, k is a divisor of b. Add the divisor k of each b to the set of list2
for k in range(1,b+1):
    if b%k==0:
       list2.append(k)
print(list2)

#The intersection of list1 and list2 is list3, which is also the set of common divisors of a and b
list3=[var for var in list1 if var in list2]

#Use len() to find the number of elements in list3, that is, the common divisor of a and b
ng=len(list3)


print("The number of common divisors of a and b are ",ng)      #Output the number of all common divisors, do not alter


print("=================================Question 2==================================")    # do not alter

"""
2. The Taylor series expansion form of the cosine function cos(x) is

cos(x) = 1 - x**2/2!  + x**4/4! - x**6/6! + ...

Write a program, use the Taylor series expansion formula to calculate the cosine value of any angle between 0 and 360 degrees,
The absolute value of the last item of the series is required to be less than 1e-6. (10 points)

"""
theta=random.uniform(0,360)      # Generate a random angle theta between 0-360 degrees, do not alter
print("theta = ", theta, " degree ")   #Output value of theta, do not alter

#Please complete the code below, use Taylor series expansion to calculate the value of cos(theta)
#Calculation results are saved to the variable cos_theta

cos_theta=1
t=1
n=1
rad=math.radians(theta) #Convert degree to radians
while abs(rad**(2*n)/t)>=1e-6: #confirm accuracy
    t = math.factorial(2*n) #Calculate the factorial
    cos_theta+=((-1)**n)*rad**(2*n)/t
    n+=1

print("cos(theta)  =  ", cos_theta)      #output value of cos_theta, do not alter


print("=================================Question 3==================================")    # do not alter

"""
3. In order to calculate the average distance between any two points on a circle with a radius of 10, we will conduct 20 experiments

In each experiment, we will randomly hit 100 points on a circle with a radius of 10, and then calculate the shortest distance and the longest distance between the two points in the 100 points
And the average distance (that is, average the distance between all two points).

After 20 experiments are completed, we will base on the results of 20 experiments
Calculate the average of the shortest distance, longest distance and average distance between two points on the circle.

(20 points)

Attachment: Code that randomly generates 100 point coordinates on a circle with a radius of 10 will generate a list of 100 point coordinates
point_list=[]
r=10.0
for i in range(100):
    theta = random.uniform(0,2.0*math.pi)
	x = r*math.cos(theta)
    y =	r*math.sin(theta)
	point_list.append([x,y])

"""

#Please complete the code below to calculate the 100 randomly generated points on the circle,
#The mean value of the maximum distance, minimum distance and average distance between two points after 20 experiments
#The calculation results are saved in the three variables mean_max, mean_min, and mean_ave


ave_sum=0 #Record the sum of the average
max_sum=0 #Record the sum of the maximum
min_sum=0 #Record the sum of the minimum

for n in range(20): #20 experiments
    point_list=[]
    r=10.0
    for i in range(100):
        theta = random.uniform(0,2.0*math.pi)
        x = r*math.cos(theta)
        y =	r*math.sin(theta)
        point_list.append([x,y])

    print(point_list)

    dis_max=0 #The initial value is replaced the first time
    dis_min=100 #The initial value is replaced the first time
    dis_sum=0
    count=0
    for i in range(99):
        for j in range(i+1,100): #Two loops traverse each possibility without repeating
            distance=math.sqrt((point_list[i][0]-point_list[j][0])**2+ (point_list[i][1]-point_list[j][1])**2) #计算距离
            if distance < dis_min:
                dis_min=distance #replace
            if distance > dis_max:
                dis_max=distance #replace
            dis_sum+=distance  #The sum is used to calculate the average later
            count+=1
    ave_sum+=dis_sum/count #The sum of the averages is used to calculate the average of the averages later
    max_sum+=dis_max    #The sum is used to calculate the average later
    min_sum+=dis_min    #The sum is used to calculate the average later

mean_ave=ave_sum/20     #Find the average of 20 times
mean_max=max_sum/20
mean_min=min_sum/20



#The following outputs mean_max, mean_min, mean_ave results, do not alter
print("The mean maximum distance is： ",mean_max)
print("The mean minimum distance is： ",mean_min)
print("The mean average distance is： ",mean_ave)
