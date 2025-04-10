"""
Question 7: Build Tower

Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors.
A tower block is represented with the "*" character.

Example:
For 3 floors:
[
  "  *  ",
  " *** ",
  "*****"
]

For 6 floors:
[
  "     *     ",
  "    ***    ",
  "   *****   ",
  "  *******  ",
  " ********* ",
  "***********"
]
"""

# ==== YOUR SOLUTION ====
def tower_builder(n_floors):
    # TODO: Write your code here
    pass


# ==== TESTS ====
from runner import run_question

def test_tower_builder():
    return [
        ([ 3 ], [
            "  *  ",
            " *** ",
            "*****"
        ]),
        ([ 6 ], [
            "     *     ",
            "    ***    ",
            "   *****   ",
            "  *******  ",
            " ********* ",
            "***********"
        ]),
        ([ 1 ], ["*"]),
        ([ 2 ], [" * ", "***"]),
    ]

run_question(7, tower_builder, test_tower_builder)
