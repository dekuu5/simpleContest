"""
Question 2: Convert number to reversed array of digits

Given a random non-negative number, return the digits of this number in reverse order.

Examples:
35231 => [1, 3, 2, 5, 3]
0     => [0]
"""

# ==== YOUR SOLUTION ====
def digitize(n):
    # TODO: Write your code here
    pass


# ==== TESTS ====
from runner import run_question

def test_digitize():
    return [
        ([35231], [1, 3, 2, 5, 3]),
        ([0], [0]),
        ([7], [7]),
        ([100], [0, 0, 1]),
        ([987654321], [1, 2, 3, 4, 5, 6, 7, 8, 9])
    ]

run_question(2, digitize, test_digitize)
