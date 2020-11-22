#!/usr/bin/env python
"""
Make a stopwatch``
"""

import time

__author__ = "Stijn Janssen"
__email__ = "stijn.janssen@student.kdg.be"
__status__ = "Development"

#define the correct convertion of hte time
def time_convert(sec):
    min = sec // 60
    sec = sec % 60
    hour = min // 60
    min = min % 60
    print("Time lapsed = {0}:{1}:{2}".format(int(hour), int(min),sec))


def main():
    #input = enter, then start timer
    input("Press Enter to start")
    start_time = time.time()
    #input = enter, then stop timer
    input("Press Enter to stop")
    end_time = time.time()
    time_lapsed = end_time - start_time
    time_convert(time_lapsed)

if __name__ == '__main__':  # code to execute if called from command-line
    main()
