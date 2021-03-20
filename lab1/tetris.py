from stackA import Stack
from random import randint
from time import time


def game(no_of_stacks=3, no_of_games=1, max_length=6, turn_time=5):
    """Game of tetris

    Args:
        no_of_stacks: int -- How many rows to play (Default value: 3)
        no_of_games: int -- Number of rounds to play (Default value: 1)
        max_length: int -- Maximum height of blocks on the stack (Default value: 6)
        turn_time: int -- Time in seconds given to make each move (Default value: 5)
    """
    score = 0
    for game in range(no_of_games):
        # Number of blocks
        blocks = []
        for i in range(max_length):
            blocks.append(randint(0, 2))
        # Create stacks
        stack_list = []
        for i in range(no_of_stacks):
            stack_list.append(Stack())
        while len(blocks) > 0:
            # Check max length of stacks
            for check_stack in stack_list:
                if check_stack.length() > max_length:
                    break
            next = blocks.pop()
            print('------------\nTetris (press \'q\' to quit)\n------------')
            # Print stacks
            print()
            for index in range(no_of_stacks):
                print(index + 1, stack_list[index])
            print()
            print('Next -> ', next)
            print('Press \'p\' to pass or')

            # Get user input and time taken
            start = time()
            next_row = input('Select row: ')
            end = time()
            time_taken = end - start

            if next_row == 'q':
                break
            elif time_taken > turn_time:
                print('You took too long!')
                next_row = randint(0, no_of_stacks-1)
            elif next_row in str(range(1, no_of_stacks+1)):
                next_row = int(next_row)-1
            else:
                next_row = randint(0, no_of_stacks-1)

            if next == stack_list[next_row].top():
                score += 1
                stack_list[next_row].pop()
            else:
                stack_list[next_row].push(next)
    print('---------\nGame Over\nScore:', score, '\n---------')


if __name__ == '__main__':
    # no_of_games = 3
    # max_length = 5
    # turn_time = 5
    # game(no_of_stacks, no_of_games, max_length, turn_time)
    game()
