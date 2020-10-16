from stackA import *

def stackReverser(in_stack):
    if not isinstance(in_stack, Stack):
        return 'err'
    reverse_stack = Stack()
    while in_stack.length() > 0:
        reverse_stack.push(in_stack.pop())
    return reverse_stack

def bracketChecker(input_string):
    open_brackets = ['(', '[', '{']
    close_brackets = [')', ']', '}']
    stack = Stack()
    for char in input_string:
        if char in open_brackets:
            stack.push(char)
        elif char in close_brackets:
            if char == ')':
                if stack.top() != '(':
                    return False
                stack.pop()
            elif char == ']':
                if stack.top() != '[':
                    return False
                stack.pop()
            elif char == '}':
                if stack.top() != '{':
                    return False
                stack.pop()
    return True

def main():
    print('stackReverser\n')
    stack1 = Stack()
    alpha = ['a', 'b', 'c', 'd', 'e']
    alpha = [1, 2, 3]
    for i in range(len(alpha)):
        stack1.push(alpha[i])

    rev_stack = stackReverser(stack1)
    print(rev_stack)

    for i in range(stack1.length()):
        print(stack1.pop())

    for i in range(rev_stack.length()):
        print(rev_stack.pop())

    print(rev_stack)

    print('bracketChecker\n')
    test_string = '[he{}ll(ooo)oooooo(o)]'
    print(bracketChecker(test_string))

if __name__ == '__main__':
    main()
