import random

print("=== Number Guessing Game ===\n")

# --- Round 1: Guess the missing operator (2 numbers) ---
num1 = int(input("Please tell me a number: "))
num2 = int(input("Please tell me another number: "))

op_list = ['+', '-', '*']
op = random.randint(0, 2)

if op == 0:
    rhs = num1 + num2
elif op == 1:
    rhs = num1 - num2
elif op == 2:
    rhs = num1 * num2

print("\nCan you tell me the missing operator?")
answer = input(f"{num1} __ {num2} = {rhs}\n> ")

if answer.strip() == op_list[op]:
    print("Well done!\n")
else:
    print(f"Wrong! The answer was '{op_list[op]}'\n")

# --- Round 2: Guess two missing operators (3 numbers) ---
num3 = random.randint(1, 100)
print(f"New number chosen: {num3}")

op1 = random.randint(0, 1)  # + or -
op2 = random.randint(0, 1)  # + or -

if op1 == 0:
    rhs = num1 + num2
else:
    rhs = num1 - num2

if op2 == 0:
    rhs = rhs + num3
else:
    rhs = rhs - num3

print("\nCan you tell me the two missing operators? (e.g. +-)")
answer = input(f"{num1} __ {num2} __ {num3} = {rhs}\n> ")

if len(answer) >= 2 and answer[0] == op_list[op1] and answer[1] == op_list[op2]:
    print("Well done!")
else:
    print(f"Wrong! The answer was '{op_list[op1]}{op_list[op2]}'")

print()

print("-----  |   |    /\    |\  |  |  /    |   | [---] |    |")
print("  |    |   |   /  \   | \ |  | /     |   | |   | |    |")
print("  |    |---|  /--  \  |  \|  |/       ---| |   | |    |")
print("  |    |   | /      \ |   |  |\          | |   | |    |")
print("  |    |   |/        \|   |  | \      ___| |___| |____|")
print()
