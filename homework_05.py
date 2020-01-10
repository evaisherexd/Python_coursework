# -*- coding: utf-8 -*-
"""
 Homework 5
 Due on Dec 9 at 6pm


"""
#The following modules are imported for this task, do not alter
import numpy as np
import matplotlib.pyplot as plt
import math
import random
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

print("=================================Question 1==================================")    # do not alter

"""
1. Use recursive function to find the sum of interlaced harmonic series

It is known that the interlaced harmonic series is defined as

1 - 1/2 + 1/3 - 1/4 + 1/5 - 1/6 + 1/7 ...

It is known that the series is convergent

Write a function, use the recursive method to calculate the sum of the first n items of the interlaced harmonic series.

After writing the function, call the function to calculate the level one by one

Take the sum of the first item
Take the sum of the first 2 items
Take the sum of the first 3 items
...
Take the sum of the first 712 items

After each summation, the absolute value of the difference between the summation and the theoretical convergence value of the series should also be calculated as the error.

After the calculation, you will get two lists count and err, where
count=[1,2,3,...,712] represents the number of items in the series taken for each summation
err=[take the error of 1 term, take the error of 2 terms,...,take the error of 712 terms] represents the error between the calculated value of each summation and the theoretical value

Your task for this question ends here, and then the question provides a piece of code for plotting the variation of the error with the number of summations.
Do not alter the code for drawing! If your code is calculated correctly, a file named'harmonic_error.jpg' will be generated at the end
The graph depicts the variation of the error with the summation term

Note: 1. For the theoretical value of the interlaced harmonic series, please consult the advanced mathematics textbook or Google/Baidu
2. This question requires the matplotlib library to draw a picture. If you don’t have a laptop or desktop computer, it is recommended to borrow another classmate’s computer, because the Python on the online programming platform does not have the matplotlib library.

(10 points)

"""


def alter_series(n):
    if n==1:return 1.0
    elif n%2==0:return alter_series(n-1)-1.0/n      #When n is even
    else:return alter_series(n-1)+1.0/n             #When n is odd
sum=[]
err=[]
count=[]
for i in range(1,713):
    sum.append(alter_series(i))
    err.append(abs(alter_series(i)-math.log(2)))
    count.append(i)
print(sum)
print(err)


#The following code is used for drawing, do not alter!
plt.plot(count,err,color='r')
plt.xlabel('n')
plt.ylabel('Error')
#plt.show()
plt.savefig('harmonic_error.jpg')

print("=================================Question 2==================================")    # do not alter
"""
2. Complete the function f(s) in the following code. The function f(s) is used to determine whether the input from the keyboard is a number. See the job description document for the output effect
(10 points)
"""
def f(s):
     #Please complete the content of function f below
    try:
        float(s)
        return True
    except ValueError:
        pass

#The following is the code for the test function f(s) do not alter
ss=input("please enter:")
if f(ss):
    print("You entered a number")
else:
    print("You did not enter a number")


print("=================================Question 3==================================")    # do not alter
"""
3. Rotate the curve to get the surface

In this question, you need
1) Complete a function, the function will rotate any point (x, y, z) in the three-dimensional space around the x axis
by theta angle counterclockwise, and the function returns the new point (x', y', z') obtained after the rotation
2) Read a file called'curve_data.txt' in your folder, which records the coordinates of all points on a curve in
the three-dimensional space: The first, second, and third columns of the file correspond to the x,y,z values of each point.
After reading the file, call the function you wrote before to rotate the point, and rotate the curve counterclockwise
about the x-axis every 1 degree (angle system) for a total of 360 times, so that you get a surface . After each rotation,
the coordinates [x,y,z] of each point obtained after the rotation are added to the list of points,
In this way, after you have rotated 360 times, the points list contains the coordinates of all points on the surface.
The approximate form of the points list is as follows
points=[[1.0,2.0,3.0],[23.0,34.0,45.0],...,[99.0,23.0,97.9]]

Your task ends here for this question, and then the question provides a piece of code for drawing a curved surface.
Do not alter the code for drawing! If your code is calculated correctly, a 3D surface image with the file name
'surface_rotation.jpg' will be generated at the end.



(10 points)


"""
def rotation(x,y,z,theta):
    thet=math.radians(theta)
    cos1=math.cos(thet)
    sin1=math.sin(thet)
    return (x,y*cos1-z*sin1,y*sin1+z*cos1)


a1=open('curve_data.txt')
b1=list(a1)
points=[]
for k in range(1,361):
    for i in b1:
        spl=i.split()
        points.append(rotation(float(spl[0]),float(spl[1]),float(spl[2]),k))

#The following code is used for drawing, do not alter!
fig = plt.figure()
final_data=np.array(points)
xxx=final_data[:,0]
yyy=final_data[:,1]
zzz=final_data[:,2]
ax = fig.add_subplot(1, 1, 1, projection='3d')
#Generate 3D surface
surf = ax.plot_trisurf(xxx,yyy,zzz, cmap=cm.jet,linewidth=0)
#plt.show()
plt.savefig('surface_rotation.jpg')


print("=================================Question 4==================================")    # do not alter

"""
4. Guess the number

The number guessing game (Bulls and Cows) is a puzzle game with the following rules
1) The person who wrote the question gave a four-digit number.
Each digit of this four-digit number is a number between 0-9,
and no repeated digits can appear in the four digits
(for example, 1299 contains repeated numbers. Cannot be the answer to the question).
The respondent guessed the four-digit number.
2) Every time the answerer guesses, the answerer will give feedback based on the answerer’s guess.
The feedback is given in the form of mAnB: where A represents the number of numbers with the correct position,
and B represents the number of the numbers which value is correct but the position is not.
For example, 0A2B means that the respondent gave two correct value guesses, but the position is incorrect.
3) The answerer continues to guess according to the feedback from the questioner,
and then the answerer continues to give feedback until the answerer guesses the number or the game ends.

Write a program to realize the function of guessing the number game. Your code should define at least the following two functions

Function 1: Randomly generate a four-digit number between 1000-9999 without repeated numbers as the answer to the game
You may need to use one or more of the following functions in the random module.randint(a,b)
Randomly generate an integer n, a<=n<=b
random.choice(sequence) Get an element randomly from the sequence (string, list, etc.)
random.sample(sequence,k) randomly obtain a fragment of the specified length k from the sequence sequence
random.shuffle(x) Shuffle the elements in list x

Function 2: Used to compare the answer of the answerer with the answer of the game, and return feedback in the form of mAnB

Then write a program, call these two functions, and start the number guessing game. The game should have the following features
(1) When the answerer has guessed 5 times and cannot get the correct answer, exit the loop and print the correct answer of the game
(2) When the answerer guesses the answer, print "Congratulations!", and then exit the loop

For specific game input and output effects, please refer to the instructions in this homework
Detailed description.

(20 points)

"""


def ans_num():
    num_list=[0,1,2,3,4,5,6,7,8,9]
    final=[]                            #A four-digit list of answers
    final.append(random.randint(1,9))        #Generate thousands digit
    num_list.remove(final[0])          #Avoid duplication, remove thousands from the list
    final.append(random.choice(num_list))    #Generate hundreds digit
    num_list.remove(final[1])           #Avoid duplication, remove hundreds digit from the list
    final.append(random.choice(num_list))    #Generate tens digit
    num_list.remove(final[2])           #Avoid duplication, remove tens from the list
    final.append(random.choice(num_list))    #Generate unit digit
    return final

def guessing():
    n=list(input("Please enter your answer："))
    A=0
    B=0
    place1=1                         #Remember the number of digits being compared in the input value
    place2=1                         #Remember the number of digits compared in the answer value
    for i in n:
        for k in ans_list:
            if int(i)==k:
                if place1==place2:A+=1
                else:B+=1
            place2+=1
        place1+=1
        place2=1
    print (A,"A",B,"B")
    if A==4:
        return True
    return False

ans_list=ans_num()              #Randomly generate a four-digit number that meets the conditions and split it into the list ans_list
flag=False                    #The Boolean variable flag is used to determine whether the correct answer needs to be output after five cycles
for i in range(5):
    if guessing():
        print("Congradulations!")
        flag=True
        break
if not flag:               #If you fail to guess 5 times, flag=False will output the correct answer
    print("The correct answer is：",ans_list[0]*1000+ans_list[1]*100+ans_list[2]*10+ans_list[3])
