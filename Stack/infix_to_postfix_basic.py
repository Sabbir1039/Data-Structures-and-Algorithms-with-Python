def infix_to_postfix(expression):
    pass

if __name__ == "__main__":
    infix = "{ (A*B) + (C*D) } - e"
    postfix = infix_to_postfix(infix)
    print(postfix)