# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 15:22:43 2019

@author: Wei Huajing
@company: Nanjing University
@e-mail: jerryweihuajing@126.com

@title：Module-Base Converter
"""

from o_stack import stack

#------------------------------------------------------------------------------
"""
Converts a decimal number to any base

Args:
    which_num: num to be converted
    base: new base
    
Returns:
    number with new base
"""
def BaseConverter(which_num,base):
    
    s=stack()
    
    #16 base
    digits='0123456789ABCDEF'
    
    while which_num!=0:
        
        s.Push(which_num%base)
        
        which_num//=base
        
    #construct new str
    new_num=''
    
    for k in range(len(s.items)):
        
        new_num+=digits[s.items.pop()]
        
    return new_num

a=BaseConverter(112,2)
b=BaseConverter(23,17)