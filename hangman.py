# Write your code here
import random
print("H A N G M A N")
print()
words = ['python', 'java', 'kotlin', 'javascript']
correct_word = random.choice(words)
display = len(correct_word) * '-'
display_list = list(display)
lives = 8
entered_letters = []

while lives != 0:
    print()
    print(display)
    user_guess = input("Input a letter: ")
    if user_guess in entered_letters:
        print("You already typed this letter")
        continue
    entered_letters.append(user_guess)

    if len(user_guess) != 1:
        print("You should input a single letter")
        continue

    if user_guess.islower() is False:
        print("It is not an ASCII lowercase letter")
        continue

    if user_guess in correct_word:
        count = correct_word.count(user_guess)

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
    print("You are hanged!")




