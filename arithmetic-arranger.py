import re
import pdb

def arithmetic_arranger(problems, show_answers=False):
    
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    
    #Check to see if there are too many problems    
    try:
        if len(problems) > 5:
            raise BaseException
    except:
        return "Error: Too many problems."
    
    #Separate and store each problem as separate parts and check exceptions
    for problem in problems:
        operator = re.search('[+-]', problem)
        
        try:
            if operator is None:
                raise BaseException
        except:     
            return "Error: Operator must be '+' or '-'."
        
        operator = operator.group().strip()
        operands = problem.split(operator)
        x = operands[0].strip()
        y = operands[1].strip()
        
        try:
            if not x.isdigit() or not y.isdigit():
                raise BaseException
        except:
            return "Error: Numbers must only contain digits." 
        try:
            if len(x) > 4 or len(y) > 4:
                raise BaseException
        except:
            return "Error: Numbers cannot be more than four digits."
        
        
        
        print(x,y)
   
    

arithmetic_arranger(["35144 + 21", "251 - 15"])

        
        
    
    
    
