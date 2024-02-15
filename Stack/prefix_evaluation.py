from collections import deque

class prefixEvaluation:

    def __init__(self) -> None:
        self.stack = deque()
        self.operatiors = set(["+", "-", "*", "/", "^"])
        
    def perform_operation(self, op1, op2, operator):
        exp = f"{op1} {operator} {op2}"
        return eval(exp)
        
    def prefix_evaluation(self, expression):
        start = len(expression)-1   
        for i in range(start, -1, -1): # loop through expression in reverse
            if expression[i].isdigit():
                self.stack.append(expression[i])
            elif expression[i] in self.operatiors:
                op1 = self.stack.pop()
                op2 = self.stack.pop()
                result = self.perform_operation(op1, op2, expression[i])
                self.stack.append(result)
        return self.stack[-1]
        
if __name__ == "__main__":
    expression = "- + * 5 7 * 4 2 5"
    
    prefix = prefixEvaluation()
    result = prefix.prefix_evaluation(expression)
    print(result)