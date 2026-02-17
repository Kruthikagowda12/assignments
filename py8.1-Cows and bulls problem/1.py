import random
secret = str(random.randint(1000, 9999))
attempts = 0
print("Welcome to the Cows and Bulls Game!")
while True:
    guess = input("Enter a 4-digit number: ")
    
    if len(guess) != 4 or not guess.isdigit():
        print("Enter a valid 4-digit number.")
        continue

    attempts += 1
    cows = 0
    bulls = 0
    for i in range(4):
        if guess[i] == secret[i]:
            cows += 1
        elif guess[i] in secret:
            bulls += 1
    if cows == 4:
        print("Correct! The number was", secret)
        print("Attempts:", attempts)
        break
    else:
        print(cows, "cows,", bulls, "bulls")
