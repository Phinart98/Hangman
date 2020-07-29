# Write your code here
import random
print("H A N G M A N")
print()
# word library
words = ["python", "java", "kotlin", "javascript", "algorithm", "apache", "ajax", "bootstrap", "codeigniter",
         "coffeescript", "django", "flask", "framework", "git", "github", "swift", "jquery", "linux", "mongodb",
         "mysql", "php", "postgresql", "bit", "bug", "byte", "code", "command", "computer", "computing", "pycharm",
         "pytorch", "tensorflow", "machine", "data", "science", "function", "loop", "parameter", "programming",
         "program", "variable", "react", "angular", "matrix", "facebook", "microsoft", "apple", "amazon", "netflix",
         "google", "samsung", "dell", "sony", "ibm", "intel", "uber", "twitter", "snapchat", "tesla", "hyperloop"]

# select word and hide from player
correct_word = random.choice(words)
display = len(correct_word) * '-'
display_list = list(display)
lives = 8
entered_letters = set()  # will contain letters that user enters.

# continue asking user for these till word is guessed or lives are finished
while lives != 0:
    print()
    print("Guess the word below:")
    print("Note: All words entered are supposed to be lowercase.")
    print(display)
    print(f"You have {lives} lives left.")
    user_guess = input("Input a letter: ")

    # life reduction exception cases
    if user_guess in entered_letters:
        print("You already typed this letter")
        continue
    entered_letters.add(user_guess)

    if len(user_guess) != 1:
        print("You should input a single letter")
        continue

    if user_guess.islower() is False:
        print("It is not an ASCII lowercase letter")
        continue

    # comparing user guesses to letters in computer choice
    if user_guess in correct_word:
        count = correct_word.count(user_guess)

        # accounting for instances where the letter entered appears in the word multiple times instead of just once
        if count < 2:
            index = correct_word.find(user_guess)
            display_list[index] = user_guess
            display = ''.join(display_list)
            if display == correct_word:
                print(f"You guessed the word {correct_word}")
                print("You survived!")
                break
        else:
            indexes = []
            for i in range(len(correct_word)):
                if correct_word[i] == user_guess:
                    indexes.append(i)
            for index in indexes:
                display_list[index] = user_guess
                display = ''.join(display_list)
                if display == correct_word:
                    print(f"You guessed the word {correct_word}")
                    print("You survived!")
                    break

    else:
        print("No such letter in the word")
        lives -= 1

else:
    print(f"The correct word is: {correct_word}")
    print("You are hanged!")




