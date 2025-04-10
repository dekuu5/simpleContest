"""
Question 10: ROT13

ROT13 is a simple letter substitution cipher that replaces a letter with the letter 
13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with ROT13. 
If there are numbers or special characters included in the string, they should be returned as they are.
Only letters from the Latin/English alphabet should be shifted, like in the original ROT13 "implementation".

Note: Using encode is considered cheating.
"""

# ==== YOUR SOLUTION ====
def rot13(string):
    # TODO: Write your code here
    pass


# ==== TESTS ====
from runner import run_question

def test_rot13():
    return [
        ([ "Hello, World!" ], "Uryyb, Jbeyq!"),
        ([ "abc" ], "nop"),
        ([ "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" ], "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"),
        ([ "12345!@#abcXYZ" ], "12345!@#nopKLM")
    ]

run_question(10, rot13, test_rot13)
