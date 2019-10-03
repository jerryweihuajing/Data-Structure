# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 14:45:35 2019

@author: Wei Huajing
@company: Nanjing University
@e-mail: jerryweihuajing@126.com

@title：Object-stack
"""

#==============================================================================  
#common data structure stack
#==============================================================================  
class stack:
    
    def __init__(self):
        
        self.items=[]
    
    #juege whether the stack is empty    
    def IsEmpty(self):
        
        return self.items==[]

    #push an element to top of stack: O(1)
    def Push(self,item):
        
        self.items.append(item)
    
    #pop an element to top of stack: O(1) 
    def Pop(self):
        
        self.items.pop()
       
    #have a look at base element
    def Base(self):
        
        return self.items[0]
    
    #have a look at top element
    def Top(self):
        
        return self.items[-1]
    
    #return size of stack
    def Size(self):
        
        return len(self.items)
    