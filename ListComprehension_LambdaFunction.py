# Comprehensive list:
# Write a list comprehension to generate squares of numbers from 1 to 10.

# 
squares = []

for i in range(1,11):
    squares.append(i ** 2)

print(squares)

# using list comprehension
squares = [i**2 for i in range(1,11)]
print(squares)

# 2. Create a list of even numbers between 1 and 50 using list comprehension.

# using list comprehension
even_numbers = [n for n in range(1, 51) if n % 2 == 0]
print(even_numbers)

# WITHOUT list comprehension
even_numbers = []
for n in range(1,51):
    if n % 2 == 0:
        even_numbers.append(n)
print(even_numbers)

# 3. Convert all strings in a list to uppercase using list comprehension.

words = ["apple", "banana", "mango", "grapes"]
upper_words = [word.upper() for word in words]
print(upper_words)

# WITHOUT list comprehension
words = ["apple", "banana", "mango", "grapes"]

upper_words = []
for i in words:
    upper_words.append(i.upper())
print(upper_words)


# 4. Given a list of integers, create a new list that contains only the positive numbers.

numbers = [-1,-2,-5,2, 5, 340, -4]
integers = [n for n in numbers if n > 0]
print(integers)

# WITHOUT list comprehension
integers = []

numbers = [-1,-2,-5, 2, 5, 340, -4]
for n in numbers:
    if n > 0:
        integers.append(n)
print(integers)

# 5. Create a list of tuples (num, num^2) for numbers 1 to 5.
# 
pairs = [(n, n**2) for n in range(1,6)]
print(pairs)

# 
pairs = []
for n in range(1,6):
    pairs.append((n, n**2))
print(pairs)

# 6. Extract all vowels from a given string using list comprehension.
# 
text = "Extract vowels from this string"
vowels = [ch for ch in text if ch.lower() in "aeiou"]
print(vowels)

# 
text = "Extract vowels from this string"
vowels = []

for i in text:
    if i.lower() in "aeiou":
        vowels.append(i)

print(vowels)


# 7. Flatten a 2D list using list comprehension.
# Flatten a 2D list using list comprehension
matrix = [[1, 2, 3], [4, 5], [6, 7, 8]]

flat_list = [item for row in matrix for item in row]
print(flat_list)


# 8. Replace all negative numbers in a list with 0 using list comprehension.
list1 = [0,4,5,6,-2,30,-5,-2,4,-3]
negNum = [0 if n <0 else n for n in list1 ]
print(negNum)

# 9. Given a list of words, create a list of lengths of each word.
fruits = ["apple", "banana", "kiwi", "grapes"]
lenFruits = [len(fruit) for fruit in fruits]
print(lenFruits)

# 10. Filter out words that start with the letter 'A' or 'a'.
# 
fruits = ["Apple", "banana", "Avocado", "mango", "apricot", "Grapes"]

filtered = [f for f in fruits if not f.lower().startswith('a')]
print(filtered)


# 
fruits = ["Apple", "banana", "Avocado", "mango", "apricot", "Grapes"]

filtered = []
for i in fruits:
    if not (i.startswith('A') or i.startswith("a")):
        filtered.append(i)

print(filtered)


# 11. From a list of numbers, generate a list of “even” or “odd” strings using list comprehension.
# (Like → [“even”, “odd”, “odd”, “even”…])
num = [2, 5, 7, 8, 10]
compre = ['even' if i%2 == 0 else 'odd' for i in num]
print(compre)



# 12. Create a list of numbers divisible by both 3 and 5 in range 1–100.

divide = [n for n in range(1,101) if n% 3 == 0 and n%5 == 0]
print(divide)

# 13. Write a nested list comprehension to generate a multiplication table for 1–5.
table = [[i * j for j in range(1, 11)] for i in range(1, 6)]
print(table)


# 14. Convert a dictionary’s keys into a list using list comprehension.
data = {"name": "Vibha", "age": 22, "city": "Pune"}
keys = [key for key in data]
print(keys)

# 15. Extract numeric digits from a string using list comprehension.
text = "Room 402, Floor 7, Pune 411001"

digits = [ch for ch in text if ch.isdigit()]
print(digits)


# 16. Use list comprehension to remove all spaces from a string.

text = "remove all spaces from me"

result = "".join([ch for ch in text if ch != " "])
print(result)


# 17. Create a list of characters that appear more than once in a string.
str = "programming"
result = [ch for ch in set(str) if str.count(ch) > 1]
print(result)

# 18. From a list of sentences, generate a list of all words (split using list comprehension).
sentences = ["I love Python", "List comprehension is powerful"]
words = [word for sentence in sentences for word in sentence.split()]
print(words)

# FOR each sentence in sentences
#     FOR each word in sentence.split()
#         ADD word to list


# 19. Create a list of unique elements from a list using list comprehension + condition.

nums = [1, 2, 2, 3, 4, 4, 5, 1]
unique = []
[unique.append(n) for n in nums if n not in unique]
print(unique)

# 20. Generate all pairs (x, y) where x is from list A and y is from list B (cartesian product).

A = [1, 2]
B = ['a', 'b']

pairs = [(x, y) for x in A for y in B]
print(pairs)

# [ expression for outer_var in outer_iterable for inner_var in inner_iterable ]
# for outer_var in outer_iterable:
#     for inner_var in inner_iterable:
#         expression


# Lambda functions
# 1. Write a lambda to add two numbers.
add = lambda a,b: a+b
print(add(1,4))

# 2. Create a lambda to check if a number is even.
evenNum = lambda a: a%2 == 0
print(evenNum(6))

# 3. Write a lambda to get the last character of a string.
lastchar = lambda a: a[-1]
print(lastchar("BLABLAB"))

# 4. Use lambda with map() to square every number in a list.
nums = [1,2,3,4,5]
squares = list(map(lambda x: x**2, nums))
print(squares)

# 5. Use lambda with filter() to get only odd numbers from a list.
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
oddNum = list(filter(lambda x: x%2 != 0, lst))
print(oddNum)

# 
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
oddNum = sorted(filter(lambda x: x % 2 != 0, lst), reverse=False)
print(oddNum)

# 6. Use sorted() + lambda to sort a list of tuples by second value.
tuples_list = [(1, 3), (4, 1), (2, 2), (5, 0)]

sorted_list = sorted(tuples_list, key=lambda x: x[1])
print(sorted_list)

# 7. Create a lambda to check if a string is a palindrome.
is_palindrome = lambda s: s == s[::-1]

print(is_palindrome("madam"))   # True
print(is_palindrome("python"))  # False

# 8. Use lambda to find maximum of three numbers.
lst = 10, 25, 15
maximum = lambda a,b,c : max(a,b,c )
print(maximum(*lst))

# 
max_of_three = lambda a, b, c: max(a, b, c)

print(max_of_three(10, 25, 15))  # 25
print(max_of_three(7, 3, 9))     # 9

# 9. Write a lambda to reverse a string.
str = "python"
rev_str = lambda x: x[::-1]
print(rev_str(str))

# 10. Use lambda with map() to convert a list of strings to integers.
str_list = ["1", "2", "3", "4", "5"]
int_list = list(map(lambda x: int(x), str_list))
print(int_list)

# 11. Use lambda with filter() to remove empty strings from a list.
list1 = ["apple", "", "banana", "", "kiwi", ""]
filtered_list1 = list(filter(lambda x: x != "", list1))
print(filtered_list1)

# 12. Use lambda to compute factorial using reduce() (yeah, that one-liner madness).
from functools import reduce
factorial = lambda n : reduce(lambda x, y: x*y, range(1, n+1))
print(factorial(5))

# 13. Write a lambda that returns the larger of two numbers.

larger = lambda x,y: x if x> y else y
print(larger(1000,100))


# 14. Use lambda to check if number is divisible by 5.
div = lambda x:  x% 5 == 0 
print(div(14))

# 15. Use lambda + map() to add 10 to each element of a list.
lst = [5, 10, 15, 20]
addingElem = list(map(lambda x: x+ 10, lst))
print(addingElem)

# 16. Use lambda to sort a list of dictionaries by a key (like "age").
dict1 = [{"name": "Amit", "age": 25}, {"name": "Neha", "age": 22}, {"name": "Rahul", "age": 30}]
dict_sort = sorted(dict1, key = lambda x : x["age"])
print(dict_sort)

# 17. Write a lambda that returns True if a character is a vowel.
is_vowel = lambda ch:ch.lower() in 'aeiou'

ch = input("Enter a character: ")
print(is_vowel)

# 18. Use lambda + filter to extract words of length > 5 from a list.
words = ["python", "java", "programming", "sql", "analytics", "AI"]

extract_word = list(filter(lambda x : len(x) > 5, words))
print(extract_word)

# 19. Use lambda to calculate the area of a circle (πr²).
areaOfCircle = lambda r : 22/7 * r**2
print(areaOfCircle(5))

# 20. Write a lambda to remove duplicates from a list using filter + set.

lst = lst = [1, 2, 2, 3, 4, 4, 5, 1]
seen = set()
remove_duplicates = list(filter(lambda x : x not in seen and not seen.add(x), lst))
print(remove_duplicates)

# 21. Use lambda with reduce() to find the product of all numbers in a list.

from functools import reduce
lst = [1, 2, 3, 4, 5]

product = reduce(lambda x, y: x*y, lst)
print(product)


# 22. Write a lambda that returns absolute value of a number.
absolute = lambda x: x if x>= 0 else -x
num = int(input("Enter a number: "))
print(absolute(num))

# 23. Use lambda to sort a list of strings by their length.
words = ["python", "java", "sql", "analytics"]
result = sorted(words, key=lambda x: len(x))
print(result)

# 24. Use lambda to get only uppercase characters from a string.
text = "PyTHon"
result = list(filter(lambda x: x.isupper(), text))
print(result)


# 25. Write a lambda that returns the square if number is even, cube if odd.
num = [1,2,3,4,5,6]
res = list(map(lambda x: x**2 if x%2 == 0 else x**3, num))
print(res) 

# 26. Use lambda with map to convert Celsius to Fahrenheit.
celsius = [0, 20, 30, 40]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(fahrenheit)


# 27. Write a lambda to check if two strings are anagrams.
anagram = lambda x, y : set(x) ==set(y)
print(anagram("Vibha", "aVhbi"))

# 28. Use lambda to extract only numeric values from a mixed list.
lst = [1, 'a', 35, 34, 7, 'viobha']
num = list(filter(lambda x: isinstance(x, (int, float)), lst))
print(num)

# 29. Use lambda inside any() to check if any list element is negative.
lst = [3, 5, -2, 8]
result = any(map(lambda x: x < 0, lst))
print(result)

# 30. Use lambda to generate a function that multiplies any number by n
lst = [3, 5, -2, 8]
result = any(map(lambda x: x < 0, lst))
print(result)
