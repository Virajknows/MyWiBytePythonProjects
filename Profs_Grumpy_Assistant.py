print()
print("Halt! You wish to see the Prof ???")
print()
print("Nobody gets past me without proving themselves first")
print()
print("Answer my questions, and maybe... just maybe... you'll get a slot")

print()

answer = input("What do we call a word that describes a noun? (e.g. 'happy', 'tall')\n")

if answer.lower() == "adjective":
    print()
    print()
    print("Correct, but don't get comfortable yet ...")
    
    if len(answer) == len(answer.strip()):
        print("Bonus: no extra spaces either. Tidy answer.")
    else:
        print("Bonus: I noticed extra spaces in there. Sloppy, but I'll let it go.")
else:
    print("Grrr ... your chances of meeting the Prof. are very low")
print()

answer = input("Give me a 6 letter English word with at least 2 vowels\n")
if len(answer) == 6:
    print("Your word has 6 letters ...")
    count_a = answer.lower().count('a')
    count_e = answer.lower().count('e')
    count_i = answer.lower().count('i')
    count_o = answer.lower().count('o')
    count_u = answer.lower().count('u')

    count_vowels = count_a + count_e + count_i + count_o + count_u

    if count_vowels > 2:
        print("Oof ... you gave me more than 2 vowels")
        print("You are wasting my time, I needed only 2.")
    elif count_vowels < 2:
        print("That had less than 2 vowels")
        print("You tried to act smart, but I caught you.")
    else:
        print("What ... exactly 2 vowels ...")
        print("You are not motivated, you are not putting any extra effort")
else:
    print("You seem to be a disaster.")
    print("That word did not even have 6 letters.")
print()

sentence = input("Ok, tell me a sentence ending in 'humble student' (no question please)\n")
if sentence.endswith('humble student'):
    print("Haven't you learnt about punctuations?")
elif sentence.endswith('humble student.'):
    len_first = sentence.find(' ')

    if len_first < 4:
        print("The first word in the sentence is too short.")
    else:
        print("Decent opener. The Prof. might actually approve.")
else:
    print("I really think you will make the prof. furious.")
print()

print("Fine. Choose your appointment slot for next Friday (A/B/C/D)")
print("A. 5 mins after sunrise", "B. 12 mins before lunch", sep='\t')
print("C. 30 mins past noon", "D. 10 mins before closing", sep='\t')
appointment = input('Select your slot (A/B/C/D)\n')

if appointment == 'A':
    print("Risky, the Prof. is not a morning person.")
elif appointment == 'B':
    print("Careful, the Prof. gets cranky when hungry before lunch.")
elif appointment == 'C':
    print("Decent choice, the Prof. is usually in a good mood after lunch.")
else:
    print("Bold, the Prof. is usually rushing to leave by then.")
print()

print("That's it. Best of luck surviving the actual meeting!")
