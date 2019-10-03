# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 14:57:07 2019

@author: Wei Huajing
@company: Nanjing University
@e-mail: jerryweihuajing@126.com

@title：Module-Parenthesis Matching
"""

from o_stack import stack

#------------------------------------------------------------------------------
"""
Determines if the opening and closing parentheses in a string match

Args:
    which_str: symbol string
    
Returns:
    bool
"""
def ParenthesisChecker(which_str):
    
    #construct a new stack object
    s=stack()
    
    #bool representing whether the string is balanced
    balanced=True
    
    #list open and close
    str_open='([{'
    str_close=')]}'
    
    #transform str to list
    list_open=[this_str for this_str in str_open]
    list_close=[this_str for this_str in str_close]

    #construct map between open to close
    map_open_close=dict(zip(list_open,list_close))
    
    index=0
    
    while index<len(which_str):
        
        if which_str[index] in str_open:
            
            s.Push(which_str[index])
            balanced=False
            
        if which_str[index] in str_close:
        
            if s.IsEmpty():
                
                balanced=False
                
            #new element matches the top
            elif which_str[index]==map_open_close[s.Top()]:
   
                s.Pop()
                balanced=True
            
        index+=1
            
    if s.IsEmpty() and balanced:
        
        return True
    
    else:
        
        return False

a=ParenthesisChecker('(([{}]))')
b=ParenthesisChecker('(([{]))')    
c=ParenthesisChecker('(([{]}))')  
