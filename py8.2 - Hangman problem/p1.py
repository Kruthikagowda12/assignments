import random
def load_words(filename):
    with open(filename, "r") as file:
        words = [line.strip().upper() for line in file if line.strip()]
    return words
def choose_word(word_list):
    return random.choice(word_list)
def play_game(words):
    word = choose_word(words)
    guessed_letters = set()
    attempts_left = 6

    print("\nWelcome to Hangman!")

    while attempts_left > 0:
     
        display = [letter if letter in guessed_letters else "_" for letter in word]
        print(" ".join(display))

   
        if "_" not in display:
            print("You won! The word was:", word)
            return

        guess = input("Guess your letter: ").upper()

        if not guess.isalpha() or len(guess) != 1:
            print("Enter only one letter.")
            continue

    
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

       
        if guess in word:
            print("Correct!")
        else:
            attempts_left -= 1
            print("Incorrect!")
            print("You left with", attempts_left, "chances.")

    print("You lost! The word was:", word)



words = load_words("C:\\Users\\krithika KJ\\assignments\\py8.2 - Hangman problem\\words.txt")

while True:
    play_game(words)
    again = input("Play again? (y/n): ").lower()
    if again != "y":
        break
