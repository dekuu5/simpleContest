"""
Question 9: Moving Zeros To The End

Write an algorithm that takes an array and moves all of the zeros to the end, 
preserving the order of the other elements.

Example:
move_zeros([1, 0, 1, 2, 0, 1, 3]) --> [1, 1, 2, 1, 3, 0, 0]
"""

# ==== YOUR SOLUTION ====
def move_zeros(arr):
    # TODO: Write your code here
    pass


# ==== TESTS ====
from runner import run_question

def test_move_zeros():
    return [
        ([ [1, 0, 1, 2, 0, 1, 3] ], [1, 1, 2, 1, 3, 0, 0]),
        ([ [0, 0, 0, 1, 2, 3] ], [1, 2, 3, 0, 0, 0]),
        ([ [1, 2, 3, 0] ], [1, 2, 3, 0]),
        ([ [0, 0, 0] ], [0, 0, 0]),
        ([ [] ], [])
    ]

run_question(9, move_zeros, test_move_zeros)
