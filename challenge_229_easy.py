# Write a program to calculate the Dottie number. 
# This is the number you get when you type any number
# into a scientific calculator and then repeatedly 
# press the cos button, with the calculator set to radians. 
# The number displayed updates, getting closer and closer to
# a certain number, and eventually stops changing.
# cos here is the trigonometric function cosine, 
# but you don't need to know any trigonometry, or 
# what cosine means, for this challenge. 
# Just do the same thing you would with a handheld 
# calculator: take cosine over and over again until you
# get the answer.

#==========================================================
# Resolution using 'for'

import math

def do_cos (value):
    x = math.cos(value)
    return x

value = 20

for x in range(0,100):
    value = do_cos(value)
print "Dottie Number = %d" % value

#==========================================================
print ""
#==========================================================
# Resolution using 'while'


value = 50
while (True) :
    aux = math.cos(value)
    if aux == value:
        break
    value = aux
print "Dottie number = %d" % value

#==========================================================
print ""
#==========================================================
# OPTIONAL CHALLENGE

# The Dottie number is what's known as the fixed point of 
# the function f(x) = cos(x). Find the fixed point of the 
# function f(x) = x - tan(x), with a starting value of 
# x = 2. Do you recognize this number?

x = 2
while (True) : 
    aux = x - math.tan(x)
    if aux == x:
        break
    x = aux
print "Pi = %f" % x


#==========================================================
print ""
#==========================================================
# Find a fixed point of f(x) = 1 + 1/x (you may need to 
# try more than one starting number). Do you recognize 
# this number?


x = 50.0
while (True) : 
    aux = 1 + 1/x
    if aux == x:
        break
    x = aux 
print "Phi = %f" % x


#==========================================================
print ""
#==========================================================
# What happens when you try to find the fixed point of 
# f(x)= 4x(1-x), known as the logistic map, with most 
# starting values between 0 and 1?

