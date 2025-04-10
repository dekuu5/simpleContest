"""
Question 1:
Write a function `add(a, b)` that returns the sum of a and b.

Example:
>>> add(2, 3)
5
"""

# ==== YOUR SOLUTION ====
def add(a, b):
    return a + b  +2

# ==== TESTS (do not modify below) ====

from runner import run_question

def test_add():
    tests = [
        ((2, 3), 5),
        ((-1, 1), 0),
        ((100, 200), 300)
    ]
    return tests

run_question(1, add, test_add)
