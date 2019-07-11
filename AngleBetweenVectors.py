#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import math

print("Welcome to Eric's program on finding the angle between two vectors.")
print('\n')
time.sleep(1.0)

def dot_product(vector1,vector2): #dot product
    
    #first vector
    
    i = vector1[0]
    
    j = vector1[1]

    k = vector1[2]
    
    #second vector
    
    i2 = vector2[0]

    j2 = vector2[1]

    k2 = vector2[2]

    return (i*i2) + (j*j2) + (k*k2)

def mag(vector1): #calculates the magnitude of the given vector
    #first vector
    
    i = vector1[0]
    
    j = vector1[1]

    k = vector1[2]
    
    return ((i)**2+(j)**2+(k)**2)**.5

def mag2(vector2): #calculates the magnitude of the given vector
    #second vector
    
    i = vector2[0]
    
    j = vector2[1]

    k = vector2[2]
    
    return ((i)**2+(j)**2+(k)**2)**.5
    
def NewCalc(): #Basically a restart function after first set of vectors have been entered
    
    new_calc = input('Recalulate? (Y or N): ').lower()
    
    if new_calc ==  'y':
        
        return 'y'
    else:
        return False
while True:    

    i_j_k_1 = input("Enter your 1st vector in the following format-> i,j,k: ")

    vector1 = tuple(map(int, i_j_k_1.split(','))) #gets rid of the commas between the vector 
                                              #and converts into a tuple

    i_j_k_2 = input("Enter your 2nd vector in the following format-> i,j,k: ")

    vector2 = tuple(map(int, i_j_k_2.split(',')))

    dp = dot_product(vector1,vector2)

    m1 = mag(vector1)

    m2 = mag2(vector2)

    x = dp/(m1*m2) #here we divide the dot product of both vectors by the product of their magnitudes 

    theta = math.acos(x) #we then take cosine inverse of the variable 'x', giving us the angle between the vectors

    angle = round(math.degrees(theta),2) #rounds to the nearest hundredth

    print('\n')

    time.sleep(1.0)

    print(f'The angle between the vectors is..{angle}')
    
    if not NewCalc():
        break
    




# In[ ]:




