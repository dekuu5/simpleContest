"""
Question 3: Beginner - Lost Without a Map

Given an array of integers, return a new array with each value doubled.

Example:
[1, 2, 3] --> [2, 4, 6]
"""

# ==== YOUR SOLUTION ====
def maps(arr):
    # TODO: Write your code here
    pass


# ==== TESTS ====
from runner import run_question

def test_maps():
    return [
        ([ [1, 2, 3] ], [2, 4, 6]),
        ([ [0, -1, 5] ], [0, -2, 10]),
        ([ [] ], []),
        ([ [100] ], [200])
    ]

run_question(3, maps, test_maps)
