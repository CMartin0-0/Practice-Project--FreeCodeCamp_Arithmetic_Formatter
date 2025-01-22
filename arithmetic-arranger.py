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
        
        spacing = len(x) + 2 if len(x) > len(y) else len(y) + 2
        
        #check to see if a problem has already been arranged
        if len(line1) > 0:
            #add in proper spacing between arranged problems
            line1 += 4 * " " 
            line2 += 4 * " "
            line3 += 4 * " "
        line1 += x.rjust(spacing, " ")
        line2 += operator + (spacing - 1 - len(y)) * " " + y
        line3 += spacing * "-"
        if show_answers == True:
            if len(line4) > 0:
                line4 += 4 * " "
            if operator == "+":
                solution = int(x) + int(y)
            else:
                solution = int(x) - int(y)
            line4 += str(solution).rjust(spacing, " ")
    #include solutions in return if show answers is true
    if show_answers == True:
        return line1 + "\n" + line2 + "\n" + line3 + "\n" + line4
    return line1 + "\n" + line2 + "\n" + line3
                
            
    
            
        
            
        
        

   
    
print(arithmetic_arranger(["351 + 21", "251 - 15", "444 + 4", "2 - 333"]))



        
        
    
    
    
