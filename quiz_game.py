# ----------------------------
import random


def new_game():
    guesses = []
    correct_guesses = 0
    wrong_guesses = 0
    questions_num = 1
    for key in questions:
        print("--------------------------------------------------------")
        print(key)
        for i in options[questions_num - 1]:
            print(i)
        questions_num += 1
        guess = input("Answer : ").upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
    display_score(correct_guesses, guesses)

# ----------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("Correct Answer")
        return 1
    else:
        print("False Answer")
        return 0
# ----------------------------
def display_score(correct_guesses, guesses):
    print("----------------------------")
    print("RESULTS")
    print("----------------------------")

    print("Guesses : ", end="\n")
    for i in guesses:
            print(i, end=" ")
    score = (correct_guesses/len(questions)) * 100
    print(f"\n%{score} of the answers were correct.")
    x = input("Do you want to play again? (yes/no)")
    play_again(x)
# ----------------------------
def play_again(yes):
    if yes.lower() != "yes":
        print("Bye")
    else:
        new_game()
# ----------------------------


questions = {
"Who created Python?: ": "A",
"What year was Python created?: ": "B",
"Python is tributed to which comedy group?: ": "C",
"Is the Earth round?: ": "A"
}
options = [
                ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
                ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
                ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
                ["A. True", "B. False", "C. sometimes", "D. What's Earth?"]
]

new_game()
