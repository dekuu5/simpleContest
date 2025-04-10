"""
Question 8: Equal Sides Of An Array

You are given an array of integers. Your job is to find an index N where the sum of the integers
to the left of N is equal to the sum of the integers to the right of N.

If there is no such index, return -1.

Example 1:
{1, 2, 3, 4, 3, 2, 1} --> return 3 (since the sum of left {1,2,3} and right {3,2,1} both equal 6)

Example 2:
{1, 100, 50, -51, 1, 1} --> return 1 (left {1} and right {50,-51,1,1} both equal 1)

Example 3:
{20, 10, -80, 10, 10, 15, 35} --> return 0 (left {} and right {10,-80,10,10,15,35} both equal 0)
"""

# ==== YOUR SOLUTION ====
def find_even_index(arr):
    # TODO: Write your code here
    pass


# ==== TESTS ====
from runner import run_question

def test_find_even_index():
    return [
        ([ [1, 2, 3, 4, 3, 2, 1] ], 3),
        ([ [1, 100, 50, -51, 1, 1] ], 1),
        ([ [20, 10, -80, 10, 10, 15, 35] ], 0),
        ([ [1, 2, 3] ], -1),
        ([ [1, 2, 3, 4] ], -1),
    ]

run_question(8, find_even_index, test_find_even_index)
