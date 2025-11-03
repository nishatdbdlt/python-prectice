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


def find_missing_number(num):
    n = len(num) +1
    total = n* (n+1) //2
    return total - sum(num)

num=[1,2,4,5,6,7,8,9]
print("missing numner",find_missing_number(num))

def find_missing(num):
    n =len(num) + 1
    totall =n * (n + 1) // 2
    return totall - sum(num)
num =[1,2,3,4,6,9]
print(find_missing(num))


def two_number(nums,target):
    seen={}
    for i, num in enumerate(nums):
        remain= target -num
        if remain in seen:
            return [seen[remain],i]
        seen [num]= i

    return []

print(two_number([2,7,11,15], 9))

def two_number(nums ,target):
    seen ={}
    for i , num in enumerate(nums):
        remain = target - num
        if remain in seen:
            return [seen[remain],i]
        seen[num] =1

    return []
print(two_number([2,7,11,15], 9))


import string
text='putin my friend'
translator = str.maketrans('','',string.punctuation)
clean_text=text.translate(translator)
clean_text =clean_text.lower()
words= clean_text.split()
print(words)

def two(nums,target):
    seen ={}
    for i, num in enumerate(nums):
        remain = target - num
        if remain in seen:
            return [seen[remain],i]
        seen[num] =1

    return []
print(two([6,7,8,0],target=8))

def number(nums,target):
    seen ={}
    for i, num in enumerate(nums):
        remain = target - num

        if remain in seen:
            return [seen[remain],i]
        seen [num] = i

    return []
print(number([1,4,7,9],target=5))
