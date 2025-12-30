#print("I am a pretty pretty princess")

import math
import os
import random
import re
import sys

def test_weird_function():
    test_cases = [
        (3, "Weird"),
        (24, "Not Weird"),
        (100, "Not Weird")
    ]

    for n, expected in test_cases:
        result = check_weird(n)  # Assuming you create a function for the logic
        print(f"Input: {n}, Expected: {expected}, Got: {result}")

def check_weird(n):
    if n % 2 == 1:
        return "Weird"
    else:
        if 2 <= n <= 5:
            return "Not Weird"
        elif 6 <= n <= 20:
            return "Weird"
        else:
            return "Not Weird"

# Run the tests
test_weird_function()

