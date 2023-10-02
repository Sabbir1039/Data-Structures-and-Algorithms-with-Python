from collections import deque

class PostFixEvaluation:
    def __init__(self) -> None:
        self.stack = deque()
        self.operators = set(['+', '-', '*', '/', '^'])
    
    def perform_operation(self, op1, op2, char):
        return (int(op1) + char + int(op2))
        
    def evaluate_postfix_exp(self, expression):
        for char in expression:
            if char.isdigit():
                self.stack.append(char)
            elif char in self.operators:
                op2 = self.stack.pop()
                op1 = self.stack.pop()
                res = self.perform_operation(op1, op2, char)
                self.stack.append(res)

if __name__ == "__main__":
    expression = "2 3 * 5 4 * + 9 -"