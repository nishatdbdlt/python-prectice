#1
import re

def count_unique_words(text):
    # remove punctuation and make lowercase
    words = re.findall(r'\b\w+\b', text.lower())
    unique_words = set(words)
    return len(unique_words)

text = "Bangladesh is a beautiful country. Bangladesh has rivers."
print("Unique words:", count_unique_words(text))

#2
import string

text = "Bangladesh is rich Country"

# punctuation remove
translator = str.maketrans('', '', string.punctuation)
clean_text = text.translate(translator)

# lowercase
clean_text = clean_text.lower()

# split into words
words = clean_text.split()

# print the word list
print(words)
#3
import string

text =" bangladesh is richcountry"

translator=str.maketrans('','',string.punctuation)
clean_text =text.translate(translator)
clean_text=clean_text.lower()

words=clean_text.split()
print(words)


import string
text ="india is bainchod country"

translator=str.maketrans('','',string.punctuation)
clean_text=text.translate(translator)
clean_text=clean_text.lower()
words=clean_text.split()
print(words)