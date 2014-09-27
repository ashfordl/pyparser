'''
Parses mathematical expressions
'''

OPERATORS = ["^", "*", "/", "+", "-"]

def find_closing_bracket(string, opening_index):
    '''
    Finds and returns the closing index of a bracket
    '''

    level = 1
    for index in range(opening_index+1, len(string)):
        if string[index] == '(':
            level += 1
        elif string[index] == ")":
            level -= 1
            if level == 0:
                return index

    # If loop finishes before bracket is found, raise an exception
    raise ValueError("No closing bracket for index " + opening_index)

def add_term(exp, term):
    '''
    Adds the given term to the given expression
    '''

    if term != '':
        exp.append(term)

def char_decimal_point(expression, i, term):
    '''
    Parses a '.' when converting an expression to a list
    '''

    try:
        if expression[i+1].isdigit():
            if term == '':
                term += '0'
            term += '.'
    except IndexError: # In case x+1 exceeds the string length
        pass

    return term

def char_open_bracket(expression, i, term, exp):
    '''
    Parses a '(' when converting an expression to a list
    '''

    add_term(exp, term)

    # Find the index of the corresponding closing bracket
    close = find_closing_bracket(expression, i)

    # Find the expression contained within the brackets
    substring = expression[i+1 : close]

    # Parse this sub-expression and append it as a list to the array
    exp.append(convert_to_list(substring))

    # Return the original expression with bracketed expression removed
    return expression[0:i] + expression[close + 1:]

def convert_to_list(expression):
    '''
    Converts the given expression to a collection of terms
    '''

    exp = []
    current_term = ""

    # While loop needed as the condition needs to be evaluated each iteration
    # This is because the expression is modified within the loop
    i = 0
    while i < len(expression):
        char = expression[i]

        # If the character is a digit
        if char.isdigit():
            current_term += char

        # If the character is a decimal point
        elif char == '.' and '.' not in current_term:
            current_term = char_decimal_point(expression, i, current_term)

        # If the character is a minus sign, and the current term is not a number
        elif char == '-' and current_term == '':
            current_term += '-'

        # If the character is an operator
        elif char in OPERATORS:
            add_term(exp, current_term)

            current_term = ''
            exp.append(char)

        # If the character is a bracket
        elif char == '(':
            expression = char_open_bracket(expression, i, current_term, exp)
            current_term = ''

            # Don't increment the iterator, as brackets were replaced
            continue

        # The character isn't recognised
        else:
            raise ValueError("Alien character present at index " + str(i))

        # Increment the iterator
        i += 1

    # Add the last term found
    add_term(exp, current_term)

    return exp

def parse(expression):
    '''
    Parses the given expression and prints the result
    '''

    print(convert_to_list(expression))
