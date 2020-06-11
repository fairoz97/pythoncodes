print("Hello lets play Hangman")

turns = 9
secret_word = "PYTHON"
guesses = ""

while (turns > 0):
    blanks =0
    for letters in secret_word:
        if letters in guesses:
            print(letters, end = ' ')
        else:
            print ('_', end = ' ' )
            blanks +=1
    if blanks ==0:
        print("\nYou got it! End of game")
        break

    guess = input("\nEnter the letter: ").upper()

    #print(guesses)

    if guess not in secret_word:
        turns -=1
        print("Wrong letter!\n")
        print("You have " + str(turns) + " turns left\n")

        if guess in guesses:
            print("You have guessed this letter before\n")

    guesses += guess

    if turns ==0:
        print("You lose, the word was " + secret_word )

