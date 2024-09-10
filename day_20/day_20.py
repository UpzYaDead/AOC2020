
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


def evaluate_expression(list_expression) -> int:
    list_expression = [str(i) for i in list_expression]
    copy_list = list_expression[::]
    for (j, el) in enumerate(list_expression):
        if "(" not in el:
            continue
        # Change the elements in the list
        print(el[1:-1])
        # raise  ValueError("Not implemented")
        copy_list[j] = evaluate(el[1:-1])
    total = int(copy_list[0])
    print(f"\nINPUT: {copy_list}, length: {len(copy_list)}")
    
    if NEW_RULE and len(copy_list) > 3 and '+' in copy_list:
        print("NEW RULE enter")
        new_list = []
        for i in range(1, len(copy_list), 2):
            if copy_list[i] == '+':
                res = [str(int(copy_list[i-1]) + int(copy_list[i+1]))]
                print("To evaluate: ", new_list + res + copy_list[i+2:])
                return evaluate_expression(new_list + res + copy_list[i+2:])
            else:
                new_list.append(copy_list[i-1])
                new_list.append(copy_list[i])
        copy_list = new_list

                
    print(f"START CALCULATING:\n{copy_list}")

    for i in range(1, len(copy_list), 2):
        if copy_list[i] == '+':
            # print("Adding: ", total, " + ", int(copy_list[i+1]))
            total += int(copy_list[i+1])
        elif copy_list[i] == '*':
            # print("Multiplying: ", total, " * ", copy_list[i+1])
            total *= int(copy_list[i+1])
        else:
            raise ValueError("Unkown operator")
    return total
        
        

def evaluate(str_expression) -> int:
    print(f"\n\nWe get the expression: {str_expression}")
    list_expression = transform_expression(str_expression)
    print("The l_expression is: ", list_expression)
    return evaluate_expression(list_expression)


expression = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
NEW_RULE = True
print(evaluate(expression))


total = 0

for line in open("data.txt"):
    line = line.strip()
    total += evaluate(line)

print("The total is: ", total)