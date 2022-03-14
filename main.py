secret_place = 'Germany'
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = input('Guess:')
    guess_count += 1
    if guess == secret_place:
        print('You are correct')
        break
else:
    print('Sorry you were incorrect')
