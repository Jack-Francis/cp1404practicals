"""
Do This Now - Week 4
"""

VOWELS = "aeiouAEIOU"

name = input("Name: ")
vowel_count = 0
for char in name:
    # if char.lower() in VOWELS:
    if char in VOWELS:
        vowel_count += 1
print("Out of {} letters, {} has {} vowels.".format(len(name), name, vowel_count))
# print(f"Out of {len(name)} letters, {name} has {vowel_count} vowels.")

# TODO: * 'unpacks' when printing lists (Add to info Document)