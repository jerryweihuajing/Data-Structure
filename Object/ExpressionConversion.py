# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 15:57:40 2019

@author: Wei Huajing
@company: Nanjing University
@e-mail: jerryweihuajing@126.com

@title：Module-Expression Conversion
"""

from o_stack import stack

#------------------------------------------------------------------------------
"""
Converts a string expression to a list

Args:
    which_expression: string to be converted
    
Returns:
    expression list
"""
def ExpressionStr2List(which_expression):
    
    #final expression
    list_expression=[]
    
    #stack which stores operands
    operand_stack=stack()
    
    #all operators
    operators='(+-*/)'
    
    for item in which_expression:
        
        #push operand
        if item not in operators:
            
            operand_stack.Push(item)
  
        #pop operand
        if item in operators:
            
            if not operand_stack.IsEmpty():
                
                #include many bit
                this_operand=''
                
                while not operand_stack.IsEmpty():
                    
                    this_operand+=operand_stack.Top()
                    operand_stack.Pop()
                
                #this operand to expression (reverse)
                list_expression.append(this_operand[::-1])  
                        
            list_expression.append(item)

    #include many bit
    this_operand=''
    
    #push the operators out of stack            
    while not operand_stack.IsEmpty():
        
        this_operand+=operand_stack.Top()
        
        operand_stack.Pop()
        
    list_expression.append(this_operand[::-1]) 
               
    return list_expression

#------------------------------------------------------------------------------
"""
Infix expressions are converted into suffix expressions

Args:
    which_expression: string to be converted
    
Returns:
    postfix expression
"""
def Infix2Postfix(which_expression):
    
    alphabet='QWERTYUIOPASDFGHJKLZXCVBNM'
    number='1234567890'
    
    #all operand
    operands=alphabet+alphabet.lower()+number
    
    #all operator
    operators='(+-*/)'

    #map of operator priority
    map_operator_priority={}
    
    map_operator_priority['(']=1
    map_operator_priority['+']=2
    map_operator_priority['-']=2
    map_operator_priority['*']=3
    map_operator_priority['/']=3
    
    #define new stack
    operand_stack=stack()
    
    #final expression
    new_expression=''
    
    list_expression=ExpressionStr2List(which_expression)

    for item in list_expression:

        #if operand add to expression directly   
        if item not in operators:
            
            new_expression+=item
            new_expression+=' '
            
        elif item=='(':
                
            operand_stack.Push(item)
            
        elif item==')':
                
            top_item=operand_stack.Top()
            operand_stack.Pop()
            
            #close symobl push out all operators
            while top_item!='(':
                
                #operator inside () adds to expression
                new_expression+=top_item
                new_expression+=' '
                
                top_item=operand_stack.Top()
                operand_stack.Pop()

        else:
            
            #make sure the priority of top is always the largest   
            while not operand_stack.IsEmpty()\
            and map_operator_priority[item]<=map_operator_priority[operand_stack.Top()]:
                        
                new_expression+=operand_stack.Top()
                new_expression+=' '
                
                operand_stack.Pop()
                
            operand_stack.Push(item)
   
    #push the operators out of stack
    while not operand_stack.IsEmpty():
        
         new_expression+=operand_stack.Top()
         new_expression+=' '
         
         operand_stack.Pop()
         
    return new_expression
                                   
exp='11*12+13*14'
#exp='a+b*c/(d-e*(f+g))'
      
new_exp=Infix2Postfix(exp)
