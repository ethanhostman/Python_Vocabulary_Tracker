"""
Ethan Hostman
This is the file that runs the program.
"""

#the class and modules imported
from VocabTracker import VocabTracker
import random
import csv

#constant variables used
PROBLEM_TEXT = """Enter how many quiz questions you want as a positive integer. 
Make sure it is less than or equal to the number of vocab words: """

INPUT_TEXT = """Please choose a number for the desired option or enter \"quit\" to exit. 
1: Add a new word
2: Take a quiz
3: Save your vocab to a csv
4: Print all unique words
5: Print all words and definitions
6: Set a new goal or check goal progress
quit: Quit the application
"""

def to_continue():
    """to_continue creates a momentary pause so the user presses enter.
    This is to be used to break up loops later"""
    input("Press enter to continue: ")

def quiz(number):
    """quiz creates a vocab quiz to test the user's mastery of the material"""
    keys = list(vocab_tracker.vocab.keys())
    values = list(vocab_tracker.vocab.values())
    print("Match the word with the correct definition.")
    for x in range(number):
        current_word = keys.pop(random.randint(0,len(keys) - 1))
        answers = []
        correct_answer = vocab_tracker.vocab[current_word]
        possible_answers = values[:]
        possible_answers.remove(correct_answer)
        answers.append(correct_answer)
        answers += random.sample(possible_answers, k = 3)
        random.shuffle(answers)
        print("Current Word: " + str(current_word) + ":\nAnswers: ")
        i = 1
        for x in answers:
            print(str(i) + ":", x)
            i += 1
        user_answer = input("Choose the number of the correct definition: ")
        try:
            user_answer = int(user_answer)
            answer_chosen = answers[user_answer - 1]
        except:
            print("You did not choose a valid answer. The correct answer is \"{}\".".format(correct_answer.lower()))
        else:
            if answer_chosen == correct_answer:
                print("Good job! You answered correctly with \"{}\".".format(answer_chosen.lower()))
            else:
                print("You chose \"{}\". The correct answer is \"{}\"!".format(answer_chosen.lower(), correct_answer.lower()))
        to_continue()


if __name__ == "__main__":      
    vocab_tracker = VocabTracker()
    #this while loop creates a menu, letting the user choose an option
    while True:
        user_input = input(INPUT_TEXT)

        match user_input:
            
            case "quit":
                break

            #entering 1 will allow the user to add a new vocab entry
            case "1":
                word = input("Please enter the word in Spanish: ")
                definition = input("Please enter the English definition: ")
                if vocab_tracker.add_definition(word, definition):
                    print("Successfully added!")
                else:
                    print("Word already in Vocab Tracker")
                to_continue()

            #entering 2 lets the user take a quiz
            case "2":
                while True:
                    problems = input(PROBLEM_TEXT)
                    try:
                        problems = int(problems)
                    except:
                        print("You did not enter an integer. Please try again.")
                        continue
                    if problems <= len(vocab_tracker.vocab.keys()) and problems > 0:
                        break
                    else:
                        print("You must enter a valid input. Please try again.")
                quiz(problems)

            #entering 3 lets the user save their vocab to Vocabulary.csv
            case "3":
                with open('Vocabulary.csv', 'w') as csvfile:
                    writer = csv.DictWriter(csvfile, vocab_tracker.vocab.keys())
                    writer.writeheader()
                    writer.writerow(vocab_tracker.vocab)
                print("Successfully saved.")
                to_continue()

            #entering 4 prints all vocab words
            case "4":
                vocab_tracker.print_keys()
                to_continue()

            #entering 5 prints all words and their definitions
            case "5":
                vocab_tracker.print_vocab()
                to_continue()

            #entering 6 allows the user to set a new goal or view goal progress
            case "6":
                while True:
                    #goal_text and goal_input create the option of setting a goal or viewing progress
                    goal_text = "Please enter \"1\" to set a goal or enter \"2\" to view goal progress: "
                    goal_input = input(goal_text)
                    if goal_input == "1":
                        while True:
                            goal = input("Please enter your new words goal as an integer: ")
                            try:
                                goal = int(goal)
                                if goal <= 0:
                                    raise ValueError
                            except:
                                print("You did not enter a positive integer. Please try again.")
                            else:
                                vocab_tracker.set_goal(goal)
                                break
                        break
                    elif goal_input == "2":
                        checked_goal, length = vocab_tracker.check_goal()
                        success = "You have reached your goal of {}.".format(checked_goal)
                        defeat = "You have not reached your goal of {} yet.".format(checked_goal)
                        if checked_goal <= length:
                            print(success, "\nYou have learned {} words.".format(length))
                        else:
                            print(defeat, "\nYou have learned {} words.".format(length))
                        break
                    else:
                        print("Please enter a valid input.")
                to_continue()

            #case __ ensures that the user chooses a valid menu option
            case _:
                print("Please enter a valid input.")
                to_continue()
