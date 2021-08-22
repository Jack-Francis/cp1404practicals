"""
CP1404/CP5632 - Practical
Program to determine score status
"""

import random


def main():
    score = float(input("Enter score: "))
    result = evaluate_score(score)
    print(result)
    score = random.randint(0, 100)
    result = evaluate_score(score)
    print(result)


def evaluate_score(score):
    """Evaluate whether score is Invalid, Excellent, Passable or Bad"""
    if score > 100 or score < 0:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


main()
