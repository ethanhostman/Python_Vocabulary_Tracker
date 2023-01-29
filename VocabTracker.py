"""
Ethan Hostman
This file contains the class used by VocabApplication.py 
along with two unit tests.
"""

class VocabTracker():
    """VocabTracker is a class that stores vocab and vocab goals"""
    #the default for vocab is the required input data in the form of dictionary entries
    def __init__(self, vocab = {"Hablar": "To speak", 
    "Comer": "To eat", "Correr": "To run", "Beber": "To drink"}, goal = 0):
        """__init__ is a constructor class that takes vocab and goal"""
        self.vocab = vocab
        self.__unique_keys = list(set(self.vocab.keys()))
        self.goal = goal

    def __check_word(self, word):
        """__check_word checks to see if the word is already in the dictionary"""
        return word not in self.__unique_keys

    def add_definition(self, word, definition):
        """add_definition allows the user to create new vocab entires"""
        if self.__check_word(word):
            self.vocab[word] = definition
            self.__unique_keys.append(word)
            return True
        else:
            return False

    def print_keys(self):
        """print_keys prints all vocab words in the dictionary"""
        for x in self.__unique_keys:
            print(x)

    def print_vocab(self):
        """print_vocab prints both the vocab words and their definitions"""
        for x, y in self.vocab.items():
            print(x + ":", y)

    def check_goal(self):
        """check_goal allows the user to check their goal progress"""
        checked_goal = tuple([self.goal, len(self.__unique_keys)])
        return checked_goal


    def set_goal(self, goal):
        """set_goal allows the user to set a new goal"""
        self.goal = goal

    def __eq__(self, object):
        """__eq__ compares the types of two objects"""
        return type(self) == type(object)

    def __del__(self):
        """__del__ deletes the instance of the VocabTracker to save space"""
        print("Vocab Tracker deleted")

    def __str__(self):
        """__str__ returns a description of the class, i.e. the vocab list"""
        return str(self.vocab)

#this block contains both unit tests for the public methods
if __name__ == "__main__":
    vocab_tracker = VocabTracker()
    try:
        assert vocab_tracker.add_definition("Hablar", "To speak") == False
        print("add_definition unit test successful")
    except:
        print("add_definition unit test not succesful")

    try:
        vocab_tracker.set_goal(5)
        
        assert vocab_tracker.check_goal() == (5,4)
        print("set_goal and check_goal unit tests successful")
    except:
        print("set_goal and check_goal unit tests not succesful")