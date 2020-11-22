#!/usr/bin/env python
"""
Ask for a string and print the lenght of that string.
"""

#import

__author__ = "Stijn Janssen"
__email__ = "stijn.janssen@student.kdg.be"
__status__ = "Development"


def main():
    #Ask for a word
    word = input("Give me a word.\n")
    #Give the lenght of the word
    print(len(word))

if __name__ == '__main__':  # code to execute if called from command-line
    main()
