import random
import string


def RandomName(hangman_games):
    
    return random.choice(hangman_games)

def HangmanChecker(hangman_name, user_query, correct_index):
    user_query = user_query.lower()
    count = 0
    counter = 0
        
    for letter in hangman_name:
        if user_query == letter:
            correct_index[counter] = (user_query)
        counter += 1
    if user_query not in hangman_name:
        Death()

    x = ''.join(correct_index[letter] + ' ' for letter in correct_index)
    print(x)
    return correct_index

def Death():
    global lives
    lives -= 1
    print(f'Lives remaining: {lives}')
    if lives == 0:
        print('You are a loser!')
        quit()
        
def ListInit(hangman_name):
    correct_index = {}     
    count = 0

    while count < len(hangman_name):
        
        correct_index[count] = '-'
        count += 1
    print(correct_index)
    return correct_index
#

hangman_name = ['rainbow', 'computer', 'science', 'programming',  
         'python', 'mathematics', 'player', 'condition',  
         'reverse', 'water', 'board', 'geeks']
random_name = RandomName(hangman_name)
lives = 6
correct_index = ListInit(random_name)
    
print('Welcome to Arman\'s hangman game!\n----------------')
#game loop
while True:
    
    user_input = input('Please enter a letter: ')
    while not(user_input.isalpha()):
        user_input = input('We dont accept numbers. Please enter a letter: ')

    output_list = HangmanChecker(random_name, user_input, correct_index)
    if any(output_list[x] == '-' for x in output_list):
        pass
    else:
        print('You won!')
        break
