"""
Lab 6 - Strings and Tuples 
(100 marks in total, including 5 exercises - each 20 marks)

Author:  <your name>
Due Date: This Friday (Mar. 1) 11am.
Submission: Upload your lab python file to your GitHub repository.

Objective:
1. Learn how to write a good python docstring for documenting functions'
purpose, parameters, return values. A good docstring helps other developers 
understand how to use the function and serves as documentation that can be 
displayed in tools like IDEs. A sample docstring has been written for exercise 1 and 2,
students need to write good docstrings for all the other exercises.
2. Review how to code simple Python functions and write unit tests using assert
3. Practice how to operate on strings and tuples (similar to lists, but strings and tuples are immutable)
4. Review iterations using loop
5. Review the boolean expression and conditionals
6. Review the accumulator algorithm pattern (Initialize-Loop-Return):
   Initialize a variable that is assigned to an integer, a list, a string, etc.; 
   Loop (for or while) to update the variable based on requirements; 
   Return the variable or a value related to this variable.
"""

"""
Exercise 1 (20 marks: function implementation: 10 marks, unit tests: 10 marks)

Complete the function below to reverse a string.

For example, 
reverse_str("Abd") should return "dbA".
reverse_str("COMP115") should return "511PMOC".

Hint: the accumulator algorithm and the string concatenation using the operator '+'
"""
def reverse_str(s):
    """
    This function reverses string s.

    E.g., 
    >>> reverse_str('app')
    'ppa'

    Parameters:
    - s (string): The string to be reversed

    Returns:
    - (string): A reversed version of string s.

   """
    r = ""
    for item in s: 
        r =  item + r 
    return(r)

    

# Your unit tests

assert reverse_str('hallo') == 'ollah'
assert reverse_str('Apple') == 'elppA'
assert reverse_str('Banana5') == '5ananaB'


"""
Exercise 2 (20 marks: function implementation: 10 marks, unit tests: 10 marks)

Complete the function below to count how many vowels ('a', 'e', 'i', 'o', 'u') in a string.

For example, 
count_vowels("Apple") should return 2, since 'A' and 'e' are vowels.
count_vowels("Hmmm") should return 0, since there are no vowels.

Hint: you may want to convert the input string to its lowercase version using s.lower() first.
"""
def count_vowels(s):
    """
    This function counts the number of vowels in the string s.

    E.g., 
    >>> count_vowels("Apple")
    2

    Parameters:
    - s (string): The string in which vowels are counted.

    Returns:
    - (int): The total number of vowels in the string s.

    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0

    for item in s: 
        
        if item.lower() in vowels:
            count = count + 1 
    return(count)     
            
    

# Your unit tests

assert count_vowels("Cookie") == 4
assert count_vowels("Why") == 0
assert count_vowels("Chips") == 1

"""
Exercise 3 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Complete the following function to remove the duplicate characters in a string.

E.g.,
remove_duplicates("apple") == "aple"
remove_duplicates("Popsipple") == "Popsile" (Notice: 'P' and 'p' are different chars)
remove_duplicates("pear") == "pear"

Hint: We have implemented a function removing duplicates for a list in week 6. Similar.
"""
def remove_duplicates(s):
    """
      This function removes the duplicate characters in the string s.

    E.g., 
    >>> remove_duplicates("Apple")
    "Aple"

    Parameters:
    - s (string): The string in which the duplicates are are removed.

    Returns:
    - (string): The new string without the duplicate characters.
    """
    removed = ""
    for item in s: 
        if item not in removed:
            removed += item
    return(removed)


# Your unit tests

assert remove_duplicates("Leonie") == "Leoni"
assert remove_duplicates("Hannah") == "Hanh"
assert remove_duplicates("Fiona") == "Fiona"

"""
Exercise 4 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Complete the following function to return the lowerest index of a charactor t found in a string s, 
to return -1 if the character is not in the string.

E.g.,
find_index("Abd", 'b') == 1
find_index("Abdccc", 'c') == 3
find_index("Abd", 'w') == -1

Note: we should implement our own algorithm, not using the built-in function find().
"""
def find_index(s, t):
    """
      This function returns the lowest index of a character t in the string s and returns -1 if the character is not in the string.

    E.g., 
    >>> find_index("Apple", 'p')
    1

    Parameters:
    - t(character): The character to search for.
    - s (string): The string in which the lowest index of t is searched for.

    Returns:
    - (int): The number of the lowest index.
    
    """

    index = -1
    for item in s:
        if item == t:
            if index == -1:
                index = s.index(item)
            elif s.index(item) < index:
                index = s.index(item)
    return index
# Your unit tests
 
assert find_index('Apple', 'p') == 1
assert find_index('Good','d') == 3
assert find_index('Hello', 'h') == -1


"""
Exercise 5 (20 marks - doctring: 5 marks, function implementation: 10 marks, unit tests: 5 marks)

Complete the following function to return the project completion day, 
given the current day in a week and estimated time of days to completion.

E.g.,
project_completion_day('Monday', 4) returns 'Friday'.
project_completion_day('Monday', 7) returns 'Monday'.
project_completion_day('Saturday', 2) returns 'Monday'.
project_completion_day('Saturday', 1) returns 'Sunday'.

Hint:
days_week.index(day) will return the index of the day in the tuple days_week.

"""

days_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',
             'Saturday', 'Sunday')
# Notice that days_week is a tuple, and it works the same if it's a list,
# since the index operation is the same for tuple and list.


def project_completion_day(day, days_to_completion):
    """
    This function returns the day of the day of the project completion.

    E.g., 
    >>> project_completion_day("Monday", 5)
    'Saturday'

    Parameters:
    - days_to_completion (int): The number of days that is needed to complete the project.
    - day (string): The string that indicates the current day.

    Returns:
    - (string): The day of completion.

     """
    
    completion_day_int = days_week.index(day) + days_to_completion
    completion_day = completion_day_int % 7
    return days_week[completion_day]

# Your unit tests

assert project_completion_day('Monday', 6) == 'Sunday'
assert project_completion_day('Friday', 3) == 'Monday'
assert project_completion_day('Thursday', 8) == 'Friday'



"""
Congratulations on finishing your lab6. Hope you feel more confident on function implementation.

Now you just need to upload it to your GitHub repository. That's all.
"""