from stackA import *
from random import randint
from time import time

def game():
    stack = Stack()
    blocks = []
    score = 0
    for i in range(20):
        blocks.append(randint(0, 2))
    print(stack)
    # print(blocks)
    while len(blocks) > 0 and stack.length() <= 5:
        next = blocks.pop()
        print('------------\nTetris (press \'q\' to quit)\n------------')
        print()
        print(stack)
        print('Next -> ', next)
        start = time()
        choice = input('(y)es/(n)o: ')
        end = time()
        if choice == 'q':
            break
        elif (end - start) > 5 or choice == 'y':
            if (end - start) > 5:
                print('You took too long!')
            if next == stack.top():
                score += 1
                stack.pop()
            else:
                stack.push(next)
    else:
        print('---------\nGame Over\nScore:', score, '\n---------')

if __name__ == '__main__':
    game()
