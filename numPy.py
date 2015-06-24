'''
Created on 23.06.2015

@author: niklas
'''
import numpy as np

text = open("/home/niklas/Projects/WebValley/BodyTemperature_nohead.txt")

myArray = np.genfromtxt(text)

text.close()

females = 0
males = 0

averageAge = 0

sexArray = myArray[:,0]

minAge = 1000
maxAge = 0

for i in range(sexArray.size):
    if sexArray[i] == 1:
        females += 1
        
    elif sexArray[i] == 0:
        males += 1
        
    currentAge = myArray[:,1][i]
    
    #Age++++++++++++++++++++++++++++++++++++++
    if currentAge > maxAge:
        maxAge = currentAge
    
    elif currentAge < minAge:
        minAge = currentAge
        
    averageAge += currentAge
        
print "Average age: ",
print averageAge / sexArray.size

print "Max age: ",
print maxAge

print "Min age: ",
print minAge

print "Number of females: ",
print females

print "Number of males: ",
print males
