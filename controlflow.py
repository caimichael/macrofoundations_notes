# % Quick overview of Matlab control flow
# % For the course, "Macroeconomic Foundations for Asset Prices," NYU Stern.
# %
# % links
# % http://www.mathworks.com/help/matlab/ref/if.html
# % http://www.mathworks.com/help/matlab/ref/relationaloperators.html
# % http://www.mathworks.com/help/matlab/ref/for.html
# % http://www.mathworks.com/help/matlab/matlab_prog/anonymous-functions.html
# %
# % Written by:  Dave Backus, October 2014

import matplotlib.pyplot as plt
import numpy as np
import math

print(' ')
print('if statements')
print('--------------------------------------------------------------')

print(' ')
print('brute force abs value')
x = 4
if x <= 0:
    x = -x

print(x)


print(' ')
print('the else option')
x = 7
if x <= 0:
    x = -x
else:
    x = 2*x

print(x)



print(' ')
print('multiple conditions')

x = 11
if x >= 0 and x <= 10:        #  && = and, || = or
    x = 0;

print(x)




print(' ')
print('for loops')
print('--------------------------------------------------------------')

print(' ')
print('factorials')

maxit = 8
total = 1
for it in range(2,maxit+1,2):
    # had to make it maxit+1 because the second argument is not where it stops at
    total = total*it
    if total >= 10:
        break

print(total)




print(' ')
print('go through an arbitrary list')

list1 = [1, 8, 3, 99]
for x in list1:
    print(x)




print(' ')
print('find first negative number in list')

list2 = [1, 8, -3, 99]
for x in list2:
    print(x)
    if x <= 0:
        break



print(' ')
print('anonymous functions')
print('--------------------------------------------------------------')

print(' ')
print('x-squared')
f = @(x) x^2
f(7)
