"""
Question 4: A Needle in the Haystack

Can you find the needle in the haystack?

Write a function `findNeedle()` that takes an array full of junk but contains one "needle".
After your function finds the needle, it should return a message (as a string) that says:

"found the needle at position " plus the index it found the needle.

Example:
["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] 
--> "found the needle at position 5"
"""

# ==== YOUR SOLUTION ====
def find_needle(haystack):
    # TODO: Write your code here
    pass


# ==== TESTS ====
from runner import run_question

def test_find_needle():
    return [
        (["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"], "found the needle at position 5"),
        (["needle"], "found the needle at position 0"),
        (["hay", "needle", "hay"], "found the needle at position 1"),
        (["junk", "moreJunk", "randomJunk"], "needle not found")  # Edge case with no needle
    ]

run_question(4, find_needle, test_find_needle)
