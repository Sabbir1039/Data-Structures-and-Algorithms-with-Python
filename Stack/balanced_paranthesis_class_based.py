from collections import deque

class PranthesisChecker:
    def __init__(self) -> None:
        self.stack = deque()
        self.paranthesis_map = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        
    def check_balanced_paranthesis(self, expression):
        for char in expression:
            if char in ["(", "{", "["]:
                self.stack.append(char)
            elif char in [")", "}", "]"]:
                if len(self.stack) == 0 or self.paranthesis_map[char] != self.stack[-1]:
                    return False
                else:
                    self.stack.pop()
        return True if not self.stack else False
    
    
if __name__ == "__main__":
    
    paranthesis_checker = PranthesisChecker()
    expression = "[ (a+b) * (a-b) ]"
    result = paranthesis_checker.check_balanced_paranthesis(expression)
    print(result)
    