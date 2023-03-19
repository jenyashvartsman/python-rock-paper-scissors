import random

play_options = ['r', 'p', 's']
win_options = ['rs', 'pr', 'sp']

options_dict = {
    'r': 'Rock',
    'p': 'Papper',
    's': 'Scissor'
}

def game():
    user_wins = 0
    ai_wins = 0
    print('Lets play a game')
    
    while True:
        user_input = input('Enter ("end" = exit, "r" = Rock, p = "Papper", "s" = Scisors): ')
        ai_input = random.choice(['r', 'p', 's'])

        if user_input == 'end':
            print('Ending game')
            print(f'Final score: User {user_wins} - {ai_wins} AI')
            break
        elif user_input not in play_options:
            print('Invalid input')
        else:
            print(f'User: {options_dict[user_input]}, AI: {options_dict[ai_input]}')
            if (user_input == ai_input):
                print('Draw')
            elif f'{user_input}{ai_input}' in win_options:
                user_wins += 1
            else:
                ai_wins += 1
            print(f'Current score: User {user_wins} - {ai_wins} AI')

    
        print('------------------------------------------')


game()