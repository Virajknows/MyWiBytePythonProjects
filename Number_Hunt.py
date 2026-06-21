import random
import time



print("=" * 50)
print("   WELCOME TO NUMBER HUNT SUPER EDITION")
print("=" * 50)
print()


close_reactions = ["So close!", "Ooh, almost!", "You're heating up!"]
far_reactions = ["Way off!", "Not even close!", "Brrr, cold!"]


n = random.randint(1, 100)
print("ROUND 1: I have selected a number between 1 and 100.")
print("Can you guess it?\n")

attempts = 0
done = False  

while not done:
    guess = int(input("Guess the number: "))
    attempts = attempts + 1

    
    distance = abs(guess - n)

    if guess > n:
        print("My number is smaller than that.", random.choice(
            close_reactions if distance <= 5 else far_reactions))

    if guess < n:
        print("My number is larger than that.", random.choice(
            close_reactions if distance <= 5 else far_reactions))

    if guess == n:
        print("\nBINGO! That is correct!")
        print("You took", attempts, "attempt(s) to guess it.")

        # Fun scoring: fewer attempts = a fancier rank
        if attempts <= 3:
            print("Rank: LEGENDARY GUESSER")
        elif attempts <= 6:
            print("Rank: Sharp Shooter")
        else:
            print("Rank: Persistent Detective")

        done = True

print()
print()


done = False
print("ROUND 2: Now it's your turn to pick!")
print("Think of a number between 1 and 100.")
input("Press Enter when you're ready... ")
print()
print("Okay, here I go, taking my best shot step by step...")
time.sleep(0.5)

guess = 0
attempts = 0
guess_step = 10
prev_answer = "l"

while not done:
    answer = input(
        "Is it " + str(guess) +
        "? (y = Yes, s = smaller than that, l = larger than that): "
    )
    attempts = attempts + 1

    if attempts > 1:
        if answer != prev_answer:
            guess_step = guess_step - 1

    prev_answer = answer

    if answer.lower() == "s":
        guess = guess - guess_step
        print("Adjusting... trying a smaller number.")

    if answer.lower() == "l":
        guess = guess + guess_step
        print("Adjusting... trying a bigger number.")

    if answer.lower() == "y":
        print("\nBingo! I got it!")
        print("I took", attempts, "attempt(s) to guess it.")
        if attempts <= 5:
            print("Not bad, huh?")
        else:
            print("Okay that took a while... I think I can do better.")
        done = True

print()
print()


print("I think I can do this smarter...")
print("Let me try BINARY SEARCH this time. Watch me go!")
print()
print("Think of a NEW number between 1 and 100 (you can pick the same one if you like).")
input("Press Enter when you're ready... ")
print()

done = False
low = 0
high = 100
attempts = 0


history = []

while not done:
    guess = round((low + high) / 2)
    print(f"(Search range is currently {low} to {high})")
    answer = input(
        "Is it " + str(guess) +
        "? (y = Yes, s = smaller than that, l = larger than that): "
    )
    attempts = attempts + 1
    history.append(guess)

    if answer.lower() == "s":
        high = guess

    if answer.lower() == "l":
        low = guess

    if answer.lower() == "y":
        print("\nBingo! Got it!")
        print("I took", attempts, "attempt(s) to guess it.")
        print("My guesses were:", history)
        print()
        
        print("Fun fact: with numbers 1-100, binary search NEVER")
        print("needs more than 7 guesses. That's the power of always")
        print("cutting the possibilities in half!")
        done = True

print()
print("=" * 50)
print("Thanks for playing NUMBER HUNT SUPER EDITION!")
print("=" * 50)
