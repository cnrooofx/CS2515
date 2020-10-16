from stackA import *
from random import randint

def game():
    stack = Stack()
    blocks = []
    for i in range(20):
        blocks.append(randint(0, 2))
    print(stack)
    # print(blocks)
    while len(blocks) > 0:
        next = blocks.pop()
        print('Tetris (press \'q\' to quit)')
        print()
        print(stack)
        print('Next -> ', next)
        choice = input('(y)es/(n)o: ')
        if choice == 'y':
            stack.push(next)
        elif choice == 'q':
            break

if __name__ == '__main__':
    game()
