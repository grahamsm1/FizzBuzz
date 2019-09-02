#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:12:46 2019

@author: stephaniegraham
"""

number=input ('Choose a number between 1 and 100:')
number=int(number)

if number %3 == 0 and number %5 !=0:
    print ("fizz")
      
elif number %5 ==0 and number %3 !=0:
       print("buzz")
       
elif number %3==0 and number %5 ==0:
        print ("fizzbuzz")       

else:
    print (number) 