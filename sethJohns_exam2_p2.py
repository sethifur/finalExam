#!/usr/bin/env python3
'''
Alternating sum program python 3
'''
import sys

def get_input():
    '''
    Retrieves numbers in an array
    '''
    nums = []
    while True:
        try:
            nums.append(int(input('Enter values(blank line to quit):')))
        except (TypeError,ValueError):
            return nums
            
def calc_alt():
    '''
    calls get_input and adds alternating values
    '''
    altsum = 0
    nums = get_input()
    for num in range(0,len(nums)):
        if (num % 2) == 0:
            altsum += nums[num]
        else:
            altsum -= nums[num]
    print('The alternating sum is ', altsum)

# Main Function
def main():
    '''
    Test Function
    '''
    calc_alt()
    return

if __name__ == '__main__':
    #Call Main
    main()

    exit(0)
