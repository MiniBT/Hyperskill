from random import choice
choices = ["python", "java", "kotlin", "javascript"]
answer = choice(choices)
hint = ["-"] * len(answer)
word_length = len(answer)
lives = 8
guess_list = []
print("H A N G M A N")
game = input(' Type "play" to play the game, "exit to quit: ')

while game == "play":
    while lives > 0:
        if hint == answer:
            break
        print()
        print("".join(hint))
        guess = input("Input a letter: ")    
        if len(guess) != 1:
            print("You should print a single letter")
        if not (guess.isascii() and guess.islower()):
            print("It is not an ASCII lowercase letter")
        if guess in guess_list:
            print("You already typed this letter")
        guess_list.append(guess)        
        if guess in answer:
            if guess not in hint:
                for i in range(word_length):
                    if answer[i] == guess:
                        hint[i] = guess
            else:
                print("You already typed this letter")
        else:
            print("No such letter in the word")
            lives -= 1
    else:
        print("You are hanged")
        game = input(' Type "play" to play the game, "exit to quit: ')
        
    print(answer)
    print("You guessed the word!")
    print("You survived!")
    game = input(' Type "play" to play the game, "exit to quit: ')