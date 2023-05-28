import random
import ascii_art


def get_random_word(wordfile="/usr/share/dict/wordlist-probable.txt"):
    candidate_words = []
    with open(wordfile) as f:
        for word in f:
            word = word.strip()
            if len(word) >= 8 and word.islower() and word.isalpha():
                candidate_words.append(word)
    word = random.choice(candidate_words)

    return word


def get_partial_solution(word):
    return "_" * len(word)


def display_hangman(num_wrong_guesses):
    return ascii_art.gallows[num_wrong_guesses]


def display_word_and_guesses(partial_solution, wrong_guesses):
    return f"Mystery Word = {partial_solution}, Wrong Guesses = {wrong_guesses}"


def get_user_input():
    return input("Your guess is - ").lower()


def play_game():
    mystery_word = get_random_word()
    wrong_guesses = []
    partial_solution = get_partial_solution(mystery_word)

    
    display_hangman(len(wrong_guesses))
    print(display_word_and_guesses(partial_solution, wrong_guesses))

    while partial_solution != mystery_word:
        guess = get_user_input()

        if guess in mystery_word:
            for i, x in enumerate(mystery_word):
                if x == guess:
                    partial_solution = (
                        partial_solution[:i] + guess + partial_solution[i + 1 :]
                    )

        else:
            if guess not in wrong_guesses:
                wrong_guesses.append(guess)

        print(display_hangman(len(wrong_guesses)))
        print(display_word_and_guesses(partial_solution, wrong_guesses))

    if mystery_word == partial_solution:
        print("You Win!")
    else:
        print(f"You Lose!, the Mystery Word was {mystery_word}")


if __name__ == "__main__":
    play_game()
