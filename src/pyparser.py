OPERATORS = ["^", "*", "/", "+", "-"]

def find_closing_bracket(string, opening_index):
    level = 1
    for index in range(opening_index+1, len(string)):
        if string[index] == '(':
            level += 1
        elif string[index] == ")":
            level -= 1
            if level == 0:
                return index

def convert_to_list(expression):
    exp = []

    current_term = ""

    i = 0
    while i < len(expression):
        char = expression[i]

        # If the character is a digit
        if char.isdigit():
            current_term += char

        # If the character is a decimal point
        elif char == "." and "." not in current_term:
            try:
                if expression[i+1].isdigit():
                    if current_term == '':
                        current_term += '0'
                    current_term += '.'
            except IndexError: # In case x+1 exceeds the string length
                pass

        elif char in OPERATORS: # If the character is an operator
            if current_term != '':
                exp.append(current_term)
                
            current_term = ''
            exp.append(char)

        # If the character is a bracket
        elif char == "(":
            if current_term != '':
                exp.append(current_term)

            close = find_closing_bracket(expression, i)
            substring = expression[i+1 : close]

            exp.append(convert_to_list(substring))

            current_term = ""

            expression = expression[0:i] + expression[close + 1:]

            # Don't increment the iterator, as brackets were replaced
            continue

        # The character isn't recognised
        else:
            raise Exception("Alien character present at index " + str(i))

        # Increment the iterator
        i += 1
    # Add the last term found
    if current_term != "":
        exp.append(current_term)

    return exp

def parse(expression):
    print(convert_to_list(expression))
