import re

def transform_expression(expression):
    # This regex will find numbers, operators, or anything inside parentheses
    pattern = r'\d+|\+|\*|\([^()]*\)|\([^()]*\(.*?\)[^()]*\)'

    # Find all matches using the regex pattern
    matches = re.findall(pattern, expression)

    # Initialize an empty list to hold the transformed elements
    transformed_list = []

    i = 0
    while i < len(matches):
        match = matches[i]
        # If the match is a number or an operator, add it to the list
        if re.match(r'\d+|\+|\*', match):
            transformed_list.append(match)
        else:
            # Handle nested expressions
            if match.startswith('('):
                transformed_list.append(match)
        i += 1

    return transformed_list

# Example usage
expression = "1 + (2 * 3) + (4 * (5 + 6))"
result = transform_expression(expression)
print(result)
