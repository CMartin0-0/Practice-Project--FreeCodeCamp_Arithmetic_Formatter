import re
import pdb

def arithmetic_arranger(problems, show_answers=False):
    
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    
    try:
        if len(problems) > 5:
            raise BaseException
    except:
        return "Error: Too many problems."
    
    for problem in problems:
        operator = re.search('\\s[+-]\\s', problem)
        if operator is None: 
            return "Error: Operator must be '+' or '-'."
        operator = operator.group().strip()
   
        print(operator)
   
    

arithmetic_arranger(["351 + 21"])

        
        
    
    
    
