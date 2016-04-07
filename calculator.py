"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *

def continue_play():    
 
    repeat = 1   
    while repeat > 0:
        user_input = raw_input(">>") 
        user_input = user_input.strip()
        tokens = user_input.split(" ")
        for item in tokens:
                if item == '':
                    tokens.remove('')
                else:
                    pass            
                    
        operator = tokens[0]

        if operator == '+':
            print add(tokens[1],tokens[2])
        elif operator == '-':
            print subtract(tokens[1],tokens[2])
        elif operator == '*':
            print multiply(tokens[1],tokens[2])
        elif operator == '/':
            print divide(tokens[1],tokens[2])
        elif operator == 'square':
            print square(tokens[1])
        elif operator == 'cube':
            print cube(tokens[1])
        elif operator == 'pow':
            print power(tokens[1],tokens[2])
        elif operator == 'mod':
            print mod(tokens[1], tokens[2])
        elif operator == 'q':
            print "goodbye"
            break
        else:
            print "error"

continue_play()