import random
import ascii_art


def get_random_word(wordfile="/usr/share/dict/wordlist-probable.txt"):
    candidate_words = []
    with open(wordfile) as f:
        for word in f:
            word = word.strip()
            if len(word) >= 7 and word.islower() and word.isalpha():
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


def update_masked_word(hidden_word, masked_word, guess=" ", wrong_guesses=[]):
    if guess in hidden_word:
        for i, x in enumerate(hidden_word):
            if x == guess:
                masked_word = (
                    masked_word[:i] + guess + masked_word[i + 1 :]
                )
        return masked_word, wrong_guesses

    else:
        if guess not in wrong_guesses:
            wrong_guesses.append(guess)
        return masked_word, wrong_guesses


def check_game_over(mystery_word, partial_solution):
    if mystery_word == partial_solution:
        return "You Win!"
    else:
        return f"You Lose!, the Mystery Word was -> {mystery_word}"


def check_game_loop(partial_solution, mystery_word, wrong_guesses=[]):
    if partial_solution != mystery_word and len(wrong_guesses) < len(ascii_art.gallows) - 1:
        return True
    return False


def display_game_status(partial_solution, wrong_guesses=[]):
    print(display_hangman(len(wrong_guesses)))
    print(display_word_and_guesses(partial_solution, wrong_guesses))


def main():
    mystery_word = get_random_word()
    wrong_guesses = []
    partial_solution = get_partial_solution(mystery_word)

    # print once
    display_game_status(wrong_guesses, partial_solution)

    while check_game_loop(partial_solution, mystery_word, wrong_guesses):
        guess = get_user_input()
        partial_solution, wrong_guesses = update_masked_word(mystery_word, partial_solution, guess, wrong_guesses)
        display_game_status(wrong_guesses, partial_solution)

    print(check_game_over(mystery_word, partial_solution))


if __name__ == "__main__":
    main()
