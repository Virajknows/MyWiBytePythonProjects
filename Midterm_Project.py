print(THE PROF'S WORD TRIAL  (sequel to Profs_Grumpy_Assistant))
print(You made it past the grumpy assistant... now the Prof)
print(himself will test you with his famous Word Trial.)
print(Guess the secret word one letter at a time before)
print(your 6 chances run out!)

print()

import random


word_bank = ["python", "grammar", "adjective", "scholar", "library", "professor"]


wins = 0


play_again = "yes"

print()
print("So... you actually got past my assistant. Impressive. Barely.")


while play_again == "yes":

    
    secret_word = random.choice(word_bank)

    
    progress = "_" * len(secret_word)

    
    guessed_letters = ""

    
    chances = 6

    print()
    print("Here is my secret word:", progress)
    print("You have", chances, "wrong guesses. Do NOT waste my time.")
    print()

    
    while chances > 0 and progress != secret_word:

    
        guess = input("Guess a letter: ").strip().lower()

        print()

      
        if len(guess) != 1 or not guess.isalpha():

            print("ONE letter. A LETTER. Is that so hard?")

        elif guess in guessed_letters:

            print("You already tried '" + guess.upper() + "'. Pay attention!")

        elif guess in secret_word:

            guessed_letters = guessed_letters + guess


            new_progress = ""
            position = 0
            while position < len(secret_word):
                if secret_word[position] in guessed_letters:
                    new_progress = new_progress + secret_word[position]
                else:
                    new_progress = new_progress + "_"
                position = position + 1
            progress = new_progress


            print("Hmph. '" + guess + "' appears", secret_word.count(guess), "time(s).")

        else:

            guessed_letters = guessed_letters + guess
            chances = chances - 1
            print("WRONG. That letter is nowhere in my word.")


            print("Prof's patience: [" + "#" * chances + "-" * (6 - chances) + "]")


        print("Word so far:  " + progress.replace("", " ").strip())
        print("Letters tried:", guessed_letters.upper())
        print("Chances left:", chances)
        print()

    # ---------------- END OF ROUND ----------------
    if progress == secret_word:
        wins = wins + 1

        print("Unbelievable... the word was indeed '" + secret_word.title() + "'.")
        print("Fine. You have earned five minutes of my office hours.")
    else:
        print("HA! Out of chances. The word was '" + secret_word + "'.")
        print("Come back when you own a dictionary.")

    print()
    print("Trials won so far:", wins)
    print()


    answer = input("Dare to face another word? (yes/no): ").strip().lower()
    if answer.startswith("y"):
        play_again = "yes"
    else:
        play_again = "no"


print()
if wins == 0:
    print("Zero wins. My assistant was right about you.")
elif wins == 1:
    print("One win. Beginner's luck, obviously.")
else:
    print("Multiple wins... perhaps you are not hopeless after all.")

print("Now leave. I have papers to grade.")
print()
