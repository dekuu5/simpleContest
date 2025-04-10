"""
Question 6: Sum of two lowest positive integers

Create a function that returns the sum of the two lowest positive numbers 
given an array of at least 4 positive integers. No floats or non-positive integers will be passed.

Examples:
[19, 5, 42, 2, 77] --> 7
[10, 343445353, 3453445, 3453545353453] --> 3453455
"""

# ==== YOUR SOLUTION ====
def sum_two_smallest_numbers(arr):
    # TODO: Write your code here
    pass


# ==== TESTS ====
from runner import run_question

def test_sum_two_smallest_numbers():
    return [
        ([ [19, 5, 42, 2, 77] ], 7),
        ([ [10, 343445353, 3453445, 3453545353453] ], 3453455),
        ([ [1, 2, 3, 4] ], 3),
        ([ [5, 1, 2, 3, 4] ], 3),
        ([ [7, 8, 2, 4] ], 6)
    ]

run_question(6, sum_two_smallest_numbers, test_sum_two_smallest_numbers)
