"""
Question 1: Counting sheep...

Consider an array/list of sheep where some sheep may be missing from their place. 
We need a function that counts the number of sheep present in the array (`True` means present).

Example:
[True,  True,  True,  False,
 True,  True,  True,  True,
 True,  False, True,  False,
 True,  False, False, True,
 True,  True,  True,  True,
 False, False, True,  True]

The correct answer would be 17.

Hint: Don't forget to check for bad values like None.
"""

# ==== YOUR SOLUTION ====
def count_sheep(sheep):
    # TODO: Write your code here
    pass


# ==== TESTS ====
from runner import run_question

def test_count_sheep():
    return [
        (
            [
                [True, True, True, False,
                 True, True, True, True,
                 True, False, True, False,
                 True, False, False, True,
                 True, True, True, True,
                 False, False, True, True],
                17
            ]
        ),
        (
            [
                [None, True, False, True, "yes", True],
                3
            ]
        ),
        (
            [
                [],
                0
            ]
        ),
        (
            [
                [False, False, None, 0],
                0
            ]
        )
    ]

run_question(1, count_sheep, test_count_sheep)
