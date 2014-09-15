operators = ["^", "*", "/", "+", "-"]

def convertToList(expression):
    exp = []
    
    i = -1
    currentType = ""
    currentTerm = ""
    while i+1 < len(expression):
        i += 1
        char = expression[i]
        
        if char.isdigit() and currentType in ["", "integer", "float"]:
            currentTerm += char
            currentType = currentType if currentType != "" else "integer"
            
        elif char == "." and currentType == "integer":
            currentType = "float"
            currentTerm += char
            try:
                if not expression[i+1].isdigit():
                    raise Exception("Decimal point at index %s is not followed by decimal.", i)
            except IndexError: # In case x+1 exceeds the string length
                raise Exception("Decimal point at index %s is not followed by decimal.", i)
            
        elif char in operators:
            exp.append(currentTerm)
            currentTerm = ""
            currentType = ""
            exp.append(char) 
                 
    exp.append(currentTerm)
    
    return exp
            
def parse(expression):
    print(convertToList(expression))