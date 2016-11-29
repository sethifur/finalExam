#!/usr/bin/env python3
"""
Python 1 finantial assistance for low income households
"""
import sys

def get_input():
    """
    Retireves input for income number of children
    """
    try:
        income = int(input('What is the household income(-1 to quit)? '))
    except(TypeError,ValueError):
        print('Must be an Integer')
        exit()
    if income < 0:
        exit() 
    try:
        children = int(input('How many children? '))
    except(TypeError,ValueError):
        print('Must be an Integer')
        exit()
    finantial_assistance(income,children)

def finantial_assistance(income,children):
    """
    Calculates the finantial assistance
    Args:
        income is how much a family earns.
        children the amount of kids the user has.
    """
    aid = 0
    if income >= 30000 and income < 40000 and children >= 3:
        aid = children * 1000
    elif income < 30000 and income >= 20000 and children >=2:
        aid = children * 1500
    elif income < 20000:
        aid = children * 2000
    else:
        aid = 0
    print('The assistance amount is $', aid)


# Main Function
def main():
    '''
    Test Function
    '''
    get_input()
    return

if __name__ == '__main__':
    #Call Main
    main()

    exit(0)
