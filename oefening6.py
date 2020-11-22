#!/usr/bin/env python
"""
Print a list
Ask for a number of words
Put these words in a list``
"""

#import

__author__ = "Stijn Janssen"
__email__ = "stijn.janssen@student.kdg.be"
__status__ = "Development"


def main():
    #Make a list and print it
    a = ["banaan", "appel", "citroen", "mango"]
    print(a)
    #Ask for a word
    b = input("Give me some words.\n")
    #Make a new list
    c = []
    #Put the words in the list and print the new list
    c.append(b)
    print(c)


if __name__ == '__main__':  # code to execute if called from command-line
    main()
