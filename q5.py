"""
Question 5: Sum Arrays

Write a function that takes an array of numbers and returns the sum of the numbers. 
The numbers can be negative or non-integer. If the array does not contain any numbers, return 0.

Examples:
Input: [1, 5.2, 4, 0, -1] 
Output: 9.2

Input: [] 
Output: 0

Input: [-2.398] 
Output: -2.398
"""

# ==== YOUR SOLUTION ====
def sum_array(arr):
    # TODO: Write your code here
    pass


# ==== TESTS ====
from runner import run_question

def test_sum_array():
    return [
        ([ [1, 5.2, 4, 0, -1] ], 9.2),
        ([ [] ], 0),
        ([ [-2.398] ], -2.398),
        ([ [3.1, -1, 4, -2] ], 4.1)
    ]

run_question(5, sum_array, test_sum_array)
