import random

words = ['hello', 'man', 'parrot', 'sea', 'fish', 'human', 'golf']

word = random.choice(words) # randomly chooses a word from the list

print(word)

lives = 5
output = ''

print('Computer guessed word is : ', '_ '*len(word))

try:
    while len(word) > 0 and lives > 0:
        print()
        letters = input('Enter a letter at a time: ')
        lives -= 1

        if letters in word:
            k = word.count(letters)
            for _ in range(k):
                output += letters

        for char in word:
            if char in output and len(word) != len(output):
                print(char, end=' ')
            elif len(word) == len(output):
                print(f'You have guessed the word {word} correctly.')
                exit()
            else:
                print('_', end=' ')
        if lives <= 0 and len(word) != len(output):
            print()
            print('You lost! Try again...')
            print(f'The word is {word}')
except KeyboardInterrupt:
    print()
    print('Bye! Try again.')
    exit()
