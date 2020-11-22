#!/usr/bin/env python
"""
Ask for the age
calculate when the person is born
calculate when the person wil be 50
"""

import datetime

__author__ = "Stijn Janssen"
__email__ = "stijn.janssen@student.kdg.be"
__status__ = "Development"


def main():
    #Ask for the age
    age = int(input("Give me your age please.\n"))
    #Put the year in variable now
    now = datetime.datetime.now()
    #Calculate the birthyear
    birth = now.year - age
    #Print the birthyear and calculate the year when you will be 50.
    print(f"You where born in the year {birth}. You will be 50 in the year {birth + 50}")


if __name__ == '__main__':  # code to execute if called from command-line
    main()
