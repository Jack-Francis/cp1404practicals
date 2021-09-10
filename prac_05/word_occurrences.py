"""
CP1404/CP5632 Practical
Count word occurrences in a string
"""

# Solutions were viewed after completion to fix/optimise code

word_to_word_count = {}      # Dictionary
text = input("Text: ")
words = text.split()
for word in words:
    word_occurrence = word_to_word_count.get(word, 0)
    word_to_word_count[word] = word_occurrence + 1
words = list(word_to_word_count.keys())
words.sort()
max_word_length = max((len(word) for word in words))
for word in words:
    print(f"{word:{max_word_length}} : {word_to_word_count[word]}")
