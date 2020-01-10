"""
Homework 2

Due on 6 pm Wednesday, Oct 16
"""

import random     #import random module, do not alter



print("=================================Question 1==================================")    # do not alter

# 1. Fix following code error, make it work as in the comment(5 marks)
#
# generate an integer randomly in the range (0,100) and give it to AA
AA=random.randint(0,100)    #do not alter
#if AA>=50,output AA>=50 and value of AA
if AA>=50:
    print("AA>=50  AA = ",AA)
#otherwise,output AA<50 and value of AA
else:
    print("AA<50   AA = ", AA)




print("=================================Question 2==================================")    # do not alter



# 2. Fix following code error, make it work as in the comment(5 marks)

# let the variable be 760, and output its value using print function
aaa=760
print("The value of this variable is: ", aaa)
print("=================================Question 3==================================")    # do not alter


# 3. Please learn about complex number operations, arithmetic operators and built-in mathematical operation functions in Chapter 4, and complete the following operations
#    Note: It is forbidden to use functions in the math or cmath module in your code in this question (10 marks)

c1=6+8j

#Complete the expression and assign the value of the real part of c1 to the variable c1_r
c1_r=c1.real
print(c1_r)  #do not alter

#Complete the expression and assign the value of the imaginary part of c1 to the variable c1_i
c1_i=c1.imag
print(c1_i)  #do not alter

#Complete the expression and assign the conjugate complex number of c1 to the variable c1_cj
c1_cj=c1.conjugate()
print(c1_cj)  #do not alter

#Complete the expression and assign the value of the modulus of c1 to the variable c1_mod
c1_mod=abs(c1)
print(c1_mod)   #do not alter

r1=2.319965e-2
#Complete the expression, round r1 to 5 decimal places and assign it to r2
r2=round(r1,5)
print(r2)   #do not alter





print("=================================Question 4==================================")    # do not alter


# 4. According to the requirements of the comment, complete the following code to realize the conversion from rectangular coordinates to polar coordinates (10 points)
#
x = random.uniform(-10,10)    #Assign a value to the x coordinate so that it is equal to a randomly generated floating point number between -10-10
y = random.uniform(-10,10)    #Assign a value to the y coordinate so that it is equal to a randomly generated floating point number between -10-10

print("x = ", x)
print("y = ", y)

# There is no need to modify the above lines of code in this subtitle. Please write the program below to set the coordinates (x, y) in the rectangular coordinate system
# Convert to (rho, theta) in the polar coordinate system, where rho is the polar diameter and theta is the polar angle
# Please note that the final polar angle unit requires the angle system instead of the radian system, and the final result expressed in the radian system will be deducted
# Tip: You may need to use some functions in the math module, and the range of the polar angle in polar coordinates is 0-360 degrees

rho=(x**2+y**2)**(1/2)
import math
theta=math.degrees(math.atan2(y,x))
if theta<0:
    theta=theta+360

# When your program is completed, we will output the values of rho and theta, no need to modify the following
print("rho = ",rho)
print("theta = ", theta, " degree ")
