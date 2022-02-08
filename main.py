from dataclasses import replace
import stages
import os
import time

clear = lambda: os.system('cls')

def main():
    submittedWord = input("Enter the word you are looking for: ")
    word = []
    searchedWord = []
    attemptedLetters = []
    count = 0
    stage = 0

    # Leave
    if submittedWord == 'exit':
        exit()

    for l in submittedWord:
        if l == ' ':
            word.append('-')
        else:
            word.append(l)

        if l == ' ':
            searchedWord.append('-')
        else:
            searchedWord.append('_')

    # Game
    startTime = time.time()
    while True:
        usedLetters = ' '.join(attemptedLetters)
        print(usedLetters.replace(' ', '|'))
        letter = input("Please enter a letter: ")

        while True:
            if len(letter) > 1:
                print(f"You may only enter one letter! But you typed {len(letter)}.")
                letter = input("Please enter a new letter: ")
            else:
                break

        while True:
            if letter in attemptedLetters:
                print(f"You have already tried the letter [{letter}]!")
                letter = input("Please enter a new letter: ")

            if letter not in attemptedLetters:
                break
                
        if letter in word:
            while True:
                if letter in word:
                    position = word.index(letter)
                    attemptedLetters.append(letter)
                    searchedWord[position] = letter
                    word[position] = '|'
                else:
                    break
        else:
            stage += 1
            stages.Hangman(stage)
            print(f"The letter [{letter}] was wrong!")
            attemptedLetters.append(letter)
        
        print(' '.join(searchedWord))
        count += 1

        if '_' not in searchedWord:
            break

        if count == 3:
            input('Please press enter to clear the field!')
        else:
            print()
            print()
    
    clear()
    print("You win the game!")
    print()
    print("Your stage:")
    stages.Hangman(stage)
    print()
    print(f"The searched word was: {' '.join(searchedWord)}!")
    print(f"You needed {round(time.time() - startTime, 3)}s.")

if __name__ == '__main__':
    main()