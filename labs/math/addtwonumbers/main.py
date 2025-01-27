"""
Math and Variables Lab
By: Chase Kalina-Wilson FIXME #fixed#
CSCI 110 Lab
Date: 2/6/2024 FIXME #fixed#
 
Read and solve: Add Two Numbers - https://open.kattis.com/problems/addtwonumbers 
 
Algorithm steps:
  1. Read data as a line
  2. Split the line into two integers
  3. Add them up
  4. print the result
"""

import sys


def main1():
    """Main function that solves the problem
    """
    
    # FIXME1 - read input data into a variable #fixed#
    line = input()
    # split the data into two numbers
    a, b = line.split()
    # check to see if the data is split correctly
    print(f'{a=}, {b=}', file=sys.stderr)
    # FIXME 2: convert string a into integer #fixed#
    a = int(a)
    # FIXME 3: convert string b into integer #fixed#
    b = int(b)
    # FIXME 4: add two numbers and store the result into ans variable #fixed#
    ans = (a+b)
    # FIXME 5: print the answer as shown in the sample output #fixed#
    print(ans)

main1()  # call main function
