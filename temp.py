# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

This script helps children with multiplication. It lists the numbers between 1 and 100, 
if the number is divisible by 3 it will instead say fizz, 
if divisible by 5 it will say buzz, if divisible by 3 and 5 it will say fizzbuzz

"""
for x in range (1,101):
    
        if x %3 == 0 and x %5 != 0:
            print ("fizz")
      
        elif x %5 ==0 and x %3 !=0:
            print ("buzz")
       
        elif x %3==0 and x %5 ==0:
           print ("fizzbuzz")  
    
        else: print (x) 
        
 
     

    
