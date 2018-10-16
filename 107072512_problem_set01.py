#-*- coding:utf-8 -*- 
#Author: Chen Ching-Chih
#hint range(start, stop, step)
#problem 1
print('Problem 1')
x = list(range(4,51,2))
print(x)

#problem 2
print('Problem 2')
import random

random.seed(1)
x=[random.uniform(0,1)for i in range(21)]
print(x)
#(a) Extract the odd-index elements of x.
#be careful about the relative poisition
a=x[0::2]
print('Extract the odd-index elements of',a)

#(b) Extract the odd-index elements of x.
b=x[1::2]
print('Extract the odd-index elements of x',b)

#(c) Add 5 to each elements.
#be familiar with the List comprehension.
c = [x[i]+5 for i in range(len(x))]
print('Add 5 to each elements',c)

#(d) Add 1 to just the odd-index elements.
d=[x[i]+1 for i in range(1,21,2)]
print('Add 1 to just the odd-index elements',d)

#(e)Compute the square root of each elements.
import math
e=[math.sqrt(i) for i in range(len(x))]
print('square root of each elements is',e)

#(f) Compute the square of each elements.
f=[x[i]**2 for i in range(len(x))]
print('Compute the square of each elements',f)


#problem 3

x=[4,2,5,8]
y=[2,1,4,5]
print('Problem 3')
#(a) Raise each element of x to the power specified by the corresponding element in y.
a=[]
end_index = len(x)
for i in range(end_index):
    a.append(x[i]**y[i])
print('Raise each element of x to the power specified by the corresponding element in y',a)


#(b) Divide each element of y by the corresponding elements in x .
print([y[i]/x[i] for i in range(4)])

#(c) Multiply each element of x by the correponding y.
c=[]
end_index = len(x)
for i in range(end_index):
    c.append(x[i]*y[i])
print('Multiply each element of x by the correponding y',c)

# Problem 4
print('Problem 4')
# Extract the elements greater than or equal to 3

import random

random.seed(1)
n = 20
m = 20
x = [random.randint(1,n) for i in range ( m )]
a=[]
for i in range(len(x)):
    if x[i]>3:
        a.append(x[i])
    i=i+1
print('Extract the elements greater than or equal to 3', a)

# Problem 5
print('Problem 5')
#(1) 的抽樣利用 #2 的 code, (2) 的再抽樣利用 #4 的 code
# Generate a uniformly distributed random sample between 0 and 1 of size 20. Call this sample x
import random
random.seed(1)
m=20
x = [random.uniform(0, 1) for i in range ( m )]
#print( x )
#(a) How many elements of x are greater than 0.5?
a=[]
for i in range(len(x)):
    if x[i]>0.5:
        a.append(x[i])
    i=i+1
print("There are",len(a), "elements of x greater than 0.5")

#(b) Extract the elements greater than 0.5
import random
random.seed(1)
n = 20
m = 20
x = [random.randint(1,n) for i in range ( m )]
b=[]
for i in range(len(x)):
    if x[i]>0.5:
        b.append(x[i])
    i=i+1
print("the elements greater than 0.5 :", b)
                

#Problem 6
print('Problem 6')
#(a) Create the list: ['alex', 'ben', 'chris', 'dan']
a=['alex', 'ben', 'chris', 'dan']
print('Create the list',a)

#(b) Extract the first letter of each word in the list and combine them to yield the string: 'abcd'.
b="".join(i[0] for i in a)
print('Extract the first letter :',b)

#Problem 7
#(a)
print('Problem 7 (a)')
L=[print('$'*i) for i in range(6)]

#(b)
print('Problem 7 (b)')
L="apple"
S=[print(L[:6-i]) for i in range(len(L))]

#Problem 9
print('Problem 9')
import math
x=2
tol=1e-8
dist=1
S_old=1
n=1
while dist>tol:
    f_x=(x**n)/math.factorial(n)
    S_new = S_old + f_x
    dist=math.fabs(S_new - S_old)
    S_old=S_new
    n+=1
print(S_new)

#Problem 8
print('Problem 8')
#Write a function that calculates n! for any positive integer n.
print('Calculate the factorize')
def my_factorize(n):
    x=1
    for i in range(1,n+1):
        x=x*i
    return x
f=my_factorize(int(input("Input a integer:")))
print('factorize of your integer is :',f)


