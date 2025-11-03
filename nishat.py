import re

def count_unique_words(text):
    # remove punctuation and make lowercase
    words = re.findall(r'\b\w+\b', text.lower())
    unique_words = set(words)
    return len(unique_words)

text = "Bangladesh is a beautiful country. Bangladesh has rivers."
print("Unique words:", count_unique_words(text))