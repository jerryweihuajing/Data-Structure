# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 23:02:05 2019

@author: Wei Huajing
@company: Nanjing University
@e-mail: jerryweihuajing@126.com

@title：Object-queue
"""

#==============================================================================  
#common data structure queue
#==============================================================================  
class queue:
    
    def __init__(self):
        
        self.items=[]
    
    #juege whether the queue is empty    
    def IsEmpty(self):
        
        return self.items==[]

    #push an element to rear of queue: O(n)
    def Enqueue(self,item):
        
        self.items.insert(0,item)
    
    #pop an element to front of queue: O(1) 
    def Dequeue(self):
        
        self.items.pop()
       
    #have a look at front element
    def Front(self):
        
        return self.items[-1]
    
    #have a look at rear element
    def Rear(self):
        
        return self.items[0]
    
    #return size of queue
    def Size(self):
        
        return len(self.items)
    