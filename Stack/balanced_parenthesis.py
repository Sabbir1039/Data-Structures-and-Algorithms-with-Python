# Check for balanced parenthesis

from collections import deque

def check_balanced_parenthesis(exp):
    stack = deque()
    mapping = {
        ')':'(',
        '}': '{',
        ']':'['
        }
    
    for char in exp:
        if char == ("(" or "{" or "["):
            stack.append(char)
        elif char == (")" or "}" or "]"):
            if len(stack) == 0 or mapping[char] != stack[-1]:
                return False
            else:
                stack.pop()
    return True if not stack else False

if __name__ == "__main__":
    exp = "[2 + (a * b) - (c]"
    if check_balanced_parenthesis(exp):
        print("Parenthesis are balanced!")
    else:
        print("Parenhesis are not balanced!")