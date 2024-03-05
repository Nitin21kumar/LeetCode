# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 19:54:36 2024

@author: Ankit Sharma
"""

#Minimum length of string after deleting similar ends

s ="aabccabba"

i = 0
j= len(s)-1



while(i < j and s[i]==s[j]):
    ch = s[i]
    while(i<j and s[i] == ch):
        i+=1
    while( i<=j and s[j]==ch):
        j-=1
print(j-i+1)
        
    