# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 19:29:19 2019

@author: Wei Huajing
@company: Nanjing University
@e-mail: jerryweihuajing@126.com

@title：Module-Expression Evaluation
"""

from o_stack import stack

import ExpressionConversion as EC

#------------------------------------------------------------------------------
"""
Arithmetic

Args:
    operand_a: former operand
    operand_b: latter operand
    operator: '+' '-' '*' '/'
    
Returns:
    evaluation result
"""
def Evaluation(operand_a,operand_b,operator):
    
    if operator=='+':
        
        return operand_a+operand_b
    
    if operator=='-':
        
        return operand_a-operand_b
    
    if operator=='*':
        
        return operand_a*operand_b
    
    if operator=='/':
        
        return operand_a/operand_b
    
#------------------------------------------------------------------------------
"""
Evaluate the suffix expression

Args:
    which_expression: string to be evaluated
    
Returns:
    evaluation result
"""
def PostfixEvaluation(which_expression):
    
    #convert to postfix expression
    postfix_expression=EC.Infix2Postfix(which_expression)
    
    #all operators
    operators='(+-*/)'
    
    list_expression=postfix_expression.strip(' ').split(' ')
    
    #stack stores operands
    operand_stack=stack()

    for item in list_expression:
        
        #push and store
        if item not in operators:
            
            operand_stack.Push(item)
            
        #pop and evaluate
        if item in operators:
            
            operand_b=float(operand_stack.Top())
            operand_stack.Pop()
            
            operand_a=float(operand_stack.Top())
            operand_stack.Pop()
            
            operand_stack.Push(Evaluation(operand_a,operand_b,item))
            
    return operand_stack.Top()

exp='12*(12+12)*12'

result=PostfixEvaluation(exp)